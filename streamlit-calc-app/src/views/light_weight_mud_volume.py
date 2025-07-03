import streamlit as st

def light_weight_mud_volume():
    st.markdown("<h2 style='text-align: center;'>Light Weight Mud Volume Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    This calculator determines how much light weight fluid (e.g., base oil) is required to reduce the original mud weight to a new, lower mud weight.

    Light weight fluid volume (bbl) = V₁ × (W₁ − W₂) ÷ (W₂ − D_l)

    Where:  
    - V₁ = Initial mud volume (bbl)  
    - W₁ = Initial mud weight (ppg)  
    - W₂ = Final mud weight (ppg)  
    - D_l = Density of light weight fluid (ppg)
    """)

    v1 = st.number_input("Initial mud volume (V₁, bbl)", min_value=0.0, value=200.0, key="lw_v1")
    w1 = st.number_input("Initial mud weight (W₁, ppg)", min_value=0.0, value=13.8, key="lw_w1")
    w2 = st.number_input("Final mud weight (W₂, ppg)", min_value=0.0, value=10.0, key="lw_w2")
    dw = st.number_input("Density of light weight fluid (Dₗ, ppg)", min_value=0.0, value=7.2, key="lw_dw")

    denominator = w2 - dw
    if denominator != 0:
        lw_volume = v1 * (w1 - w2) / denominator
        if lw_volume < 0:
            st.error("Calculated light weight fluid volume is negative. Please check your input values.")
        else:
            st.success(f"**Light weight fluid volume required:** {lw_volume:.1f} bbl")
    else:
        st.error("Final mud weight (W₂) must not be equal to density of light weight fluid (Dₗ).")