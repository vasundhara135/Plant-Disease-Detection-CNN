
import json
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿"
)

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("plant_disease_model.h5", compile=False)

with open("class_names.json", "r") as f:
    class_names = json.load(f)

model = load_model()

st.title("🌿 Plant Disease Detection")
st.write("Upload a plant leaf image to predict its disease class.")

uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded leaf image", width=300)

    resized_image = image.resize((128, 128))
    image_array = np.array(resized_image, dtype=np.float32)
    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array, verbose=0)[0]
    predicted_index = int(np.argmax(predictions))

    st.subheader("Prediction")
    st.write(class_names[predicted_index])
    st.write(f"Model confidence: {predictions[predicted_index] * 100:.2f}%")
