import streamlit as st
from PIL import Image
import requests

# Título de la aplicación
st.title("Criptografía de Curva Elíptica (ECC)")

# Imagen relacionada con criptografía
image_url = "https://pbs.twimg.com/media/Fe-xmLbUUAARO3X?format=jpg&name=large"
image = Image.open(requests.get(image_url, stream=True).raw)
st.image(image, caption="Criptografía", use_column_width=True)

# Sección de Introducción
st.header("Introducción")
st.write("""
La criptografía de curva elíptica (ECC) es una forma potente de criptografía moderna, que permite obtener claves públicas y privadas para compartir y proteger secretos de manera segura. ECC es reconocida por su alta eficiencia, rapidez y escalabilidad, lo que la hace ideal para su uso en tecnologías como blockchain, garantizando una altísima seguridad.
""")

# Sección: ¿Qué es la Criptografía de Curva Elíptica (ECC)?
st.header("¿Qué es la Criptografía de Curva Elíptica (ECC)?")
st.write("""
La criptografía de curva elíptica (ECC) es un método de cifrado asimétrico que utiliza estructuras algebraicas de curvas elípticas sobre campos finitos. Esto permite que las claves sean más pequeñas en comparación con otros sistemas criptográficos, sin comprometer la seguridad. La ECC es ampliamente utilizada en acuerdos de claves, firmas digitales y generadores pseudoaleatorios, además de combinarse con cifrados simétricos para mayor protección. Su seguridad se basa en la dificultad de resolver el problema de logaritmo discreto de curva elíptica (ECDLP).
""")

# Sección: Historia de la ECC
st.header("Historia de la ECC")
st.write("""
La criptografía basada en curvas elípticas fue propuesta en la década de 1980 por Victor Miller y Neal Koblitz, destacando sus propiedades matemáticas para aplicaciones criptográficas seguras. Desde entonces, la ECC ha soportado múltiples ataques y se ha normalizado por estándares como ANSI, NIST y FIPS, demostrando su confiabilidad y aplicabilidad en empresas y dispositivos inalámbricos donde la seguridad es vital.
""")

# Sección: ¿Cómo funciona la ECC?
st.header("¿Cómo funciona la ECC?")
st.write("""
Los algoritmos ECC, como el Algoritmo de Firma Digital de Curva Elíptica (ECDSA), utilizan coordenadas en una curva elíptica en lugar de números primos, como en el RSA. Una curva elíptica se representa algebraicamente con la ecuación:
""")
st.latex(r'''y^2 = x^3 + ax + b''')
st.write("""
Dependiendo de los valores de a y b, las curvas elípticas toman diferentes formas. En el caso de Bitcoin, se utiliza una curva elíptica ECDSA con la curva secp256k1.
""")

# Imagen relacionada con criptografía
image_url1 = "https://wiki.bitcoinsv.io/images/thumb/0/08/Elliptic-Curve-E-0-7-Real-Number.png/450px-Elliptic-Curve-E-0-7-Real-Number.png"
image1 = Image.open(requests.get(image_url1, stream=True).raw)
st.image(image1, caption="Criptografía de Curva Elíptica", use_column_width=True)


# Panel interactivo para modificar a y b
import matplotlib.pyplot as plt
import numpy as np

st.header("Interactividad: Modificar los valores de a y b")

a = st.slider("Valor de a", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
b = st.slider("Valor de b", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

# Crear la gráfica
x = np.linspace(-10, 10, 400)
y = np.sqrt(x**3 + a * x + b)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y^2 = x^3 + ax + b')
plt.plot(x, -y, label='y^2 = x^3 + ax + b (reflejado)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title(f'Curva Elíptica para a = {a}, b = {b}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
st.pyplot(plt)

# Sección: ¿Qué es el algoritmo de firma ECDSA?
st.header("¿Qué es el algoritmo de firma ECDSA?")
st.write("""
El algoritmo de firma ECDSA es una técnica de criptografía asimétrica que se basa en el uso de curvas elípticas sobre campos finitos. Funciona mediante la generación de un par de claves: una clave privada y una clave pública. La clave privada se utiliza para firmar digitalmente un mensaje, mientras que la clave pública se utiliza para verificar la autenticidad de la firma.

Es importante destacar que el algoritmo de firma ECDSA se utiliza mucho en aplicaciones donde la seguridad y la autenticidad de los datos son prioritarias, como en transacciones financieras, sistemas de autenticación y protocolos de seguridad en internet. Su eficiencia y robustez lo convierten en una opción preferida en entornos donde se requiere una protección sólida contra fraudes y ataques cibernéticos. Además, su implementación en dispositivos de hardware, como tarjetas inteligentes y dispositivos móviles, ha ampliado su alcance.
""")

#########
import streamlit as st

# Título de la aplicación
st.title("Curvas y Longitud de Clave en ECC")

st.write("""
Los algoritmos criptográficos de ECC pueden usar diferentes curvas elípticas subyacentes. Diferentes curvas proporcionan diferentes niveles de seguridad (fuerza criptográfica), rendimiento (velocidad) y longitud de clave, y también pueden involucrar diferentes algoritmos.

Las curvas ECC, adoptadas en las bibliotecas criptográficas populares y en los estándares de seguridad, tienen un nombre (curvas nombradas, por ejemplo, [secp256k1](https://neuromancer.sk/std/secg/secp256k1) o [Curve25519](https://neuromancer.sk/std/secg/curve25519)), tamaño del campo (que define la longitud de la clave, por ejemplo, 256 bits), fuerza de seguridad (generalmente el tamaño del campo / 2 o menos), rendimiento (operaciones/seg) y muchos otros parámetros.

Las claves ECC tienen una longitud que depende directamente de la curva subyacente. En la mayoría de las aplicaciones (como OpenSSL, OpenSSH y Bitcoin), la longitud de clave predeterminada para las claves privadas de ECC es de 256 bits, pero dependiendo de la curva, son posibles muchas longitudes de clave ECC diferentes: 192 bits (curva [secp192r1](https://neuromancer.sk/std/secg/secp192r1)), 233 bits (curva [sect233k1](https://neuromancer.sk/std/secg/sect233k1)), 224 bits (curva [secp224k1](https://neuromancer.sk/std/secg/secp224k1)), 256 bits (curvas secp256k1 y Curve25519), 283 bits (curva [sect283k1](https://neuromancer.sk/std/secg/sect283k1)), 384 bits (curvas p384 y [secp384r1](https://neuromancer.sk/std/secg/secp384r1)), 409 bits (curva [sect409r1](https://neuromancer.sk/std/secg/sect409r1)), 414 bits (curva [Curve41417](https://neuromancer.sk/std/secg/curve41417)), 448 bits (curva [Curve448-Goldilocks](https://neuromancer.sk/std/secg/curve448-goldilocks)), 511 bits (curva M-511), 521 bits (curva P-521), 571 bits (curva [sect571k1](https://neuromancer.sk/std/secg/sect571k1)) y muchas otras.
""")



