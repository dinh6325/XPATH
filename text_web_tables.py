from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1️⃣ Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.maximize_window()  # Phóng to cửa sổ trình duyệt
driver.get("https://demoqa.com/webtables")

try:
    # 2️⃣ Nhập dữ liệu mới
    driver.find_element(By.XPATH, "//*[@id='addNewRecordButton']").click()
    driver.find_element(By.XPATH, "//*[@id='firstName']").send_keys("Dinh")
    driver.find_element(By.XPATH, "//*[@id='lastName']").send_keys("van")
    driver.find_element(By.XPATH, "//*[@id='userEmail']").send_keys("dinhvan@example.com")
    driver.find_element(By.XPATH, "//*[@id='age']").send_keys("30")
    driver.find_element(By.XPATH, "//*[@id='salary']").send_keys("5000")
    driver.find_element(By.XPATH, "//*[@id='department']").send_keys("IT")

    # 3️⃣ Nhấn nút Submit
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))).click()

    # 4️⃣ Chờ một lúc để xem kết quả
    time.sleep(2)

    # 5️⃣ Kiểm tra dữ liệu có hiển thị đúng không (Assertion)
    rows = driver.find_elements(By.XPATH, "//div[@class='rt-tr-group']")
    found = False
    for row in rows:
        if "Dinh" in row.text and "van" in row.text:
            found = True
            break

    assert found, "❌ Không tìm thấy dữ liệu vừa nhập!"
    print("✅ Test Passed - Dữ liệu mới đã được thêm thành công!")

except Exception as e:
    print(f"❌ Test Failed - Lỗi: {e}")

finally:
    # 6️⃣ Đóng trình duyệt sau khi kiểm tra xong
    time.sleep(5)
    driver.quit()
