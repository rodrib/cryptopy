import streamlit as st
import random

# Título
st.title("Generadores de números aleatorios (RNGs)")

# Información sobre los tipos de RNGs
st.write("Son algoritmos o dispositivos que producen secuencias de números que parecen aleatorios. Pueden ser de dos tipos:")
st.write("- **Verdaderamente aleatorios (TRNGs):** Utilizan fuentes físicas impredecibles para generar números aleatorios, como el ruido térmico o la desintegración radiactiva.")
st.write("- **Pseudoaleatorios (PRNGs):** Utilizan un algoritmo matemático para generar números que parecen aleatorios a partir de un valor inicial (semilla).")

# Función para generar números aleatorios
def generar_numeros_aleatorios(semilla, cantidad):
    numeros = []
    rng = random.Random(semilla)
    for _ in range(cantidad):
        numeros.append(rng.random())
    return numeros

# Interfaz de usuario
st.title("Generador de Números Aleatorios")
semilla = st.text_input("Ingrese la semilla para el generador de números aleatorios:")
try:
    semilla = int(semilla)
except ValueError:
    st.error("La semilla debe ser un número entero.")

cantidad = st.number_input("Ingrese la cantidad de números aleatorios a generar:", min_value=1, step=1)
if isinstance(semilla, int):
    numeros_aleatorios = generar_numeros_aleatorios(semilla, cantidad)
    st.write("Números Aleatorios Generados:")
    st.write(numeros_aleatorios)

# Criptoanálisis
st.title("Criptoanálisis")
st.write("El criptoanálisis es el estudio de sistemas criptográficos para detectar vulnerabilidades y descifrar información protegida sin acceso a la clave de cifrado.")

# Términos Criptográficos
st.title("Términos Criptográficos")
st.subheader("COA: Certificado de Autoridad de Certificación")
st.write("Es un documento digital emitido por una Autoridad de Certificación (CA) que valida la identidad de una persona o entidad.")
st.subheader("KPA: Algoritmo de Acuerdo de Clave")
st.write("Es un protocolo criptográfico que permite a dos o más partes generar un par de claves públicas y privadas de forma segura, incluso si no comparten un canal de comunicación seguro.")
st.subheader("CPA: Ataque de Texto Claro Elegido")
st.write("Es un tipo de ataque criptográfico en el que el atacante puede elegir el texto claro que desea cifrar y observar el texto cifrado correspondiente. Esta información puede ser utilizada para debilitar la seguridad del sistema criptográfico.")
st.subheader("CCA: Ataque de Texto Cifrado Elegido")
st.write("Es un tipo de ataque criptográfico similar al CPA, pero en este caso el atacante puede elegir el texto cifrado que desea descifrar y observar el texto claro correspondiente.")
st.subheader("Ataque de Canal Lateral (Side Channel Attack)")
st.write("Es un tipo de ataque criptográfico que explota información adicional, como el tiempo de ejecución del algoritmo o el consumo de energía, para obtener información sobre la clave o el mensaje original.")

# Seguridad Informática vs Seguridad Computacional
st.title("Seguridad Informática vs Seguridad Computacional")
resumen = """
La seguridad informática protege datos, sistemas y redes contra amenazas digitales, mientras que la seguridad computacional 
asegura la fiabilidad y funcionamiento adecuado de hardware y software. Es como proteger una casa: cerraduras mantienen 
intrusos fuera (seguridad informática), mientras que la estructura y sistemas eléctricos previenen accidentes 
(seguridad computacional).
"""
st.write(resumen)

# One-Time Pad
resumen1 = "El One-Time Pad (OTP) es un método de cifrado que utiliza una clave aleatoria del mismo tamaño que el mensaje y se utiliza solo una vez. El cifrado es teóricamente perfecto y no puede ser descifrado sin la clave."
st.write(resumen1)
