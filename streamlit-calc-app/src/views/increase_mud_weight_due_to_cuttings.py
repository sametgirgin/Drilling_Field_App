import streamlit as st

def increase_mud_weight_due_to_cuttings():
    st.markdown("<h2 style='text-align: center;'>Increase in Mud Weight Due to Cuttings Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Cutting generated while drilling will increase drilling fluid density and it will finally affect equivalent 
    circulating density while drilling. 
    
    This calculator estimates the increase in effective mud weight due to drilled cuttings in the wellbore.

    **Formula:**  
    ρ_eff = [(ρ_m × Q) + (1.414296 × 10⁻² × ROP × d_b²)] ÷ [Q + (6.7995 × 10⁻⁴ × ROP × d_b²)]

    - ρ_eff: Effective mud density (ppg)
    - ρ_m>: Mud density (ppg)
    - Q: Flow rate (gpm)
    - ROP: Rate of penetration (ft/hr)
    - d_b: Bit diameter (in)
    """)

    mud_density = st.number_input("Mud density (ρm, ppg)", min_value=0.0, value=12.0)
    flow_rate = st.number_input("Flow rate (Q, gpm)", min_value=0.0, value=500.0)
    rop = st.number_input("Rate of penetration (ROP, ft/hr)", min_value=0.0, value=50.0)
    bit_diameter = st.number_input("Bit diameter (db, in)", min_value=0.0, value=8.5)

    numerator = (mud_density * flow_rate) + (1.414296e-2 * rop * bit_diameter ** 2)
    denominator = flow_rate + (6.7995e-4 * rop * bit_diameter ** 2)

    if denominator > 0:
        rho_eff = numerator / denominator
        st.success(f"**Effective Mud Density (ρeff): {rho_eff:.3f} ppg**")
    else:
        st.error("Denominator is zero or negative. Please check your input values.")