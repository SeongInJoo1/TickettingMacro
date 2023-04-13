

from selenium import webdriver
from selenium.webdriver.common.by import By

print("이메일을 입력하세요:")
email = input("Email: ")
print("이름을 입력하세요:")
name = input("Name: ")
print("전화번호를 입력하세요:")
phone = input("Phone Number: ")
print("나이를 입력하세요:")
age = input("Age: ")
print("좌석번호를 입력하세요: ")
seat = input("Seat: ")


driver = webdriver.Chrome()
driver.get("http://tornadooo.store/index/")

driver.implicitly_wait(5)

while (1):
    driver.find_element(By.CSS_SELECTOR, '.destinations_container.item_grid .destination.item .destination_image').click()
    driver.find_element(By.CSS_SELECTOR, 'body > center > div > button').click()
    driver.find_element(By.CSS_SELECTOR, '#id_email').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, '[id="id_name"]').send_keys(name)
    driver.find_element(By.CSS_SELECTOR, '[id="id_mobile"]').send_keys(phone)
    driver.find_element(By.CSS_SELECTOR, '[id="id_age"]').send_keys(age)
    driver.find_element(By.CSS_SELECTOR, '[id="id_seats"]').send_keys(seat)
    driver.find_element(By.CSS_SELECTOR, '.btn').click()
    driver.find_element(By.CSS_SELECTOR, 'h3').click()

