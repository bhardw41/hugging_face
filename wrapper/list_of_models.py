#Written by Dr Dirk Colbry

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_models():
    install_path = ChromeDriverManager().install()
    #Setup Chrome driver 
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome()
    # executable_path=install_path
    time.sleep(10)
    from bs4 import BeautifulSoup

    nummodels = 10
    page = 0;
    models = set()
    while nummodels > 0:
        print(f"Parcing page {page}")
        url = f"https://huggingface.co/models?pipeline_tag=image-segmentation&p={page}&sort=downloads"
        driver.get(url)
        time.sleep(5)
        body = driver.page_source
        soup = BeautifulSoup(body, 'html.parser')
        h4s= soup.find_all('h4')

        for h4 in h4s:
            models.add(h4.get_text())

        nummodels = len(h4s)
        page = page + 1
    return models