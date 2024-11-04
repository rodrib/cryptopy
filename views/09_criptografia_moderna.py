import streamlit as st

# Título de la aplicación
st.title("Infraestructura de Llave Pública (PKI)")

# Descripción de la PKI
st.write("""
La Infraestructura de Llave Pública (PKI) es un criptosistema que define roles, políticas y procedimientos para distribuir y revocar certificados firmados utilizando criptografía asimétrica. Se utiliza ampliamente para asegurar la comunicación segura a través de internet y otros sistemas.

### Componentes de la PKI:

- **Autoridad Certificadora (CA)**: Entidad que emite y gestiona certificados digitales.
- **Autoridad Registradora (RA)**: Facilita la verificación de identidad de los solicitantes de certificados antes de enviar la solicitud a la CA.
- **Autoridad Validadora (VA)**: Encargada de verificar la autenticidad de un certificado digital.
- **Sellos de Tiempo**: Servicios que proporcionan evidencia de que los datos existían en un momento específico.
- **Repositorios con Información Adicional**: Almacenan y distribuyen certificados y listas de revocación.

### TLS (Transport Layer Security):

TLS es un protocolo criptográfico que asegura las comunicaciones en internet mediante el uso de PKI. Establece un canal seguro para el intercambio de datos mediante autenticación, integridad de datos y confidencialidad.

### PKCS (Public Key Cryptography Standards):

PKCS es un conjunto de estándares para criptografía asimétrica, principalmente alrededor del algoritmo RSA. Define formatos de clave pública, operaciones criptográficas y gestión de certificados digitales. Es ampliamente utilizado en organizaciones para asegurar la autenticación y la comunicación segura.
""")

# Links
st.markdown("- [TLS en Wikipedia](https://es.wikipedia.org/wiki/Transport_Layer_Security)")
st.markdown("- [PKCS en Wikipedia](https://es.wikipedia.org/wiki/Public_Key_Cryptography_Standards)")



# Título de la sección
st.title("Sistemas de Pruebas Interactivos (SPI)")

# Descripción de los SPI
st.markdown("""
En el ámbito de la criptografía, los sistemas de pruebas interactivos (SPI) desempeñan un papel crucial en la verificación de información sin revelar secretos. Estos sistemas permiten a un probador (que posee información confidencial) demostrar a un verificador (que no posee dicha información) que cumple con ciertas condiciones sin revelar la información en sí.

### Principio fundamental de los SPI:

Los SPI se basan en el concepto de conocimiento cero, donde el probador puede demostrar al verificador que posee cierta información sin revelarla durante el proceso.

### Funcionamiento de los SPI:

1. El probador y el verificador acuerdan un protocolo de comunicación.
2. El probador envía un mensaje inicial al verificador, que puede incluir información pública y/o compromisos criptográficos.
3. El verificador desafía al probador con una serie de preguntas o tareas según el protocolo.
4. El probador responde a los desafíos utilizando cálculos criptográficos y/o revelaciones parciales de información.
5. El verificador verifica las respuestas y decide si aceptar o rechazar la prueba.

### Propiedades clave de los SPI:

- **Seguridad**: El verificador no obtiene información confidencial incluso si la prueba falla.
- **Completitud**: Si el probador posee realmente la información, podrá convencer al verificador con alta probabilidad.
- **Solidez**: Si el verificador acepta la prueba, significa que el probador realmente posee la información requerida.

### Aplicaciones de los SPI en criptografía:

- **Firmas digitales**: Verificar la posesión de una clave privada sin revelarla.
- **Autenticación de identidad**: Demostrar la identidad sin exponer contraseñas.
- **Criptografía de curva elíptica**: Intercambio seguro de claves entre dos partes.
- **Pruebas de conocimiento cero**: Construcción de pruebas que demuestran la posesión de información sin divulgarla.

### Ejemplos de SPI en criptografía:

- Protocolo Fiat-Shamir
- Protocolo Guillou-Quisquater
- Protocolo Schnorr
- Protocolo Sigma

En resumen, los sistemas de pruebas interactivos son herramientas esenciales en criptografía para verificar información sin comprometer la seguridad y privacidad de los datos.
""")

