import streamlit as st

def critical_rpm_calculator():
    st.markdown("<h2 style='text-align: center;'>Critical RPM Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Critical RPM refers to the rotational speed at which the natural frequency of the drill string or BHA (Bottom Hole Assembly) coincides with the frequency of rotation. When these frequencies match, resonance occurs, leading to:

    - Severe axial (bit bounce), lateral (whirl), and torsional (stick-slip) vibrations
    - Equipment fatigue (especially in the drill pipe, top drive, and MWD tools)
    - Increased likelihood of twist-off or connection failure
    
    This makes identifying and avoiding critical RPM ranges essential during drilling operations. This calculator determines the critical RPM for a drill pipe.

    **Formula:**  
    Critical RPM = 33,055 × √(OD² + ID²) ÷ (L)²

    Where:  
    - OD = drill pipe outside diameter (inches)  
    - ID = drill pipe inside diameter (inches)  
    - L = length of one joint of drill pipe (feet)
    """)

    od = st.number_input("Drill pipe outside diameter (OD, in)", min_value=0.0, value=4.0, key="critrpm_od")
    id_ = st.number_input("Drill pipe inside diameter (ID, in)", min_value=0.0, value=3.5, key="critrpm_id")
    l = st.number_input("Length of one joint (L, ft)", min_value=0.1, value=32.0, key="critrpm_l")

    if l > 0:
        critical_rpm = 33055 * ((od**2 + id_**2) ** 0.5) / (l ** 2)
        st.success(f"**Critical RPM:** {critical_rpm:.0f} RPM")
    else:
        st.error("Length (L) must be greater than zero.")
        
    st.markdown("""
    ### Warning:
    
    This is a first-order approximation based on simplified beam theory. It’s useful when high-fidelity software (like TADPRO, WellPlan, or Landmark StressCheck) isn't available.

    ⚠️ Limitations: The equation doesn't factor in:
    - Weight on bit (WOB)
    - Mud weight and damping effect
    - Eccentricity of tools
    - Borehole curvature
    - Coupling effects of drill collars/BHA stabilizers
    """)
