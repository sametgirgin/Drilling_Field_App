import streamlit as st

def max_rop_before_fracture():
    st.markdown("<h2 style='text-align: center;'>Maximum ROP Before Fracture Formation Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    This calculator estimates the maximum rate of penetration (ROP) before the risk of fracturing the formation.

    **Formula:**  
    Max ROP = [Q × (ECD − ρ_a − ρ_m)] ÷ [d_b² × (1.414296 × 10⁻² − (6.7995 × 10⁻⁴ × (ECD − ρ_a)))]

    - ECD: Equivalent Circulating Density (ppg, use Fracture Gradient from LOT)
    - ρ_m: Mud density (ppg)
    - ρ_a: Annular pressure loss (ppg)
    - Q: Flow rate (gpm)
    - d_b: Bit size or hole size (in)
    """)

    ecd = st.number_input("Fracture Gradient (FG, ppg)", min_value=0.0, value=15.0)
    mud_density = st.number_input("Mud density (ρ_m, ppg)", min_value=0.0, value=12.0)
    annular_pressure_loss_psi = st.number_input("Annular pressure loss (psi)", min_value=0.0, value=300.0)
    tvd = st.number_input("True Vertical Depth (TVD, ft)", min_value=0.01, value=10000.0)
    flow_rate = st.number_input("Flow rate (Q, gpm)", min_value=0.0, value=500.0)
    bit_diameter = st.number_input("Bit size (d_b, in)", min_value=0.01, value=8.5)

    # Calculate annular pressure loss in ppg
    annular_pressure_loss_ppg = annular_pressure_loss_psi / (0.052 * tvd)
    st.markdown(f"**Annular pressure loss (ρ_a): {annular_pressure_loss_ppg:.3f} ppg**")

    denominator = bit_diameter ** 2 * (1.414296e-2 - (6.7995e-4 * (ecd - annular_pressure_loss_ppg)))
    numerator = flow_rate * (ecd - annular_pressure_loss_ppg - mud_density)

    if denominator != 0:
        max_rop = numerator / denominator
        st.success(f"**Maximum ROP before fracture: {max_rop:.2f} ft/hr**")
    else:
        st.error("Denominator is zero. Please check your input values.")