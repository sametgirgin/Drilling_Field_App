import streamlit as st
import math

def surge_swab_pressure_calculator():
    st.markdown("<h2 style='text-align: center;'>Surge & Swab Pressure Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    This tool calculates surge and swab pressures using the Power Law model for non-Newtonian fluids.

    **Steps:**  
    1. Calculate n and K from viscometer readings  
    2. Calculate fluid velocities around drill pipe and drill collar  
    3. Calculate maximum pipe velocities  
    4. Calculate pressure losses  
    5. Calculate total pressure loss  
    6. Calculate bottom hole pressure for surge and swab

    ---
    """)

    st.subheader("Rheology Inputs")
    theta_600 = st.number_input("Viscometer Reading at 600 rpm (Θ600)", min_value=0.01, value=80.0, key="ssp_600")
    theta_300 = st.number_input("Viscometer Reading at 300 rpm (Θ300)", min_value=0.01, value=47.0, key="ssp_300")

    st.subheader("Drill Pipe Geometry & Movement")
    Dp = st.number_input("Drill Pipe OD (Dp, in)", min_value=0.01, value=4.0, key="ssp_dp")
    Di = st.number_input("Drill Pipe ID (Di, in)", min_value=0.01, value=3.34, key="ssp_di")
    Ldp = st.number_input("Drill Pipe Length (Ldp, ft)", min_value=0.0, value=12270.0, key="ssp_ldp")
    Vp = st.number_input("Pipe Movement Velocity (Vp, ft/min)", min_value=0.0, value=20.0, key="ssp_vp")

    st.subheader("Drill Collar Geometry")
    Dc = st.number_input("Drill Collar OD (Dc, in)", min_value=0.01, value=5.0, key="ssp_dc")
    Dci = st.number_input("Drill Collar ID (Dci, in)", min_value=0.01, value=2.25, key="ssp_dci")
    Ldc = st.number_input("Drill Collar Length (Ldc, ft)", min_value=0.0, value=100.0, key="ssp_ldc")

    st.subheader("Hole & Mud Properties")
    Dh = st.number_input("Hole Diameter (Dh, in)", min_value=0.01, value=6.35, key="ssp_dh")
    #PV = st.number_input("Plastic Viscosity (PV, cP)", min_value=0.0, value=12.0, key="ssp_pv")
    MW = st.number_input("Mud Weight (ppg)", min_value=0.0, value=13.2, key="ssp_mw")
    H = st.number_input("True Vertical Depth (ft)", min_value=0.0, value=9972.0, key="ssp_h")

    st.markdown("#### Step 1: Calculate n and K")
    n = 3.23 * math.log10(theta_600 / theta_300)
    K = theta_300 / (511 ** n)
    PV = (theta_600 - theta_300)
    st.markdown(f"**n (Power Law Exponent): {n:.4f}**")
    st.markdown(f"**K (Consistency Index): {K:.4f}**")

    st.markdown("#### Step 2: Fluid Velocity Around Drill Pipe")
    pipe_end_type = st.radio("Pipe End Type", ["Closed-ended (plugged)", "Open-ended"], key="ssp_endtype")

    if pipe_end_type == "Closed-ended (plugged)":
        Vdp = (0.45 + (Dp ** 2) / (Dh ** 2 - Dp ** 2)) * Vp
        Vdc = (0.45 + (Dc ** 2) / (Dh ** 2 - Dc ** 2)) * Vp
    else:
        Vdp = (0.45 + (Dp ** 2 - Di ** 2) / (Dh ** 2 - Dp ** 2 + Di ** 2)) * Vp
        Vdc = (0.45 + (Dc ** 2 - Dci ** 2) / (Dh ** 2 - Dc ** 2 + Dci ** 2)) * Vp

    st.markdown(f"**Fluid velocity around drill pipe (Vdp): {Vdp:.2f} ft/min**")
    st.markdown(f"**Fluid velocity around drill collar (Vdc): {Vdc:.2f} ft/min**")

    st.markdown("#### Step 3: Maximum Pipe Velocity")
    Vm_dp = Vdp * 1.5
    Vm_dc = Vdc * 1.5
    st.markdown(f"**Maximum pipe velocity (Vm, drill pipe): {Vm_dp:.2f} ft/min**")
    st.markdown(f"**Maximum pipe velocity (Vm, drill collar): {Vm_dc:.2f} ft/min**")

    st.markdown("#### Step 4: Pressure Loss Calculations")
    # Drill pipe pressure loss
    try:
        Pdp = ((2.4 * Vm_dp / (Dh - Dp)) * ((2 * n + 1) / (3 * n))) ** n * (K * Ldp / (300 * (Dh - Dp)))
    except Exception:
        Pdp = 0
    # Drill collar pressure loss
    try:
        Pdc = ((2.4 * Vm_dc / (Dh - Dc)) * ((2 * n + 1) / (3 * n))) ** n * (K * Ldc / (300 * (Dh - Dc)))
    except Exception:
        Pdc = 0

    st.markdown(f"**Pressure loss around drill pipe (Pdp): {Pdp:.2f} psi**")
    st.markdown(f"**Pressure loss around drill collar (Pdc): {Pdc:.2f} psi**")

    st.markdown("#### Step 5: Total Pressure Loss")
    Pt = Pdp + Pdc
    st.success(f"**Total Pressure Loss: {Pt:.2f} psi**")

    st.markdown("#### Step 6: Hydrostatic & Bottom Hole Pressure")
    # Hydrostatic pressure
    hydrostatic = 0.052 * MW * H
    st.markdown(f"**Hydrostatic Pressure: {hydrostatic:.2f} psi**")

    surge_bhp = hydrostatic + Pt
    swab_bhp = hydrostatic - Pt

    st.success(f"**Bottom hole pressure (Surge): {surge_bhp:.2f} psi**")
    st.success(f"**Bottom hole pressure (Swab): {swab_bhp:.2f} psi**")