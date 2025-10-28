# Project 4: End-to-End Testing of a To-Do Web Application

## 🎯 Project Goal
Create a comprehensive test suite that validates all layers of a web application—from backend API endpoints to full user workflows—while achieving high test coverage and demonstrating mastery of modern testing practices.

---

## 📄 General Description
Welcome to the **capstone project** of this course! 🎉

In this final assignment, you will bring together everything you've learned: API testing with `requests`, UI automation with Selenium, and best practices for writing robust automated tests.

You are provided with a simple **Flask-based To-Do List web application** (`app.py`). Your task is to write a complete test suite that validates both the backend API and the end-user experience. You will also measure and report your **test coverage** to ensure your tests are thorough. This project simulates real-world scenarios where QA engineers must validate that all parts of an application work correctly, both individually and together.

---

## 🔧 Tools & Technologies
You will need the following tools and dependencies:
-   **Python 3.8+**
-   **Flask** (the web framework for the application)
-   **pytest** (for organizing and running tests)
-   **requests** (for API testing)
-   **selenium** (for UI automation)
-   **pytest-cov** (for measuring test coverage)

> 💡 **Tip:** Install all dependencies with:
> `pip install flask pytest requests selenium pytest-cov`

---

## 🚦 Getting Started: Running the Application
Before you can test the application, you must run it. Open a terminal in this project's folder and run:
```bash
python app.py

This will start the Flask development server. Your application will be running at http://127.0.0.1:5000/. Your UI tests should point to this address. You will need to keep this terminal running while you execute your tests.


📝 Core Tasks
You will create a comprehensive test suite that includes three types of tests.

1. API Tests (Backend Testing)
Create a file named test_api.py. In this file, use the requests library to directly test the REST API endpoints. Your tests must run against the running application (http://127.0.0.1:5000).

GET /tasks: Write a test that sends a GET request to /tasks. Assert that the status code is 200 and the response is a JSON list.

POST /tasks: Write a test that sends a POST request with a JSON payload like {"task": "Write API tests"}. Assert that the status code is 201 and the response contains the new task with an id.

DELETE /tasks/<id>: Write a test that first adds a task (via POST), gets its ID, then sends a DELETE request for that ID. Assert the status code is 204 (No Content).

2. End-to-End UI Test (Full User Scenario)
Create a file named test_ui.py. In this file, use Selenium to simulate a complete user interaction.

Your test should automate the following scenario:

1.Open the browser and navigate to http://127.0.0.1:5000/.

2.Find the task input field, type in a new task (e.g., "Buy milk"), and click the "Add Task" button.

3.Assert that the new task ("Buy milk") appears in the task list on the page.

4.Find the "Delete" button next to that specific task and click it.

5.Assert that the task is removed from the list and no longer visible.

Test Coverage Report
After completing your test suite, you must measure your test coverage.

1.Run your tests using pytest-cov. This command runs all your pytest files and measures how many lines of app.py were executed:
Bash

pytest --cov=app

2.Review the output. Your test suite must achieve at least 85% test coverage for the app.py file.

✅Acceptance Criteria
Your project submission will be considered complete when:

A test_api.py file exists with at least three tests covering GET, POST, and DELETE.

A test_ui.py file exists with the complete end-to-end user scenario.

All your tests pass successfully when you run pytest -v.

Your test coverage for app.py is at least 85%.

Your code is well-organized, readable, and follows good testing practices.

💡 Bonus Points (Optional)
For extra credit, try one or more of the following challenges:

Write a test for the edge case where a user tries to add an empty task (blank input). Verify that the API returns a 400 error and the UI displays an error.

Achieve 95% or higher test coverage.

(Advanced) Refactor your tests to use pytest fixtures to manage setup and teardown (e.g., creating a test client or starting the Selenium driver).

📥 How to Submit
Submit your project using the following workflow:

Create a new Branch in Git named project-4-solution.

Commit and Push your test_api.py and test_ui.py files to this branch.

Create a Pull Request from your branch to the main branch of the original repository.