# Project 3: Automating the Login Process of a Web Application

## 🎯 Project Goal
Learn how to automate web-based user interactions using Selenium WebDriver and validate the behavior of a login workflow through automated UI tests.

---

## 📄 General Description
In this project, you will use **Selenium WebDriver** to automate and test the login process of the demo website **[SauceDemo](https://www.saucedemo.com)**.

UI automation testing allows us to simulate real user actions—such as typing input, clicking buttons, and verifying screen updates—to ensure that web applications behave as expected. Selenium is a powerful tool for this purpose, enabling you to interact directly with web elements in real browsers. By completing this assignment, you’ll gain practical experience in writing automated browser tests.

---

## 🔧 Tools & Technologies
You will need the following tools and dependencies:
-   **Python 3.8+**
-   **pytest** (for organizing and running the automated tests)
-   **selenium** (for controlling the browser)
-   **ChromeDriver** (WebDriver for Chrome)

> 💡 **Tip:** Install the required packages with:
> `pip install pytest selenium`

---

## 🚦 Getting Started: WebDriver Setup (Important!)
Selenium requires a "WebDriver" to communicate with a browser.
1.  **Download ChromeDriver:** You must download the ChromeDriver that **matches your version of Google Chrome**. You can find the correct version at the [Chrome for Testing dashboard](https://googlechromelabs.github.io/chrome-for-testing/).
2.  **Place the Driver:** Unzip the download. The easiest way to get started is to place the `chromedriver.exe` (or `chromedriver` on Mac/Linux) in the **same folder** as your `test_login.py` file.

---

## 📝 Core Tasks

You will create a test suite named `test_login.py` that contains the automated scenarios below.

### 1. Test a Successful Login
Steps to automate:
1.  Open the browser and navigate to `https://www.saucedemo.com`.
2.  Find the **username** and **password** input fields.
3.  Enter the following valid credentials:
    * **Username:** `standard_user`
    * **Password:** `secret_sauce`
4.  Click the **Login** button.
5.  Assert that the login was successful by checking that the page URL contains `/inventory.html`.

### 2. Test a Failed Login (Wrong Password)
Steps to automate:
1.  Navigate to `https://www.saucedemo.com`.
2.  Find the **username** and **password** input fields.
3.  Enter the following invalid credentials:
    * **Username:** `standard_user`
    * **Password:** `wrong_password`
4.  Click the **Login** button.
5.  Assert that the login failed by verifying that an error message appears.
6.  Check that the error text matches exactly:
    `"Epic sadface: Username and password do not match any user in this service"`

> **Hints for finding elements:**
> * Username field: `id="user-name"`
> * Password field: `id="password"`
> * Login button: `id="login-button"`
> * Error message: `css selector="h3[data-test='error']"`

---

## 🚀 Getting Started: Code Sample
You can use this code snippet as a template for your first test:

```python
# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_successful_login():
    """
    Tests the successful login workflow for the SauceDemo website.
    """
    # 1. Initialize the WebDriver
    # Assumes 'chromedriver' is in the same folder or in your system's PATH
    driver = webdriver.Chrome()

    # 2. Navigate to the login page
    driver.get("[https://www.saucedemo.com](https://www.saucedemo.com)")

    # 3. Find elements and enter credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # 4. Click the login button
    driver.find_element(By.ID, "login-button").click()

    # 5. Assert the URL has changed (wait a moment for the page to load)
    time.sleep(1) 
    assert "/inventory.html" in driver.current_url

    # 6. Close the browser
    driver.quit()


✅ Acceptance Criteria

Your submission will be considered complete when:

A file named test_login.py exists and contains both required tests.

Tests are implemented using pytest functions (e.g., def test_successful_login():).

Each test launches a browser, interacts with web elements, and performs meaningful assertions.

Proper element locators are used (id, name, or css selector).

The test suite closes the browser instance at the end of each test (using driver.quit()).

All tests pass successfully when you run pytest -v.

💡 Bonus Points (Optional)
For an optional challenge and extra credit:

After a successful login, write a test that adds an item to the shopping cart and verifies that the cart icon updates to show "1".

📥 How to Submit
Submit your project using the following workflow:

Create a new Branch in Git named project-3-solution.

Commit and Push your code to this branch.

Create a Pull Request from your branch to the main branch of the original repository.