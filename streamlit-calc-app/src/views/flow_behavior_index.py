import streamlit as st
import math

def flow_behavior_index_calculator():
    st.markdown("<h2 style='text-align: center;'>Flow Behavior Index (n) & Consistency Factor (K) Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Many types of drilling mud are classified as non-Newtonian fluid which is the behavior between Newtonian fluid model and Bingham Plastic model. The relationship between shear rate and shear stress is defined by the power law model shown below:

    τ = K × (γ˙)ⁿ    
     
    τ = shear rate
    K = consistency factor
    γ˙= shear rate
    n = flow behavior index

    n and K can be calculated from any two value of shear rate and shear stress. The method of reading shear rate on the rig comes from a V-G meter. Typically, 600 rpm, 300 rpm and 3 rpm are obtained from every mud test and we can use those reading to determine n and K.

    This tool calculates the flow behavior index (n) and consistency factor (K) for drilling fluids.

    **Inputs:**  
    - θ300: Viscometer reading at 300 rpm  
    - θ3: Viscometer reading at 3 rpm

    **Formulas:**  
    - n = 0.5 × log₁₀(θ300 / θ3)  
    - K = 5.11 × θ300 / 511ⁿ

    - n: Flow behavior index (dimensionless)  
    - K: Consistency factor (poise)
    """)

    theta_300 = st.number_input("Viscometer Reading at 300 rpm (θ300)", min_value=0.0, value=40.0, key="fbi_300")
    theta_3 = st.number_input("Viscometer Reading at 3 rpm (θ3)", min_value=0.01, value=2.0, key="fbi_3")  # Avoid zero to prevent division error

    if theta_3 > 0:
        n = 0.5 * math.log10(theta_300 / theta_3)
        K = 5.11 * theta_300 / (511 ** n)
        st.success(f"**Flow behavior index (n): {n:.3f}**")
        st.success(f"**Consistency factor (K): {K:.3f} poise**")
    else:
        st.error("θ3 must be greater than zero.")