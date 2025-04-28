from selenium import webdriver
from selenium.webdriver.common.by import By  # <--- не хватало этого импорта

driver = webdriver.Chrome()
driver.get("https://demoga.com/")

input("Press Enter to continue...")  # Пауза, чтобы ты мог успеть что-то увидеть

# Ищем элемент
try:
    icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
    if icon:
        print('Элемент найден')
except:
    print('Элемент не найден')

driver.quit()