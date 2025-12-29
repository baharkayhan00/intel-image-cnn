import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# Modeli yükle
model = tf.keras.models.load_model("intel_image_model.h5")

# Sınıf isimleri (klasör isimleriyle AYNI sırada)
class_names = [
    "buildings",
    "forest",
    "glacier",
    "mountain",
    "sea",
    "street"
]

def predict_image(image):
    image = image.resize((150, 150))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    predictions = model.predict(image)[0]
    return {class_names[i]: float(predictions[i]) for i in range(len(class_names))}

demo = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil", label="Görüntü Yükle"),
    outputs=gr.Label(num_top_classes=3, label="Tahmin Sonuçları"),
    title="Intel Image Classification CNN",
    description="CNN modeli ile 6 sınıflı görüntü sınıflandırma"
)

demo.launch()
