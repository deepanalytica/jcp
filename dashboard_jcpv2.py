import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Datos de la labor parlamentaria del Senador (reemplazar con datos reales)
data = {
    "Tema": [
        "Marco funcional efectivo para nuevos gobiernos regionales",
        "Creación de sistema nacional de emergencia y protección civil",
        "Acuerdo entre padre y madre para determinar orden de apellidos",
        "Normas de eficiencia hídrica y adaptación al cambio climático",
        "Nuevo Bono Clase Media y Préstamo Solidario",
        "Postergación de próximas elecciones municipales",
        "Sistema de salud para fuerzas de orden y seguridad pública",
        "Creación de una comisión de alto nivel para crisis alimentaria",
        # ... (agregar más temas)
    ],
    "Fecha": [
        "2021-03-23",
        "2021-03-30",
        "2021-03-31",
        "2021-04-01",
        "2021-04-04",
        "2021-04-05",
        "2022-04-05",
        "2022-04-06",
        # ... (agregar más fechas)
    ],
    "Tipo": [
        "Intervención",
        "Intervención",
        "Intervención",
        "Mociones",
        "Intervención",
        "Intervención",
        "Proyecto de Acuerdo",
        "Proyecto de Acuerdo",
        # ... (agregar más tipos)
    ],
    "Región": [
        "Región del Maule",
        "Nacional",
        "Nacional",
        "Nacional",
        "Región del Maule",
        "Nacional",
        "Nacional",
        "Nacional",
        # ... (agregar más regiones)
    ],
    "Resumen": [
        "Propuesta para fortalecer la descentralización y otorgar mayores facultades a los gobiernos regionales.",
        "Discusión sobre la creación de un sistema nacional de emergencia y protección civil.",
        "Intervención sobre el proyecto de ley que permite cambiar el orden de los apellidos.",
        "Presentación de una moción para establecer normas de eficiencia hídrica.",
        "Votación en contra del nuevo Bono Clase Media por considerarlo un aumento desmedido del gasto público.",
        "Apoyo a la postergación de las elecciones municipales debido a la pandemia.",
        "Proyecto de acuerdo para establecer un sistema de salud para las fuerzas del orden.",
        "Solicitud para la creación de una comisión que aborde la crisis alimentaria en el país.",
        # ... (agregar más resúmenes)
    ],
    "Enlace": [
        # ... (agregar enlaces a los documentos/videos de cada intervención)
    ]
}

df = pd.DataFrame(data)
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Configurar página de Streamlit
st.set_page_config(page_title="Labor Parlamentaria", layout="wide")

# Título del Dashboard
st.title("Labor Parlamentaria - Senador Juan Enrique Castro Prieto")

# Introducción con Storytelling
st.markdown("""
<div style="text-align: justify;">
El Senador Juan Castro ha dedicado su labor parlamentaria a defender los intereses de la Región del Maule y del país, enfocándose en temas cruciales como la descentralización, la seguridad pública, la protección de la infancia y la eficiencia en el uso de los recursos. 
Este dashboard interactivo permite a la comunidad explorar su trabajo, conocer sus posturas y comprender su compromiso con el bienestar de Chile. 
</div>
""", unsafe_allow_html=True)

# Filtros para el Dashboard
st.sidebar.title("Filtros")
selected_type = st.sidebar.multiselect("Tipo de Intervención:", df["Tipo"].unique(), default=df["Tipo"].unique())
start_date = st.sidebar.date_input("Fecha de Inicio:", df["Fecha"].min())
end_date = st.sidebar.date_input("Fecha de Término:", df["Fecha"].max())

# Aplicar Filtros a los Datos
filtered_df = df[
    (df["Tipo"].isin(selected_type)) &
    (df["Fecha"] >= start_date) &
    (df["Fecha"] <= end_date)
]

# Gráfico Interactivo 1: Cantidad de Intervenciones por Tipo
fig1 = px.bar(filtered_df, x="Tipo", title="Cantidad de Intervenciones por Tipo")
st.plotly_chart(fig1)

# Gráfico Interactivo 2: Intervenciones por Región
fig2 = px.pie(filtered_df, values=filtered_df["Región"].value_counts().values, 
             names=filtered_df["Región"].value_counts().index, 
             title="Distribución de Intervenciones por Región")
st.plotly_chart(fig2)

# Gráfico Interactivo 3: Evolución de Intervenciones a lo largo del tiempo
fig3 = px.line(filtered_df.groupby(pd.Grouper(key='Fecha', freq='M')).size().reset_index(name='count'),
              x="Fecha", y="count", title="Evolución de Intervenciones en el Tiempo")
st.plotly_chart(fig3)

# Mostrar las Intervenciones
st.header("Intervenciones")
for index, row in filtered_df.iterrows():
    with st.expander(f"{row['Tema']} - {row['Fecha'].strftime('%d de %B de %Y')} - {row['Región']}"):
        st.write(row["Resumen"])
        if row["Enlace"]:
            st.markdown(f"[Enlace al documento/video]({row['Enlace']})")
