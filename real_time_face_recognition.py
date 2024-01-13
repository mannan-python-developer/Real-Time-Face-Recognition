import face_recognition
import cv2

# Load images with faces
image_of_person1 = face_recognition.load_image_file("person1.jpg")
image_of_person2 = face_recognition.load_image_file("person2.jpg")

# Encode faces
person1_face_encoding = face_recognition.face_encodings(image_of_person1)[0]
person2_face_encoding = face_recognition.face_encodings(image_of_person2)[0]

known_face_encodings = [person1_face_encoding, person2_face_encoding]
known_face_names = ["Person 1", "Person 2"]

# Open the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture each frame from the webcam
    _, frame = video_capture.read()

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known face
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match is found, use the name of the known face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a rectangle and display the name on the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Real Time Face Recognition', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
