import streamlit as st
from PIL import Image
import numpy as np
import requests
from io import BytesIO

st.title("Ofuscador y Esteganografía")

def cargar_imagen_desde_url(url):
    if not url:
        st.warning("Por favor, ingrese una URL válida.")
        return None

    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        imagen = Image.open(BytesIO(respuesta.content))
        return imagen
    else:
        st.warning(f"No se pudo cargar la imagen desde la URL. Código de estado: {respuesta.status_code}")
        return None

def ofuscar_imagen(imagen):
    # Convertir la imagen a un arreglo NumPy
    array_imagen = np.array(imagen)

    # Cambiar los valores de los píxeles (ofuscación simple)
    array_imagen = array_imagen + 50  # Puedes ajustar este valor según tus necesidades

    # Crear una nueva imagen a partir del arreglo NumPy modificado
    nueva_imagen = Image.fromarray(array_imagen)

    return nueva_imagen

def reemplazar_letras(texto):
    reemplazos = {'e': '3', 'a': '4', 'o': '0', 'i': '1', 'u': '_'}
    texto_ofuscado = ''.join(reemplazos.get(char, char) for char in texto)
    return texto_ofuscado

# Selector de función
seleccion = st.radio("Seleccione una función:", ["Ofuscador de Texto", "Esteganografía"])

if seleccion == "Ofuscador de Texto":
    st.subheader("Ofuscador de Texto")
    texto_original = st.text_area("Ingrese el texto original:")
    if st.button("Ofuscar Texto"):
        texto_ofuscado = reemplazar_letras(texto_original)
        st.write(f"Texto Ofuscado: {texto_ofuscado}")

elif seleccion == "Esteganografía":
    st.subheader("Esteganografía")
    st.write("La esteganografía oculta mensajes secretos dentro de archivos 'contenedores', como imágenes, audio o video.")
    st.write("Esta ocultación implica ajustar ligeramente los bits del archivo portador para codificar el mensaje, manteniendo la apariencia normal del archivo.")

    # Selector de carga de imagen
    carga_local = st.checkbox("Cargar imagen localmente")
    if carga_local:
        imagen_original = st.file_uploader("Seleccione una imagen:", type=["jpg", "jpeg", "png"])
    else:
        url_imagen = st.text_input("Ingrese la URL de la imagen:")
        imagen_original = cargar_imagen_desde_url(url_imagen)

    # Botón para ofuscar la imagen
    if st.button("Ofuscar Imagen") and imagen_original:
        if carga_local:
            imagen_pil = Image.open(imagen_original)
        else:
            imagen_pil = imagen_original  # Ya es PIL si se cargó desde URL
        # Ofuscar la imagen
        imagen_ofuscada = ofuscar_imagen(imagen_pil)
        # Mostrar la imagen original y ofuscada
        st.image([imagen_pil, imagen_ofuscada], caption=["Imagen Original", "Imagen Ofuscada"], width=300)
