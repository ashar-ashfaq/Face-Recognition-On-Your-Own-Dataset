import face_recognition
from tqdm import tqdm
import numpy as np
import cv2
import os

os.makedirs('face_encodings', exist_ok=True)

def save_encoding(image_path):
    files = os.listdir(image_path)
    for file in tqdm(files, desc='Saving face encodings'):
        img = cv2.imread(os.path.join(image_path, file))
        if img is None:
            continue

        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb_img)
        identity_name = file.split('.')[0]
        if encodings:
            np.save(f'face_encodings/{identity_name}', encodings[0])