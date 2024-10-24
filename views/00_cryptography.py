import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Título de la aplicación
st.title("Criptografía")

# URL de la nueva imagen
image_url = "https://www.fortinet.com/content/fortinet-com/zh_tw/resources/cyberglossary/what-is-cryptography/_jcr_content/par/c05_container_copy_c/par/c28_image_copy_copy.img.jpg/1701209624270.jpg"

# Cargar la imagen desde la URL
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Agregar la imagen debajo del título
st.image(image, caption="Criptografía", use_column_width=True)

# Título y definición de la criptografía
st.header("Introducción")
st.write("La criptografía es el estudio y la práctica de técnicas seguras de comunicación.")
st.write("Involucra la codificación y decodificación de la información para asegurar la confidencialidad, integridad y autenticidad de los datos.\n")
