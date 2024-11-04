import streamlit as st
#hola

st.title(":🧮 : Aritmética Modular")

st.write("La aritmética modular es un sistema matemático que trata con números enteros, pero en lugar de trabajar con números continuos, se enfoca en los residuos de la división.")

st.write("**Definición básica:**")

st.write("En la aritmética modular, dos números enteros se consideran equivalentes si tienen el mismo residuo cuando se dividen por un número fijo llamado módulo. Si dos números 'a' y 'b' tienen el mismo residuo cuando se dividen por el módulo 'p', se escriben como 'a ≡ b (mod p)'.")

st.write("**Ejemplo:**")

st.write("Si el módulo es 5, entonces 8 y 3 son equivalentes módulo 5, ya que ambos tienen un residuo de 3 cuando se dividen por 5. Por lo tanto, '8 ≡ 3 (mod 5)'.")

st.write("**Operaciones básicas:**")

st.write("- **Adición:** La suma de dos números módulo 'p' es el residuo de la suma cuando se divide por 'p'.")
st.write("- **Sustracción:** La resta de dos números módulo 'p' es el residuo de la resta cuando se divide por 'p'.")
st.write("- **Multiplicación:** El producto de dos números módulo 'p' es el residuo del producto cuando se divide por 'p'.")
st.write("- **Exponentiación:** El resultado de elevar un número a una potencia módulo 'p' es el residuo de la potencia cuando se divide por 'p'.")

st.write("**Grupos en Aritmética Modular:**")

st.write("En el contexto de la aritmética modular, un grupo es un conjunto de elementos junto con una operación binaria que satisface las propiedades de cierre, asociatividad, identidad e inverso. Los grupos pueden ser aditivos o multiplicativos.")

st.write("**Grupo Aditivo:**")

st.write("El conjunto de números enteros módulo 'p' con la operación de adición forma un grupo abeliano. Este grupo cumple las siguientes propiedades:")
st.write("- **Cierre:** Si 'a' y 'b' están en el conjunto, entonces 'a + b' también está en el conjunto.")
st.write("- **Asociatividad:** La suma es asociativa: '((a + b) + c) ≡ (a + (b + c)) (mod p)'.")
st.write("- **Identidad:** Existe un elemento identidad '0' tal que 'a + 0 ≡ a (mod p)' para todo 'a' en el conjunto.")
st.write("- **Inverso:** Para cada 'a', existe un inverso '-a' tal que 'a + (-a) ≡ 0 (mod p)'.")

st.write("**Grupo Multiplicativo:**")

st.write("El conjunto de números enteros coprimos con 'p' (es decir, aquellos entre 1 y p-1 que no tienen factores comunes con 'p') con la operación de multiplicación forma un grupo multiplicativo. Este grupo cumple las siguientes propiedades:")
st.write("- **Cierre:** Si 'a' y 'b' están en el conjunto, entonces 'a * b' también está en el conjunto.")
st.write("- **Asociatividad:** La multiplicación es asociativa: '((a * b) * c) ≡ (a * (b * c)) (mod p)'.")
st.write("- **Identidad:** Existe un elemento identidad '1' tal que 'a * 1 ≡ a (mod p)' para todo 'a' en el conjunto.")
st.write("- **Inverso:** Para cada 'a', existe un inverso 'a^(-1)' tal que 'a * a^(-1) ≡ 1 (mod p)'. Este inverso existe si y solo si 'a' es coprimo con 'p'.")

st.write("**Reglas de la Aritmética Modular:**")

st.write("Las operaciones básicas de la aritmética modular incluyen:")
st.write("- **Adición:** '(a + b) mod p'.")
st.write("- **Sustracción:** '(a - b) mod p'.")
st.write("- **Multiplicación:** '(a * b) mod p'.")
st.write("- **Exponentiación:** '(a^b) mod p'. Esto se calcula de manera eficiente mediante el algoritmo de exponenciación modular.")