# Links de referencia
st.markdown("- [Más información sobre los SPI](https://es.wikipedia.org/wiki/Sistema_de_prueba_interactiva)")


# Título de la sección
st.title("Computación Cuántica")

# Descripción de la Computación Cuántica
st.markdown("""
La Computación Cuántica es un campo de estudio que explora el uso de principios cuánticos para procesar información de manera más eficiente que la computación clásica. Existe interés y debate sobre cómo podría afectar a la criptografía a largo plazo.

### Impacto en la Criptografía:

Se discute si la computación cuántica podría eventualmente romper algunos criptosistemas actuales al aprovechar sus capacidades únicas, como la superposición y el entrelazamiento cuántico. Sin embargo, esto es un área de investigación y existen limitaciones significativas.

### Qubits y Superposición:

Un qubit, abreviatura de quantum bit, es la unidad básica de información cuántica. A diferencia de los bits clásicos que son 0 o 1, un qubit puede estar en una superposición de ambos estados simultáneamente, lo cual es fundamental para los cálculos cuánticos.

### Ejemplo del Experimento de Doble Rendija:

El experimento de doble rendija ilustra propiedades cuánticas donde un qubit puede comportarse de manera diferente cuando no se observa. Esto podría aplicarse a resolver problemas complejos ajustando las propiedades del entorno adecuadamente.

En resumen, aunque la Computación Cuántica promete avances significativos en ciertos campos, como la optimización y simulación molecular, su impacto en la criptografía es un área de estudio en desarrollo con implicaciones aún por determinar.
""")

# Link de referencia
st.markdown("- [Más información sobre Computación Cuántica](https://es.wikipedia.org/wiki/Computaci%C3%B3n_cu%C3%A1ntica)")


import requests
from PIL import Image
from io import BytesIO


# URL de la imagen del experimento de doble rendija
image_url = "https://www.dciencia.es/wp-content/uploads/Doble-rendija1.jpg"

# Cargar la imagen desde la URL
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Agregar la imagen debajo del título
st.image(image, caption="Figura 1. Esquema del experimento de la doble rendija. A la izquierda cuando estamos observando, a la derecha cuando no estamos observando. Imagen tomada de: https://institucional.us.es/blogimus/2019/04/y-las-ondas-se-convirtieron-en-particulas/", use_column_width=True)

# URL de la imagen del qubit
image_url1 = "https://miro.medium.com/v2/resize:fit:1400/format:webp/1*tr-EJH8iKZ5vfnGq4Iqf-w.png"

# Cargar la imagen desde la URL
response = requests.get(image_url1)
image1 = Image.open(BytesIO(response.content))

# Agregar la imagen debajo del título
st.image(image1, caption="Qubit", use_column_width=True)

# Texto estructurado como items
texto = """
- Un qubit solo puede tomar valores entre 0 y 1.
- Recopilar más información o colocar más qubits juntos puede desestabilizarlos fácilmente, requiriendo condiciones muy específicas como el aislamiento ambiental y bajas temperaturas.
- Se puede utilizar para paralelizar problemas como el cálculo del logaritmo discreto y la factorización de números primos grandes.
- Teóricamente, estas técnicas podrían romper el criptosistema RSA.
- Estudios recientes indican que se necesitan alrededor de un millón de qubits para factorizar números primos grandes.
- A este nivel, los qubits se vuelven tan inestables que es difícil mantener su coherencia en conjunto.
"""

# Mostrar en Streamlit
st.title("Problemas y aplicaciones de los qubits")
st.markdown(texto)


# """ import streamlit as st
# from PIL import Image
# import requests
# from io import BytesIO

# # URL de la imagen del circuito cuántico
# image_url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Quantum_teleportation_circuit.svg/1920px-Quantum_teleportation_circuit.svg.png"


# # Cargar la imagen desde la URL
# response = requests.get(image_url2)
# image2 = Image.open(BytesIO(response.content)) """

# # Texto para mostrar debajo de la imagen
# caption_text = """
# Circuito que realiza la teletransportación de un qubit.
# Este circuito consta tanto de puertas cuánticas como de medidas.
# La medición es un fenómeno cuántico que no ocurre en los circuitos clásicos.
# """

