# -*- coding: utf-8 -*-
"""Untitled38.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14nnLJ0HQ6DYiiPrCBH-hPUex4ITEjsOg
"""

#!pip install streamlit

import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Polygon

st.title("Mi App Especial ❤️")

# Mensaje especial
if st.button("Te amo"):
    st.write("🌸 **Feliz mes, mi vida** 🌸")

# Función para dibujar el Bernés de la Montaña
def draw_bernes():
    fig, ax = plt.subplots()

    # Cuerpo y cabeza
    ax.add_patch(Circle((0, 0), 0.4, color="black"))  # Cabeza
    ax.add_patch(Circle((0, -0.6), 0.5, color="black"))  # Cuerpo

    # Pecho blanco
    ax.add_patch(Ellipse((0, -0.5), 0.3, 0.4, color="white"))

    # Ojos
    ax.add_patch(Circle((-0.15, 0.1), 0.07, color="white"))
    ax.add_patch(Circle((0.15, 0.1), 0.07, color="white"))

    # Pupilas
    ax.add_patch(Circle((-0.15, 0.1), 0.03, color="black"))
    ax.add_patch(Circle((0.15, 0.1), 0.03, color="black"))

    # Nariz
    ax.add_patch(Circle((0, -0.15), 0.05, color="black"))

    # Patas marrones
    ax.add_patch(Circle((-0.3, -0.8), 0.15, color="saddlebrown"))
    ax.add_patch(Circle((0.3, -0.8), 0.15, color="saddlebrown"))

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1.2, 0.5)
    ax.set_aspect('equal')
    plt.axis('off')

    return fig

# Función para dibujar el Panda
def draw_panda():
    fig, ax = plt.subplots()

    # Cuerpo y cabeza
    ax.add_patch(Circle((0, 0), 0.4, color="white"))  # Cabeza
    ax.add_patch(Circle((0, -0.6), 0.5, color="white"))  # Cuerpo

    # Ojos negros
    ax.add_patch(Ellipse((-0.15, 0.1), 0.15, 0.2, color="black"))
    ax.add_patch(Ellipse((0.15, 0.1), 0.15, 0.2, color="black"))

    # Pupilas blancas
    ax.add_patch(Circle((-0.15, 0.1), 0.05, color="white"))
    ax.add_patch(Circle((0.15, 0.1), 0.05, color="white"))

    # Nariz
    ax.add_patch(Circle((0, -0.15), 0.05, color="black"))

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1.2, 0.5)
    ax.set_aspect('equal')
    plt.axis('off')

    return fig

# Función para dibujar la Mariposa
def draw_butterfly():
    fig, ax = plt.subplots()

    # Alas (forma de triángulo)
    wing1 = Polygon([(-0.5, 0), (-0.2, 0.5), (0, 0.3)], color="purple")
    wing2 = Polygon([(0.5, 0), (0.2, 0.5), (0, 0.3)], color="purple")
    wing3 = Polygon([(-0.4, 0), (-0.2, -0.5), (0, -0.3)], color="blue")
    wing4 = Polygon([(0.4, 0), (0.2, -0.5), (0, -0.3)], color="blue")

    ax.add_patch(wing1)
    ax.add_patch(wing2)
    ax.add_patch(wing3)
    ax.add_patch(wing4)

    # Cuerpo
    ax.add_patch(Ellipse((0, 0), 0.1, 0.6, color="black"))

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    plt.axis('off')

    return fig

# Dibujar las figuras en Streamlit
st.pyplot(draw_bernes())
st.pyplot(draw_panda())
st.pyplot(draw_butterfly())