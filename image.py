import argparse
import re
import cv2
import numpy as np
from keras.models import load_model

saved_models_path = "C:/Users/Kannan kailash/OneDrive/Desktop/Cubethon/Facial Emotional Reg/models/saved_models/"
model_name = "fer2013_simple_CNN-e88-a0.65.hdf5"


def detect_classify_display(frame, model):
    emotions = ['angry', 'disgust', 'fear',
                'happy', 'sad', 'surprise', 'neutral']
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        frame_gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    for (x, y, w, h) in faces:
        face = frame_gray[y:y+h, x:x+w]
        face = cv2.resize(face, (48, 48)) / 255
        face = np.expand_dims(face, axis=0)
        face = np.expand_dims(face, axis=-1)

        predictions = model.predict(face)
        pred = np.argmax(predictions)
        prob = predictions[0, pred] * 100
        frame = cv2.rectangle(
            frame, (x, y), (x + w, y + h), (255, 255, 255), 4)
        cv2.putText(frame, emotions[pred] + f'   {prob:.2f}%',
                    (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 3)
    cv2.imshow('Emotion recognition', frame)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image Emotion Detection')
    parser.add_argument('--model_path', help='Path to model.', default='models/saved_models/fer2013_resnet50_1-e41-a0.71.hdf5')
    args = parser.parse_args()

    # Loading model
    model_path = args.model_path
    model = load_model(saved_models_path + model_name)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

    # Provide the path to the image here
    image_path = "C:\Users\Kannan kailash\OneDrive\Desktop\Cubethon\Facial Emotional Reg\pexels-simon-robben-614810.jpg"

    frame = cv2.imread(image_path)
    if frame is None:
        print('Error loading the image.')
        exit(1)

    detect_classify_display(frame, model)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