# # Agregar la imagen debajo del título
# st.image(image2, caption=caption_text, use_column_width=True)


st.title("Investigación en Criptografía")

# Descripción
st.write("""
Los artículos sobre criptografía más importantes que abarcan el pasado, el presente y el futuro de los criptosistemas y la criptología.
""")

import streamlit as st
from PIL import Image

# Cargar imagen desde un archivo local
#imagen_local = "math-paper1.png"
#imagen = st.image(imagen_local, caption="Non-Malleable Cryptography", use_column_width=True)



# Título
st.header("Criptografía No Maleable")

# Resumen
st.write("""
**Criptografía No Maleable**  
Danny Dolev, Cynthia Dwork y Moni Naor — Publicado en enero de 1991

"Maleable" significa capaz de transformarse en otra forma sin romperse ni agrietarse.

La no-maleabilidad, según se define en la Seguridad Semántica (Goldwasser y Micali, 1982), dice que al ver una encriptación de un mensaje, no nos ayuda a encontrar los detalles del mensaje en texto plano. El adversario no aprende nada sobre el mensaje original solo viendo la encriptación y no puede producir ningún texto plano relacionado con el mensaje.

El concepto de criptografía no maleable, una extensión de la criptografía semánticamente segura, va un paso más allá: dado el texto cifrado de un mensaje, es imposible generar un texto cifrado diferente de modo que los respectivos textos planos estén relacionados.

El mismo concepto tiene sentido en los contextos de compromiso de cadenas y pruebas de conocimiento cero. Se presentan esquemas no maleables para cada uno de estos tres problemas. Los esquemas no suponen un centro de confianza; un usuario no necesita saber nada sobre el número o la identidad de otros usuarios del sistema.

En el momento de su publicación, este criptosistema fue el primero en demostrarse seguro contra un tipo fuerte de ataque de texto cifrado elegido propuesto por Rackoff y Simon, en el que el atacante conoce el texto cifrado que desea romper y puede consultar el oráculo de descifrado sobre cualquier texto cifrado que no sea el objetivo.
""")

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/b62c499ec81e5053ef904e5c497283a2b0f056d9.pdf)")


# Cargar imagen desde un archivo local
#imagen_local2 = "math-paper2.png"
#imagen = st.image(imagen_local2, caption="On the (Im)possibility of Obfuscating Programs", use_column_width=True)

# Título
st.header("Sobre la (im)posibilidad de ofuscar programas")

# Resumen
st.write("""
**Sobre la (im)posibilidad de ofuscar programas**  
Los artículos sobre la ofuscación de programas abordan cómo hacer que un programa sea ininteligible pero funcionalmente preservado.
Esto permite que una parte entregue un programa ejecutable a otra parte sin revelar su funcionamiento interno.
La investigación comenzó en 2001 con la demostración de la imposibilidad de la ofuscación de caja negra virtual y la introducción de la ofuscación de indistinguibilidad (IO) más débil. Artículos posteriores incluyen propuestas de esquemas de IO candidatos y aplicaciones de programas perforados, resolviendo problemas como el cifrado negable y construyendo IO basado en suposiciones criptográficas.
""")

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/539a6d18a0e90fe6d9d27769b7d42469298fc329.pdf)")


##########
# Cargar imagen desde un archivo local
#imagen_local3 = "math-paper3.png"
#imagen = st.image(imagen_local2, caption="Computer Systems Established, Maintained and Trusted by Mutually Suspicious Groups", use_column_width=True)

#Titulo
st.header("Sistemas informáticos establecidos, mantenidos y en los que confían grupos mutuamente sospechosos")


# Resumen del artículo
resumen3 = """
Este artículo es la primera propuesta conocida de un protocolo de blockchain.

Chaum describe el diseño de un sistema informático distribuido que puede ser establecido, mantenido y confiable por grupos mutuamente desconfiados.

Es un sistema de registro público con consistencia de membresía grupal y cálculos de transacciones privadas que protege la privacidad individual a través de la seguridad física.

Los componentes del sistema incluyen "bóvedas" físicamente seguras, primitivas criptográficas existentes (cifrado simétrico y asimétrico, funciones hash criptográficas, firmas digitales) y una nueva primitiva introducida por Chaum: el reparto secreto umbral, donde un umbral de claves subparciales es suficiente para reconstruir la clave original.

Para más sobre la historia de las tecnologías blockchain, considere "On the Origins and Variations of Blockchain Technologies".
"""

