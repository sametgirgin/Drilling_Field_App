import streamlit as st
import math

def max_pit_gain():
    st.markdown("<h2 style='text-align: center;'>Maximum Pit Gain from Gas Kick in Water Based Mud</h2>", unsafe_allow_html=True)
    st.markdown("""
    This tool estimates the maximum pit gain due to a gas influx in a 
    water-based mud system using the following formula:

    **Max Pit Gain = 4 × √(P × V × C / Kill Weight Mud)**

    - Max Pit Gain: Maximum pit gain (bbl)
    - P: Formation pressure (psi)
    - V: Original pit gain (bbl)
    - C: Annular capacity (bbl/ft)
    - Kill Weight Mud: Kill weight mud (ppg)
    """)

    formation_pressure = st.number_input("Formation pressure, P (psi)", min_value=0.0, value=3620.0)
    original_pit_gain = st.number_input("Original pit gain, V (bbl)", min_value=0.0, value=20.0)
    annular_capacity = st.number_input("Annular capacity, C (bbl/ft)", min_value=0.0, value=0.1215)
    kill_weight_mud = st.number_input("Kill Weight Mud (ppg)", min_value=0.01, value=14.5)

    if st.button("Calculate Maximum Pit Gain"):
        try:
            value = (formation_pressure * original_pit_gain * annular_capacity) / kill_weight_mud
            if value < 0:
                st.error("Calculation under the square root resulted in a negative number. Please check your inputs.")
            else:
                max_pit_gain = 4 * math.sqrt(value)
                st.success(f"**Maximum Pit Gain: {max_pit_gain:.2f} bbl**")
        except Exception as e:
            st.error(f"Error in calculation: {e}")