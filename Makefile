.PHONY: venv install install-dev test test-verbose test-coverage test-watch lint format clean help

# Default target
help:
	@echo "Available commands:"
	@echo "  venv         - Create virtual environment"
	@echo "  install      - Install production dependencies (in venv)"
	@echo "  install-dev  - Install development dependencies (in venv)"
	@echo "  test         - Run tests"
	@echo "  test-verbose - Run tests with verbose output"
	@echo "  test-coverage- Run tests with coverage report"
	@echo "  test-watch   - Run tests in watch mode"
	@echo "  test-no-install - Run tests without installing (requires pytest in PATH)"
	@echo "  lint         - Run linting checks"
	@echo "  format       - Format code with black and isort"
	@echo "  clean        - Clean up generated files"

# Create virtual environment
venv:
	python -m venv venv
	@echo "Virtual environment created. Activate with: source venv/bin/activate"

# Install dependencies (assumes venv is activated)
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

# Run tests
test:
	pytest

test-verbose:
	pytest -v

test-coverage:
	pytest --cov=src --cov-report=html --cov-report=term-missing

test-watch:
	pytest --watch

test-no-install:
	python -m pytest

# Code quality
lint:
	flake8 src __tests__
	mypy src

format:
	black src __tests__
	isort src __tests__

# Clean up
clean:
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf __pycache__/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