# Título y descripción principal
st.title(":closed_lock_with_key: Intercambio de Claves Diffie-Hellman")

# Descripción del protocolo Diffie-Hellman
st.markdown("""
El intercambio de claves **Diffie-Hellman (D-H)** es un protocolo fundamental que permite a dos partes establecer una clave secreta compartida a través de un canal inseguro, como internet.

### Ejemplo de funcionamiento:

1. **Alice y Bob acuerdan un módulo grande** `p` **y un generador** `g`.
2. **Alice elige un secreto aleatorio** `a` **y calcula** `A = g^a mod p`.
3. **Bob elige un secreto aleatorio** `b` **y calcula** `B = g^b mod p`.
4. **Alice envía** `A` **a Bob y Bob envía** `B` **a Alice**.
5. **Alice calcula** `K = B^a mod p`.
6. **Bob calcula** `K = A^b mod p`.

### Seguridad:

La seguridad del protocolo D-H se basa en la dificultad de calcular el logaritmo discreto.

### Problema del logaritmo discreto:

- **Definición:** Dado un módulo `p`, un generador `g` y un elemento `h` en el grupo cíclico `Z/pZ`, encontrar el entero `x` tal que `g^x = h mod p`.

### Dificultad:

El problema del logaritmo discreto se considera computacionalmente difícil para módulos grandes. No se conoce un algoritmo eficiente para resolverlo en general.
""")

st.markdown("""
    ### Compromiso

En 1976, Whitfield Diffie y Martin Hellman publicaron un método para establecer un secreto compartido entre dos partes, permitiendo un canal de comunicación eficiente. Este método genera una llave privada conocida por ambas partes para encriptar y desencriptar información simétricamente. Aunque la criptografía asimétrica es ineficiente para compartir muchos mensajes extensos, es ideal para compartir una llave de encriptación simétrica.

El protocolo Diffie-Hellman establece un canal de comunicación asimétrica para compartir información en una única ocasión por sesión. Las partes generan una llave simétrica a partir de sus claves privadas y públicas, permitiendo un canal de comunicación simétrico descifrable solo por ellos con una llave compartida.
""")

st.markdown("""
    ### Protocolo
""")

import base64
# Nota antes de la animación
st.markdown("**Nota:** En la animación que sigue, cada parte tiene un espacio privado (seguro para los secretos) y comparten un espacio público disponible para ellos y cualquier tercero.")

# URL de la animación GIF
animation_url = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-1.gif"

# Mostrar la animación desde la URL
st.markdown(f'<img src="{animation_url}" alt="Animación del intercambio de claves Diffie-Hellman">', unsafe_allow_html=True)


# Segunda parte de la descripción
st.markdown("""
            
En lugar de Alice y Bob definir una llave pública y una llave privada respectivamente, solo nos interesa que definan su llave privada (`a` y `b`) y que acuerden entre sí, expuestos al público, dos valores `g` y `p`.
""")

# URL de la segunda animación GIF
animation_url_2 = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-2.gif"

# Mostrar la segunda animación desde la URL
st.markdown(f'<img src="{animation_url_2}" alt="Animación del intercambio de claves Diffie-Hellman, segunda parte">', unsafe_allow_html=True)

# Tercera parte de la descripción
st.markdown("""
Note que al pie de cada región llevamos un registro de las variables a las que han tenido acceso sus respectivos usuarios.
""")

# URL de la tercera animación GIF
animation_url_3 = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-3.gif"

# Mostrar la tercera animación desde la URL
st.markdown(f'<img src="{animation_url_3}" alt="Registro de variables en el intercambio de claves Diffie-Hellman">', unsafe_allow_html=True)


# Cuarta parte de la descripción
st.markdown("""
Con sus respectivas claves privadas, Alice y Bob computan un valor combinado con el generador `g` (recuerde que `g` es público). Este proceso de ‘mezclar’ los valores tiene un sentido matemático específico que impide que se pueda deshacer la operación (No es imposible pero sí en exceso difícil y costoso). Respectivamente, Alice y Bob produjeron los valores `ag` y `bg` de los cuales no se pueden inferir las claves privadas `a` y `b`. Sin `p`, esta operación es imposible.
""")