# Mostrar el resumen en Streamlit
st.write(resumen3)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/e630610a9c7c3c8f950cfb5632b44ecf1b8926d2.pdf)")


# Cargar imagen desde un archivo local
#imagen_local4 = "math-paper4.png"
#imagen = st.image(imagen_local4, caption="A Digital Signature Based on a Conventional Encryption Function", use_column_width=True)

#Titulo
st.header("Una firma digital basada en una función de cifrado convencional")

resumen4 = """
En este artículo, Ralph C. Merkle desarrolló el concepto de los árboles de Merkle, que permiten almacenar datos eficientemente, ahorrando memoria y potencia de procesamiento.

Los árboles de Merkle utilizan funciones hash, que calculan un valor único y fijo (hash) a partir de datos. Un pequeño cambio en la entrada cambia completamente el hash; los hashes son únicos y unidireccionales. Los árboles de Merkle organizan y verifican datos mediante la creación de un árbol de hashes, donde cada nodo padre se forma a partir de los hashes de sus nodos hijos.

Los cambios en cualquier punto del árbol afectan los hashes siguientes, incluyendo el hash raíz. Las pruebas de Merkle verifican la integridad de los hashes en todas las ramas del árbol. Estos árboles son esenciales en criptomonedas como Bitcoin y Ethereum.
"""


# Mostrar el resumen en Streamlit
st.write(resumen4)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/5bcd990b11e068234c3a13b021f3266bb45a2964.pdf)")


#Titulo
st.header("La complejidad del conocimiento de los sistemas de prueba interactivos")

# Resumen del artículo sobre Zero-Knowledge Proofs
resumen5 = """
En este artículo, Shafi Goldwasser, Silvio Micali y Charles Rackoff introdujeron las pruebas de conocimiento cero (ZKP), una técnica criptográfica que permite a un probador demostrar a un verificador que un cálculo es correcto sin revelar más información que la veracidad de la declaración. Los ZKP permiten verificar la integridad de los datos sin exponer detalles subyacentes. En 2012, Goldwasser y Micali recibieron el Premio Turing por su trabajo en la teoría de la complejidad en criptografía. Una versión preliminar del artículo se publicó en 1986 y la versión revisada en 1989.
"""

# Mostrar el resumen en Streamlit
st.write(resumen5)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/0216c6a57ccda410243a2e4b165e141439d2c5ea.pdf)")


#Titulo
st.header("Longitudes de clave mínimas para cifrados simétricos para proporcionar una seguridad comercial adecuada")


resumen6 = """
La criptografía se basa en la gestión eficaz de las claves de cifrado. Un estudio histórico de criptógrafos e informáticos destaca que las claves más largas ofrecen mayor resistencia a ataques, sin aumentar significativamente el costo del cifrado. Se recomienda que los datos cifrados permanezcan seguros por al menos 20 años. Los tamaños de las claves se miden en bits, y su seguridad crece exponencialmente con cada bit adicional. Aumentar la longitud de la clave en un bit duplica las posibles combinaciones, mientras que diez bits las multiplican por más de mil. Esta relación entre longitud de clave y seguridad es fundamental para entender y aplicar la criptografía moderna de manera efectiva.
"""

st.write(resumen6)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/a1f8074ba7d8eca67be24ae22d0d0b2a3544e759.pdf)")


#Titulo
st.header("CryptDB: protección de la confidencialidad con procesamiento de consultas cifradas")

resumen7 = """
CryptDB, desarrollado por Popa, Redfield, Zeldovich y Balakrishnan en 2011, es un sistema pionero que permite procesar consultas SQL sobre datos cifrados sin acceso a las claves de descifrado. Este enfoque representa un punto intermedio entre bases de datos convencionales y el cifrado totalmente homomórfico. CryptDB responde a la creciente necesidad de que las aplicaciones se protejan a sí mismas, especialmente en interacciones con bases de datos, ya sea en la nube o localmente. El sistema utiliza esquemas de cifrado compatibles con SQL para ejecutar consultas sobre datos cifrados, ofreciendo confidencialidad práctica y demostrable. Su eficacia se basa en que la mayoría de las consultas SQL usan un conjunto limitado de operadores, que CryptDB puede manejar eficientemente en datos cifrados.
"""

