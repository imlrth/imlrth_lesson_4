import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
                     #REGISTRATION
# driver.get("https://practice.automationtesting.in/")
# account_btn = driver.find_element_by_id("menu-item-50")
# account_btn.click()
# mail_field = driver.find_element_by_id("reg_email")
# mail_field.send_keys("sentinell@mail.ru")
# time.sleep(3)
# pass_field = driver.find_element_by_id("reg_password")
# pass_field.send_keys("Q162534r!")
# reg_btn = driver.find_element_by_name("register")
# reg_btn.click()
#
# driver.quit()
#######################################################
                        #LOGIN
# driver.get("https://practice.automationtesting.in/")
# account_btn = driver.find_element_by_id("menu-item-50")
# account_btn.click()
# log_field = driver.find_element_by_id("username")
# log_field.send_keys("sentinell@mail.ru")
# time.sleep(3)
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("Q162534r!")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# logout_check = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
# logout_text = logout_check.text
# assert logout_text == "Logout"
# print ("Элемент 'Logout' найден")
#
# driver.quit()