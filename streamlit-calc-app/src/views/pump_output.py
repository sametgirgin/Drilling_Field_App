import streamlit as st

def pump_output():
    st.markdown("<h2 style='text-align: center;'>Pump Output Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    The rig pump output, usually measured in volume per stroke, is a crucial parameter to 
    know on the rig. This value is essential for calculating various operational metrics 
    such as bottoms-up strokes, washout depth, and monitoring the movement of drilling fluid.
    
    Calculate the pump output for Duplex and Triplex mud pumps.

    **Triplex Pump Output:**  
    Triplex Output = 0.000243 × (Liner Diameter)² × (Stroke Length) × Pump Efficiency

    **Duplex Pump Output:**  
    Duplex Output = 0.000162 × Stroke Length × [2 × (Liner Diameter)² − (Rod Diameter)²] × Pump Efficiency

    - Liner Diameter (D): in
    - Stroke Length (S): in
    - Rod Diameter (d): in (for Duplex only)
    - Pump Efficiency: (as a decimal, e.g., 0.9 for 90%)
    """)

    st.markdown("#### Triplex Pump Output")
    liner_dia_tri = st.number_input("Triplex Liner Diameter (in)", min_value=0.0, value=6.0, key="tri_liner")
    stroke_len_tri = st.number_input("Triplex Stroke Length (in)", min_value=0.0, value=12.0, key="tri_stroke")
    eff_tri = st.number_input("Triplex Pump Efficiency (0-1)", min_value=0.0, max_value=1.0, value=0.9, key="tri_eff")

    if st.button("Calculate Triplex Pump Output"):
        output_tri = 0.000243 * (liner_dia_tri ** 2) * stroke_len_tri * eff_tri
        st.success(f"**Triplex Pump Output: {output_tri:.2f} bbl/stroke**")

    st.markdown("---")
    st.markdown("#### Duplex Pump Output")
    liner_dia_dup = st.number_input("Duplex Liner Diameter (D, in)", min_value=0.0, value=6.0, key="dup_liner")
    rod_dia_dup = st.number_input("Duplex Rod Diameter (d, in)", min_value=0.0, value=2.75, key="dup_rod")
    stroke_len_dup = st.number_input("Duplex Stroke Length (S, in)", min_value=0.0, value=12.0, key="dup_stroke")
    eff_dup = st.number_input("Duplex Pump Efficiency (0-1)", min_value=0.0, max_value=1.0, value=0.9, key="dup_eff")

    if st.button("Calculate Duplex Pump Output"):
        output_dup = 0.000162 * stroke_len_dup * (2 * (liner_dia_dup ** 2) - (rod_dia_dup ** 2)) * eff_dup
        st.success(f"**Duplex Pump Output: {output_dup:.2f} bbl/stroke**")