# Project 1: Your First Steps in Unit Testing

## 🎯 Project Goal
Learn the fundamentals of writing and running unit tests using Python's `pytest` framework to verify that individual functions work correctly.

---

## 📄 General Description
Welcome to your first testing project! 🎉

**Unit testing** is the practice of writing small, focused tests that verify individual pieces (or "units") of your code work as expected. Think of it as checking each ingredient in a recipe before you start cooking—if the ingredients are good, you're more likely to make a great meal.

Unit tests help catch bugs early, make your code more reliable, and give you confidence when making changes. This is a foundational skill for all software developers. In this project, you'll write tests for a simple calculator module.

---

## 🔧 Tools & Technologies
You will need the following:
- **Python 3.8+**
- **pytest** (a popular testing framework for Python)

> 💡 **Tip:** To install pytest, simply run this command in your terminal:
> `pip install pytest`

---

## 📝 Core Tasks

You are provided with the `calculator.py` file in this folder. Your task is to create a new file named `test_calculator.py` and write **at least two tests for each of the four functions** (a total of at least 8 tests).

For each function (`add`, `subtract`, `multiply`, `divide`), you should write:
1.  **A "happy path" test:** Test the function with typical, straightforward inputs (e.g., positive integers).
2.  **An "edge case" test:** Test the function with unusual or boundary inputs to make sure it handles them correctly.

### Specific Test Requirements

* **For `add()`:** Test adding positive numbers and test adding negative numbers or zero.
* **For `subtract()`:** Test simple subtraction and test subtracting a larger number from a smaller one.
* **For `multiply()`:** Test multiplying positive numbers and test multiplying by zero.
* **For `divide()`:**
    * Test a standard division (e.g., `divide(10, 2)` should return `5.0`).
    * **Important:** Write a test that ensures the function correctly raises a `ValueError` when dividing by zero. You must use `pytest.raises()` for this.

**Example for the division-by-zero test:**
```python
import pytest
from calculator import divide # Make sure to import the function

def test_divide_by_zero_raises_error():
    """Checks if the divide function raises ValueError on division by zero."""
    with pytest.raises(ValueError):
        divide(10, 0)


How to Run Your Tests
Once you've written your tests, open your terminal in this folder and run:

Bash

pytest -v

The -v (verbose) flag gives you detailed output about which tests passed or failed.

✅ Acceptance Criteria
Your submission will be considered complete when:

A file named test_calculator.py exists.

The file contains at least 8 tests (2 per function).

All tests pass successfully when you run pytest -v.

The test for divide() correctly uses pytest.raises() to verify the ValueError.

Your code is readable and your test functions have clear, descriptive names.

💡 Bonus Points (Optional)
For an extra challenge:

Learn about parametrized tests using pytest.mark.parametrize. This allows you to run the same test function with multiple different inputs. Try to refactor your add tests into a single parametrized test.

📥 How to Submit
Submit your project using the following workflow:

Create a new Branch in Git named project-1-solution.

Commit and Push your test_calculator.py file to this branch.

Create a Pull Request from your branch to the main branch of the original repository.