st.write(resumen7)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/22a5eeb8608b35e371b7544a54fabeadca8866e3.pdf)")

#Titulo
st.header("Protocolos para cálculos seguros")



resumen8 = """
Andrew C. Yao, en su publicación de 1982 "Protocolos para cálculos seguros", introdujo el concepto revolucionario de computación multipartita segura (MPC). Este innovador enfoque permite que múltiples entidades independientes realicen operaciones conjuntas sobre sus datos privados agregados, obteniendo resultados sin revelar la información individual de cada parte. La MPC representa un avance significativo en la protección de la privacidad en cálculos colaborativos, equilibrando la necesidad de compartir resultados con la confidencialidad de los datos de entrada. Esta tecnología tiene aplicaciones potenciales en diversos campos como finanzas, investigación médica y análisis de datos, donde la privacidad y la colaboración son igualmente cruciales. Para profundizar en el tema, se recomienda consultar la "Introducción pragmática a la computación multipartita segura".
"""

st.write(resumen8)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/0e0427aedfed65c8dd688c094b181feacf4eaab4.pdf)")


#Titulo
st.header("Bitcoin: un sistema de efectivo electrónico entre pares")



resumen9 = """
Satoshi Nakamoto introdujo Bitcoin en 2008 como un sistema de dinero electrónico peer-to-peer que elimina la necesidad de intermediarios en las transacciones. Basado en criptografía de clave pública, Bitcoin resolvió por primera vez el problema de los generales bizantinos, estableciendo confianza en redes no confiables. Utiliza una cadena de firmas digitales para crear monedas y una prueba de trabajo basada en hash para prevenir el doble gasto sin terceros de confianza. Este innovador enfoque ha inspirado el desarrollo de otras criptomonedas y redes como Ethereum. Bitcoin representa un hito en la tecnología financiera, combinando conceptos de criptografía, descentralización y consenso distribuido para crear un sistema monetario revolucionario y resistente a la censura.
"""

st.write(resumen9)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/8de2fdb04edce612738eb51e14ecc426381f8ed8.pdf)")


#Titulo
st.header("Un esquema de cifrado completamente homomórfico")



resumen10 = """
En "A fully homomorphic encryption scheme", Craig Gentry presenta la primera construcción plausible de un esquema de cifrado totalmente homomórfico (FHE), respondiendo al problema planteado en 1978 por Rivest, Adleman y Dertouzos. El FHE permite realizar cálculos arbitrarios en datos cifrados sin necesidad de descifrarlos o tener una clave secreta, siendo homomorfo tanto para la suma como para la multiplicación. Aunque aún no es práctico para una implementación generalizada, el avance de Gentry tiene implicaciones significativas para la seguridad de la computación en la nube y la privacidad de datos. Gentry advierte sobre los riesgos de almacenar datos sin cifrar en la nube, destacando la importancia del FHE para prevenir un futuro "orwelliano" de vigilancia.
"""

st.write(resumen10)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/5496636b7474ef68f79248de4a63dd879db55334.pdf)")


#Titulo
st.header("Sobre los bancos de datos y los homomorfismos de la privacidad")



resumen11 = """
Rivest, Adleman y Dertouzos plantearon en "On Data Banks and Privacy Homomorphisms" dos desafíos cruciales: realizar operaciones seguras en datos cifrados y construir un esquema de cifrado totalmente homomórfico (FHE). El sistema RSA es un ejemplo de cifrado parcialmente homomórfico, donde la multiplicación del texto cifrado se refleja en el texto plano. Un FHE permite tanto suma como multiplicación en datos cifrados sin descifrarlos ni usar clave secreta. Esto posibilita procesar datos cifrados manteniéndolos seguros. Aunque propuesto en los 70, el primer esquema FHE plausible fue presentado por Craig Gentry en 2009, marcando un hito en criptografía y privacidad de datos.
"""

st.write(resumen11)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/c365f01d330b2211e74069120e88cff37eacbcf5.pdf)")

