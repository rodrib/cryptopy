import streamlit as st
from cryptography.fernet import Fernet
from PyPDF2 import PdfReader

# Título
st.title("Ransomware")

# Texto
texto = """
El ransomware es una amenaza de gran importancia que continúa creciendo con el paso del tiempo. 
Según el reciente análisis de mitad de año llevado a cabo por Cisco, 
ya domina el mercado de malware y es el tipo de malware más rentable de la historia.
"""

# Mostrar el texto en Streamlit
st.write(texto)

texto1 = """
En síntesis, el ransomware utiliza una variedad de técnicas para bloquear el acceso al sistema o a los archivos de la víctima, y por lo general requiere el pago de un rescate para recuperar el acceso. Recientemente notamos un aumento significativo de un tipo muy particular, conocido como ransomware criptográfico.
"""

st.write(texto1)


# Título
st.title("¿Por qué utiliza cifrado el ransomware criptográfico?")

# Contenido reformulado
texto2 = """
El ransomware criptográfico se apoya en el cifrado para asegurar la confidencialidad de los datos, permitiendo que solo quienes poseen la clave secreta puedan acceder al contenido original. Esto es crucial para los atacantes, ya que les permite modificar archivos o estructuras críticas en un sistema, haciendo que solo puedan restaurarse con la clave que ellos controlan.

Este enfoque es comparable a tomar datos como rehenes, pidiendo un rescate a cambio de liberarlos. Además, el cifrado asegura la comunicación entre el malware y su servidor, donde reside la clave necesaria para restaurar los archivos afectados.

Actualmente, los atacantes combinan cifrado simétrico y asimétrico para maximizar el rendimiento y la eficacia. El cifrado simétrico, que utiliza la misma clave para cifrar y descifrar, es eficiente y permite que el ransomware opere rápidamente. Por otro lado, el cifrado asimétrico, que emplea una clave pública y otra privada, facilita la gestión de claves para múltiples víctimas, protegiendo la clave simétrica secreta con una clave privada.

En resumen, el ransomware criptográfico emplea el cifrado simétrico para bloquear los archivos de las víctimas y el cifrado asimétrico para salvaguardar la clave que permite su descifrado, combinando así eficiencia y seguridad en sus operaciones.
"""

st.write(texto2)


from PIL import Image
import requests
from io import BytesIO

# URL de la nueva imagen
image_url = "https://web-assets.esetstatic.com/wls/2016/09/ransomware_espa%C3%B1ol.jpg"

# Cargar la imagen desde la URL
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Agregar la imagen debajo del título
st.image(image, caption="Esquema de cifrado doble en el ransomware criptográfico", use_column_width=True)


import streamlit as st

# Título de la sección
st.title("Comunicación con los servidores de comando y control: evasión y confidencialidad")



# Resumen del texto
resumen = """
El cifrado en la comunicación con servidores de C&C busca evasión y confidencialidad. Inicialmente, el ransomware se centraba en la confidencialidad, pero ahora usa estándares como TLS, dificultando la detección. Redes sin capacidades de inspección de tráfico permiten que el malware se comunique sin ser detectado, lo que resulta en una protección reactiva.
"""

# Mostrar el resumen

st.write(resumen)


import streamlit as st

st.title("Cómo evitar y combatir el ransomware criptográfico")

st.header("Evitar el ransomware criptográfico")
st.write("Para evitar el ransomware criptográfico, ESET recomienda:")
st.write(
    "Usar una solución de seguridad confiable y habilitar medidas proactivas como el sistema HIPS y la protección Anti-Phishing.",
    "Tener conductas seguras: configurar el equipo para mostrar las extensiones ocultas de los archivos y no abrir vínculos ni mensajes de origen desconocido."
)

st.header("Combatir el ransomware criptográfico")
st.write("En caso de infección, es crucial:")
st.write(
    "Tener un backup reciente, validado y offline de tus archivos. Crear copias de seguridad periódicamente, evitando guardarlas en unidades asignadas a tu equipo.",
    "Como último recurso, intentar descifrar tus archivos con las herramientas de descifrado proporcionadas por los investigadores de seguridad para algunas familias específicas de ransomware criptográfico. ESET cuenta con estas herramientas."
)

st.write("Siguiendo estas recomendaciones, podrás evitar y combatir eficazmente el ransomware criptográfico, protegiendo tus archivos y datos valiosos.")

# # Funciones
# def generarKey():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
#     return key

# def encryp(file, key):
#     fernet = Fernet(key)
#     file_data = file.read()
#     encrypted_data = fernet.encrypt(file_data)
#     return file_data, encrypted_data

# def mostrar_contenido_pdf(file):
#     pdf_reader = PdfReader(file)
#     texto_pdf = ""
#     for page in pdf_reader.pages:
#         texto_pdf += page.extract_text()
#     return texto_pdf

# # Generar y mostrar la clave
# st.title("Cifrador de Archivos PDF")

# """ 
# key = generarKey()
# st.write("Clave generada:")
# st.code(key.decode(), language="text") 
#  
# uploaded_file = st.file_uploader("Cargar un archivo PDF", type="pdf") 
