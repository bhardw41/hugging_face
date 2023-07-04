import sys
sys.path.append('./see-segment')

from SEE_hug import list_of_models
from pathlib import Path
import numpy as np
from PIL import Image

print("DONE importing Libraries")

models = list_of_models.fetch_models()
image_names = list(list_of_models.get_imagefiles())

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

if len(sys.argv) < 3:
    imagenum = int(sys.argv[1])
    imagenum = imagenum % len(image_names) # if imagenum > number of images
    print(f"There are {len(image_names)} in the folder")
    imagename,GTname = image_namesS[imagenum]
else:
    imagename = sys.argv[1]
    GTname = sys.argv[2]

print(f"#Running image {imagename} with {GTname} ground truth")

img = Image.open(imagename).convert("RGB")
GT = np.array(Image.open(GTname).convert("RGB"))[:,:,0]

print("images loaded")

results = list_of_models.checkall(img, GT, models)

print("#COMPLETE")