# URL de la cuarta animación GIF
animation_url_4 = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-4.gif"

# Mostrar la cuarta animación desde la URL
st.markdown(f'<img src="{animation_url_4}" alt="Proceso de mezclar valores en el intercambio de claves Diffie-Hellman">', unsafe_allow_html=True)


# Quinta parte de la descripción
st.markdown("""
Una vez generados estos cifrados, Alice y Bob los intercambian. Note que como aún no hay un canal seguro de comunicación, `ag` y `bg` son públicos.
""")

# URL de la quinta animación GIF
animation_url_5 = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-5.gif"

# Mostrar la quinta animación desde la URL
st.markdown(f'<img src="{animation_url_5}" alt="Intercambio de cifrados en el intercambio de claves Diffie-Hellman">', unsafe_allow_html=True)

# Sexta parte de la descripción
st.markdown("""
Nuevamente realizamos la operación de ‘mezclado’. Alice mezclará el cifrado público que acaba de recibir de Bob con su clave privada (`bg` con `a`, produce `abg`). Bob, hará lo mismo con su clave privada y el cifrado público que recibió de Alice (`ag` con `b`, produce `abg`).
""")

# URL de la sexta animación GIF
animation_url_6 = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-6.gif"

# Mostrar la sexta animación desde la URL
st.markdown(f'<img src="{animation_url_6}" alt="Operación de mezclado en el intercambio de claves Diffie-Hellman">', unsafe_allow_html=True)


# Séptima parte de la descripción
st.markdown("""
Note que ahora Alice y Bob comparten un cifrado irreversible (idéntico para ambos) el cual pueden utilizar para encriptar cualquier mensaje consecuente. Alice y Bob pueden ahora establecer un canal de comunicación seguro, con encriptación simétrica.

Veamos ahora, que únicamente Alice y Bob pueden generar la llave simétrica `abg`. El público tiene acceso al generador `g`, el valor `p` y las llaves cifradas `ag` y `bg`. No hay forma de ‘mezclar’ estos valores de forma tal que generen `abg`. Intentar ‘mezclar’ `bg` con `ag` produciría algo como `abgg`, lo cual es un valor completamente distinto y que no sirve para descifrar los mensajes entre Alice y Bob. ¡Hemos establecido un canal seguro de encriptación simétrica!
""")

# URL de la séptima animación GIF
animation_url_7 = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-7.gif"

# Mostrar la séptima animación desde la URL
st.markdown(f'<img src="{animation_url_7}" alt="Establecimiento de canal seguro en el intercambio de claves Diffie-Hellman">', unsafe_allow_html=True)


import streamlit as st

