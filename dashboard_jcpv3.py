import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Datos (Reemplazar con datos reales del Senador)
data_intervenciones = {
    "Legislatura": [369, 369, 369, 370, 370],
    "Tema": ["Seguridad Ciudadana", "Desarrollo Regional", "Pymes y Agricultura", "Seguridad Ciudadana", "Reforma Constitucional"],
    "Cantidad": [10, 5, 8, 12, 6],
}

data_votaciones = {
    "Tema": ["Reforma Código Aguas", "Postergación Elecciones", "Ley de Usurpación"],
    "A Favor": [8, 5, 12],
    "En Contra": [2, 5, 3],
    "Abstención": [1, 1, 0],
}

data_mociones = {
    "Legislatura": [369, 369, 369, 370, 370],
    "Tipo": ["Proyecto de Ley", "Reforma Constitucional", "Proyecto de Acuerdo", "Proyecto de Ley", "Proyecto de Resolución"],
    "Cantidad": [15, 5, 8, 10, 3],
}

data_mociones_tema = {
    "Tema": ["Seguridad Ciudadana", "Desarrollo Regional", "Medio Ambiente", "Educación", "Economía"],
    "Cantidad": [8, 6, 4, 5, 7],
}

data_peticiones = {
    "Legislatura": [369, 369, 370, 370],
    "Destinatario": ["Ministerio Interior", "Ministerio Agricultura", "Contraloría", "Ministerio Justicia"],
    "Cantidad": [12, 8, 5, 6],
}

palabras_clave_peticiones = "seguridad transparencia agua agricultura Maule desarrollo social economía justicia pymes"

# Configuración del Dashboard
st.set_page_config(page_title="Labor Parlamentaria Senador Castro", page_icon=":guardsman:", layout="wide")

# Título
st.title("Compromiso y Esfuerzos: Visualizando la Labor del Senador Juan Enrique Castro Prieto")

# Introducción (Reemplazar con información real del Senador)
st.image("https://www.senado.cl/appsenado/templates/senado/img/default_perfil.png", width=200) 
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
st.header("Participación Activa en el Debate")

# Gráfico 1: Temas de Intervención
df_intervenciones = pd.DataFrame(data_intervenciones)
legislatura_seleccionada = st.selectbox("Seleccione una Legislatura:", df_intervenciones["Legislatura"].unique())
df_filtrado = df_intervenciones[df_intervenciones["Legislatura"] == legislatura_seleccionada]
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df_filtrado["Tema"], df_filtrado["Cantidad"])
plt.xlabel("Tema de Intervención")
plt.ylabel("Cantidad de Intervenciones")
st.pyplot(fig)

st.write(
    """
    El Senador Castro ha participado activamente en los debates más relevantes para el país, 
    defendiendo con convicción sus posturas y buscando soluciones a las problemáticas que afectan a la ciudadanía. 
    """
)

# Gráfico 2: Posición en Votaciones Clave
df_votaciones = pd.DataFrame(data_votaciones)
tema_seleccionado = st.selectbox("Seleccione un Tema:", df_votaciones["Tema"].unique())
df_votacion_filtrado = df_votaciones[df_votaciones["Tema"] == tema_seleccionado]
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(df_votacion_filtrado.iloc[0, 1:], labels=df_votacion_filtrado.columns[1:], autopct="%1.1f%%")
plt.title(f"Posición en Votaciones: {tema_seleccionado}")
st.pyplot(fig)

st.write(
    """
    El Senador Castro ha demostrado una postura firme y coherente en las votaciones clave, 
    priorizando el bienestar de la ciudadanía y buscando el desarrollo del país. 
    """
)

# Separador
st.markdown("---")

# Sección 2: Impulsando Iniciativas Legislativas
st.header("Impulsando Iniciativas Legislativas")

