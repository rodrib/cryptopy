import streamlit as st

# Función de cifrado César
def cifrado_cesar(texto, desplazamiento):
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            index = ord(char) - ascii_offset
            index = (index + desplazamiento) % 26
            texto_cifrado += chr(index + ascii_offset)
        else:
            texto_cifrado += char
    return texto_cifrado

# Función de cifrado Atbash
def cifrado_atbash(texto):
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            index = ord(char) - ascii_offset
            index = 25 - index  # Reemplazar con el opuesto en el alfabeto
            texto_cifrado += chr(index + ascii_offset)
        else:
            texto_cifrado += char
    return texto_cifrado

# Función de cifrado de columna
def cifrado_columna(texto):
    num_columnas = 3
    longitud_texto = len(texto)
    num_filas = (longitud_texto + num_columnas - 1) // num_columnas
    texto += ' ' * (num_filas * num_columnas - longitud_texto)
    columnas_original = [texto[i::num_filas] for i in range(num_filas)]
    columnas_cifradas = ['[' + col + ']' for col in columnas_original]
    texto_cifrado = ''.join(columnas_cifradas)
    return texto_cifrado

# Interfaz de usuario de Streamlit
st.title("Criptografía Clásica")

st.write("La criptografía clásica abarca una serie de técnicas criptográficas que se desarrollaron antes del auge de la computación moderna. Estas técnicas se caracterizan por su simplicidad matemática y su enfoque manual para el cifrado y descifrado.")

st.write("Tipos de Criptografía Clásica:")

st.subheader("Cifrado por sustitución:")
st.write("- **Cifrado de César:** Reemplaza cada letra por otra letra ubicada a una distancia fija en el alfabeto.")
st.write("- **Cifrado de Atbash:** Sustituye las letras por su opuesto en el alfabeto.")

st.subheader("Cifrado por transposición:")
st.write("- **Cifrado de columna:** Reordena las letras del mensaje en columnas y luego las lee por filas.")
st.write("- **Cifrado de Vigenère:** Utiliza una tabla de sustitución basada en una palabra clave.")

# Opciones para el usuario
seleccion = st.selectbox("Seleccione un tipo de cifrado:", ["Cifrado de César", "Cifrado de Atbash", "Cifrado de columna"])

if seleccion == "Cifrado de César":
    texto_original = st.text_area("Ingrese el texto original:")
    desplazamiento = st.number_input("Ingrese el valor del desplazamiento:", value=3, step=1)
    if st.button("Cifrar"):
        texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
        st.write("Texto cifrado:", texto_cifrado)

elif seleccion == "Cifrado de Atbash":
    texto_original = st.text_area("Ingrese el texto original:")
    if st.button("Cifrar"):
        texto_cifrado = cifrado_atbash(texto_original)
        st.write("Texto cifrado:", texto_cifrado)

elif seleccion == "Cifrado de columna":
    texto_original = st.text_area("Ingrese el texto original:")
    if st.button("Cifrar"):
        texto_cifrado = cifrado_columna(texto_original)
        st.write("Texto cifrado:", texto_cifrado)

# Información adicional sobre cifrados simétricos y asimétricos
st.title("Cifrados Simétricos y Asimétricos")

st.write("En el mundo de la criptografía, los cifrados simétricos y asimétricos juegan roles fundamentales en la seguridad de la información en línea.")

st.write("Cifrados Simétricos:")
st.write("En este escenario, Bob y Alice desean comunicarse de forma segura, pero temen que Eve pueda interceptar sus mensajes. Bob cifra sus mensajes utilizando una clave compartida, convirtiendo el mensaje en texto cifrado. Luego, Alice utiliza la misma clave para descifrar el mensaje y recuperar el texto original. En este proceso, la seguridad radica en la confidencialidad de la clave compartida. Si Eve no tiene acceso a esta clave, no puede descifrar el mensaje. Sin embargo, si Eve logra obtener la clave, puede leer todos los mensajes cifrados.")

st.write("Cifrados Asimétricos:")
st.write("Los cifrados asimétricos ofrecen una solución más sofisticada. En este caso, cada persona tiene un par de claves: una pública y otra privada. Bob utiliza la clave pública de Alice para cifrar su mensaje, convirtiéndolo en texto cifrado. Solo la clave privada de Alice puede descifrar este mensaje, garantizando así que solo ella pueda leerlo. Este método elimina la necesidad de compartir una clave secreta, lo que reduce el riesgo de comprometer la seguridad si una clave se ve comprometida.")

# Matemática y propiedades de cifrado seguro
st.title("Propiedades de un Cifrado Seguro")

st.write("Sea $(K, M, C, e, d)$ la especificación de nuestro cifrado. Para que este sea seguro satisfactoriamente tendría que cumplir las siguientes propiedades:")

st.markdown("1. $\\forall k \\in K, m \\in M$ tiene que ser fácil de computar el cifrado $e_k(m)$.")
st.markdown("2. $\\forall k \\in K, c \\in C$ tiene que ser fácil de computar el descifrado $d_k(c)$.")

st.markdown("3. Dados uno o más textos cifrados $c_1, c_2, ..., c_n \\in C$, tiene que ser computacionalmente difícil calcular los textos en claro $d_k(c_1), ..., d_k(c_n) \\in M$ sin saber la clave $k$.")

st.markdown("4. Seguridad contra un ataque de texto en claro conocido: sean $(m_1, c_1), (m_2, c_2), ..., (m_n, c_n)$ tiene que ser difícil desencriptar cualquier cifrado $c$ que no está en la lista sin saber $k$.")

st.markdown("5. Seguridad contra un ataque de texto plano elegido: sean $m_1, ..., m_n \\in M$ elegido por el adversario y conociendo los textos cifrados $e_k(m_1), ..., e_k(m_n)$, tiene que ser difícil desencriptar un texto $c$ que no esté en la lista sin saber $k$.")