st.markdown("""
Vulnerabilidades
---

El procedimiento parece robusto, pero su intención es solo escudar a 2 partidos de un ojo fisgón. ¿Qué pasa cuando introducimos a una tercera parte, Mallory, que tiene el poder de interceptar y manipular mensajes entre partes en la red? Tenemos también la preocupación de que información secreta de alguna de las partes sea liberada al público. ¿Podemos satisfacer que los mensajes previos están seguros?

Ataque de intermediario (Man in the Middle)
---

Suponga un mismo escenario donde Alice y Bob quieren establecer un canal de comunicación de encriptación simétrica, solo que ahora una tercera parte, Mallory, puede intervenir sobre la información que viaja en la red. Por ejemplo, si Alice quisiera mandar su propuesta de un generador `g` a Bob, Mallory sabría que esto está sucediendo evitar que esto suceda, o escoger su propio mensaje para enviarle a Bob. Note que hasta ahora, nuestro método de comunicación no tiene forma de validar el origen de un mensaje en la red, por lo que Mallory puede estar seguro de que su intromisión en el canal de Alice y Bob no es detectable (aún).

El concepto de este ataque es bastante sencillo. Todo lo que debe hacer Mallory para poder interpretar todos los futuros mensaje entre Alice y Bob es suplantarlos al momento de generar la llave compartida, de forma que Mallory comparte una llave con Bob y una con Alice.

1. Alice y Bob acuerdan un `g` y `p` públicos y generan sus llaves privadas respectivas.
2. Alice genera `ag` y lo publica en la red con la intención de que lo reciba Bob. Bob hace lo mismo para Alice con `bg`.
3. Mallory intercepta estos mensajes y evita que lleguen al destinatario correspondiente.
4. Mallory genera su propia llave privada `m` y produce `mg`.
5. Mallory responde a Alice con `mg` suplantando a Bob. Alice cree que lo que acaba de recibir es `bg`.
6. Mallory responde a Bob con `mg` suplantando a Alice. Bob cree que lo que acaba de recibir es `ag`.
7. Alice y Bob calculan respectivamente `mag` y `mbg`.
8. Mallory calcula `mag` y `mbg`. Ahora comparte un secreto con el cual establecer un canal encriptado simétrico con ambos Alice y Bob. Estos no se han percatado del ataque.

Cualquier cifrado enviado por Alice con la intención de que lo reciba únicamente Bob, llega primero a Mallory. Mallory puede decidir hacer lo que quiera con este. Si la intención es solo mediar la comunicación entre Alice y Bob, Mallory debe descifrar el cifrado entrante y encriptarlo con el secreto contrario. Esto le permite editarlo, borrarlo, o incluso compartirlo con otros.

Esta vulnerabilidad fue descubierta pronto, por lo cual se volvió una práctica común agregar un paso de autenticación al cifrado simétrico. Entran ahora en juego las llaves públicas.

Forward secrecy (PFS)
---

Forward secrecy es la intención de proteger mensajes pasados en caso de que su cifrado haya sido guardado por terceros y el secreto compartido sea publicado. En este caso, la responsabilidad sobre la liberación de estos mensajes no recae sobre alguna falla de Diffie-Hellman. En un inicio mencionamos la noción de una sesión de comunicación. La idea de tener sesiones cortas sobre las cuales habilitar el canal de comunicación es beneficiosa ya que cada vez que se inicie una sesión, la llave compartida puede generarse desde cero en cada ocasión, de forma que, si se libera la clave, solo los mensajes de esa sesión son vulnerables. En teoría, nada impide que utilicemos una nueva llave para cada mensaje o para cada sub-cadena de 126 bits o menos. Recordemos que comunicarse por encriptación asimétrica es un proceso costoso, por lo que quisiéramos minimizar su uso. Cada vez que intercambiamos claves y generamos un secreto compartido estamos efectuando encriptación asimétrica, ya depende de los dueños del canal establecer la frecuencia con la que se generan estas llaves efímeras.
""")

###########

import streamlit as st

class Partido:
    # Podemos inicializar cada partido con una llave privada.
    def __init__(self, private_key, important_message):
        # Definimos la llave privada como una variable protegida
        self.__private_key = private_key
        
        # Definimos el mensaje que Alice va a querer enviar a Bob.
        self.__message = important_message
        
        # Por lo pronto no hemos establecido el secreto compartido.
        self.__shared_key = None
    
    # A un partido podemos pedirle su clave pública dados un generador g y un módulo p.
    def calculate_public_key(self, g, p):
        # P_A = g^a mod p ó
        # P_B = g^b mod p
        return g ** self.__private_key % p
    
    # Si conocemos la clave pública del otro partido podemos conocer el secreto compartido.
    def assign_shared_secret(self, others_public_key, p):
        # S = B^a mod p ó
        # S = A^b mod p
        self.__shared_key = others_public_key ** self.__private_key % p
    
    # Si tenemos un secreto compartido, podemos cifrar y entregar el mensaje cifrado.
    # Si aún no tenemos un secreto compartido, el mensaje cifrado es vacío.
    # Este cifrado es simple y potencialmente vulnerable, pero un cifrado robusto no es nuestro enfoque del momento,
    # por lo pronto, solo interesa que el cifrado sea simétrico.
    def give_cypher(self):
        outward_cypher = ""
        if self.__shared_key:
            for char in self.__message:
                outward_cypher += chr(ord(char) + self.__shared_key)
        return outward_cypher
    
    # Dado un cifrado público, probamos descifrarlo con el secreto compartido.
    def decypher(self, inward_cypher):
        message = ""
        for char in inward_cypher:
            message += chr(ord(char) - self.__shared_key)
        return message

