# Project 2: Validating an Online Movie Information Service

## 🎯 Project Goal
To practice writing automated tests that verify the correctness and reliability of a public API, using Python’s `pytest` framework and the `requests` library.

---

## 📄 General Description
In this project, you will explore **API testing** by interacting with the **OMDb API**, a free online movie database. Your task is to write automated tests that send HTTP requests to the API and validate the responses.

API testing is essential in modern software development because it ensures that web services return accurate data and handle error cases properly. By completing this project, you’ll gain hands-on experience with RESTful APIs, learn how to verify response data, and understand how to deal with different types of responses (success, failure, and unauthorized access).

---

## 🔧 Tools & Technologies
You will need the following tools and dependencies:
-   **Python 3.8+**
-   **pytest** (for running test cases)
-   **requests** (for sending HTTP requests)
-   A **free OMDb API key** (register at [omdbapi.com](https://www.omdbapi.com) to obtain one)

> 💡 **Tip:** Install the required packages with:
> `pip install pytest requests`

---

## 📝 Core Tasks

You will create a test suite named `test_omdb_api.py` that contains at least the following tests:

1.  **Successful Movie Search:**
    * Send a `GET` request to the OMDb API searching for a known movie, for example, `"Inception"`.
    * Assert that the HTTP status code is `200`.
    * Verify that the `"Title"` key in the JSON response matches `"Inception"`.

2.  **Failed Movie Search (Non-Existent Movie):**
    * Search for a random, non-existent movie title (e.g., `"ThisMovieDoesNotExist123"`).
    * Assert that the HTTP status code is `200` (the request is valid, but the movie was not found).
    * Check that the JSON response contains `"Response": "False"`.

3.  **Invalid API Key:**
    * Intentionally use an invalid API key in your request.
    * Assert that the HTTP status code is `401` (Unauthorized).
    * Optionally, verify that the response contains a relevant error message (e.g., `"Invalid API key!"`).

---

## 🚀 Getting Started: Code Sample
You can use this code snippet as a template for your first test:

```python
# test_omdb_api.py
import requests

API_KEY = "YOUR_API_KEY_HERE" # Place your API Key here
BASE_URL = "[http://www.omdbapi.com/](http://www.omdbapi.com/)"

def test_successful_movie_search():
    """
    Tests if a known movie can be found successfully.
    """
    params = {
        "apikey": API_KEY,
        "t": "Inception"
    }
    response = requests.get(BASE_URL, params=params)
    
    # 1. Check the status code
    assert response.status_code == 200
    
    # 2. Parse the JSON response
    response_data = response.json()
    
    # 3. Check the content
    assert response_data["Response"] == "True"
    assert response_data["Title"] == "Inception"


⚠️ Important Security Note: Never commit API keys, passwords, or other sensitive credentials directly into your code and push them to GitHub! In a real-world scenario, this information is securely managed using Environment Variables. For this academic project, placing the key in the file is acceptable, but always remember this critical best practice. 

✅ Acceptance Criteria :

Your submission will be considered complete when:

A file named test_omdb_api.py is included in your project.

All three core test scenarios are implemented and pass when executed.

Each test includes clear assertions checking both status codes and response content.

Your code follows good testing practices (readable, properly named functions, minimal duplication).

💡 Bonus Points (Optional):

For an optional challenge and extra credit:

Write a test that searches for a movie using a specific year parameter (e.g., "Inception" from 2010) and validates that the returned data matches the year provided.

📥 How to Submit
Submit your project using the following workflow:

Create a new Branch in Git named project-2-solution.

Commit and Push your code to this branch.

Create a Pull Request from your branch to the main branch of the original repository.

Happy Testing! 🧪
_______________________________________________________________________________
