import time
import csv
import sys
import pandas as pd
from selenium import webdriver

import matplotlib.pyplot as plt
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

url = "https://www.divan.ru/category/promo-dostavim-bystro-moscow?types%5B%5D=1"
driver.get(url)

# Задержка для загрузки страницы
time.sleep(10)

# Явное ожидание
name_element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'span[itemprop="name"]'))
)

# Поиск цен на диваны
prices = []

products = driver.find_elements(By.CLASS_NAME, 'lsooF')
print("Найдено продуктов:", len(products))
if products == 0:
    sys.exit()

parsed_data = []

for product in products:
    try:
        name_element = driver.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]')
        product_name = name_element.text

        print(product_name)  # Выводим название продукта

        price = product.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')

        parsed_data.append([product_name, price])
        print(parsed_data)
    except Exception as e:
        print("Нет такого элемента:", e)
        continue

    driver.quit()

    with open("divans.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Название товара', 'Цена'])
        writer.writerows(parsed_data)

for product in products:
    price_text = product.text.replace('₽', '').replace(' ', '')
    if price_text.isdigit():
        prices.append(int(price_text))



# Сохранение данных в CSV файл
df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('divan_prices.csv', index=False)

# Нахождение средней цены
average_price = df['Price'].mean()
print(f'Средняя цена на диваны: {average_price} ₽')

# Построение гистограммы цен
plt.hist(df['Price'], bins=20, alpha=0.7, color='blue', edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Закрытие браузера
driver.quit()