# Interfaz de Streamlit
st.title("Intercambio de Claves Diffie-Hellman")

# Inputs para los usuarios
private_key_alice = st.number_input("Llave privada de Alice", min_value=1, value=5, step=1)
private_key_bob = st.number_input("Llave privada de Bob", min_value=1, value=7, step=1)
message = st.text_input("Mensaje importante de Alice a Bob", "Hola Bob!")

# Crear instancias de Alice y Bob
alice = Partido(private_key_alice, message)
bob = Partido(private_key_bob, "")

# Generador y módulo público
g = 9
p = 23

# Calcular claves públicas
public_key_alice = alice.calculate_public_key(g, p)
public_key_bob = bob.calculate_public_key(g, p)

# Asignar secretos compartidos
alice.assign_shared_secret(public_key_bob, p)
bob.assign_shared_secret(public_key_alice, p)

# Cifrar el mensaje
cypher_message = alice.give_cypher()

# Descifrar el mensaje
decyphered_message = bob.decypher(cypher_message)

# Mostrar resultados
st.subheader("Resultados")
st.write(f"Clave pública de Alice: {public_key_alice}")
st.write(f"Clave pública de Bob: {public_key_bob}")
st.write(f"Secreto compartido de Alice: {alice._Partido__shared_key}")
st.write(f"Secreto compartido de Bob: {bob._Partido__shared_key}")
st.write(f"Mensaje cifrado: {cypher_message}")
st.write(f"Mensaje descifrado por Bob: {decyphered_message}")


######
import streamlit as st

st.title(":closed_lock_with_key: Teoría del RSA")

st.write("""
En la sección de Diffie-Hellman, exploramos el comportamiento de un sistema de intercambio de claves cuyo propósito es establecer un canal de comunicación con cifrado simétrico. Para evaluar la efectividad de este método, usamos cifrados escogidos de forma arbitraria, así como sesiones para las llaves efímeras de un único mensaje. Estas decisiones no son características de Diffie-Hellman, ya que es un sistema que contempla solo el primer requisito para establecer comunicación.

### Introducción al RSA

Introduciremos el RSA. Nombrado así por los tres investigadores que publicaron su hallazgo en 1977, el RSA es un sistema criptográfico que, al igual que Diffie-Hellman, contempla una fase de generación y distribución de llaves, pero también incluye métodos de encriptación y descifrado específicos del protocolo.

### Generación y Distribución de Llaves

- **Fase de Generación de Llaves**:
    - En RSA, se generan dos claves: una clave pública y una clave privada.
    - La clave pública se distribuye abiertamente, mientras que la clave privada se mantiene secreta.

- **Distribución de Llaves**:
    - La clave pública se utiliza para cifrar mensajes, y solo la clave privada correspondiente puede descifrarlos.

### Encripción y Descifrado

- **Encripción**:
    - Para enviar un mensaje seguro, el remitente utiliza la clave pública del destinatario para cifrar el mensaje.

- **Descifrado**:
    - El destinatario utiliza su clave privada para descifrar el mensaje recibido.

El RSA, por lo tanto, no solo facilita el intercambio de claves, sino que también asegura que los mensajes cifrados solo puedan ser descifrados por el destinatario previsto, garantizando así la confidencialidad y la integridad de la comunicación.
""")


st.header("Idea General")

