import streamlit as st

def drill_pipe_elongation_temp():
    st.markdown("<h2 style='text-align: center;'>Drill Pipe Elongation Due to Temperature Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Drill pipe elongation will occur because the higher bottom hole temperature.
    Pipe will elongate approximately 0.83 inc per 100 ft of length, per 100 degree F 
    increase in Temperature.

    This calculator estimates the elongation of drill pipe due to temperature increase.

    **Formulas:**  
    - Average Temperature = (Bottom Hole Temperature + Surface Temperature) ÷ 2  
    - ΔTemperature = Average Temperature − Surface Temperature  
    - Pipe Elongation (in) = (L ÷ 100) × (ΔTemperature ÷ 100) × 0.83

    Where:
    - L: Total length of pipe (ft)
    - Temperatures in °F
    - Pipe Elongation in inches
    """)

    length = st.number_input("Total length of pipe (ft)", min_value=0.0, value=10000.0)
    surface_temp = st.number_input("Surface temperature (°F)", min_value=-100.0, value=80.0)
    bottom_temp = st.number_input("Bottom hole temperature (°F)", min_value=-100.0, value=375.0)

    avg_temp = (bottom_temp + surface_temp) / 2
    delta_temp = avg_temp - surface_temp
    elongation = (length / 100) * (delta_temp / 100) * 0.83

    st.markdown(f"**Average T:** {avg_temp:.2f} °F")
    st.markdown(f"**ΔT:** {delta_temp:.2f} °F")
    st.success(f"**Pipe Elongation:** {elongation:.2f} inch")