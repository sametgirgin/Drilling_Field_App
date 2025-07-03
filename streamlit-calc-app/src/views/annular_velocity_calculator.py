import streamlit as st

def annular_velocity_calculator():
    st.markdown("<h2 style='text-align: center;'>Annular Velocity (AV) Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Three main factors affecting annular velocity are size of hole (bigger ID), size of drill pipe (smaller OD) and pump rate. 
    
    Annular velocity (ft/min) = (24.5 × Flow Rate) ÷ (Dh² − Dp²)

    - Flow Rate: gpm
    - Dh: Inside diameter of casing or hole size (in)
    - Dp: Outside diameter of pipe, tubing, or collars (in)
    """)

    flow_rate = st.number_input("Flow Rate (gpm)", min_value=0.0, value=800.0, key="av_flow_rate")
    dh = st.number_input("Hole size / Casing ID (Dh, in)", min_value=0.0, value=10.0, key="av_dh")
    dp = st.number_input("Pipe OD (Dp, in)", min_value=0.0, value=5.0, key="av_dp")

    denominator = dh**2 - dp**2
    if denominator > 0:
        av = (24.5 * flow_rate) / denominator
        st.success(f"Annular velocity: {av:.2f} ft/min")
    else:
        st.error("Dh² must be greater than Dp² for a valid calculation.")