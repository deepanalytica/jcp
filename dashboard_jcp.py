import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter

# Data (ejemplo con enlaces reales a documentos del Senado)
data = {
    "Fecha": [
        "2023-03-15",
        "2023-03-21",
        "2023-03-30",
        "2023-03-30",
        "2023-04-04",
        "2023-04-12",
        "2023-04-18",
        "2023-04-18",
        "2023-05-10",
        "2023-05-16",
        "2023-05-17",
        "2023-06-19",
        "2023-06-20",
        "2023-06-20",
        "2023-07-03",
        "2023-07-05",
        "2023-07-05",
        "2023-07-12",
        "2023-07-12",
        "2023-07-18",
        "2023-08-08",
        "2023-08-08",
    ],
    "Labor Parlamentaria": [
        "Intervención",
        "Intervención",
        "Intervención",
        "Intervención",
        "Intervención",
        "Intervención",
        "Intervención",
        "Intervención",
        "Intervención",
        "Intervención",
        "Intervención",
        "Intervención en Comisión",
        "Intervención en Comisión",
        "Intervención en Comisión",
        "Intervención en Comisión",
        "Intervención en Comisión",
        "Intervención en Comisión",
        "Mociones",
        "Proyecto de Acuerdo",
        "Proyecto de Acuerdo",
        "Intervención",
        "Intervención",
    ],
    "Tema": [
        "Obras Viales",
        "Trabajo",
        "Seguridad",
        "Seguridad",
        "Seguridad",
        "Bomberos",
        "Agricultura",
        "Agricultura",
        "Agricultura",
        "Agricultura",
        "Economía",
        "Seguridad",
        "Seguridad",
        "Seguridad",
        "Corrupción",
        "Litio",
        "Corrupción",
        "Bomberos",
        "Desarrollo Regional",
        "Libertad de Expresión",
        "Feriados",
        "Salud",
    ],
    "Descripción": [
        "OBLIGACIÓN A CONCESIONARIAS DE OBRAS VIALES...",
        "REDUCCIÓN DE JORNADA LABORAL",
        "MODIFICACIÓN DE CÓDIGO PENAL EN MATERIA...",
        "REFORZAMIENTO DE COMPETENCIAS DE GENDARMERÍA...",
        "FORTALECIMIENTO Y PROTECCIÓN DE EJERCICIO...",
        "ENTREGA DE ACREENCIAS BANCARIAS VENCIDAS...",
        "ACUERDOS DE COMITÉS",
        "AMPLIACIÓN DE PLAZO DE INSCRIPCIÓN...",
        "NORMAS PARA FOMENTO DE INVERSIÓN PRIVADA...",
        "MODIFICACIÓN DE SANCIONES ADMINISTRATIVAS...",
        "REAJUSTE DE INGRESO MÍNIMO MENSUAL...",
        "CREACIÓN DE MINISTERIO DE SEGURIDAD PÚBLICA",
        "PRÓRROGA DE VIGENCIA DE ESTADO DE EXCEPCIÓN...",
        "CREACIÓN DE MINISTERIO DE SEGURIDAD PÚBLICA",
        "TRASPASOS DE RECURSOS FISCALES...",
        "ESTRATEGIA NACIONAL DEL LITIO...",
        "TRASPASOS DE RECURSOS FISCALES...",
        "Proyecto de ley, iniciado en moción...",
        "De los Honorables Senadores señor Sandoval...",
        "De los Honorables Senadores señor Coloma...",
        "DECLARACIÓN DE 10 DE AGOSTO DE 2023...",
        "CUIDADO INTEGRAL DE SALUD DE PERSONAS...",
    ],
    "Enlace": [
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8078",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8089",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8113",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8114",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8129",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8151",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8158",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8159",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8208",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8221",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8230",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8280",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8288",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8289",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8315",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8321",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8324",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8339",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8341",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8347",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8396",
        "https://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid=8398",
    ],
}

df = pd.DataFrame(data)
df["Fecha"] = pd.to_datetime(df["Fecha"])  # Convertir la columna "Fecha" a tipo datetime

# Streamlit app
st.title("Labor Parlamentaria Juan Enrique Castro Prieto")
st.subheader("Legislatura número 371 (13 de marzo de 2023 al 11 de marzo de 2024)")

st.markdown("## Un Vistazo General a la Gestión")
st.markdown("Este dashboard interactivo te permite explorar la actividad parlamentaria de Juan Enrique Castro Prieto durante la legislatura 371.  \
            A continuación, se muestra un resumen de las labores realizadas en este período:")

# Filtro por fecha
start_date, end_date = st.date_input(
    "Seleccione un rango de fechas para un análisis más detallado:",
    [df["Fecha"].min(), df["Fecha"].max()],
)

# Convertir start_date y end_date a datetime64[ns]
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

filtered_df = df[(df["Fecha"] >= start_date) & (df["Fecha"] <= end_date)]

# --- Gráfico 1: Distribución de Labores Parlamentarias ---
st.markdown("### Tipos de Labores Parlamentarias")
fig_pie = px.pie(
    df, names="Labor Parlamentaria", title="Distribución de Labores", hole=0.4
)
fig_pie.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig_pie)

# --- Gráfico 2: Evolución Temporal de las Labores ---
st.markdown("### Actividad a lo largo del Tiempo")
filtered_df["Mes"] = filtered_df["Fecha"].dt.strftime("%Y-%m") # Agregar columna "Mes"
labor_counts = filtered_df.groupby(["Mes", "Labor Parlamentaria"]).size().reset_index(name="Cantidad")
fig_line = px.line(
    labor_counts, 
    x="Mes", 
    y="Cantidad", 
    color="Labor Parlamentaria", 
    markers=True,
    title="Evolución de las Labores Parlamentarias por Mes"
)
st.plotly_chart(fig_line)

# --- Gráfico 3: Temas Más Abordados ---
st.markdown("### Temas de Mayor Interés")
tema_counts = Counter(filtered_df["Tema"])
top_temas = tema_counts.most_common(5)  # Top 5 temas
temas, counts = zip(*top_temas)
fig_bar = px.bar(
    x=temas, y=counts, labels={"x": "Tema", "y": "Cantidad"}, title="Temas Más Abordados"
)
st.plotly_chart(fig_bar)

# --- Tabla con Enlaces ---
st.markdown("### Detalle de la Actividad Parlamentaria")
for index, row in filtered_df.iterrows():
    st.write(f"**{row['Labor Parlamentaria']} - {row['Fecha'].strftime('%Y-%m-%d')}**")
    st.write(f"**Tema:** {row['Tema']}")
    st.write(row["Descripción"])
    st.write(f"[Ver documento]({row['Enlace']})")
    st.write("---")

# --- Notas Explicativas ---
st.markdown("## Notas Explicativas")
st.markdown(
    """
    Esta información ha sido construida a partir de los Diarios de Sesiones de la Cámara de Diputados y del  Senado. 
    Se incluyen las  participaciones  del  legislador,  documentos,  fundamentos,  debates  y votaciones.

    También se presenta su labor fiscalizadora, de representación, de diplomacia parlamentaria y atribuciones propias.

    La información se actualiza continuamente. 
    """
)