st.write("""
En el caso de la criptografía simétrica, debe establecerse una clave única para cada canal de comunicación. Si, volviendo a nuestro ejemplo ilustrativo del Diffie-Hellman, muchas otras personas quisieran comunicarse con Alice con cifrado simétrico, esta tendría que establecer una llave secreta con cada uno de estos.

Un acercamiento a la criptografía asimétrica más rudimentario no es muy distinto, ya que un destinatario de un mensaje tiene una llave pública única con la que debería encriptarse su mensaje para que este pueda descifrarlo con su clave privada. En este caso, la cantidad de llaves que Alice debe manejar en función del destinatario es mínima. Alice tan solo contempla su clave pública, con la que todos pueden encriptar un mensaje destinado a ella, y su clave privada, con la que descifrará todo mensaje destinado a ella.

Una analogía común es aquella del candado y la llave, donde si Alice quiere recibir un mensaje de Bob, le puede prestar una caja con un candado sin llave. Bob empaca su mensaje y lo sella con el candado y despacha la caja para donde Alice. Alice, propietaria de la llave, abre el candado y lee el mensaje de Bob. Es evidente que el candado es el equivalente a una llave pública y la llave del candado su complemento privado.
""")

#########3
########

import streamlit as st

st.title("Teoría del RSA")

st.subheader("Definición de la Función φ de Euler")

st.markdown("""
Definición: La función φ, denominada φ de Euler, se define para un número \( n \) entero positivo de la siguiente forma:
""")

st.latex(r'''\phi: \mathbb{Z}^+ \to \mathbb{N}''')

st.latex(r'''\phi(n) = | \{ k \in \mathbb{Z}^+ \mid k \leq n, \gcd(k, n) = 1 \} |''')

st.markdown("""
es decir, φ(n) indica la cantidad de primos relativos menores o iguales a \( n \).

Esta función está presente en varios resultados importantes de la teoría de números y algunas de sus propiedades se usan en la implementación del RSA. En primer lugar, de su definición es claro que:
""")

st.latex(r'''\phi(p) = p - 1 \text{ si } p \text{ es un primo.}''')

st.markdown("""
Por otro lado, un resultado muy útil y no tan obvio de esta función es que es multiplicativa. Esto quiere decir que para cualesquiera dos números \( m \) y \( n \) primos relativos se tiene:
""")

st.latex(r'''\phi(mn) = \phi(m) \phi(n)''')

st.markdown("""
Existen distintas formas de demostrar este hecho, como por ejemplo usando técnicas de teoría de números como la inversión de Möbius. Otra forma más avanzada de demostrar esta propiedad es que es un corolario del teorema chino de los residuos de la teoría de anillos (Esto puede verse en la página 265 de la tercera edición del libro de Álgebra Abstracta de Dummit y Foote).

Finalmente, es importante el siguiente teorema:
""")

############
import streamlit as st

st.title("Teorema de Euler-Fermat")

st.markdown("""
Sean \(a\) y \(n\) enteros positivos, primos relativos, entonces se tiene la congruencia:
""")
st.latex(r'''n^{\phi(a)} \equiv 1 \mod a''')

####### Firma Digital

import streamlit as st
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

st.title("Firma digital con RSA")

st.markdown("""
La firma digital permite garantizar la autenticidad e integridad de un mensaje o documento. En el caso de RSA, el proceso funciona de la siguiente manera:
""")

st.markdown("""
1. **Generación de claves**: Se generan un par de claves, una clave privada \(d\) y una clave pública \(e\). La clave privada se mantiene en secreto, mientras que la clave pública se distribuye.
2. **Creación del hash**: Se calcula un hash criptográfico del mensaje que se desea firmar. El hash es un resumen digital del mensaje que permite verificar su integridad.
3. **Firma**: El hash se cifra con la clave privada \(d\) para generar la firma digital.
4. **Verificación**: El receptor del mensaje utiliza la clave pública \(e\) para descifrar la firma digital.
    - Si el valor descifrado coincide con el hash calculado del mensaje original, se verifica la autenticidad e integridad del mensaje.
""")

