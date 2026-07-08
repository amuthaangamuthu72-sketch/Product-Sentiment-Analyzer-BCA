from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_reviews(product):

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    url = f"https://www.amazon.in/s?k={product}"

    driver.get(url)

    time.sleep(5)

    reviews = []

    try:
        titles = driver.find_elements(
            By.CSS_SELECTOR,
            "h2"
        )

        for item in titles[:10]:
            text = item.text

            if text:
                reviews.append(text)

    except:
        pass

    driver.quit()

    return reviews