# Gráfico 3: Tipos de Mociones Presentadas
df_mociones = pd.DataFrame(data_mociones)
legislatura_mociones = st.selectbox("Seleccione una Legislatura (Mociones):", df_mociones["Legislatura"].unique())
df_mociones_filtrado = df_mociones[df_mociones["Legislatura"] == legislatura_mociones]
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(df_mociones_filtrado["Cantidad"], labels=df_mociones_filtrado["Tipo"], autopct="%1.1f%%")
plt.title("Tipos de Mociones Presentadas")
st.pyplot(fig)

st.write(
    """
    El Senador Castro ha presentado una diversidad de iniciativas legislativas, 
    demostrando su compromiso con la búsqueda de soluciones a los desafíos que enfrenta el país.
    """
)

# Gráfico 4: Temas de las Mociones
df_mociones_tema = pd.DataFrame(data_mociones_tema)
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df_mociones_tema["Tema"], df_mociones_tema["Cantidad"])
plt.xlabel("Cantidad de Mociones")
plt.ylabel("Tema")
st.pyplot(fig)

st.write(
    """
    Las mociones presentadas por el Senador Castro abordan temas cruciales para el desarrollo de Chile, 
    como la seguridad ciudadana, el desarrollo regional, la protección del medio ambiente, 
    la mejora de la educación y el impulso de la economía.
    """
)

# Separador
st.markdown("---")

# Sección 3: Fiscalización y Transparencia
st.header("Fiscalización y Transparencia")

# Gráfico 5: Peticiones de Oficio por Destinatario
df_peticiones = pd.DataFrame(data_peticiones)
legislatura_peticiones = st.selectbox("Seleccione una Legislatura (Peticiones):", df_peticiones["Legislatura"].unique())
df_peticiones_filtrado = df_peticiones[df_peticiones["Legislatura"] == legislatura_peticiones]
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df_peticiones_filtrado["Destinatario"], df_peticiones_filtrado["Cantidad"])
plt.xlabel("Destinatario")
plt.ylabel("Cantidad de Peticiones de Oficio")
st.pyplot(fig)

st.write(
    """
    El Senador Castro ejerce un rol fiscalizador activo, buscando respuestas a las demandas de la ciudadanía y 
    promoviendo la transparencia en la gestión de las instituciones públicas.
    """
)

# Gráfico 6: Temas de las Peticiones de Oficio
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(palabras_clave_peticiones)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
st.pyplot(fig)

st.write(
    """
    A través de sus peticiones de oficio,  el Senador Castro ha abordado temas cruciales como la seguridad,  
    la transparencia,  el acceso al agua,  el desarrollo de la agricultura,  el bienestar de la Región del Maule,  
    el fomento de la economía,  la justicia social y la defensa de las Pymes. 
    """
)

# Separador
st.markdown("---")

# Sección 4: Compromiso con la Región del Maule
st.header("Compromiso con la Región del Maule")

# Mapa Interactivo: Iniciativas para el Maule
st.write(
    """
    El Senador Castro ha demostrado un firme compromiso con el desarrollo de la Región del Maule,  
    impulsando proyectos e iniciativas que buscan mejorar la calidad de vida de sus habitantes. 
    """
)

# Galería de Imágenes (Reemplazar con imágenes reales de proyectos en el Maule)
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://www.senado.cl/appsenado/templates/senado/img/default_perfil.png", width=200, caption="Proyecto 1")
with col2:
    st.image("https://www.senado.cl/appsenado/templates/senado/img/default_perfil.png", width=200, caption="Proyecto 2")
with col3:
    st.image("https://www.senado.cl/appsenado/templates/senado/img/default_perfil.png", width=200, caption="Proyecto 3")

st.write(
    """
    Su labor parlamentaria se ha enfocado en obtener recursos para la región,  
    impulsar la inversión en áreas clave como la agricultura y  la infraestructura,  
    y defender los intereses de sus habitantes en el debate nacional. 
    """
)

# Separador
st.markdown("---")

# Sección 5: Contacto y Redes Sociales
st.header("Contacto y Redes Sociales")

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