# Generate RSA keys
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Create hash of the message
def create_hash(message):
    hash_obj = SHA256.new(message.encode('utf-8'))
    return hash_obj

# Sign the message
def sign_message(private_key, hash_obj):
    rsa_private_key = RSA.import_key(private_key)
    signature = pkcs1_15.new(rsa_private_key).sign(hash_obj)
    return base64.b64encode(signature).decode('utf-8')

# Verify the signature
def verify_signature(public_key, signature, message):
    rsa_public_key = RSA.import_key(public_key)
    hash_obj = create_hash(message)
    signature_bytes = base64.b64decode(signature.encode('utf-8'))
    try:
        pkcs1_15.new(rsa_public_key).verify(hash_obj, signature_bytes)
        return True
    except (ValueError, TypeError):
        return False

# Streamlit interface
if 'private_key' not in st.session_state:
    st.session_state.private_key, st.session_state.public_key = generate_keys()

st.markdown("### 1. Generación de claves")
st.text_area("Clave privada (mantener en secreto):", st.session_state.private_key.decode('utf-8'), height=100)
st.text_area("Clave pública (distribuir):", st.session_state.public_key.decode('utf-8'), height=100)

st.markdown("### 2. Creación del hash")
message = st.text_area("Mensaje a firmar:", "Este es un mensaje secreto.")
hash_obj = create_hash(message)
st.text_input("Hash del mensaje:", hash_obj.hexdigest())

st.markdown("### 3. Firma")
if st.button("Firmar mensaje"):
    signature = sign_message(st.session_state.private_key, hash_obj)
    st.session_state.signature = signature
    st.text_input("Firma digital:", signature)

st.markdown("### 4. Verificación")
signature_to_verify = st.text_input("Firma digital a verificar:", st.session_state.get('signature', ''))
message_to_verify = st.text_area("Mensaje original para verificación:", message)

if st.button("Verificar firma"):
    is_valid = verify_signature(st.session_state.public_key, signature_to_verify, message_to_verify)
    if is_valid:
        st.success("La firma es válida. El mensaje es auténtico y no ha sido alterado.")
    else:
        st.error("La firma no es válida. El mensaje puede haber sido alterado o la firma es incorrecta.")



#########

import streamlit as st
import random
from PIL import Image
import requests
from io import BytesIO

# Título de la aplicación
st.title("Práctica con RSA")

# Contexto
st.write("""
Digamos que Andrés tiene algo muy importante que decirle a su amiga Sofía. Para que Andrés le pueda enviar el mensaje secreto, Sofía implementa un sistema de RSA.
Lo primero que hace entonces es seleccionar dos números primos P y Q muy grandes.
""")

# URL de la imagen de criptografía
image_url = "https://miro.medium.com/v2/resize:fit:828/format:webp/1*iQ6VqwTlVn8v4FkgPsv-0g.png"

# Cargar la imagen desde la URL
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Agregar la imagen debajo del título
st.image(image, caption="Criptografía", use_column_width=True)

# Generación de los números primos P y Q
st.subheader("Generación de los números primos P y Q")

def isPrime(n):
    k = 0
    for i in range(2, n):
        if n % i == 0:
            k = i
            break
    return k == 0

a = 1000
b = 2000

P = random.randint(a, b)
while not isPrime(P):
    P = random.randint(a, b)

Q = random.randint(a, b)
while not isPrime(Q):
    Q = random.randint(a, b)

st.write(f"P = {P}")
st.write(f"Q = {Q}")

# Selección del número e y cálculo de N, phi(N), d
st.subheader("Selección del número e y cálculo de N, phi(N), d")

alpha = 10
beta = 50
e = random.randint(alpha, beta)
N = P * Q

def gcd(v1, v2): 
    if v2 == 0: 
        return v1
    else: 
        return gcd(v2, v1 % v2) 

