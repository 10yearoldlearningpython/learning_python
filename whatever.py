import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.northerntool.com/shop/tools/category_clearance_0_96_P-SalesRank%7C1")
driver.implicitly_wait(8)
cards = driver.find_elements(By.CSS_SELECTOR, ".prod-listing")
for card in cards:
    title = card.find_element(By.CSS_SELECTOR, ".title")
    print(title.text)

    price = card.find_element(By.CSS_SELECTOR, ".sale-price-med")
    price = price.text.replace("Sale $", "")
    print(price)

    reg = card.find_element(By.CSS_SELECTOR, ".was-price")
    reg = reg.text.replace("Reg. $", '')
    print(reg)

    try:
        sale = float(price) / float(reg)
        print(sale)
    except:
        print()
