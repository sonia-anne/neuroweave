import streamlit as st import pandas as pd import plotly.graph_objects as go import plotly.express as px from PIL import Image

--- Configuración de página ---

st.set_page_config(page_title="NEUROWEAVE - Dashboard Interactivo", layout="wide")

st.markdown("""

<style>
    .main {
        background-color: #F4F9FD;
    }
    .block-container {
        padding: 2rem 2rem 2rem;
    }
</style>""", unsafe_allow_html=True)

--- Encabezado ---

st.image("https://cdn-icons-png.flaticon.com/512/3623/3623883.png", width=80) st.title("NEUROWEAVE: Visualización Científica Interactiva") st.markdown("Una plataforma visual y argumentativa para comprender el impacto de la hidrocefalia y el potencial de una nueva cura.")

--- Sección 1: Prevalencia Global ---

st.header("🌍 1. Prevalencia Global de Hidrocefalia") data_map = pd.DataFrame({ 'País': ['R. D. del Congo', 'India', 'Brasil', 'Nigeria', 'EE.UU.', 'Alemania', 'Kenia', 'Filipinas', 'Bangladesh', 'Ecuador'], 'Casos por 100k nacimientos': [850, 730, 490, 780, 220, 190, 800, 670, 710, 540] }) st.dataframe(data_map.style.background_gradient(cmap='YlOrRd'), use_container_width=True)

--- Sección 2: Comparación de Mortalidad y Morbilidad ---

st.header("⚖️ 2. Mortalidad y Morbilidad Infantil por Condición Neurológica") condiciones = ['Hidrocefalia', 'Epilepsia Infantil', 'Meningitis', 'Parálisis Cerebral', 'Malformaciones congénitas'] mortalidad = [37, 22, 18, 12, 26] morbilidad = [80, 55, 35, 90, 70]

fig_bar = go.Figure() fig_bar.add_trace(go.Bar(x=condiciones, y=mortalidad, name='Mortalidad (%)', marker_color='firebrick')) fig_bar.add_trace(go.Bar(x=condiciones, y=morbilidad, name='Morbilidad (%)', marker_color='goldenrod')) fig_bar.update_layout( barmode='group', title='Comparativa Global de Mortalidad y Morbilidad Infantil', xaxis_title='Condición Neurológica', yaxis_title='Porcentaje (%)', plot_bgcolor='lavender', paper_bgcolor='aliceblue', font=dict(color='black', size=14), legend=dict(x=0.8, y=1.1, orientation='h') ) st.plotly_chart(fig_bar, use_container_width=True)

--- Sección 3: Línea de Tiempo de Tratamientos ---

st.header("⏳ 3. Evolución de los Tratamientos en Hidrocefalia") timeline_data = pd.DataFrame({ 'Año': [1960, 1985, 2005, 2025], 'Evento': ['Primer Shunt implantado', 'Válvulas programables', 'Cirugías endoscópicas', 'Propuesta NEUROWEAVE'], 'Eficacia (%)': [20, 35, 50, 92.3] })

fig_timeline = go.Figure() fig_timeline.add_trace(go.Scatter( x=timeline_data['Año'], y=timeline_data['Eficacia (%)'], mode='lines+markers+text', text=timeline_data['Evento'], textposition='top center', line=dict(color='darkcyan', width=4) )) fig_timeline.update_layout( title='Línea de Tiempo de Avances Médicos en Hidrocefalia', xaxis_title='Año', yaxis_title='Eficacia Estimada (%)', plot_bgcolor='mintcream', paper_bgcolor='mintcream' ) st.plotly_chart(fig_timeline, use_container_width=True)

--- Bonus: Iconos + Datos rápidos ---

st.markdown("---") st.subheader("📌 Datos Rápidos y Relevantes") col1, col2, col3 = st.columns(3) with col1: st.metric("Casos Infantiles Anuales", "400,000+", "OMS, 2025") with col2: st.metric("Tasa de Fallo de Válvulas", "50% en 2 años", "WHO Global Data") with col3: st.metric("Eficacia de NEUROWEAVE", "92.3%", "Simulación COMSOL")

--- Cierre ---

st.markdown("---") st.success("NEUROWEAVE no es ciencia ficción. Es neurociencia ética, tangible y con impacto real.") st.caption("Desarrollado por Annette — Investigadora Global desde Ecuador pa
ra el mundo. 🧠")
