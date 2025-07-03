import streamlit as st

def mix_fluids_volume():
    st.markdown("<h2 style='text-align: center;'>Volume to Mix Different Fluids Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    #### 1- Mixing Fluids of Different Densities with Pit Space Limitation
    
    Mixing Fluids of Different Densities with Pit Space Limitation
    
    You many have different drilling fluid densities in your mud pits so you can have option to mix different fluid densities together in order to get you desired mud weight and desired volume. The concept is to weighted average volume and density of each mud component. 
    """)
    st.markdown("""
    This calculator determines the required volumes of two fluids with different densities to achieve a desired final volume and density.

    **Inputs:**  
    - V_F: Final fluid volume (bbl, gal, etc.)  
    - D_F: Final fluid density (ppg, lb/ft³, etc.)  
    - D_1: Density of fluid 1  
    - D_2: Density of fluid 2

    **Formulas:**  
    1. V₁ + V₂ = V_F  
    2. (V₁ × D₁) + (V₂ × D₂) = V_F × D_F

    **Solution:**  
    V₂ = (V_F × (D_F − D₁)) ÷ (D₂ − D₁)  
    V₁ = V_F − V₂

    """)
    d1 = st.number_input("Density of fluid 1 (D1)", min_value=0.0, value=10.0, key="mix_d1")
    d2 = st.number_input("Density of fluid 2 (D2)", min_value=0.0, value=14.0, key="mix_d2")
    df = st.number_input("Final fluid density (DF)", min_value=0.0, value=12.0, key="mix_df")
    vf = st.number_input("Final fluid volume (VF)", min_value=0.0, value=300.0, key="mix_vf")
    if d1 == d2:
        st.error("Density of fluid 1 and fluid 2 must be different.")
    elif d2 - d1 == 0:
        st.error("Cannot divide by zero. Please check your densities.")
    else:
        v2 = (vf * (df - d1)) / (d2 - d1)
        v1 = vf - v2
        if v1 < 0 or v2 < 0:
            st.error("Calculated volume is negative. Please check your input values.")
        else:
            st.success(f"**Volume of fluid 1 required:** {v1:.2f}")
            st.success(f"**Volume of fluid 2 required:** {v2:.2f}")
    
    st.markdown("---")
    
    st.markdown("""
    #### 2- Mixing Fluids of Different Densities without Pit Space Limitation
    """)
    st.markdown("""
    This calculator determines the final volume and density when mixing two fluids of different densities, **without pit space limitation**.

    **Formula:**  
    (V₁ × D₁) + (V₂ × D₂) = V_F × D_F  
    Where:  
    - V₁ = volume of fluid 1  
    - D₁ = density of fluid 1  
    - V₂ = volume of fluid 2  
    - D₂ = density of fluid 2  
    - V_F: Final fluid volume (bbl, gal, etc.)  
    - D_F: Final fluid density (ppg, lb/ft³, etc.)  

    """)
    
    d1 = st.number_input("Density of fluid 1 (D1)", min_value=0.0, value=10.0, key="mix2_d1")
    d2 = st.number_input("Density of fluid 2 (D2)", min_value=0.0, value=14.0, key="mix2_d2")
    v1 = st.number_input("Volume of fluid 1 (V1)", min_value=0.0, value=200.0, key="mix2_v1")
    v2 = st.number_input("Volume of fluid 2 (V2)", min_value=0.0, value=300.0, key="mix2_v2")

    vf = v1 + v2
    if vf > 0:
        df = (v1 * d1 + v2 * d2) / vf
        st.success(f"**Final volume (VF): {vf:.2f}**")
        st.success(f"**Final density (DF): {df:.2f}**")
    else:
        st.error("Total volume must be greater than zero.")
    
    
    