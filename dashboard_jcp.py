import streamlit as st
import pandas as pd
import plotly.express as px

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
df["Fecha"] = pd.to_datetime(df["Fecha"]) # Convertir la columna "Fecha" a tipo datetime

# Streamlit app
st.title("Labor Parlamentaria Juan Enrique Castro Prieto")
st.subheader("Legislatura número 371 (13 de marzo de 2023 al 11 de marzo de 2024)")

# Filtro por fecha
start_date, end_date = st.date_input(
    "Seleccione un rango de fechas:",
    [df["Fecha"].min(), df["Fecha"].max()],
)

# Convertir start_date y end_date a datetime64[ns]
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

filtered_df = df[(df["Fecha"] >= start_date) & (df["Fecha"] <= end_date)]

# Gráfico de torta
fig_pie = px.pie(
    filtered_df, names="Labor Parlamentaria", title="Distribución porcentual de las labores"
)
st.plotly_chart(fig_pie)

# Tabla con enlaces
for index, row in filtered_df.iterrows():
    st.write(f"**{row['Labor Parlamentaria']} - {row['Fecha'].strftime('%Y-%m-%d')}**")
    st.write(row["Descripción"])
    st.write(f"[Ver documento]({row['Enlace']})")
    st.write("---")

# Notas explicativas
st.markdown(
    """
    **Nota Explicativa:**

    Esta  Labor  Parlamentaria  ha  sido  construida  a  partir  de  la información contenida en los Diarios de Sesiones de la Cámara de Diputados y del  Senado, referidas  a  las  participaciones  del  legislador,  documentos,  fundamentos,  debates  y votaciones que determinan las decisiones legislativas en cada etapa del proceso de formación de la ley.

    Junto a ello se entrega acceso a su labor fiscalizadora, de representación, de diplomacia parlamentaria y atribuciones propias según corresponda.

    Cabe  considerar  que  la  información  contenida  en  este  dashboard  se  encuentra  en  continuo poblamiento, de manera tal que día a día se va actualizando la información que lo conforma.
    """
)
