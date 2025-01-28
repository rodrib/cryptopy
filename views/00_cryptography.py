import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Título de la aplicación
st.title("Criptografía")

# URL de la nueva imagen


# Cargar la imagen desde la URL

image = "cryp2.jpg"


# Agregar la imagen debajo del título
st.image(image, caption="Criptografía", use_column_width=True)

# Título y definición de la criptografía
st.header("Introducción")
st.write("La criptografía es el estudio y la práctica de técnicas seguras de comunicación.")
st.write("Involucra la codificación y decodificación de la información para asegurar la confidencialidad, integridad y autenticidad de los datos.\n")
