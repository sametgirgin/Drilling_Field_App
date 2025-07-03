import streamlit as st

def calculate_effective_viscosity(Ka, Va, Dh, Do, na):
    try:
        diameter_difference = Dh - Do
        if diameter_difference <= 0:
            return None
        bracket_term = (144 * Va) / diameter_difference
        exponent = na - 1
        if bracket_term <= 0 and exponent != 0:
            return None
        power_term = bracket_term ** exponent
        mu_ea = 100 * Ka * power_term
        return mu_ea
    except Exception:
        return None

def calculate_annular_velocity(Q, Dh, Dp):
    denominator = (Dh**2 - Dp**2)*60
    if denominator <= 0:
        return None
    else:
        AV = (24.5 * Q) / denominator
        return AV

def effective_viscosity_calculator():
    st.markdown("<h2 style='text-align: center;'>Effective Viscosity Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    The viscosity of drilling mud will change with a change in the shear rate because in some degree drilling fluids are shear-thinning. Because of its nature of drilling mud, people create the new term of viscosity called “Effective Viscosity” to compensate the change in shear rate of viscosity. By definition, the effective viscosity means the viscosity of Newtonian fluid that gives the same shear stress at the same shear rate.

    This tool calculates the **effective viscosity (μₑₐ)** for non-Newtonian fluids in annular flow.

    **Formula:**  
    μₑₐ = 100 × Kₐ × [(144 × Vₐ) / (Dₕ − Dₒ)]^(nₐ − 1)

    Where:  
    - Kₐ = Consistency index (annular flow)  
    - Vₐ = Annular velocity (ft/sec)  
    - Dₕ = Hole diameter (in)  
    - Dₒ = Outer pipe diameter (in)  
    - nₐ = Flow behavior index (dimensionless)

    ---
    **Annular velocity (ft/sec):**  
    AV = (24.5 × Flow Rate) ÷ ((Dh² – Dp²)*60)
    - Flow Rate in gpm  
    - Dh = hole/casing ID (in)  
    - Dp = pipe OD (in)
    """)

    Ka = st.number_input("Consistency index (Ka)", min_value=0.0, value=0.5, key="ev_ka")
    Va_method = st.radio("How do you want to provide Annular Velocity (Va)?", ["Calculate from Flow Rate", "Enter directly"])
    if Va_method == "Calculate from Flow Rate":
        Q = st.number_input("Flow Rate (Q, gpm)", min_value=0.0, value=500.0, key="ev_q")
        Dh = st.number_input("Hole diameter (Dh, in)", min_value=0.0, value=8.5, key="ev_dh")
        Dp = st.number_input("Pipe diameter (Dp, in)", min_value=0.0, value=4.5, key="ev_dp")
        Va = calculate_annular_velocity(Q, Dh, Dp)
        if Va is not None:
            st.markdown(f"**Calculated Annular Velocity (Va): {Va:.2f} ft/min**")
        else:
            st.error("Invalid input for Annular Velocity. Hole diameter must be greater than pipe diameter.")
        Do = Dp
    else:
        Va = st.number_input("Annular Velocity (Va, ft/sec)", min_value=0.0, value=150.0, key="ev_va")
        Dh = st.number_input("Hole diameter (Dh, in)", min_value=0.0, value=8.5, key="ev_dh2")
        Do = st.number_input("Outer pipe diameter (Do, in)", min_value=0.0, value=4.5, key="ev_do")

    na = st.number_input("Flow behavior index (na)", min_value=0.000, value=0.700, key="ev_na")

    if Va is not None and Dh > 0 and Do >= 0:
        mu_ea = calculate_effective_viscosity(Ka, Va, Dh, Do, na)
        if mu_ea is not None:
            st.success(f"**Effective viscosity (μₑₐ): {mu_ea:.2f}**")
        else:
            st.error("Invalid input for effective viscosity calculation. Ensure Dh > Do and all values are positive.")