import streamlit as st

def equivalent_circulating_density():
    st.markdown("<h2 style='text-align: center;'>Equivalent Circulating Density (ECD) Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    **Equivalent circulating density (ECD)** is the effective density of 
    the circulating fluid in the wellbore resulting from the sum of the 
    hydrostatic pressure imposed by the static fluid column and the 
    friction pressure.

    **For MW ≤ 13.0 ppg:**  
    ECD = MW + (0.1 × Y.P) / (Hole ID − Pipe OD)

    **For MW > 13.0 ppg:**  
    ECD = MW + [0.1 / (Hole ID − Pipe OD)] × [Y.P + (P.V × A.V) / (300 × (Hole ID − Pipe OD))]

    - MW: Mud Weight (ppg)
    - Reading at 600 rpm
    - Reading at 300 rpm
    - Q: Flow rate (gpm)
    - Hole ID: Hole diameter (in)
    - Pipe OD: Drill pipe OD (in)
    """)

    mw = st.number_input("Mud Weight (MW, ppg)", min_value=0.0, value=12.0)
    reading_600 = st.number_input("Viscometer Reading at 600 rpm", min_value=0.0, value=40.0)
    reading_300 = st.number_input("Viscometer Reading at 300 rpm", min_value=0.0, value=30.0)
    q = st.number_input("Flow Rate (Q, gpm)", min_value=0.0, value=500.0)
    hole_id = st.number_input("Hole Diameter (Hole ID, in)", min_value=0.01, value=8.5)
    pipe_od = st.number_input("Drill Pipe OD (Pipe OD, in)", min_value=0.0, value=5.0)

    denominator = hole_id - pipe_od
    if denominator <= 0:
        st.error("Hole diameter must be greater than pipe OD.")
        return

    pv = reading_600 - reading_300
    yp = reading_300 - pv
    av = (24.5 * q) / (hole_id**2 - pipe_od**2) if (hole_id**2 - pipe_od**2) != 0 else 0

    st.markdown(f"**Plastic Viscosity (PV): {pv:.2f} cP**")
    st.markdown(f"**Yield Point (YP): {yp:.2f} lb/100 sq ft**")
    st.markdown(f"**Annular Velocity (AV): {av:.2f} ft/min**")

    if st.button("Calculate ECD"):
        if mw <= 13.0:
            ecd = mw + (0.1 * yp) / denominator
        else:
            ecd = mw + (0.1 / denominator) * (yp + (pv * av) / (300 * denominator))
        st.success(f"**Equivalent Circulating Density (ECD): {ecd:.3f} ppg**")