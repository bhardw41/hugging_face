#Written by Dr Dirk Colbry

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

from pathlib import Path


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
        print(f"Parsing page {page}")
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
#         driver.close()
    return models
from pathlib import Path


def save_models(models, filename='modelfile.txt', directory='.'):
    path = Path(directory) / filename
    with path.open('w') as file:
        for model in models:
            file.write(f"{model}\n")
        file.close()
    print(f"The list has been saved as a text file at {path}.")




def load_models(filename='modelfile.txt', directory='.'):
    file_path = Path(directory) / filename
    models = []
    with file_path.open('r') as file:
        model_list = [line.strip() for line in file.readlines()]
        models.extend(model_list)
    return models



