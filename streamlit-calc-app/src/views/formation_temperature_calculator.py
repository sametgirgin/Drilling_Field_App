import streamlit as st

def formation_temperature_calculator():
    st.markdown("<h2 style='text-align: center;'>Formation Temperature Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    **Formula:**  
    Formation temperature (°F) = Ambient surface temperature (°F) + [Temperature gradient (°F/ft) × Well TVD (ft)]

    **Where:**  
    - Formation temperature: °F  
    - Ambient surface temperature: °F  
    - Temperature gradient: °F/ft  
    - Well TVD: ft

    """)

    surface_temp = st.number_input("Ambient surface temperature (°F)", min_value=-100.0, value=90.0, key="ftc_surface")
    temp_gradient = st.number_input("Temperature gradient (°F/ft)", min_value=0.0, value=0.015, format="%.3f", key="ftc_gradient")
    tvd = st.number_input("Well TVD (ft)", min_value=0.0, value=12000.0, key="ftc_tvd")

    formation_temp = surface_temp + (temp_gradient * tvd)
    st.success(f"**Estimated Formation Temperature:** {formation_temp:.2f} °F")