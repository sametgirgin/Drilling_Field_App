import streamlit as st

def hydrostatic_pressure_calculator():
    st.markdown("<h2 style='text-align: center;'>Hydrostatic Pressure Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""

    Hydrostatic Pressure (HP) = 0.052 × Mud Weight × True Vertical Depth (TVD)

    Where:  
    - Mud Weight: ppg  
    - True Vertical Depth (TVD): ft
    
    """)

    mud_weight = st.number_input("Mud Weight (ppg)", min_value=0.0, value=12.0, key="hp_mw")
    tvd = st.number_input("True Vertical Depth (TVD, ft)", min_value=0.0, value=10000.0, key="hp_tvd")

    hp = 0.052 * mud_weight * tvd
    st.success(f"**Hydrostatic Pressure (HP): {hp:,.2f} psi**")