#Titulo
st.header("Un algoritmo rápido de mecánica cuántica para la búsqueda de bases de datos")



resumen12 = """
El "Algoritmo cuántico rápido para búsqueda en bases de datos" de Grover representa una amenaza para la criptografía simétrica estándar, como AES. Este algoritmo puede encontrar la entrada de una función de caja negra dada su salida en tiempo O(√n), siendo asintóticamente óptimo. Su impacto en criptosistemas simétricos es significativo: reduce la seguridad de AES-256 al nivel de AES-128. Para contrarrestar ataques basados en el algoritmo de Grover, se recomienda duplicar el tamaño de bit del esquema criptográfico. Por ejemplo, usar AES-256 en lugar de AES-128, ya que Grover puede romper un esquema de 256 bits en 2^128 iteraciones en lugar de 2^256, manteniendo así un nivel de seguridad adecuado.
"""


st.write(resumen12)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/ad75b43834fc0da81bccc4072ab2c58ce37516f4.pdf)")

#Titulo
st.header("Algoritmos de tiempo polinomial para factorización prima y logaritmos discretos en una computadora cuántica")



resumen13 = """
Peter Shor, en 1994, demostró que los problemas de factorización de enteros y logaritmos discretos, base de criptosistemas como RSA y de curva elíptica, pueden resolverse en tiempo polinomial en un ordenador cuántico. Este avance amenaza la seguridad de los criptosistemas de clave pública actuales, incluyendo los usados en HTTPS. Shor advierte que la computación cuántica podría convertirse en una técnica especializada para vulnerar estos sistemas. Como respuesta, el NIST está estandarizando algoritmos de criptografía resistentes a la computación cuántica. Evervault planea acelerar la implementación de esta nueva criptografía para proteger los datos en la web, anticipándose a la era de los ordenadores cuánticos prácticos.
"""


st.write(resumen13)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/703d0b290a4ece50c17854ed72ecc808ce3e6f43.pdf)")

#Titulo
st.header("Uso de curvas elípticas en criptografía")



resumen14 = """
Este artículo, junto con "Elliptic Curve Cryptosystems", introdujo independientemente el uso de curvas elípticas en criptografía. A diferencia de RSA, basado en la factorización de números grandes, la criptografía de curva elíptica (ECC) se fundamenta en el problema del logaritmo discreto de curva elíptica. ECC ofrece seguridad comparable a RSA pero con claves más cortas y cálculos más eficientes. El desafío en ECC es encontrar un número entero n tal que Q = nP, dados dos puntos P y Q en una curva elíptica. Actualmente, ECC, especialmente el protocolo Elliptic Curve Diffie-Hellman (ECDH), es el método preferido para la autenticación en navegación web segura a través de SSL/TLS, demostrando su importancia en la criptografía moderna.
"""

st.write(resumen14)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/eadb771624c6bb59e2f1a1aede341e953c227032.pdf)")

#Titulo
st.header("Criptosistemas de curva elíptica")


resumen15 = """
Este artículo, junto con "Uso de curvas elípticas en criptografía", introdujo independientemente la criptografía de curva elíptica (ECC). A diferencia de RSA, que se basa en la factorización de grandes números primos, ECC utiliza el problema del logaritmo discreto de curva elíptica: encontrar n tal que Q = nP en una curva elíptica. ECC ofrece seguridad comparable a RSA con claves más cortas y cálculos más eficientes. Actualmente, ECC, especialmente el protocolo Elliptic Curve Diffie-Hellman (ECDH), es el método preferido para autenticación en navegación web segura mediante SSL/TLS. Esta innovación ha transformado significativamente la criptografía moderna, ofreciendo una alternativa más eficiente y segura a los métodos tradicionales de clave pública.
"""

st.write(resumen15)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/72c46c82327564ca337538202ffd311234a25cbf.pdf)")


#Titulo
st.header("Un método para obtener firmas digitales y criptosistemas de clave pública")



