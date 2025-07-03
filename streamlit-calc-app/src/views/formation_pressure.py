import streamlit as st

def formation_pressure():
    st.markdown("<h2 style='text-align: center;'>Formation Pressure from Kick Analysis</h2>", unsafe_allow_html=True)
    st.markdown("""
    After closing the well and measuring the shut-in drill pipe pressure, 
    you can use hydrostatic pressure principles to estimate the formation pressure. 
    
    Formation Pressure = SIDPP + (0.052 × Hole TVD × Current Mud Weight)

    - Formation Pressure in psi
    - SIDPP (Shut In Drill Pipe Pressure) in psi
    - Hole TVD (True Vertical Depth) in ft
    - Current Mud Weight in ppg
    """)

    sidpp = st.number_input("Shut In Drill Pipe Pressure (SIDPP, psi)", min_value=0.0, value=300.0)
    hole_tvd = st.number_input("Hole TVD (ft)", min_value=0.0, value=8000.0)
    mud_weight = st.number_input("Current Mud Weight (ppg)", min_value=0.0, value=10.0)

    if st.button("Calculate", key="calculate_formation_pressure"):
        formation_pressure = sidpp + (0.052 * hole_tvd * mud_weight)
        st.success(f"**Formation Pressure:** {formation_pressure:.2f} psi")