# Real-Time Face Recognition

This Python script utilizes the face_recognition and OpenCV libraries to perform real-time face recognition using your webcam. The code detects faces in the video stream, compares them with pre-encoded faces, and displays the recognized names on the faces in the live feed.

## Features

- Detects faces in real-time using your webcam.
- Compares detected faces with pre-encoded faces of known individuals.
- Displays the names of recognized individuals on the faces in the live video feed.

## Requirements

- Python 3.x
- face_recognition library
- OpenCV (cv2) library

## Usage

1. Install the required libraries:

   ```bash
   pip install face_recognition opencv-python
     ```

2. Run the script:
   ```bash
   python real_time_face_recognition.py
   ```

3. Press 'q' to exit the application.

   
Press 'q' to exit the application.

## Known Faces

The script is pre-configured with known faces and their respective encodings (`person1` and `person2`). If you want to detect and recognize other individuals, follow these steps:

1. Add Images:
   - Add images of the individuals you want to recognize in the project directory.
   - Rename the image files appropriately (e.g., `person3.jpg`, `person4.jpg`).

2. Update Code:
   - Open the script (`real_time_face_recognition.py`) in a text editor.
   - Locate the `known_face_encodings` and `known_face_names` lists.
   - Add the face encodings and names for the new individuals.

   ```python
   # Load images with faces
   image_of_person3 = face_recognition.load_image_file("person3.jpg")
   image_of_person4 = face_recognition.load_image_file("person4.jpg")

   # Encode faces
   person3_face_encoding = face_recognition.face_encodings(image_of_person3)[0]
   person4_face_encoding = face_recognition.face_encodings(image_of_person4)[0]

   known_face_encodings = [person1_face_encoding, person2_face_encoding, person3_face_encoding, person4_face_encoding]
   known_face_names = ["Person 1", "Person 2", "Person 3", "Person 4"]

## License

This project is licensed under the MIT License.

Feel free to use and modify the code as needed. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

