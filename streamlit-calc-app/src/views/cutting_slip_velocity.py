import streamlit as st
import math

def calculate_annular_velocity(Q, Dh, Dp):
    denominator = (Dh**2 - Dp**2)
    if denominator <= 0:
        return None
    else:
        AV = (24.5 * Q) / denominator
        return AV

def calculate_slip_velocity(PV, MW, Dp, DenP):
    try:
        common_term_denominator = MW * Dp
        if common_term_denominator == 0:
            return None
        common_term = PV / common_term_denominator

        term_under_sqrt_numerator = 36800 * Dp
        term_under_sqrt_denominator_squared = common_term ** 2
        if term_under_sqrt_denominator_squared == 0:
            return None

        if MW == 0:
            return None
        density_ratio_term = (DenP / MW) - 1

        term_under_sqrt_inside_paren = (term_under_sqrt_numerator / term_under_sqrt_denominator_squared) * density_ratio_term
        if term_under_sqrt_inside_paren < 0:
            return None

        main_sqrt_term = math.sqrt(term_under_sqrt_inside_paren + 1)
        Vs = 0.45 * common_term * (main_sqrt_term - 1)
        return Vs
    except Exception:
        return None

def cutting_slip_velocity():
    st.markdown("<h2 style='text-align: center;'>Cutting Slip Velocity & Net Rise Velocity Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    To ensure effective hole cleaning in drilling operations, it's crucial to understand the dynamics of cutting slip velocity. This involves calculating the annular velocity (AV), which is the upward speed of the drilling mud, and the cutting slip velocity (Vs), which represents how quickly cuttings fall due to gravity. The difference between these two, the net rise velocity, indicates whether cuttings are being successfully lifted out of the wellbore or accumulating at the bottom. A positive net rise velocity signifies good hole cleaning, while a negative value suggests the flow rate is insufficient to carry cuttings, potentially leading to a cutting bed.           
                
    This tool calculates:
    - **Annular Velocity (AV)**: Based on flow rate, hole diameter, and pipe diameter.
    - **Cutting Slip Velocity (Vs)**: Based on mud and cutting properties.
    - **Net Rise Velocity**: AV - Vs (indicates if cuttings are being lifted or falling).

    **If Net Rise Velocity is positive:** Good hole cleaning.  
    **If Net Rise Velocity is negative:** Flow rate is NOT enough to carry cuttings.
    """)

    st.subheader("Input Parameters")
    Q = st.number_input("Flow rate (Q, GPM)", min_value=0.0, value=500.0, key="csv_q")
    Dh = st.number_input("Hole diameter (Dh, in)", min_value=0.0, value=12.25, key="csv_dh")
    Dp = st.number_input("Pipe diameter (Dp, in)", min_value=0.0, value=5.0, key="csv_dp")
    PV = st.number_input("Plastic Viscosity (PV, cP)", min_value=0.0, value=17.0, key="csv_pv")
    MW = st.number_input("Mud Weight (MW, ppg)", min_value=0.0, value=9.2, key="csv_mw")
    Dcut = st.number_input("Cutting diameter (Dp, in)", min_value=0.0, value=0.05, key="csv_dcut")
    DenP = st.number_input("Cutting density (DenP, ppg)", min_value=0.0, value=20.8, key="csv_denp")

    AV = calculate_annular_velocity(Q, Dh, Dp)
    Vs = calculate_slip_velocity(PV, MW, Dcut, DenP)

    if AV is not None:
        st.markdown(f"**Annular Velocity (AV): {AV:.2f} ft/min**")
    else:
        st.error("Invalid input for Annular Velocity. Hole diameter must be greater than pipe diameter.")

    if Vs is not None:
        st.markdown(f"**Cutting Slip Velocity (Vs): {Vs:.2f} ft/min**")
    else:
        st.error("Invalid input for Slip Velocity. Check mud weight, cutting diameter, or other parameters.")

    if AV is not None and Vs is not None:
        net_rise = AV - Vs
        st.markdown(f"**Net Rise Velocity (AV - Vs): {net_rise:.1f} ft/min**")
        if net_rise > 0:
            st.success("Net rise velocity is positive: Good flow rate to carry cuttings.")
        else:
            st.error("Net rise velocity is negative: Flow rate is NOT enough to carry cuttings.")