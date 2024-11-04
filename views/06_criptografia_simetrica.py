import streamlit as st

st.title("Criptografía Simétrica")

st.write("Un 'cypher' o 'cipher' es una técnica o algoritmo utilizado para cifrar o codificar información de manera que sea incomprensible para aquellos que no tengan la clave o el conocimiento necesario para descifrarlo.")



st.markdown(r"$c = \text{Encrypt}(p, k) \quad \text{y} \quad p = \text{Decrypt}(c, k)$", unsafe_allow_html=True)

# Subtítulo para el concepto de rondas de encriptación
st.subheader("Rondas de encriptación")

# Explicación sobre rondas de encriptación
st.write("""Las 'rondas de encriptación' son pasos repetitivos que se aplican en un algoritmo de cifrado para aumentar la seguridad del proceso.
          Durante cada ronda, se realizan operaciones de transformación en los datos, como substituciones, permutaciones o combinaciones con la clave de cifrado.
          Estas operaciones se aplican de manera iterativa sobre el texto plano o el texto cifrado, dependiendo del algoritmo, y pueden variar en complejidad y número de repeticiones según el diseño del cifrador. 
         El objetivo de las rondas de encriptación es incrementar la resistencia del cifrado ante métodos criptoanalíticos, haciendo que sea más difícil para un atacante descifrar el mensaje sin conocer la clave correcta.""")




st.subheader("Diagrama de rondas de encriptación")

# URL de la imagen
url_imagen = "https://braincoke.fr/assets/static/block_cipher_encryption.e9b60af.cfed321ab98feb7a6c376bf02267b14b.png"

# Mostrar la imagen en Streamlit
st.image(url_imagen, use_column_width=True)


st.subheader("Modos de Operación en Criptografía Simétrica")

resumen = """
En criptografía simétrica, se utilizan varios modos de operación para cifrar y descifrar datos de manera segura. Tres de los principales modos son:

**Electronic Codebook (ECB):**
Cada bloque de texto plano se cifra de forma independiente utilizando la misma clave. Sin embargo, es vulnerable a patrones repetitivos, lo que puede ser explotado por un atacante.

**Cipher Block Chaining (CBC):**
Introduce retroalimentación, combinando cada bloque de texto plano con el bloque cifrado anterior. Más seguro que ECB, pero no es paralelizable.

**Counter (CTR):**
Convierte un cifrador de bloque en un cifrador de flujo, permitiendo la encriptación paralela. Utiliza valores pseudoaleatorios (nonce) para producir texto cifrado final.

Estos modos ofrecen diferentes niveles de seguridad y eficiencia en la criptografía simétrica.
"""

st.markdown(resumen)

url_imagen1 = "https://upload.wikimedia.org/wikipedia/commons/b/b0/BlockcipherModesofOperation.png"

# Mostrar la imagen en Streamlit
st.image(url_imagen1, use_column_width=True)

st.subheader("AES")

resumen1 = """El Estándar de Cifrado Avanzado (AES) es un algoritmo de cifrado simétrico ampliamente utilizado para proteger datos sensibles.
 AES utiliza claves de 128, 192 o 256 bits para cifrar 
y descifrar información de manera segura y eficiente.
"""

st.markdown(resumen1)

url_imagen2 = "https://img.brainkart.com/imagebk9/QRvrZFg.jpg"

# Mostrar la imagen en Streamlit
st.image(url_imagen2, use_column_width=True)

############
import streamlit as st
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import base64
import io



###########
import streamlit as st
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Function to encrypt using AES in CBC mode
def encrypt_AES_CBC(data, key, iv):
    padder = padding.PKCS7(128).padder()  
    padded_data = padder.update(data.encode('utf-8'))  
    padded_data += padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())  
    encryptor = cipher.encryptor()  
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()  

    return ciphertext

# Function to decrypt using AES in CBC mode
def decrypt_AES_CBC(ciphertext, key, iv):
    decryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).decryptor()  
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize() 

    unpadder = padding.PKCS7(128).unpadder()  
    unpadded_data = unpadder.update(decrypted_data)  
    unpadded_data += unpadder.finalize()

    return unpadded_data.decode('utf-8')  

# Configuración del título y descripción
st.title("Cifrado y Descifrado de Textos")
st.write("Esta aplicación permite cifrar y descifrar texto utilizando el algoritmo AES en modo CBC.")

