import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Labor Parlamentaria", 
                   layout="wide", 
                   initial_sidebar_state="expanded")

# --- ESTILO CSS PERSONALIZADO PARA MEJORAR UI/UX ---
st.markdown("""
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
.Widget>label {
    color: white;
    font-size: 18px;
}
[data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
    width: 400px;
}
[data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
    width: 400px;
    margin-left: -400px;
}
.st-b7 {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# --- CARGA DE DATOS ---
# Debes reemplazar esto con la información real extraída de los PDFs
df = pd.DataFrame({
    "Legislatura": [367, 367, 368, 369, 369, 370, 370, 370, 370],
    "Fecha": pd.to_datetime(["2019-03-23", "2019-06-05", "2020-05-20", "2021-04-04", 
                            "2021-06-15", "2022-03-22", "2022-04-05", "2022-05-18", "2022-08-31"]),
    "Tema": [
        "Designación de Secretario General",
        "Cuenta pública de TVN",
        "Procedencia de prisión preventiva para mujeres embarazadas", 
        "Nuevo Bono Clase Media", 
        "Modificación de diversos cuerpos normativos", 
        "Prohibición de informar deudas por atención de salud",
        "Fortalecimiento del Servicio Agrícola y Ganadero",
        "Día Nacional del Futbolista Amateur",
        "Regulación de la actividad apícola"
    ],
    "Tipo": [
        "Intervención",
        "Intervención", 
        "Intervención", 
        "Intervención", 
        "Intervención", 
        "Intervención", 
        "Informante", 
        "Intervención",
        "Informante"
    ],
    "Área": [
        "Administración del Estado", 
        "Comunicaciones", 
        "Justicia",
        "Economía", 
        "Vivienda", 
        "Salud", 
        "Agricultura",
        "Deporte", 
        "Agricultura"
    ],
    "Región": [
        "Nacional", 
        "Nacional", 
        "Nacional",
        "Región del Maule", 
        "Nacional", 
        "Nacional",
        "Nacional", 
        "Región del Maule", 
        "Nacional"
    ],
    "Resumen": [
        "Comentarios sobre la necesidad de orden y control en el Senado, y la importancia del rol del nuevo Secretario General.",
        "Críticas al desempeño financiero de TVN y la necesidad de un directorio comprometido con la eficiencia.",
        "Oposición al proyecto que busca la suspensión de la prisión preventiva para mujeres embarazadas por considerar que se beneficia a quienes cometen delitos.",
        "Rechazo al nuevo Bono Clase Media por considerarlo un aumento desmedido del gasto público.",
        "Apoyo al proyecto de ley de Integración Social y Urbana para agilizar proyectos habitacionales.",
        "Apoyo a la prohibición de informar deudas contraidas para financiar atenciones de salud, destacando la necesidad de una reforma a la salud.",
        "Informe del proyecto de ley que fortalece al Servicio Agrícola y Ganadero, destacando el trabajo de las comisiones y el acuerdo con el ejecutivo.",
        "Apoyo al establecimiento del Día Nacional del Futbolista Amateur y la necesidad de financiar clubes amateurs.",
        "Informe del proyecto de ley que regula la actividad apícola, destacando el trabajo realizado con diversos actores."
    ],
    "Enlace": [
        "enlace1", "enlace2", "enlace3", "enlace4", "enlace5", "enlace6", "enlace7", "enlace8", "enlace9"
        # ... (agregar enlaces a los documentos/videos)
    ],
    "Texto Completo": [
        # ... (agregar el texto completo de las intervenciones)
    ]
})

# --- PALABRAS CLAVE PARA NUBE DE PALABRAS ---
palabras_clave = " ".join(df["Tema"])

# --- SIDEBAR PARA FILTROS ---
st.sidebar.title("Filtros")
selected_year = st.sidebar.multiselect(
    "Año:", df["Fecha"].dt.year.unique(), default=df["Fecha"].dt.year.unique()
)
selected_area = st.sidebar.multiselect(
    "Área Temática:", df["Área"].unique(), default=df["Área"].unique()
)
selected_type = st.sidebar.multiselect(
    "Tipo de Intervención:", df["Tipo"].unique(), default=df["Tipo"].unique()
)
selected_region = st.sidebar.multiselect(
    "Región:", df["Región"].unique(), default=df["Región"].unique()
)

# --- APLICAR FILTROS A LOS DATOS ---
filtered_df = df[
    (df["Fecha"].dt.year.isin(selected_year)) &
    (df["Área"].isin(selected_area)) &
    (df["Tipo"].isin(selected_type)) &
    (df["Región"].isin(selected_region)) 
]

# --- NUBE DE PALABRAS ---
st.header("Nube de Conceptos Clave")
stopwords = set(STOPWORDS)
wordcloud = WordCloud(width=800, height=400, 
                      background_color="white", 
                      stopwords=stopwords, 
                      min_font_size=10).generate(palabras_clave)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
st.pyplot(plt)

# --- GRÁFICOS INTERACTIVOS ---
st.header("Visualizaciones Interactivas")

col1, col2 = st.columns(2)
with col1:
    # Gráfico de Intervenciones por Año
    fig_año = px.bar(filtered_df.groupby(filtered_df["Fecha"].dt.year).size().reset_index(name='count'), 
                    x="Fecha", y="count", title="Intervenciones por Año")
    st.plotly_chart(fig_año)

with col2:
    # Gráfico de Intervenciones por Área
    fig_area = px.pie(filtered_df, values=filtered_df["Área"].value_counts().values, 
                    names=filtered_df["Área"].value_counts().index, 
                    title="Distribución por Área Temática")
    st.plotly_chart(fig_area)

# --- MOSTRAR LAS INTERVENCIONES FILTRADAS ---
st.header("Labor Parlamentaria")
for index, row in filtered_df.iterrows():
    with st.expander(f"{row['Tema']} - {row['Fecha'].strftime('%d de %B de %Y')} - {row['Región']}"):
        st.write(row["Resumen"])
        # Puedes mostrar el texto completo o solo el resumen 
        # st.write(row["Texto Completo"])
        if row["Enlace"]:
            st.markdown(f"[Enlace al Documento]({row['Enlace']})")
