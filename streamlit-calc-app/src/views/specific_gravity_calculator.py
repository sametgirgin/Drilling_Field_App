import streamlit as st

def specific_gravity_calculator():
    st.markdown("<h2 style='text-align: center;'>Specific Gravity Calculator (from Mud Weight in PPG)</h2>", unsafe_allow_html=True)
    st.markdown("""
    Specific Gravity (SG) is a dimensionless ratio that compares the density of a substance to the density of a reference substance, typically water at 4°C (39.2°F).

    Specific Gravity (SG) = Mud weight (ppg) ÷ 8.33
    """)

    mud_weight = st.number_input("Mud weight (ppg)", min_value=0.0, value=13.0, key="sg_mud_weight")
    sg = mud_weight / 8.33
    st.success(f"**Specific Gravity (SG): {sg:.2f}**")