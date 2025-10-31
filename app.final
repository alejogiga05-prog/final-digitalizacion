import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Configuración inicial
st.set_page_config(page_title="Monitoreo y Predicción - Ecopack", layout="wide")

st.title("📊 Monitoreo y Predicción de Variables Industriales - Ecopack")
st.markdown("Esta aplicación muestra datos simulados de temperatura industrial con análisis y predicción básica.")

# === FUNCIÓN PARA GENERAR DATOS SIMULADOS ===
@st.cache_data
def generar_datos():
    ahora = datetime.now()
    fechas = [ahora - timedelta(minutes=10 * i) for i in range(50)][::-1]  # 50 datos cada 10 minutos
    temperatura = np.random.normal(loc=27, scale=3, size=50).round(2)  # promedio 27°C con variaciones
    df = pd.DataFrame({"Fecha": fechas, "Temperatura (°C)": temperatura})
    return df

# === OBTENER DATOS ===
df = generar_datos()

# === MOSTRAR DATOS ===
st.subheader("📋 Datos recientes")
st.dataframe(df.tail(10), use_container_width=True)

# === GRÁFICO DE TENDENCIA ===
st.subheader("📈 Tendencia de temperatura")
fig = px.line(df, x="Fecha", y="Temperatura (°C)", title="Evolución de la temperatura simulada", markers=True)
st.plotly_chart(fig, use_container_width=True)

# === ESTADÍSTICAS ===
st.subheader("📊 Estadísticas generales")
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura máxima (°C)", f"{df['Temperatura (°C)'].max():.2f}")
col2.metric("Temperatura mínima (°C)", f"{df['Temperatura (°C)'].min():.2f}")
col3.metric("Temperatura promedio (°C)", f"{df['Temperatura (°C)'].mean():.2f}")

# === PREDICCIÓN SIMPLE ===
st.subheader("🤖 Predicción de temperatura (modelo simple)")
# Modelo lineal muy básico
x = np.arange(len(df))
y = df["Temperatura (°C)"].values
coef = np.polyfit(x, y, 1)
pred_lineal = np.poly1d(coef)

# Predicción para los próximos 5 intervalos
x_futuro = np.arange(len(df), len(df) + 5)
y_pred = pred_lineal(x_futuro)

futuro_fechas = [df["Fecha"].iloc[-1] + timedelta(minutes=10 * (i + 1)) for i in range(5)]
pred_df = pd.DataFrame({"Fecha": futuro_fechas, "Temperatura prevista (°C)": y_pred.round(2)})

st.dataframe(pred_df, use_container_width=True)

fig_pred = px.line(pred_df, x="Fecha", y="Temperatura prevista (°C)", markers=True,
                   title="Predicción de temperatura para los próximos 50 minutos")
st.plotly_chart(fig_pred, use_container_width=True)

st.caption("Aplicación de simulación y predicción industrial - Ecopack 🌱")