resumen16 = """
El artículo "New Directions in Cryptography" de Diffie y Hellman introdujo el concepto teórico de la criptografía de clave pública (PKC). Posteriormente, Rivest, Shamir y Adleman, en "A Method for Obtaining Digital Signatures and Public Key Cryptosystems", presentaron la primera implementación práctica de PKC, conocida como RSA. Este trabajo no solo materializó la teoría de Diffie y Hellman, sino que también introdujo a los personajes icónicos Alice y Bob en la literatura criptográfica. La importancia del sistema RSA fue tal que Diffie lo calificó como la contribución más espectacular al campo de la criptografía de clave pública, marcando un hito fundamental en la historia de la seguridad de la información.
"""

st.write(resumen16)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/733b3d4a7994bd9ecd6f01fd5aae9a6c0797f591.pdf)")


#Titulo
st.header("Nuevas direcciones en criptografía")



resumen17 = """
El artículo de Whitfield Diffie y Martin E. Hellman, publicado en noviembre de 1976, marcó un hito en la historia de la criptografía al introducir el revolucionario concepto de criptografía de clave pública, también conocida como criptografía asimétrica. Este innovador enfoque utiliza dos claves distintas: una para cifrar y otra para descifrar. La principal ventaja de este sistema es que permite a dos partes comunicarse de forma segura a través de un canal no seguro sin necesidad de compartir previamente una clave secreta. Esta idea transformó fundamentalmente la seguridad de la información, sentando las bases para muchas de las comunicaciones seguras que utilizamos hoy en día en internet.
"""

st.write(resumen17)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/d32bda39418af2b8fe13792d25ca8f29ef1e4ca3.pdf)")


#Titulo
st.header("Amontonando más componentes en los circuitos integrados")



resumen18 = """
El artículo de Gordon Moore de 1965 dio origen a la Ley de Moore, que predice la duplicación de transistores en circuitos integrados cada dos años. Esta ley se relaciona directamente con el avance en velocidad de procesamiento, precio y capacidad de memoria en informática. Bruce Schneier señala su relevancia en criptografía: todos los algoritmos criptográficos son vulnerables a ataques de fuerza bruta, que se facilitan con el tiempo debido a la Ley de Moore. Esto implica que la potencia computacional creciente hace más factibles los ataques que prueban todas las claves posibles o buscan colisiones en funciones hash. Por lo tanto, la Ley de Moore tiene un impacto significativo en el criptoanálisis, influyendo en la evolución y seguridad de los sistemas criptográficos.
"""

st.write(resumen18)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/0df73868bca566aff47e809b1523f5f69580052f.pdf)")


#Titulo
st.header("Una teoría matemática de la criptografía")


resumen19 = """
Claude E. Shannon sentó las bases de la criptografía y teoría de la información modernas con tres publicaciones clave. En 1945, escribió "Una teoría matemática de la criptografía", un informe técnico que definió y demostró matemáticamente el concepto de secreto perfecto. Este trabajo fue la base para dos artículos fundamentales: "Una teoría matemática de la comunicación" (1948), considerado el fundamento de la teoría de la información moderna, y "Teoría de la comunicación de los sistemas de secreto" (1949), que vinculó la criptografía con la teoría de la información. Estos trabajos de Shannon establecieron los cimientos teóricos para el desarrollo de la criptografía y la teoría de la información, influyendo profundamente en ambos campos hasta la actualidad.
"""


st.write(resumen19)


# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/453b536b9cef87f0ae4ce1c1f6d10427edb49c28.pdf)")

#Titulo
st.header("La criptografía militar")


resumen20 = """
El artículo de Auguste Kerckhoffs de 1883 dio origen al Principio de Kerckhoffs, un concepto fundamental en criptografía. Este principio establece que la seguridad de un sistema criptográfico debe depender exclusivamente de la elección de sus claves, mientras que todos los demás aspectos, incluido el algoritmo mismo, deben considerarse de conocimiento público. El corolario de este principio sugiere que los desarrolladores deben utilizar únicamente sistemas criptográficos completamente conocidos y transparentes. Este enfoque, que prioriza la transparencia y la robustez del diseño sobre el secreto del método, es un principio básico adoptado por empresas como Evervault en sus prácticas de seguridad, promoviendo la confianza y la verificabilidad en los sistemas criptográficos.
"""


st.write(resumen20)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/cbbaa37b5870570fe75bb35c9144fb183e0e43ac.pdf)")