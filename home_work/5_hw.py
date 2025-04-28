# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoSuchElementException
# import time
#
# def find_elements_on_saucedemo():
#
#     options = Options()
#     options.add_argument("--headless")
#     service = Service()
#     driver = webdriver.Chrome(service=service, options=options)
#
#     try:
#         driver.get("https://www.saucedemo.com/")
#         time.sleep(2)
#
#         username = driver.find_element(By.ID, "user-name")
#         password = driver.find_element(By.ID, "password")
#         submit_button = driver.find_element(By.ID, "login-button")
#
#         if username and password and submit_button:
#             print("Элементы найдены")
#
#     except NoSuchElementException:
#         print("Один или несколько элементов не найдены")
#
#     finally:
#         driver.quit()
#
# find_elements_on_saucedemo()


