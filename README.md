# Incubyte TDD Assessment - String Calculator

This project demonstrates Test-Driven Development (TDD) practices through the implementation of a String Calculator kata.

## Requirements

- Python 3.11 or higher
- pip (Python package manager)

## Setup

### 1. Verify Python 3.11 Installation

```bash
python3.11 --version
# Should output: Python 3.11.x

# Clone the repository
git clone git@github.com:dexterpuru/incubyte-tdd-assessment.git/ tdd-assessment-pratyaksh
cd tdd-assessment-pratyaksh

# Create virtual environment with Python 3.11
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Verify Python version in virtual environment
python --version  # Should show Python 3.11.x

# Install dependencies
pip install -r requirements.txt

## Running Tests
pytest --html=tests/reports/test-report-$(date +%Y-%m-%d_%H-%M-%S).html --cov=string_calculator --cov-report=html:tests/reports/htmlcov-$(date +%Y-%m-%d_%H-%M-%S) --cov-report=term-missing
# Reports Location: /tests/reports/test-report-*.html
```