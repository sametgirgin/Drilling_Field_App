import streamlit as st

def oil_water_mixture_density():
    st.markdown("<h2 style='text-align: center;'>Density of Oil/Water Mixture Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    This calculator determines the density of a mixed oil and water fluid.

    **Formula:**  
    (V₁)(D₁) + (V₂)(D₂) = (V₁ + V₂) × DF

    Where:  
    - V₁ = fraction of oil (e.g., 0.8 for 80%)  
    - V₂ = fraction of water (e.g., 0.2 for 20%)  
    - D₁ = density of oil (ppg)  
    - D₂ = density of water (ppg)  
    - DF = final density of mixture (ppg)

    """)

    oil_pct = st.number_input("Oil percentage (%)", min_value=0.0, max_value=100.0, value=80.0, key="owmd_oil_pct")
    water_pct = st.number_input("Water percentage (%)", min_value=0.0, max_value=100.0, value=20.0, key="owmd_water_pct")
    oil_density = st.number_input("Oil density (ppg)", min_value=0.0, value=7.0, key="owmd_oil_density")
    water_density = st.number_input("Water density (ppg)", min_value=0.0, value=8.33, key="owmd_water_density")

    v1 = oil_pct / 100
    v2 = water_pct / 100

    if (v1 + v2) > 0:
        df = (v1 * oil_density + v2 * water_density) / (v1 + v2)
        st.success(f"**Density of oil/water mixture: {df:.2f} ppg**")
    else:
        st.error("Sum of oil and water percentages must be greater than zero.")