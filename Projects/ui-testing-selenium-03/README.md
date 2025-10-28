# پروژه ۳: اتوماسیون فرآیند ورود در یک وب اپلیکیشن

## 🎯 هدف پروژه
یادگیری نحوه خودکارسازی تعاملات کاربر در یک وب‌سایت واقعی با استفاده از Selenium WebDriver و اعتبارسنجی عملکرد فرآیند ورود از طریق تست‌های خودکار رابط کاربری (UI).

---

## 📄 شرح کلی
در این پروژه، شما از **Selenium WebDriver** برای خودکارسازی و تست فرآیند ورود در وب‌سایت آزمایشی **[SauceDemo](https://www.saucedemo.com)** استفاده خواهید کرد.

تست خودکار رابط کاربری به ما اجازه می‌دهد تا اعمال واقعی یک کاربر — مانند تایپ کردن، کلیک روی دکمه‌ها و بررسی تغییرات صفحه — را شبیه‌سازی کنیم تا مطمئن شویم که وب اپلیکیشن طبق انتظار عمل می‌کند. Selenium یک ابزار قدرتمند برای این کار است که به تسترها و توسعه‌دهندگان امکان تعامل مستقیم با المان‌های وب در مرورگرهای واقعی را می‌دهد. با تکمیل این پروژه، شما تجربه عملی در نوشتن و ساختاربندی تست‌های خودکار مرورگر و اعتبارسنجی سناریوهای ورود موفق و ناموفق را کسب خواهید کرد.

---

## 🔧 ابزارها و تکنولوژی‌ها
برای انجام این پروژه به موارد زیر نیاز دارید:
- **پایتون 3.8+**
- **pytest** (برای سازماندهی و اجرای تست‌ها)
- **selenium** (برای کنترل کردن مرورگر)
- **ChromeDriver** (یا WebDriver مخصوص مرورگر دیگرتان)

> 💡 **نکته:** می‌توانید پکیج‌های پایتون را با دستور `pip install pytest selenium` نصب کنید.

---

## 🚦 نحوه راه‌اندازی اولیه (بسیار مهم)
راه‌اندازی Selenium برای اولین بار نیاز به یک مرحله اضافی دارد:
۱. **نصب WebDriver:** شما باید WebDriver مخصوص مرورگر خود را دانلود کنید. برای مثال، اگر از گوگل کروم استفاده می‌کنید، باید **ChromeDriver** را از [این لینک](https://googlechromelabs.github.io/chrome-for-testing/) دانلود کنید.
۲. **تطابق نسخه:** حتماً نسخه‌ای از WebDriver را دانلود کنید که با **نسخه مرورگر** شما مطابقت داشته باشد.
۳. **قرار دادن در PATH:** ساده‌ترین راه این است که فایل اجرایی WebDriver (مثلاً `chromedriver.exe`) را در مسیری قرار دهید که در `PATH` سیستم‌عامل شما تعریف شده باشد.

---

## 📝 تسک‌های اصلی

شما باید یک مجموعه تست به نام `test_login.py` ایجاد کنید که شامل سناریوهای خودکار زیر باشد.

### ۱. تست ورود موفق
مراحل خودکارسازی:
1.  مرورگر را باز کرده و به آدرس `https://www.saucedemo.com` بروید.
2.  فیلدهای ورودی **نام کاربری** و **رمز عبور** را پیدا کنید.
3.  اطلاعات کاربری معتبر زیر را وارد کنید:
    -   **نام کاربری:** `standard_user`
    -   **رمز عبور:** `secret_sauce`
4.  روی دکمه **Login** کلیک کنید.
5.  با بررسی اینکه URL صفحه حاوی `/inventory.html` است، از موفقیت‌آمیز بودن ورود اطمینان حاصل کنید (Assert).

### ۲. تست ورود ناموفق (رمز عبور اشتباه)
مراحل خودکارسازی:
1.  به آدرس `https://www.saucedemo.com` بروید.
2.  فیلدهای ورودی **نام کاربری** و **رمز عبور** را پیدا کنید.
3.  اطلاعات کاربری نامعتبر زیر را وارد کنید:
    -   **نام کاربری:** `standard_user`
    -   **رمز عبور:** `wrong_password`
4.  روی دکمه **Login** کلیک کنید.
5.  با بررسی اینکه یک پیام خطا در صفحه ظاهر می‌شود، از ناموفق بودن ورود اطمینان حاصل کنید.
6.  بررسی کنید که متن خطا دقیقاً برابر با عبارت زیر است:
    `"Epic sadface: Username and password do not match any user in this service"`

> **راهنمایی:** برای پیدا کردن المان‌ها می‌توانید از `id` یا `css selector` استفاده کنید. برای مثال، فیلد نام کاربری دارای `id="user-name"` است.

---

## 🚀 نمونه کد برای شروع
می‌توانید از این قطعه کد به عنوان الگویی برای تست اول خود استفاده کنید:

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
    driver = webdriver.Chrome()

    # 2. Navigate to the login page
    driver.get("[https://www.saucedemo.com](https://www.saucedemo.com)")

    # 3. Find elements and enter credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # 4. Click the login button
    driver.find_element(By.ID, "login-button").click()

    # 5. Assert the URL has changed
    time.sleep(1) # Simple wait to let the page load
    assert "/inventory.html" in driver.current_url

    # 6. Close the browser
    driver.quit()

    