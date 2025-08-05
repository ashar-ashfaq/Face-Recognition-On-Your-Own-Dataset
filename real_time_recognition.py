from load_saved_encodings import load_encodings
from save_encodings import save_encoding
import face_recognition
import cv2


if __name__ == '__main__':
    choice = input("Do you want to save the encodings of images? (y/n): ").strip().lower()
    if choice == 'y':
        save_encoding('images')

    # path for saved encodings
    identity_name, known_encodings = load_encodings('face_encodings')
    print(f"Loaded classes: {identity_name}")

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_location = face_recognition.face_locations(rgb_frame)
        face_encoding = face_recognition.face_encodings(rgb_frame, face_location)

        for encode, location in zip(face_encoding, face_location):
            matches = face_recognition.compare_faces(known_encodings, encode, tolerance = 0.6)
            name = "Unknown"
            if True in matches:
                index = matches.index(True)
                name = identity_name[index].upper()
            y1, x1, y2, x2 = location
            cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,255), 2)
            cv2.putText(frame, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255), 2)
        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

