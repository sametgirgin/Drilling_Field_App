import streamlit as st

def theoretical_lag_time():
    st.markdown("<h2 style='text-align: center;'>Theoretical Lag Time Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Theoretical lag time is the time required for drilling fluid to travel from the bit to the 
    surface. It depends on the annular volume and the mud flow rate.

    **Formulas:**
    - Pump rate (bbl/min) = Pump rate (GPM) ÷ 42
    - Lag time (minutes) = Annular volume (bbl) ÷ Pump rate (bbl/min)
    - Lag time (strokes) = Annular volume (bbl) ÷ Pump output (bbl/stroke)

    """)

    annular_volume = st.number_input("Annular volume (bbl)", min_value=0.0, value=250.0)
    pump_rate_gpm = st.number_input("Pump rate (GPM)", min_value=0.0, value=300.0)
    pump_output = st.number_input("Pump output (bbl/stroke)", min_value=0.0001, value=0.102)

    pump_rate_bbl_min = pump_rate_gpm / 42 if pump_rate_gpm > 0 else 0
    lag_time_min = annular_volume / pump_rate_bbl_min if pump_rate_bbl_min > 0 else 0
    lag_time_strokes = annular_volume / pump_output if pump_output > 0 else 0

    st.markdown(f"**Pump rate:** {pump_rate_bbl_min:.2f} bbl/min")
    st.markdown(f"**Lag time:** {lag_time_min:.1f} minutes")
    st.markdown(f"**Lag time:** {lag_time_strokes:.0f} strokes")