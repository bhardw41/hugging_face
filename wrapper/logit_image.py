import cv2
import numpy as np
def logits_to_image(image, logits):
    logits_mask = np.zeros(list(logits.shape[2:4]))
    for label in range(logits.shape[1]):
        thislabel = logits[0,label,:,:].detach().numpy()
        logits_mask[thislabel > 0] = label
    mask = cv2.resize(logits_mask, dsize=image.size, interpolation=cv2.INTER_CUBIC)
    return mask