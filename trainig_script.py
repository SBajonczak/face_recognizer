import face_recognition
import os
import numpy as np
from PIL import Image, ImageDraw


# Function to get th images from the folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        if os.path.isfile(img_path):
            images.append(face_recognition.load_image_file(img_path))
    return images

# Function to train the model
def train_face_recognition_model(images_folder):
    # load the images
    face_encodings = []
    labels = []

    for filename in os.listdir(images_folder):
        img_path = os.path.join(images_folder, filename)
        if os.path.isfile(img_path):
            image = face_recognition.load_image_file(img_path)
            face_encoding = face_recognition.face_encodings(image)[0]
            face_encodings.append(face_encoding)
            labels.append(os.path.splitext(filename)[0])  # Use the filename as the label

    return face_encodings, labels


    

# The folder wit the images
images_folder = 'input'
target_image_path = 'test'

# Do the training
known_encoding, labels = train_face_recognition_model(images_folder)

print (target_image_path)
for filename in os.listdir(target_image_path):
        print(filename)
        img_path = os.path.join(target_image_path, filename)
        print(img_path)
        # load image and reconize image
        target_image = face_recognition.load_image_file(img_path)
        face_locations = face_recognition.face_locations(target_image)
        face_encodings = face_recognition.face_encodings(target_image, face_locations)
        
        # open image for drawwing
        pil_image = Image.open(img_path)
        draw = ImageDraw.Draw(pil_image)




        # Check if any of the detected faces match the known faces
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_encoding, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_encoding, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = labels[best_match_index]

            # Draw rectangle and label on the image
            draw.rectangle([left, top, right, bottom], outline="green", width=2)
            draw.text((left, top - 10), name, fill="white")
        pil_image.save(os.path.join("output", filename))