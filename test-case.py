from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo WebDriver
driver = webdriver.Chrome()

try:
    # 1. Truy cập Wikipedia
    driver.get("https://www.wikipedia.org/")

    # 2. Click chọn ngôn ngữ tiếng Việt
    vietnamese_link = driver.find_element(By.CSS_SELECTOR, "a[id='js-link-box-vi']")
    vietnamese_link.click()

    # 3. Chờ vài giây để trang load
    time.sleep(3)

    # 4. Kiểm tra xem đã chuyển sang Wikipedia tiếng Việt chưa
    if "Wikipedia tiếng Việt" in driver.title:
        print("Test Passed: Đã chuyển sang trang tiếng Việt!")
    else:
        print("Test Failed: Không chuyển đúng trang!")

finally:
    # 5. Đóng trình duyệt
    time.sleep(5)
    driver.quit()
