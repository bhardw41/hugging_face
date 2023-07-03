import sys
sys.path.append('./see-segment')

from SEE_hug import list_of_models
from pathlib import Path
import numpy as np
from PIL import Image

models = list_of_models.fetch_models()

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

img = Image.open(sys.argv[1]).convert("RGB")
GT = np.array(Image.open(sys.argv[2]).convert("RGB"))[:,:,0]

results = list_of_models.checkall(img, GT, models)
