import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image

# --- Product Design ---

# Paleta de colores profesional (ejemplo)
color_principal = "#007bff"  # Azul
color_secundario = "#6c757d"  # Gris
color_resaltado = "#28a745"  # Verde

# Estilo de la página
st.set_page_config(
    page_title="Labor Parlamentaria Senador Castro",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Fuentes y Estilos CSS
st.markdown(
    """
    <style>
    .main-header {
        color: """
    + color_principal
    + """;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }

    .section-header {
        color: """
    + color_secundario
    + """;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    .storytelling {
        font-size: 16px;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    .stButton button {
        background-color: """
    + color_principal
    + """;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# --- Datos ---

# Datos de ejemplo (Reemplazar con datos reales del Senador)
# **Nota:**  Para aprovechar al máximo las visualizaciones interactivas,  
# es recomendable tener un set de datos más amplio y detallado.
data_intervenciones = {
    "Legislatura": [369, 369, 369, 370, 370, 370, 371, 371, 371, 371],
    "Tema": [
        "Seguridad Ciudadana",
        "Desarrollo Regional",
        "Pymes y Agricultura",
        "Seguridad Ciudadana",
        "Reforma Constitucional",
        "Medio Ambiente",
        "Salud",
        "Educación",
        "Economía",
        "Justicia",
    ],
    "Cantidad": [10, 5, 8, 12, 6, 7, 4, 6, 9, 5],
}

data_votaciones = {
    "Tema": ["Reforma Código Aguas", "Postergación Elecciones", "Ley de Usurpación", "Ley de Royalty Minero"],
    "A Favor": [8, 5, 12, 10],
    "En Contra": [2, 5, 3, 4],
    "Abstención": [1, 1, 0, 1],
}

data_mociones = {
    "Legislatura": [369, 369, 369, 370, 370, 370, 371, 371, 371],
    "Tipo": [
        "Proyecto de Ley",
        "Reforma Constitucional",
        "Proyecto de Acuerdo",
        "Proyecto de Ley",
        "Proyecto de Resolución",
        "Moción Inadmisible",
        "Proyecto de Ley",
        "Reforma Constitucional",
        "Proyecto de Acuerdo",
    ],
    "Cantidad": [15, 5, 8, 10, 3, 2, 12, 4, 9],
}

data_mociones_tema = {
    "Tema": [
        "Seguridad Ciudadana",
        "Desarrollo Regional",
        "Medio Ambiente",
        "Educación",
        "Economía",
        "Salud",
        "Justicia",
    ],
    "Cantidad": [8, 6, 4, 5, 7, 3, 2],
}

data_peticiones = {
    "Legislatura": [369, 369, 370, 370, 371, 371],
    "Destinatario": [
        "Ministerio Interior",
        "Ministerio Agricultura",
        "Contraloría",
        "Ministerio Justicia",
        "Ministerio Salud",
        "Ministerio Transportes",
    ],
    "Cantidad": [12, 8, 5, 6, 7, 4],
}

palabras_clave_peticiones = "seguridad, transparencia, agua, agricultura, Maule, desarrollo social, economía, justicia, pymes, salud, educación"

# --- Contenido del Dashboard ---

# Título
st.markdown('<p class="main-header">Labor Parlamentaria del Senador Juan Enrique Castro Prieto</p>', unsafe_allow_html=True)

# Introducción
col1, col2 = st.columns([1, 3])  # Ajustar la proporción de las columnas
with col1:
    imagen_senador = Image.open("senador_castro.jpg")  # Reemplazar con imagen real
    st.image(imagen_senador, width=200)
with col2:
    st.write(
        """
        Juan Enrique Castro Prieto es un Senador comprometido con el servicio público y el desarrollo de la Región del Maule.  
        Este dashboard interactivo permite explorar su labor parlamentaria,  evidenciando su activa participación en el debate,  
        su compromiso con la generación de iniciativas legislativas y  su rol fiscalizador para promover la transparencia y el bienestar de la ciudadanía. 
        """
    )

# Separador
st.markdown("---")

# Sección 1: Participación Activa en el Debate
st.markdown('<p class="section-header">1. Participación Activa en el Debate</p>', unsafe_allow_html=True)

# Gráfico 1: Temas de Intervención
df_intervenciones = pd.DataFrame(data_intervenciones)
fig1 = px.bar(
    df_intervenciones,
    x="Tema",
    y="Cantidad",
    color="Legislatura",
    title="Temas de Intervención por Legislatura",
    labels={"Cantidad": "Cantidad de Intervenciones"},
    color_discrete_sequence=[color_principal, color_secundario],  # Asignar colores
)

fig1.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig1, use_container_width=True)

st.markdown('<p class="storytelling">El Senador Castro ha participado activamente en los debates más relevantes para el país,  defendiendo con convicción sus posturas y buscando soluciones a las problemáticas que afectan a la ciudadanía.</p>', unsafe_allow_html=True)

# Gráfico 2: Posición en Votaciones Clave
df_votaciones = pd.DataFrame(data_votaciones)
fig2 = px.pie(
    df_votaciones,
    values="A Favor",
    names="Tema",
    title="Votaciones a Favor en Temas Clave",
    color_discrete_sequence=px.colors.sequential.Greens,  # Paleta de colores verde
)

fig2.update_traces(textposition="inside", textinfo="percent+label")
st.plotly_chart(fig2, use_container_width=True)

st.markdown('<p class="storytelling">El Senador Castro ha demostrado una postura firme y coherente en las votaciones clave,  priorizando el bienestar de la ciudadanía y buscando el desarrollo del país.</p>', unsafe_allow_html=True)


# Separador
st.markdown("---")

# Sección 2: Impulsando Iniciativas Legislativas
st.markdown('<p class="section-header">2. Impulsando Iniciativas Legislativas</p>', unsafe_allow_html=True)

# Gráfico 3: Tipos de Mociones Presentadas
df_mociones = pd.DataFrame(data_mociones)
fig3 = px.pie(
    df_mociones,
    values="Cantidad",
    names="Tipo",
    title="Tipos de Mociones Presentadas por Legislatura",
    facet_col="Legislatura",
    color_discrete_sequence=px.colors.qualitative.Set2,  # Paleta de colores diversa
)

fig3.update_traces(textposition="inside", textinfo="percent+label")
st.plotly_chart(fig3, use_container_width=True)

st.markdown('<p class="storytelling">El Senador Castro ha presentado una diversidad de iniciativas legislativas,  demostrando su compromiso con la búsqueda de soluciones a los desafíos que enfrenta el país.</p>', unsafe_allow_html=True)

# Gráfico 4: Temas de las Mociones
df_mociones_tema = pd.DataFrame(data_mociones_tema)
fig4 = px.bar(
    df_mociones_tema,
    y="Tema",
    x="Cantidad",
    title="Temas de las Mociones Presentadas",
    orientation="h",
    color="Tema",
    color_discrete_sequence=px.colors.qualitative.Pastel1,  # Paleta de colores pastel
)

fig4.update_layout(xaxis_title="Cantidad de Mociones", yaxis_title="Tema")
st.plotly_chart(fig4, use_container_width=True)

st.markdown('<p class="storytelling">Las mociones presentadas por el Senador Castro abordan temas cruciales para el desarrollo de Chile,  como la seguridad ciudadana, el desarrollo regional, la protección del medio ambiente,  la mejora de la educación y el impulso de la economía.</p>', unsafe_allow_html=True)

# Separador
st.markdown("---")

# Sección 3: Fiscalización y Transparencia
st.markdown('<p class="section-header">3. Fiscalización y Transparencia</p>', unsafe_allow_html=True)

# Gráfico 5: Peticiones de Oficio por Destinatario
df_peticiones = pd.DataFrame(data_peticiones)
fig5 = px.bar(
    df_peticiones,
    x="Destinatario",
    y="Cantidad",
    color="Legislatura",
    title="Peticiones de Oficio por Destinatario y Legislatura",
    labels={"Cantidad": "Cantidad de Peticiones"},
    color_discrete_sequence=[color_principal, color_secundario],  # Asignar colores
)
fig5.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig5, use_container_width=True)

st.markdown('<p class="storytelling">El Senador Castro ejerce un rol fiscalizador activo, buscando respuestas a las demandas de la ciudadanía y promoviendo la transparencia en la gestión de las instituciones públicas.</p>', unsafe_allow_html=True)

# Gráfico 6: Temas de las Peticiones de Oficio
stopwords = set(STOPWORDS)
wordcloud = WordCloud(
    width=800, height=400, background_color="white", stopwords=stopwords, min_font_size=10
).generate(palabras_clave_peticiones)

fig6, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
st.pyplot(fig6)

st.markdown('<p class="storytelling">A través de sus peticiones de oficio,  el Senador Castro ha abordado temas cruciales como la seguridad,  la transparencia,  el acceso al agua,  el desarrollo de la agricultura,  el bienestar de la Región del Maule,  el fomento de la economía,  la justicia social y la defensa de las Pymes. </p>', unsafe_allow_html=True)

# Separador
st.markdown("---")

# Sección 4: Compromiso con la Región del Maule
st.markdown('<p class="section-header">4. Compromiso con la Región del Maule</p>', unsafe_allow_html=True)

st.markdown('<p class="storytelling">El Senador Castro ha demostrado un firme compromiso con el desarrollo de la Región del Maule,  impulsando proyectos e iniciativas que buscan mejorar la calidad de vida de sus habitantes.</p>', unsafe_allow_html=True)

# Galería de Imágenes (Reemplazar con imágenes reales de proyectos en el Maule)
col1, col2, col3 = st.columns(3)
with col1:
    st.image("proyecto1.jpg", width=200, caption="Proyecto 1: [Descripción del Proyecto]")
with col2:
    st.image("proyecto2.jpg", width=200, caption="Proyecto 2: [Descripción del Proyecto]")
with col3:
    st.image("proyecto3.jpg", width=200, caption="Proyecto 3: [Descripción del Proyecto]")

st.markdown('<p class="storytelling">Su labor parlamentaria se ha enfocado en obtener recursos para la región,  impulsar la inversión en áreas clave como la agricultura y  la infraestructura,  y defender los intereses de sus habitantes en el debate nacional.</p>', unsafe_allow_html=True)

# Mapa Interactivo: Iniciativas para el Maule (requiere geodatos)
# st.map(data_proyectos_maule) 

# Separador
st.markdown("---")

# Sección 5: Contacto y Redes Sociales
st.markdown('<p class="section-header">5. Contacto y Redes Sociales</p>', unsafe_allow_html=True)

# Información de Contacto 
# (Reemplazar con información real)
st.write(
    """
    **Contacto:** 
    * Oficina Parlamentaria:  [Dirección de la Oficina]
    * Teléfono:  [Número de Teléfono]
    * Correo Electrónico:  [Dirección de Correo Electrónico]

    **Redes Sociales:**
    * Facebook:  [Enlace a Facebook]
    * Twitter:  [Enlace a Twitter]
    * Instagram:  [Enlace a Instagram]
    """
)

# Formulario de Contacto (Opcional)

st.write("**Envíanos un Mensaje:**")
st.text_area("Mensaje:")
if st.button("Enviar"):
    st.success("Mensaje enviado correctamente.")