def phi(n):
    k = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            k = k + 1
    return k

phiN = (P - 1) * (Q - 1)
exp = phi(phiN) - 1
D = e ** exp
d = D % phiN

while not (e * d) % phiN == 1:
    e = random.randint(alpha, beta)
    D = e ** exp
    d = D % phiN
    
st.write(f"La clave privada de Sofía es el número d = {d}")
st.write(f"La clave pública que publica Sofía es el par (N, e) = ({N}, {e})")

# Información adicional sobre la clave privada y pública de Sofía
st.write("La clave privada de Sofía es el número d = 862709")
st.write("La clave pública que publica Sofía es el par (N,e) = ( 1789813 , 29 )")

# Contexto adicional sobre cómo Andrés codifica y encripta su mensaje
st.write("""
Con esta información, Andrés codifica el mensaje que le quiere enviar a Sofía. En este caso, el mensaje que le quiere enviar es “te amo”. Supongamos que Andrés y Sofía ya habían hablado previamente sobre su relación y que Sofía había decidido darle una oportunidad a Andrés para que le dijera lo que realmente sentía. Para esto, Sofía le dio entonces un tiempo a Andrés para que pensara y le dio la siguiente lista con códigos para cuando Andrés quisiera responderle: 1=si, 2=no, 3=te, 4=quiero, 5=amo, 6=ver. El mensaje de Andrés codificado con esta lista sería entonces M=35. Así, Andrés procede a encriptar su mensaje con ayuda de la clave pública de Sofía (N,e) efectuando la siguiente operación C = M^e (mod N) y publica su mensaje encriptado C. (El lector también puede escoger un mensaje diferente, codificarlo con la lista dada y pasárselo al siguiente método. Lo único que tiene que verificar es que su mensaje no sea mayor que N y que sea distinto a los dos primos P y Q)
""")

# Encriptación del mensaje de Andrés
st.subheader("Encriptación del mensaje de Andrés")

M = st.number_input("El mensaje de Andrés para Sofía es (luego de insertar el mensaje oprima ENTER): ", min_value=0, step=1)
exp = M ** e
C = exp % N
st.write(f"Mensaje encriptado C = {C}")

# Desencriptación del mensaje encriptado de Andrés
st.subheader("Desencriptación del mensaje encriptado de Andrés")

exp = C ** d
m = exp % N
st.write(f"Mensaje desencriptado MD = {m}")

# Contexto final
st.write("""
De esta manera, Sofía se entera de que Andrés en efecto sí la ama y sabe que nadie más, además de ella y Andrés, lo sabe. Así, Sofía y Andrés pudieron comunicarse de manera segura y Andrés pudo decirle lo que realmente sentía a Sofía.
""")

# Encriptar y desencriptar archivos con RSA
st.subheader("Encriptar y desencriptar archivos con RSA")

# Cargar archivo para encriptar
uploaded_file = st.file_uploader("Carga un archivo para encriptar", type=["txt"])

if uploaded_file is not None:
    # Leer el contenido del archivo
    file_content = uploaded_file.read().decode('utf-8')
    st.write("Contenido del archivo:")
    st.write(file_content)
    
    # Encriptar el contenido del archivo
    file_content_int = int.from_bytes(file_content.encode(), 'big')
    encrypted_content_int = pow(file_content_int, e, N)
    encrypted_content = encrypted_content_int.to_bytes((encrypted_content_int.bit_length() + 7) // 8, 'big')
    
    st.write("Contenido encriptado del archivo:")
    st.write(encrypted_content)
    
    # Botón para descargar el archivo encriptado
    st.download_button(label="Descargar archivo encriptado", data=encrypted_content, file_name="encrypted_file.txt")

    # Desencriptar el contenido del archivo encriptado
    decrypted_content_int = pow(encrypted_content_int, d, N)
    decrypted_content = decrypted_content_int.to_bytes((decrypted_content_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    
    st.write("Contenido desencriptado del archivo:")
    st.write(decrypted_content)