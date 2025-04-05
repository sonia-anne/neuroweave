import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image

# --- Page Configuration ---
st.set_page_config(page_title="NEUROWEAVE - Dynamic Scientific Dashboard", layout="wide", page_icon="🧠")

st.markdown("""
<style>
    .main {
        background-color: #E8F0FE;
    }
    .block-container {
        padding: 2rem 2rem 2rem;
        font-family: 'Helvetica', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.image("https://cdn-icons-png.flaticon.com/512/3623/3623883.png", width=80)
st.title("NEUROWEAVE: Dynamic & Scientific Visualization")
st.markdown("A visual, interactive and data-driven platform to understand the global impact of hydrocephalus and NEUROWEAVE’s innovative solution.")

--- Section 1: Global Prevalence with Advanced Tabs ---

st.header("🌍 Global Prevalence of Hydrocephalus") st.markdown("This section presents prevalence data, a comparison table and a mini geographical chart.")

Prevalence Data Table

with st.expander("📊 View Prevalence Table"): data_map = pd.DataFrame({ 'Country': ['D.R. Congo', 'India', 'Brazil', 'Nigeria', 'USA', 'Germany', 'Kenya', 'Philippines', 'Bangladesh', 'Ecuador'], 'Cases per 100k Births': [850, 730, 490, 780, 220, 190, 800, 670, 710, 540], 'Continent': ['Africa', 'Asia', 'South America', 'Africa', 'North America', 'Europe', 'Africa', 'Asia', 'Asia', 'South America'] }) st.dataframe(data_map.style.background_gradient(cmap='YlOrRd'), use_container_width=True)

Pie Chart by Continent

continent_data = data_map.groupby('Continent').sum().reset_index() fig_pie = px.pie(continent_data, values='Cases per 100k Births', names='Continent', title='Proportion of Hydrocephalus Cases by Continent', color_discrete_sequence=px.colors.sequential.RdBu) st.plotly_chart(fig_pie, use_container_width=True)

--- Section 2: Mortality & Morbidity Comparison ---

st.header("⚖️ Neurological Condition Impact: Mortality vs Morbidity") conditions = ['Hydrocephalus', 'Childhood Epilepsy', 'Meningitis', 'Cerebral Palsy', 'Congenital Malformations'] mortality = [37, 22, 18, 12, 26] morbidity = [80, 55, 35, 90, 70]

fig_bar = go.Figure() fig_bar.add_trace(go.Bar(x=conditions, y=mortality, name='Mortality (%)', marker_color='crimson')) fig_bar.add_trace(go.Bar(x=conditions, y=morbidity, name='Morbidity (%)', marker_color='orange')) fig_bar.update_layout( barmode='group', title='Global Comparison: Mortality vs Morbidity in Neurological Conditions', xaxis_title='Neurological Condition', yaxis_title='Percentage (%)', plot_bgcolor='whitesmoke', paper_bgcolor='white', font=dict(color='black', size=14), legend=dict(x=0.75, y=1.15, orientation='h') ) st.plotly_chart(fig_bar, use_container_width=True)

--- Section 3: Timeline of Treatments ---

st.header("⏳ Evolution of Hydrocephalus Treatments") st.markdown("From shunts to nanotechnology — how treatment efficacy has evolved over time.") timeline_data = pd.DataFrame({ 'Year': [1960, 1985, 2005, 2025], 'Innovation': ['First Shunt Implanted', 'Programmable Valves', 'Endoscopic Surgeries', 'NEUROWEAVE Proposal'], 'Effectiveness (%)': [20, 35, 50, 92.3] })

fig_timeline = go.Figure() fig_timeline.add_trace(go.Scatter( x=timeline_data['Year'], y=timeline_data['Effectiveness (%)'], mode='lines+markers+text', text=timeline_data['Innovation'], textposition='top center', line=dict(color='deepskyblue', width=4) )) fig_timeline.update_layout( title='Treatment Innovation Timeline in Hydrocephalus', xaxis_title='Year', yaxis_title='Estimated Effectiveness (%)', plot_bgcolor='honeydew', paper_bgcolor='mintcream' ) st.plotly_chart(fig_timeline, use_container_width=True)

--- Key Metrics ---

st.markdown("---") st.subheader("📌 Global Key Metrics") col1, col2, col3 = st.columns(3) with col1: st.metric("Pediatric Cases per Year", "400,000+", "WHO, 2025") with col2: st.metric("Shunt Failure Rate", "50% within 2 years", "Global Neurology Data") with col3: st.metric("NEUROWEAVE Projected Efficacy", "92.3%", "COMSOL 3D Simulation")

--- Footer ---

st.markdown("---") st.success("NEUROWEAVE is not science fiction. It’s tangible, scalable, and human-centered neuroscience.") st.caption("Created by Annette – Young Global Researcher from Ecuador rethinking neurotechnology. 🧠")

