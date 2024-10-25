"""Tests for the Git LFS binary detection pre-commit hook"""

import os
import shutil
import stat
import subprocess
import tempfile
from pathlib import Path

import pytest


class GitRepo:
    """Class to manage a test Git repository"""

    def __init__(self, path, hook_source):
        """
        Initialize GitRepo with path and hook source path

        Args:
            path: Path to create repository
            hook_source: Path to the pre-commit hook source file
        """
        self.path = Path(path)
        self.git_dir = self.path / ".git"
        self.hook_path = self.git_dir / "hooks" / "pre-commit"
        self.hook_source = Path(hook_source)

        if not self.hook_source.exists():
            raise FileNotFoundError(
                f"Pre-commit hook not found at {self.hook_source}"
            )

    def init(self):
        """Initialize a new git repository with LFS"""
        subprocess.run(["git", "init"], cwd=self.path, check=True)
        subprocess.run(["git", "lfs", "install"], cwd=self.path, check=True)
        self.install_hook()
        print("Git LFS initialized.")

    def install_hook(self):
        """Install the pre-commit hook from source"""
        self.hook_path.parent.mkdir(exist_ok=True)
        shutil.copy2(self.hook_source, self.hook_path)
        st = os.stat(self.hook_path)
        os.chmod(self.hook_path, st.st_mode | stat.S_IEXEC)
        print("Updated Git hooks.")

    def add(self, file_path):
        """Add a file to git"""
        subprocess.run(["git", "add", file_path], cwd=self.path, check=True)

    def commit(self, message):
        """Try to commit and return the process result"""
        result = subprocess.run(
            ["git", "commit", "-m", message],
            cwd=self.path,
            capture_output=True,
            text=True,
        )
        return result

    def is_lfs_tracked(self, file_path):
        """Check if a file is tracked by Git LFS"""
        try:
            with open(self.path / ".gitattributes", "r") as f:
                content = f.read()
                return str(file_path) in content and "filter=lfs" in content
        except FileNotFoundError:
            return False


class TestFiles:
    """Helper class to create different types of test files"""

    @staticmethod
    def create_text_file(path, content="This is a text file\n"):
        """Create a text file with given content"""
        path.write_text(content)

    @staticmethod
    def create_binary_file(path, size=1024):
        """Create a binary file of given size"""
        with open(path, "wb") as f:
            f.write(os.urandom(size))

    @staticmethod
    def create_minimal_pdf(path):
        """Create a minimal valid PDF file"""
        pdf_content = (
            b"%PDF-1.0\n"
            b"1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
            b"2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj\n"
            b"3 0 obj<</Type/Page/MediaBox[0 0 3 3]>>endobj\n"
            b"xref\n"
            b"0 4\n"
            b"0000000000 65535 f\n"
            b"0000000009 00000 n\n"
            b"0000000052 00000 n\n"
            b"0000000101 00000 n\n"
            b"trailer<</Size 4/Root 1 0 R>>\n"
            b"startxref\n"
            b"149\n"
            b"%%EOF\n"
        )
        path.write_bytes(pdf_content)


def get_project_root():
    """Get the project root directory"""
    return Path(__file__).parent.parent


@pytest.fixture
def repo(request):
    """
    Fixture to create and optionally preserve test repository

    Usage:
        @pytest.mark.keep_repo  # Add this decorator to keep the repo
        def test_something(repo):
            ...

    You can also run pytest with --keep-repos to keep all test repos
    """
    project_root = get_project_root()
    hook_path = project_root / "src" / "pre-commit"

    # Create temp directory with a more identifiable name
    tmp_base = project_root / "test-repos"
    tmp_base.mkdir(exist_ok=True)

    # Create a unique directory for this test
    test_name = request.node.name
    tmp_dir = tempfile.mkdtemp(prefix=f"{test_name}_", dir=tmp_base)

    repo = GitRepo(tmp_dir, hook_path)
    repo.init()

    # Setup git config for commits
    subprocess.run(
        ["git", "config", "user.email", "test@example.com"], cwd=tmp_dir
    )
    subprocess.run(["git", "config", "user.name", "Test User"], cwd=tmp_dir)

    yield repo

    # Check if we should keep this repo
    keep_this_repo = (
        request.config.getoption("--keep-repos")
        or request.node.get_closest_marker("keep_repo") is not None
    )

    if keep_this_repo:
        print(f"\nPreserving test repository at: {tmp_dir}")
    else:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_text_file(repo):
    """Test that regular text files are committed normally"""
    file_path = repo.path / "test.txt"
    TestFiles.create_text_file(file_path)

    repo.add("test.txt")
    result = repo.commit("Add text file")

    assert result.returncode == 0, "Text file should commit normally"
    assert not repo.is_lfs_tracked(
        "test.txt"
    ), "Text file should not be LFS tracked"


@pytest.mark.keep_repo
def test_binary_file_no_extension(repo):
    """Test that binary files without extensions are detected and tracked"""
    file_path = repo.path / "binary_file"
    TestFiles.create_binary_file(file_path)

    repo.add("binary_file")
    result = repo.commit("Add binary file")

    assert result.returncode == 1, "First commit should fail"
    assert repo.is_lfs_tracked(
        "binary_file"
    ), "Binary file should be LFS tracked"


def test_empty_file(repo):
    """Test that empty files are handled correctly"""
    file_path = repo.path / "empty_file"
    file_path.touch()

    repo.add("empty_file")
    result = repo.commit("Add empty file")

    assert result.returncode == 0, "Empty file should commit normally"
    assert not repo.is_lfs_tracked(
        "empty_file"
    ), "Empty file should not be LFS tracked"


def test_pdf_file(repo):
    """Test that PDF files are detected and tracked"""
    file_path = repo.path / "test.pdf"
    TestFiles.create_minimal_pdf(file_path)

    repo.add("test.pdf")
    result = repo.commit("Add PDF file")

    assert result.returncode == 1, "First commit should fail"
    assert repo.is_lfs_tracked("test.pdf"), "PDF file should be LFS tracked"


def test_symbolic_link(repo):
    """Test that symbolic links are handled correctly"""
    target_path = repo.path / "target.txt"
    TestFiles.create_text_file(target_path)
    link_path = repo.path / "link_file"
    os.symlink(target_path, link_path)

    repo.add("link_file")
    result = repo.commit("Add symbolic link")

    assert result.returncode == 0, "Symbolic link should commit normally"
    assert not repo.is_lfs_tracked(
        "link_file"
    ), "Symbolic link should not be LFS tracked"


def test_multiple_files(repo):
    """Test handling multiple files in a single commit"""
    # Create various files
    TestFiles.create_text_file(repo.path / "text1.txt")
    TestFiles.create_binary_file(repo.path / "binary1")
    TestFiles.create_text_file(repo.path / "text2.txt")
    TestFiles.create_binary_file(repo.path / "binary2")

    # Add all files
    repo.add(".")
    result = repo.commit("Add multiple files")

    assert result.returncode == 1, "First commit should fail"
    assert repo.is_lfs_tracked(
        "binary1"
    ), "First binary file should be LFS tracked"
    assert repo.is_lfs_tracked(
        "binary2"
    ), "Second binary file should be LFS tracked"
    assert not repo.is_lfs_tracked(
        "text1.txt"
    ), "First text file should not be LFS tracked"
    assert not repo.is_lfs_tracked(
        "text2.txt"
    ), "Second text file should not be LFS tracked"
