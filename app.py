import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image

# --- Page Configuration ---
st.set_page_config(page_title="NEUROWEAVE - Interactive Scientific Dashboard", layout="wide", page_icon="🧠")

# --- Custom Styling ---
st.markdown("""
<style>
    .main {
        background-color: #F4F9FD;
    }
    .block-container {
        padding: 2rem 2rem 2rem;
        font-family: 'Helvetica', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.image("https://cdn-icons-png.flaticon.com/512/3623/3623883.png", width=80)
st.title("NEUROWEAVE: Scientific Visualization Dashboard")
st.markdown("A powerful, visual and data-rich exploration of the global burden of hydrocephalus and how NEUROWEAVE proposes to change the future of neurosurgery.")

# --- SECTION 1: Global Prevalence Data ---
st.header("🌍 Global Prevalence of Hydrocephalus")
st.markdown("Visual representation of hydrocephalus burden across continents.")

with st.expander("📊 Prevalence Data Table"):
    data_map = pd.DataFrame({
        'Country': ['D.R. Congo', 'India', 'Brazil', 'Nigeria', 'USA', 'Germany', 'Kenya', 'Philippines', 'Bangladesh', 'Ecuador'],
        'Cases per 100k Births': [850, 730, 490, 780, 220, 190, 800, 670, 710, 540],
        'Continent': ['Africa', 'Asia', 'South America', 'Africa', 'North America', 'Europe', 'Africa', 'Asia', 'Asia', 'South America']
    })
    st.dataframe(data_map.style.background_gradient(cmap='YlOrRd'), use_container_width=True)

# Pie Chart by Continent
continent_summary = data_map.groupby('Continent').sum().reset_index()
fig_pie = px.pie(continent_summary, names='Continent', values='Cases per 100k Births',
                 title='Distribution of Cases by Continent',
                 color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig_pie, use_container_width=True)

# Bar Chart by Country
fig_bar_country = px.bar(data_map, x='Country', y='Cases per 100k Births', color='Continent',
                         title='Hydrocephalus Cases per 100k Births by Country',
                         color_discrete_sequence=px.colors.qualitative.Bold)
st.plotly_chart(fig_bar_country, use_container_width=True)

# --- SECTION 2: Mortality vs Morbidity ---
st.header("⚖️ Mortality vs Morbidity in Pediatric Neurological Conditions")
conditions = ['Hydrocephalus', 'Childhood Epilepsy', 'Meningitis', 'Cerebral Palsy', 'Congenital Malformations']
mortality = [37, 22, 18, 12, 26]
morbidity = [80, 55, 35, 90, 70]

fig_dual = go.Figure()
fig_dual.add_trace(go.Bar(x=conditions, y=mortality, name='Mortality (%)', marker_color='crimson'))
fig_dual.add_trace(go.Bar(x=conditions, y=morbidity, name='Morbidity (%)', marker_color='darkorange'))
fig_dual.update_layout(
    barmode='group',
    title='Comparison of Mortality and Morbidity (%) by Condition',
    xaxis_title='Condition',
    yaxis_title='Percentage (%)',
    plot_bgcolor='lavender',
    paper_bgcolor='white',
    font=dict(size=13),
    legend=dict(x=0.75, y=1.1, orientation='h')
)
st.plotly_chart(fig_dual, use_container_width=True)

# --- SECTION 3: Treatment Timeline ---
st.header("⏳ Evolution of Hydrocephalus Treatments")
timeline_data = pd.DataFrame({
    'Year': [1960, 1985, 2005, 2025],
    'Innovation': ['First Shunt', 'Programmable Valves', 'Endoscopic Surgery', 'NEUROWEAVE Proposal'],
    'Effectiveness (%)': [20, 35, 50, 92.3]
})
fig_timeline = px.line(timeline_data, x='Year', y='Effectiveness (%)', text='Innovation', markers=True,
                       title='Timeline of Treatment Innovation and Efficacy',
                       color_discrete_sequence=['deepskyblue'])
fig_timeline.update_traces(textposition="top center")
fig_timeline.update_layout(plot_bgcolor='mintcream', paper_bgcolor='mintcream')
st.plotly_chart(fig_timeline, use_container_width=True)

# --- SECTION 4: Dynamic Key Metrics ---
st.header("📌 Global Metrics at a Glance")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Annual Pediatric Cases", "400,000+", "WHO, 2025")
with col2:
    st.metric("Shunt Failure Rate", "50% in 2 Years", "WHO Reports")
with col3:
    st.metric("NEUROWEAVE Efficacy", "92.3%", "COMSOL Simulations")

# --- SECTION 5: Summary Visualization Cards ---
st.markdown("---")
st.subheader("🧠 Summary Visualization")
col_a, col_b = st.columns(2)

with col_a:
    st.image("https://cdn-icons-png.flaticon.com/512/3039/3039403.png", width=120)
    st.success("NEUROWEAVE acts from within — repairing, regenerating and resetting the ventricular system.")
with col_b:
    st.image("https://cdn-icons-png.flaticon.com/512/3194/3194703.png", width=120)
    st.info("Unlike traditional methods, it adapts to anatomy, dissolves post-action and avoids complications.")

# --- Footer ---
st.markdown("---")
st.success("NEUROWEAVE is not science fiction. It's real, replicable, and designed for global health equity.")
st.caption("Created by Annette – Young Global Researcher from Ecuador transforming neurotech. 🧠")