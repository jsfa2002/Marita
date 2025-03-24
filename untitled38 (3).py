import streamlit as st
import requests
import random
from PIL import Image
from io import BytesIO

# 🔒 Token de GitHub (¡NO compartas esto públicamente!)
GITHUB_TOKEN = "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"

# 📂 Configuración del repositorio
OWNER = "jsfa2002"
REPO = "fotos_lindas"
IMAGE_PATH = "imagenemYm"  # Verifica que la ruta sea correcta

# 🔹 Función para obtener imágenes del repo privado/público
def obtener_lista_imagenes():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{IMAGE_PATH}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_TOKEN}"  # Autenticación
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return [file["download_url"] for file in response.json() if file["name"].endswith((".png", ".jpg", ".jpeg"))]
    elif response.status_code == 403:
        st.error("❌ Acceso prohibido (403). Verifica el token o espera unos minutos.")
    elif response.status_code == 404:
        st.error("❌ No se encontró la carpeta. Verifica la ruta en GitHub.")
    else:
        st.error(f"❌ Error al obtener imágenes. Código {response.status_code}")
    return []

# 🖼 Mostrar título con emojis
st.markdown("<h1 style='text-align: center; color: pink;'>🧚‍♀️ Nuestras fotos ⛵</h1>", unsafe_allow_html=True)

# 📷 Cargar imágenes
image_urls = obtener_lista_imagenes()

if image_urls:
    if "img_index" not in st.session_state:
        st.session_state.img_index = random.randint(0, len(image_urls) - 1)

    if st.button("💖 Te amo 💖", use_container_width=True):
        st.session_state.img_index = random.randint(0, len(image_urls) - 1)

    # Descargar y mostrar la imagen
    response = requests.get(image_urls[st.session_state.img_index])
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        st.image(image, use_container_width=True)

        # 💖 Mensaje bonito debajo de la imagen
        st.markdown("<h2 style='text-align: center; color: pink;'>Eres lo más bonito de mi mundo 💖</h2>", unsafe_allow_html=True)
    else:
        st.error("❌ No se pudo cargar la imagen.")
else:
    st.warning("⚠ No hay imágenes disponibles.")
