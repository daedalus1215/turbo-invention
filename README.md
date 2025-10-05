# turbo-invention

A Python algorithms and data structures project with comprehensive testing.

## Setup

### Option 1: Using Virtual Environment (Recommended)
```bash
# Create virtual environment
make venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
make install

# Run tests
make test
```

### Option 2: Without Installing Anything Globally
```bash
# Run tests directly with Python (requires pytest in PATH)
make test-no-install

# Or run pytest directly
python -m pytest

# Or if you have pytest installed locally
pytest
```

### Option 3: Using pipx (if you have it installed)
```bash
# Install pytest with pipx (isolated installation)
pipx install pytest

# Run tests
pytest
```

## Running Tests

### Using Make (Recommended)
```bash
make test              # Run all tests
make test-verbose      # Run with detailed output
make test-coverage     # Run with coverage report
make test-watch        # Run in watch mode
make test-no-install   # Run without installing anything
```

3. **Code quality:**
   ```bash
   # Format code
   make format
   
   # Run linting
   make lint
   ```

## Project Structure

```
turbo-invention/
├── src/                    # Source code
│   ├── array_hash.py      # Array and hash table algorithms
│   ├── linked_lists.py    # Linked list algorithms
│   └── ...
├── __tests__/             # Test files
│   ├── array_hash/        # Tests for array/hash algorithms
│   ├── linked_lists/      # Tests for linked list algorithms
│   └── ...
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development dependencies
├── pytest.ini           # Pytest configuration
└── Makefile             # Convenient commands
```

## Testing

This project uses pytest for testing with the following features:
- Test discovery in `__tests__/` directory
- Coverage reporting
- Parametrized tests
- Fixtures for common test data
- Type checking with mypy

## Running Tests

### Using Make (Recommended)
```bash
make test              # Run all tests
make test-verbose      # Run with detailed output
make test-coverage     # Run with coverage report
make test-watch        # Run in watch mode
```

### Using pytest directly
```bash
pytest                 # Run all tests
pytest -v              # Verbose output
pytest --cov=src       # With coverage
pytest __tests__/array_hash/  # Run specific test directory
pytest __tests__/array_hash/test_two_sum.py  # Run specific test file
```

### Running specific tests
```bash
pytest -k "test_two_sum"           # Run tests matching pattern
pytest -m "not slow"               # Skip slow tests
pytest __tests__/array_hash/ -v    # Run array_hash tests with verbose output
```