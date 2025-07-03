import streamlit as st
import math
def bottom_hole_pressure_dry_gas():
    st.markdown("<h2 style='text-align: center;'>Bottom Hole Pressure from Wellhead Pressure (Dry Gas Well)</h2>", unsafe_allow_html=True)
    st.markdown("""
    This calculator determines the bottom hole pressure (BHP) in a dry gas well, accounting for gas compressibility.

    **Main Formula:**  
    P_bh = P_wh * math.exp((S_g / R) * (H / Tav))

    Where:  
    - P_bh = bottom hole pressure (psia)  
    - P_wh = wellhead pressure (psia)  
    - H = true vertical depth (ft)  
    - Sg = specific gravity of gas  
    - Tav = average temperature (°R = °F + 460)
    - R = 53.36 ft-lb/lb-R (gas constant for API standard condition air)

    **Hydrostatic Approximation:**  
    P_bh = P_wh + (0.052 × avg gas density × TVD)

    """)

    pwh_g = st.number_input("Wellhead pressure (psig)", min_value=0.0, value=2000.0, key="bhp_pwhg")
    h = st.number_input("True vertical depth (H, ft)", min_value=0.0, value=9000.0, key="bhp_h")
    S_g = st.number_input("Gas specific gravity (Sg)", min_value=0.0, value=0.75, key="bhp_sg")
    t_f = st.number_input("Average wellbore temperature (°F)", min_value=-459.67, value=160.0, key="bhp_tf")

    # Convert to absolute pressure and Rankine
    pwh = pwh_g + 14.7
    tav = t_f + 460

    # Main dry gas well formula
    try:
        pbh = pwh * math.exp((S_g / 53.36) * (h / tav)) - 14.7  # Simplified for typical field use
    except Exception:
        pbh = 0


    st.markdown(f"**Wellhead pressure (absolute):** {pwh:.2f} psia")
    st.markdown(f"**Average temperature (Rankine):** {tav:.2f} °R")

    st.success(f"**Bottom hole pressure (dry gas formula): {pbh:.2f} psia**")

