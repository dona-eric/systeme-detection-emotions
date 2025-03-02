from django.shortcuts import render
import cv2
import numpy as np
import tensorflow as tf
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators import gzip

# Charger le modèle pré-entraîné
model = tf.keras.models.load_model("../models/modelV0.keras")

# Labels des émotions
emotion_labels = {0: "Colère", 1: "Dégoût", 2: "Peur", 3: "Joie", 4: "Tristesse", 5: "Surprise", 6: "Neutre"}

# Classificateur de visage OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def detect_emotion(frame):
    """ Détecte les visages et leurs émotions sur une frame OpenCV. """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convertir en niveaux de gris
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)  # Détection des visages

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        roi_gray = np.expand_dims(roi_gray, axis=-1)
        roi_gray = np.expand_dims(roi_gray, axis=0)
        roi_gray = roi_gray / 255.0  # Normalisation

        prediction = model.predict(roi_gray)  # Prédiction
        emotion_index = np.argmax(prediction)
        emotion = emotion_labels[emotion_index]

        # Dessiner le rectangle autour du visage
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return frame

def generate_frames():
    """ Génère des frames en temps réel pour le streaming. """
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame = detect_emotion(frame)  # Ajouter la détection d'émotion
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@gzip.gzip_page
def video_feed(request):
    """ Vue pour afficher le streaming vidéo. """
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def index(request):
    """ Vue de la page principale. """
    return render(request, 'emotiscanner/index.html')
