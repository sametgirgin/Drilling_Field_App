import streamlit as st
import math

def fit_pressure_calculator():
    st.markdown("<h2 style='text-align: center;'>Formation Integrity Test (FIT) Pressure Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Formation Integrity Test is a method to test strength of formation and shoe by increasing Bottom Hole Pressure (BHP) to designed pressure. FIT is normally conducted to ensure that formation below a casing shoe will not be broken while drilling the next section with higher BHP or circulating gas influx in a well control situation. Normally, drilling engineers will design how much formation integrity test pressure required for each hole section.

    Pressure required for FIT (psi) = (Required FIT − Current Mud Weight) × 0.052 × True Vertical Depth of shoe

    Where:  
    - Required FIT: Required FIT (ppg)  
    - Current Mud Weight: Current mud weight (ppg)  
    - True Vertical Depth of shoe: TVD (ft)

    **Note:** FIT pressure must be rounded down.

    """)

    required_fit = st.number_input("Required FIT (ppg)", min_value=0.0, value=14.5, key="fit_required")
    current_mw = st.number_input("Current mud weight (ppg)", min_value=0.0, value=9.2, key="fit_mw")
    tvd = st.number_input("Shoe depth TVD (ft)", min_value=0.0, value=4000.0, key="fit_tvd")

    fit_pressure = (required_fit - current_mw) * 0.052 * tvd
    fit_pressure_rounded = math.floor(fit_pressure)

    st.success(f"**Pressure required for FIT: {fit_pressure_rounded} psi**")