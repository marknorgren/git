.PHONY: format lint test clean

format:
	black .
	isort .

lint:
	flake8 .
	black --check .
	isort --check-only .

test:
	pytest pre-commit-tests.py -v

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "test-repos" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name ".coverage" -delete
