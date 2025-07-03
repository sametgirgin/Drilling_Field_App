import streamlit as st

def drill_string_pressure_loss_calculator():
    st.markdown("<h2 style='text-align: center;'>Pressure Losses Through Drill String Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    This tool calculates the pressure loss through the drill string (drill pipe + drill collar).

    **Formulas:**  
    - P = 0.00001 × L × C × W × Vf × Q<sup>1.86</sup>  
    - C = 6.1 / (Di**4.86)  
    - Vf = (PV / W)**0.14
    - Pt = P_dp + Pdc

    Where:  
    - P = pressure loss (psi)  
    - L = length of pipe (ft)  
    - W = mud weight (ppg)  
    - PV = plastic viscosity (cP)  
    - Q = flow rate (gpm)  
    - Di = inside diameter of pipe (in)  
    - C = coefficient for pipe ID  
    - Vf = viscosity correction factor  
    - Pt = total pressure loss  
    - P_dp = pressure loss in drill pipe  
    - P_dc = pressure loss in drill collar
    """)

    st.subheader("Drill Pipe")
    L_dp = st.number_input("Drill pipe length (ft)", min_value=0.0, value=5000.0, key="dsp_dp_len")
    Di_dp = st.number_input("Drill pipe ID (in)", min_value=0.01, value=3.34, key="dsp_dp_id")

    st.subheader("Drill Collar")
    L_dc = st.number_input("Drill collar length (ft)", min_value=0.0, value=500.0, key="dsp_dc_len")
    Di_dc = st.number_input("Drill collar ID (in)", min_value=0.01, value=2.8, key="dsp_dc_id")

    st.subheader("Mud Properties & Flow")
    W = st.number_input("Mud Weight (ppg)", min_value=0.0, value=9.5, key="dsp_mw")
    PV = st.number_input("Plastic Viscosity (cP)", min_value=0.0, value=12.0, key="dsp_pv")
    Q = st.number_input("Flow rate (gpm)", min_value=0.0, value=600.0, key="dsp_q")

    # Viscosity correction factor
    Vf = (PV / W) ** 0.14 if W > 0 else 0

    # Drill pipe
    C_dp = 6.1 / (Di_dp ** 4.86)
    Pdp = 0.00001 * L_dp * C_dp * W * Vf * (Q ** 1.86)

    # Drill collar
    C_dc = 6.1 / (Di_dc ** 4.86)
    Pdc = 0.00001 * L_dc * C_dc * W * Vf * (Q ** 1.86)

    Pt = Pdp + Pdc

    st.markdown(f"**Pressure loss in drill pipe (Pdp): {Pdp:,.0f} psi**")
    st.markdown(f"**Pressure loss in drill collar (Pdc): {Pdc:,.0f} psi**")
    st.success(f"**Total pressure loss in drill string (Pt): {Pt:,.0f} psi**")