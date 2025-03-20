# -*- coding: utf-8 -*-
"""Untitled38.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14nnLJ0HQ6DYiiPrCBH-hPUex4ITEjsOg
"""

import streamlit as st
import requests
import random
from PIL import Image
from io import BytesIO

# 🔒 Token de GitHub (NO compartir con nadie)
GITHUB_TOKEN = "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"

# 📂 Configuración del repositorio privado
OWNER = "jsfa2002"
REPO = "fotos_lindas"
IMAGE_PATH = "imagenemYm"  # Ruta dentro del repo

# 🔹 Función para obtener imágenes del repo privado
def obtener_lista_imagenes():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{IMAGE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return [file["download_url"] for file in response.json() if file["name"].endswith((".png", ".jpg", ".jpeg"))]
    else:
        st.error("Error al obtener imágenes. Verifica el token y la ruta.")
        return []

# 📷 Cargar imágenes
image_urls = obtener_lista_imagenes()

# 🖼 Mostrar imagen aleatoria al presionar el botón
if image_urls:
    if "img_index" not in st.session_state:
        st.session_state.img_index = random.randint(0, len(image_urls) - 1)

    if st.button("Te amo 💕"):
        st.session_state.img_index = random.randint(0, len(image_urls) - 1)

    # Descargar y mostrar la imagen
    response = requests.get(image_urls[st.session_state.img_index])
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        st.image(image, use_column_width=True)
    else:
        st.error("No se pudo cargar la imagen.")

    # ✨ Mensaje bonito
    st.markdown("<h2 style='text-align: center; color: pink;'>Eres lo más boni de mi mundo 🌸</h2>", unsafe_allow_html=True)
else:
    st.warning("No hay imágenes disponibles.")