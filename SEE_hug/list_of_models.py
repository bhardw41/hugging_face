import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

from transformers import pipeline

import matplotlib.pylab as plt
import numpy as npd
from see import Segment_Fitness as sf

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
    driver.close()
    return models



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

def fetch_models(modelfile= 'modelfile.txt'):
    model_file = Path(modelfile)
    if model_file.is_file():
        models = load_models(modelfile)
    else:
        models = get_models()
        save_models(models, modelfile)
    return models

def checkall(image, GT_image, models, display=False):
    fitness = []
    # Iterate over the models and display segmented images
    
    if display:
        fig, axs = plt.subplots(1, len(models))
    
    for i, model_name in enumerate(models):
        print(f"Checking model {i} {model_name}")
        # Initialize an image segmentation pipeline
        try:
            segmentation_pipeline = pipeline("image-segmentation", trust_remote_code=True, model=model_name)
            outputs = segmentation_pipeline(image)
            inferred_segmentation = outputs[0]['mask']

            # Display the segmented image in the corresponding subplot
            if display:
                ax = axs[i] if len(models) > 1 else axs
                ax.imshow(inferred_segmentation)
            fit = sf.FitnessFunction(np.array(inferred_segmentation), GT_image)
            print(f"#FITNESS {fit}, {mdoel_name}")
            fitness.append(fit[0])
        except Exception as error:
            # handle the exception
            print("An ERROR occurred:", error)
    return fitness
