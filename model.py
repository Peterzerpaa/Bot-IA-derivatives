from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def IA(img_path, model_path, label_path):
    np.set_printoptions(suppress=True)

    # Cargar el modelo
    model = load_model(model_path, compile=False)

    # Cargar etiquetas
    class_names = [line.strip() for line in open(label_path, "r").readlines()]

    # Preparar la imagen
    size = (224, 224)
    image = Image.open(img_path).convert("RGB")
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Convertir a array
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Cargar la imagen en un array
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # Hacer predicción
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Retornar el resultado como string
    return f"Pertenece a {class_name} con un porcentaje de acierto: {confidence_score:.2f}"