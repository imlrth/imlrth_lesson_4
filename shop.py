import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()

####################################################################
               #Shop: отображение страницы товара

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
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# html5_btn = driver.find_element_by_css_selector(".post-181")
# html5_btn.click()
# text_check = WebDriverWait(driver, 20).until(
#         EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".entry-title"),"HTML5 Forms"))
# html5_check = driver.find_element_by_css_selector(".entry-title")
# assert html5_check.text == "HTML5 Forms"
# print("Заголовок книги соответствует 'HTML5 Forms'")
#
# driver.quit()
####################################################################
              #Shop: количество товаров в категории

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
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# HTML_btn = driver.find_element_by_css_selector("li.cat-item-19 > a")
# HTML_btn.click()
# item_count = driver.find_elements_by_css_selector(".product")
# if len(item_count) == 3:
#         print("На странице найдено '3' товара ")
# else:
#         print("Ошибка. Товаров на странице: " + str(len(item_count)))
#
# driver.quit()
####################################################################
                   #Shop: сортировка товаров

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
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# filter_check = driver.find_element_by_class_name("orderby")
# filter_def = filter_check.get_attribute('value')
# assert filter_def == "menu_order"
# print("Выбран вариант сортировки по умолчанию")
# select = Select(filter_check)
# select.select_by_value("price-desc")
# filter_check = driver.find_element_by_class_name("orderby")
# filter_def = filter_check.get_attribute('value')
# assert filter_def == "price-desc"
# print("Выбран вариант сортировки по цене Hight -> Low")
#
# driver.quit()
####################################################################
                   #Shop: отображение, скидка товара

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
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# android_book = driver.find_element_by_css_selector(".post-169")
# android_book.click()
# old_price_check = driver.find_element_by_css_selector("p.price del >.woocommerce-Price-amount")
# old_price_text = old_price_check.text
# assert old_price_text == "₹600.00"
# print("Старая цена книги равна ₹600.00")
# new_price_check = driver.find_element_by_css_selector("p.price ins >.woocommerce-Price-amount")
# new_price_check = new_price_check.text
# assert new_price_check == "₹450.00"
# print("Новая цена книги равна ₹450.00")
# image_check = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, ".zoom")))
# image_check.click()
# image_close_check = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# image_close_check.click()
#
# driver.quit()
####################################################################
                     #Shop: проверка цены в корзине

# driver.get("https://practice.automationtesting.in/")
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# book_html5 = driver.find_element_by_css_selector("[data-product_id='182']")
# book_html5.click()
# time.sleep(3)
# cart_field = driver.find_element_by_class_name("cartcontents")
# cart_count = cart_field.text
# assert cart_count == "1 Item"
# print("количество верное")
# cart_field = driver.find_element_by_class_name("amount")
# cart_amount = cart_field.text
# assert cart_amount == "₹180.00"
# print("верная цена")
# cart_btn = driver.find_element_by_id("wpmenucartli")
# cart_btn.click()
# subtotal_check_element = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, "td[data-title='Subtotal'] >.amount")))
# subtotal_element = driver.find_element(By.CSS_SELECTOR,"td[data-title='Subtotal'] >.amount")
# subtotal = subtotal_element.text
# print("Subtotal = ", subtotal)
# total_check_element = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.order-total > td[data-title='Total'] .woocommerce-Price-amount")))
# total_element = driver.find_element(By.CSS_SELECTOR, "tr.order-total > td[data-title='Total'] .woocommerce-Price-amount")
# total = total_element.text
# print("Total = ", total)
#
# driver.quit()

####################################################################
                         #Shop: работа в корзине

# driver.get("https://practice.automationtesting.in/")
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0, 300);")
# webapp_book = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
# webapp_book.click()
# time.sleep(3)
# data_book = driver.find_element(By.CSS_SELECTOR, "[data-product_id='180']")
# data_book.click()
# time.sleep(3)
# cart_btn = driver.find_element_by_id("wpmenucartli")
# cart_btn.click()
# del_book = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
# time.sleep(3)
# del_book.click()
# time.sleep(3)
# undo_btn = driver.find_element_by_link_text("Undo?")
# undo_btn.click()
# book_count = driver.find_element(By.CSS_SELECTOR, ".input-text.qty.text")
# book_count.clear()
# book_count.send_keys("3")
# update_btn = driver.find_element(By.NAME, "update_cart")
# update_btn.click()
# book_count = driver.find_element(By.CSS_SELECTOR, ".input-text.qty.text")
# book_check = book_count.get_attribute('value')
# assert book_check == '3'
# time.sleep(3)
# coupon_btn = driver.find_element(By.NAME, "apply_coupon")
# coupon_btn.click()
# message_check = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))
# message_win = driver.find_element(By.CLASS_NAME, "woocommerce-error")
# message = message_win.text
# print(message_check)
#
# driver.quit()

####################################################################
                        #Shop: покупка товара

# driver.get("https://practice.automationtesting.in/")
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0, 300);")
# webapp_book = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
# webapp_book.click()
# time.sleep(3)
# cart_btn = driver.find_element_by_id("wpmenucartli")
# cart_btn.click()
# checkout_check = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
# checkout_element = checkout_check.text
# print(checkout_element)
# checkout_btn = driver.find_element(By.CSS_SELECTOR, ".checkout-button")
# checkout_btn.click()
# first_name_check = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
# first_name = driver.find_element(By.ID, "billing_first_name")
# first_name.send_keys("Anton")
# last_name = driver.find_element(By.ID, "billing_last_name")
# last_name.send_keys("Kiselev")
# email = driver.find_element(By.ID, "billing_email")
# email.send_keys("sentinell@mail.ru")
# phone = driver.find_element(By.ID, "billing_phone")
# phone.send_keys("0987654321")
# country_arrow = driver.find_element(By.CLASS_NAME, "select2-arrow")
# country_arrow.click()
# country_selector = driver.find_element(By.ID, "s2id_autogen1_search")
# country_selector.send_keys("Russia")
# country_choice = driver.find_element(By.CLASS_NAME,"select2-result-label")
# country_choice.click()
# address_field = driver.find_element(By.ID, "billing_address_1")
# address_field.send_keys("Lenina 333 st.")
# city_field = driver.find_element(By.ID, "billing_city")
# city_field.send_keys("st. Petersburg")
# country_state = driver.find_element(By.ID, "billing_state")
# country_state.send_keys("Russia")
# postcode_field = driver.find_element(By.ID, "billing_postcode")
# postcode_field.send_keys("89312")
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# pay = driver.find_element(By.ID, "payment_method_cheque")
# pay.click()
# order_btn = driver.find_element(By.ID, "place_order")
# order_btn.click()
# order_check = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# order_element = driver.find_element(By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received")
# order = order_element.text
# assert "Thank you. Your order has been received." == order
# print(order)
# time.sleep(3)
# payments_check = WebDriverWait(driver, 20).until(
#         EC.text_to_be_present_in_element((By.CSS_SELECTOR, "table.shop_table.order_details >tfoot tr:nth-child(3) >td"), "Check Payments"))
# payment_element = driver.find_element(By. CSS_SELECTOR, "table.shop_table.order_details >tfoot tr:nth-child(3) >td")
# payment = payment_element.text
# assert "Check Payments" == payment
# print("Payment Method is :", payment)
#
# driver.quit()

C:/Users/79131/PycharmProjects/pythonProject1/book_store_testing