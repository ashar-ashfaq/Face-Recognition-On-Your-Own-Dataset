from load_saved_encodings import load_encodings
from save_encodings import save_encoding
import face_recognition
import cv2

def compare_images(path, encodings, identity_name):
    img = cv2.imread(path)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_location = face_recognition.face_locations(rgb_img)
    face_encoding = face_recognition.face_encodings(rgb_img, face_location)
    for encode, location in zip(face_encoding, face_location):
        matches = face_recognition.compare_faces(encodings, encode, tolerance=0.6)
        name = "Unknown"
        if True in matches:
            index = matches.index(True)
            name = identity_name[index].upper()
        y1, x1, y2, x2 = location
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
        cv2.putText(img, name, (x2, y2 + 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 255), 2)
    cv2.imshow("Face Detection", img)


if __name__ == '__main__':
    choice = input("Do you want to save the encodings of images? (y/n): ").strip().lower()
    if choice == 'y':
        save_encoding('images')
    # image path
    image_path =  'test_samples/andrew ng.jpg'
    identity_names, known_encodings = load_encodings('face_encodings')
    print(f"Loaded classes: {identity_names}")
    compare_images(image_path, known_encodings, identity_names)
    cv2.waitKey(0)