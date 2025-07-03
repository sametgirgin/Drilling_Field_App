import streamlit as st

def annular_pressure_loss():
    st.markdown("<h2 style='text-align: center;'>Annular Pressure Loss Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    **Formula:**  
    P = [(1.4327 × 10⁻⁷) × MW × L × V²] ÷ (Dh − Dp)

    Where:  
    - P = annular pressure loss (psi)  
    - MW = mud weight (ppg)  
    - L = length of annulus (ft)  
    - V = annular velocity (ft/min)  
    - Dh = hole/casing ID (in)  
    - Dp = drill pipe/collar OD (in)

    **Annular velocity (ft/min):**  
    V = (24.5 × Q) ÷ (Dh² − Dp²)  
    Where Q = circulation rate (gpm)
    """)

    mw = st.number_input("Mud weight (MW, ppg)", min_value=0.0, value=13.0, key="apl_mw")
    length = st.number_input("Annular length (L, ft)", min_value=0.0, value=8000.0, key="apl_length")
    q = st.number_input("Circulation rate (Q, gpm)", min_value=0.0, value=320.0, key="apl_q")
    dh = st.number_input("Hole/Casing ID (Dh, in)", min_value=0.0, value=6.5, key="apl_dh")
    dp = st.number_input("Drill pipe/Collar OD (Dp, in)", min_value=0.0, value=4.0, key="apl_dp")

    dh2 = dh ** 2
    dp2 = dp ** 2
    annular_area = dh2 - dp2

    if annular_area > 0:
        v = (24.5 * q) / annular_area
        st.markdown(f"**Annular velocity (V): {v:.1f} ft/min**")
        denominator = dh - dp
        if denominator > 0:
            p = ((1.4327e-7) * mw * length * v ** 2) / denominator
            st.success(f"**Annular pressure loss (P): {p:.2f} psi**")
        else:
            st.error("Hole/Casing ID (Dh) must be greater than Drill pipe/collar OD (Dp).")
    else:
        st.error("Dh² must be greater than Dp² for a valid annular area.")