# Interfaz de usuario para ingresar el texto y la clave
plaintext = st.text_input("Ingresa el texto a cifrar o descifrar:")
key = st.text_input("Ingresa la clave (16, 24 o 32 bytes) para el cifrado o descifrado:", type="password")
iv = st.text_input("Ingresa el vector de inicialización (16 bytes):")

# Botón para cifrar el texto
if st.button("Cifrar"):
    if len(key) in [16, 24, 32] and len(iv) == 16:
        encrypted_text = encrypt_AES_CBC(plaintext, key.encode('utf-8'), iv.encode('utf-8'))  
        st.success(f'Texto cifrado: {encrypted_text.hex()}')
    else:
        st.error("La longitud de la clave debe ser de 16, 24 o 32 bytes, y la del IV debe ser de 16 bytes.")

# Botón para descifrar el texto
if st.button("Descifrar"):
    if len(key) in [16, 24, 32] and len(iv) == 16:
        try:
            decrypted_text = decrypt_AES_CBC(bytes.fromhex(plaintext), key.encode('utf-8'), iv.encode('utf-8'))  
            st.success(f'Texto descifrado: {decrypted_text}')
        except ValueError:
            st.error("El texto cifrado debe estar en formato hexadecimal.")
    else:
        st.error("La longitud de la clave debe ser de 16, 24 o 32 bytes, y la del IV debe ser de 16 bytes.")


#############################
import streamlit as st
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encrypt_file_AES_CBC(data, key, iv):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

def decrypt_file_AES_CBC(ciphertext, key, iv):
    decryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data

st.title('Cifrado/Descifrado AES')

key = st.text_input('Enter the AES key (32 bytes):', value='MySuperSecretKey2222222222222222')
iv = st.text_input('Enter the AES IV (16 bytes):', value='MySuperSecretIV0')

uploaded_file = st.file_uploader("Choose a file to encrypt/decrypt", type=["txt", "bin"])

if uploaded_file is not None:
    action = st.selectbox('Choose action:', ['Encrypt', 'Decrypt'])
    output_filename = st.text_input('Enter output file name:', value='output_file')

    if st.button('Process'):
        data = uploaded_file.read()
        
        if action == 'Encrypt':
            encrypted_data = encrypt_file_AES_CBC(data, key.encode(), iv.encode())
            st.success(f'File {uploaded_file.name} encrypted.')
            st.download_button('Download Encrypted File', encrypted_data, file_name=f"{output_filename}.bin")
        else:
            decrypted_data = decrypt_file_AES_CBC(data, key.encode(), iv.encode())
            st.success(f'File {uploaded_file.name} decrypted.')
            st.download_button('Download Decrypted File', decrypted_data, file_name=f"{output_filename}.txt")

#https://www.teoria.com/jra/aes/index.html

#############

import streamlit as st
import hashlib

# Título y descripción principal
st.title(":mortar_board: Funciones de Hash")
st.markdown("##")
st.markdown("""
### Resistencia a Colisiones y a Preimágenes
Una **función de hash** es una función que toma una entrada y devuelve un valor de longitud fija, que parece aleatorio. Las funciones de hash se utilizan en una variedad de aplicaciones, incluyendo criptografía, almacenamiento de contraseñas, y verificación de integridad de datos.

#### Propiedades clave de las funciones de hash:
- **Resistencia a colisiones**: Es difícil encontrar dos entradas diferentes que produzcan el mismo valor de hash.
- **Resistencia a preimágenes**: Dado un valor de hash, es difícil encontrar cualquier entrada que lo produzca.

Estas propiedades aseguran que las funciones de hash sean seguras y fiables para su uso en aplicaciones de seguridad.
""")


# Mostrar una imagen desde una URL
image_url = "https://cadenadebloques.io/wp-content/uploads/2021/07/Hash.jpg"
st.image(image_url, caption='Funciones de Hash', use_column_width=True)


# Ejemplo de una función de hash segura
st.subheader("Ejemplo de una función de hash segura:")
st.code("""
import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

data = "Tu entrada de ejemplo"
hash_result = hash_data(data)
st.write("Resultado del hash:", hash_result)
""")

# Mostrar el resultado de hash en tiempo real
data_input = st.text_input("Ingresa un dato para hacerle hash:")
if data_input:
    hash_result = hashlib.sha256(data_input.encode()).hexdigest()
    st.write("Resultado del hash:", hash_result)