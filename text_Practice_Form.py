from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1️⃣ Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.maximize_window()  # Phóng to cửa sổ trình duyệt
driver.get("https://demoqa.com/automation-practice-form")

try:
    # 2️⃣ Nhập dữ liệu mới
    driver.find_element(By.XPATH, "//*[@id='firstName']").send_keys("Van")
    driver.find_element(By.XPATH, "//*[@id='lastName']").send_keys("Dinh")
    driver.find_element(By.XPATH, "//*[@id='userEmail']").send_keys("vandinh@example.com")
    driver.find_element(By.XPATH, "//*[@id='genterWrapper']/div[2]/div[1]").click()
    driver.find_element(By.XPATH, "//*[@id='userNumber']").send_keys("0123456789")

    # 3️⃣ Xử lý quảng cáo (iframe)
    try:
        iframe_ad = driver.find_element(By.XPATH, "//iframe[contains(@id,'google_ads_iframe')]")
        driver.execute_script("arguments[0].style.display='none';", iframe_ad)
    except:
        print("Không tìm thấy quảng cáo")

    # 4️⃣ Chọn ngày sinh bằng JavaScript để tránh lỗi click
    date_input = driver.find_element(By.XPATH, "//*[@id='dateOfBirthInput']")
    driver.execute_script("arguments[0].value = '17 Mar 2025';", date_input)

    driver.find_element(By.XPATH, "//*[@id='subjectsContainer']/div/div[1]").send_keys("Computer Science")
    driver.find_element(By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]").click()
    driver.find_element(By.XPATH, "//*[@id='uploadPicture']").send_keys("/path/to/picture.jpg")
    driver.find_element(By.XPATH, "//*[@id='currentAddress']").send_keys("123 Quảng Ngãi, Việt Nam")
    driver.find_element(By.XPATH, "//*[@id='state']/div/div[2]/div").click()
    driver.find_element(By.XPATH, "//*[@id='stateCity-wrapper']/div[3]").click()

    # 5️⃣ Nhấn nút Submit
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))).click()

    # 6️⃣ Chờ một lúc để xem kết quả
    time.sleep(2)

    # 7️⃣ Kiểm tra dữ liệu có hiển thị đúng không (Assertion)
    success_msg = driver.find_element(By.XPATH, "//div[@class='modal-content']").text
    assert "Van Dinh" in success_msg, "❌ Không tìm thấy dữ liệu vừa nhập!"
    print("✅ Test Passed - Dữ liệu mới đã được thêm thành công!")

except Exception as e:
    print(f"❌ Test Failed - Lỗi: {e}")

finally:
    # 8️⃣ Đóng trình duyệt sau khi kiểm tra xong
    time.sleep(5)
    driver.quit()