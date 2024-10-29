def pytest_addoption(parser):
    """Add command line option to keep all test repositories"""
    parser.addoption(
        "--keep-repos",
        action="store_true",
        default=False,
        help="Keep test repositories after tests complete",
    )


def pytest_configure(config):
    """Register the keep_repo marker"""
    config.addinivalue_line(
        "markers",
        "keep_repo: mark test to preserve its repository after completion",
    )
