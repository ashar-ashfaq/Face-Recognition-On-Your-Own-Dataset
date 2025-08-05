import os
import numpy as np

def load_encodings(encoding_path):
    images_encodings = []
    identity_names = []
    for file in os.listdir(encoding_path):
        if file.endswith(".npy"):
            encoding = np.load(os.path.join(encoding_path, file))
            images_encodings.append(encoding)
            identity_names.append(file.split('.')[0])
    if len(images_encodings) == 0:
        print('No encodings available')
        return [], []
    return identity_names, images_encodings