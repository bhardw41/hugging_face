'''
Huggingface interface
'''
from transformers import pipeline

import matplotlib.pylab as plt
import numpy as npd
from see import Segment_Fitness as sf

def checkall(im, GT, models, display=False):
    fitness = []
    # Iterate over the models and display segmented images
    
    for i, model_name in enumerate(models):
        print(f"Checking model {i} {model_name}")
        # Initialize an image segmentation pipeline
        try:
            segmentation_pipeline = pipeline("image-segmentation", model=model_name)
            outputs = segmentation_pipeline(image)
            inferred_segmentation = outputs[0]['mask']

            # Display the segmented image in the corresponding subplot
            ax = axs[i] if len(models) > 1 else axs
            # ax.imshow(inferred_segmentation)
            fit = sf.FitnessFunction(np.array(inferred_segmentation), GT_image)
            fitness.append(fit[0])
        except Exception as error:
            # handle the exception
            print("An ERROR occurred:", error)
    return fitness