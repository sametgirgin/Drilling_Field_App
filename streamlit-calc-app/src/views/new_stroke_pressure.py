import streamlit as st
import math

def new_stroke_pressure():
    st.markdown("<h2 style='text-align: center;'>New Pressure Loss with New Strokes</h2>", unsafe_allow_html=True)
    st.markdown("""
    Calculate the new circulating pressure based on pump pressure and pump stroke relationship:

    New circulating pressure (psi) = Present circulating pressure (psi) × (New pump rate (spm) ÷ Old pump rate (spm))²

    - Present circulating pressure in psi
    - Old pump rate in strokes per minute (spm)
    - New pump rate in strokes per minute (spm)
    """)

    present_pressure = st.number_input("Present circulating pressure (psi)", min_value=0.0, value=2500.0)
    old_pump_rate = st.number_input("Old pump rate (spm)", min_value=0.01, value=40.0)
    new_pump_rate = st.number_input("New pump rate (spm)", min_value=0.01, value=25.0)

    if st.button("Calculate New Circulating Pressure"):
        new_pressure = present_pressure * (new_pump_rate / old_pump_rate) ** 2
        st.success(f"**New circulating pressure: {new_pressure:.1f} psi**")

    st.markdown("---")

    st.markdown("**Advanced Formula with Factor n**")
    st.markdown("""
    This advanced method uses a factor (n) to calculate the new circulating pressure based on two sets of pressure and pump rates.
    
    **Step 1:**  
    Factor (n) = log (Pressure 1 ÷ Pressure 2) ÷ log (Pump rate 1 ÷ Pump rate 2)

    **Step 2:**  
    New circulating pressure (psi) = Present circulating pressure (psi) × (New pump rate (spm) ÷ Old pump rate (spm))ⁿ

    """)

    pressure1 = st.number_input("Pressure 1 (psi)", min_value=0.01, value=2700.0, key="pressure1")
    pump_rate1 = st.number_input("Pump rate 1 (spm or gpm)", min_value=0.01, value=320.0, key="pump_rate1")
    pressure2 = st.number_input("Pressure 2 (psi)", min_value=0.01, value=500.0, key="pressure2")
    pump_rate2 = st.number_input("Pump rate 2 (spm or gpm)", min_value=0.01, value=130.0, key="pump_rate2")
    present_pressure_n = st.number_input("Present circulating pressure (psi) [n method]", min_value=0.0, value=1500.0, key="present_pressure_n")
    old_pump_rate_n = st.number_input("Old pump rate (spm) [n method]", min_value=0.01, value=50.0, key="old_pump_rate_n")
    new_pump_rate_n = st.number_input("New pump rate (spm) [n method]", min_value=0.01, value=60.0, key="new_pump_rate_n")

    if st.button("Calculate Factor n and New Circulating Pressure (Advanced)"):
        try:
            n = math.log(pressure1 / pressure2) / math.log(pump_rate1 / pump_rate2)
            new_pressure_advanced = present_pressure_n * (new_pump_rate_n / old_pump_rate_n) ** n
            st.markdown(f"**Factor (n): {n:.3f}**")
            st.success(f"**New circulating pressure (advanced): {new_pressure_advanced:.2f} psi**")
        except Exception as e:
            st.error(f"Error in calculation: {e}")