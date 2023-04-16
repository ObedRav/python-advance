import cv2
import face_recognition
import os
from gtts import gTTS

# Make sure that the haarcascade_smile.xml file exists in the same directory as this script
smile_cascade_path = os.path.join(os.path.dirname(__file__), "haarcascade_smile.xml")
if not os.path.exists(smile_cascade_path):
    raise Exception("Unable to find smile cascade file")

# Load the cascade classifier for smile detection
smile_cascade = cv2.CascadeClassifier(smile_cascade_path)

# Get the video capture device
video_capture = cv2.VideoCapture(0)

# Loop through each frame in the video
while True: 
    # Capture the frame
    ret, frame = video_capture.read()
    
    # Convert the frame from BGR (OpenCV) to RGB (face_recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find the faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)

    # Loop through each face in the frame
    for (top, right, bottom, left) in face_locations:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Crop the face image
        face_image = frame[top:bottom, left:right]

        # Convert the face image from BGR (OpenCV) to RGB (face_recognition)
        face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

        # Detect smiles in the face image
        face_image_gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
        smile = smile_cascade.detectMultiScale(face_image_gray, scaleFactor=1.5, minNeighbors=15)
        
        # If a smile is detected, do something
        if len(smile) > 0:
            # Do something, e.g. print a message or play a sound
            tts = gTTS('You smiled!')
            tts.save('hello.mp3')
            os.system('mpg321 hello.mp3')
    
    # Display the resulting image
    cv2.imshow('Video', frame)
    
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close the window
video_capture.release()
cv2.destroyAllWindows()
