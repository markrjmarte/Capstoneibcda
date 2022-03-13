import numpy as np
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

def predict(img):
    IMAGE_SIZE = 64
    classes = [
    'Common Rust',
    'Eye Spot',
    'Gray Leaf Spot',
    'Northern Leaf Blight',
    'Not Corn Leaf',
    'Southern Rust',
    'Tar Spot',
    'Healthy']
    model_path = r'Model'
    model = load_model(model_path)
    img = Image.open(img)
    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
    img = img_to_array(img)
    img = img.reshape((1, IMAGE_SIZE, IMAGE_SIZE, 3))
    img = img/255.
    class_probabilities = model.predict(x=img)
    class_probabilities = np.squeeze(class_probabilities)
    prediction_index = int(np.argmax(class_probabilities))
    prediction_class = classes[prediction_index]
    prediction_probability = class_probabilities[prediction_index] * 100
    prediction_probability = round(prediction_probability, 2)
    return prediction_class, prediction_probability
