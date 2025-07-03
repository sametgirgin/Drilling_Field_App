import streamlit as st
import os

def kick_penetration():
    st.markdown("<h2 style='text-align: center;'>Kick Penetration For Stripping Operation</h2>", unsafe_allow_html=True)
    st.markdown("""
    Kick penetration is one of the most critical concerns for stripping 
    operation because a kick height will change due to change of hole 
    geometry. In this this article, we will describe about this situation.
    
    This is will be happened when the string penetrates the kick.Height 
    of influx will increase when the drillstring penetrates a kick; 
    therefore, hydrostatic pressure decreases and casing pressure increases
    in order to compensate this situation.
    
    If the casing is maintained constant while penetrating the kick, you 
    will have high chance to take more influx because of underbalance 
    situation. However, if the constant surface pressure is utilized for the stripping 
    operation, you must account for pressure increment due to height of 
    influx change. The equation below is for calculating the increase in casing pressure

    ΔCP = ΔH × (MG – KG)

    - ΔCP: Increase in casing pressure (psi)
    - ΔH: Change in length of influx (ft)
    - MG: Mud Gradient (psi/ft) (MG = 0.052 × Mud Weight)
    - KG: Kick Gradient (psi/ft)
    """)
    
    delta_h = st.number_input("Change in length of influx, ΔH (ft)", min_value=0.0, value=115.0)
    mud_weight = st.number_input("Mud weight (ppg)", min_value=0.0, value=12.0)
    kick_gradient = st.number_input("Kick gradient, KG (psi/ft)", min_value=0.0, value=0.3)

    if st.button("Calculate", key="calculate_kick_penetration"):
        mud_gradient = 0.052 * mud_weight
        delta_cp = delta_h * (mud_gradient - kick_gradient)
        st.success(f"**Increase in casing pressure (ΔCP): {delta_cp:.2f} psi**")
        st.markdown(f"- Change in influx height (ΔH): **{delta_h:.2f} ft**")
        
    image_path = os.path.join(os.path.dirname(__file__), '..', '..', 'images', 'kick_casing_pressure.jpg')

    if os.path.exists(image_path):
        st.image(image_path, width=600)
    else:
        st.warning("Image 'kick_casing_pressure.jpg' not found at the specified path.")
