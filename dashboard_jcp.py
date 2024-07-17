import streamlit as st
import pandas as pd
import plotly.express as px

# Data (ejemplo)
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
        "Intervención en Comision",
        "Intervención en Comision",
        "Intervención en Comision",
        "Intervención en Comision",
        "Intervención en Comision",
        "Intervención en Comision",
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
        "enlace_documento_1",
        "enlace_documento_2",
        "enlace_documento_3",
        "enlace_documento_4",
        "enlace_documento_5",
        "enlace_documento_6",
        "enlace_documento_7",
        "enlace_documento_8",
        "enlace_documento_9",
        "enlace_documento_10",
        "enlace_documento_11",
        "enlace_documento_12",
        "enlace_documento_13",
        "enlace_documento_14",
        "enlace_documento_15",
        "enlace_documento_16",
        "enlace_documento_17",
        "enlace_documento_18",
        "enlace_documento_19",
        "enlace_documento_20",
        "enlace_documento_21",
        "enlace_documento_22",
    ],
}
df = pd.DataFrame(data)

# Streamlit app
st.title("Labor Parlamentaria Juan Enrique Castro Prieto")
st.subheader("Legislatura número 371 (13 de marzo de 2023 al 11 de marzo de 2024)")

# Filtro por fecha
start_date, end_date = st.date_input(
    "Seleccione un rango de fechas:",
    [df["Fecha"].min(), df["Fecha"].max()],
)
filtered_df = df[(df["Fecha"] >= start_date) & (df["Fecha"] <= end_date)]

# Gráfico de torta
fig_pie = px.pie(
    filtered_df, names="Labor Parlamentaria", title="Distribución porcentual de las labores"
)
st.plotly_chart(fig_pie)

# Tabla con enlaces
st.dataframe(
    filtered_df.style.format(
        {"Enlace": lambda x: f'<a href="{x}" target="_blank">Ver documento</a>'}
    ),
    unsafe_allow_html=True,
)

# Notas explicativas
st.markdown(
    """
    **Nota Explicativa:**
    
    Esta  Labor  Parlamentaria  ha  sido  construida  a  partir  de  la información contenida en los Diarios de Sesiones de la Cámara de Diputados y del  Senado, referidas  a  las  participaciones  del  legislador,  documentos,  fundamentos,  debates  y votaciones que determinan las decisiones legislativas en cada etapa del proceso de formación de la ley. 
    
    Junto a ello se entrega acceso a su labor fiscalizadora, de representación, de diplomacia parlamentaria y atribuciones propias según corresponda.
    
    Cabe  considerar  que  la  información  contenida  en  este  dashboard  se  encuentra  en  continuo poblamiento, de manera tal que día a día se va actualizando la información que lo conforma.
    """
)
