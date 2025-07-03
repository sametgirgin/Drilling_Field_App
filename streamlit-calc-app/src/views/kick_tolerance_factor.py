import streamlit as st

def kick_tolerance_factor():
    st.markdown("<h2 style='text-align: center;'>Kick Tolerance Factor Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Kick tolerance is a term that refers to the maximum amount of gas or 
    fluid that can enter the wellbore during drilling without causing a well 
    control problem. It is an important parameter for drilling engineers to 
    consider when designing the casing program and selecting the mud weight. 
    Kick tolerance depends on several factors, such as the formation pressure, 
    the mud weight, the hole geometry, the wellbore temperature, and the type of kick.

    **Kick Tolerance Factor = (Casing Shoe TVD / Well Depth TVD) × (Maximum Allowable MW − Current MW)**

    - Casing Shoe TVD: True Vertical Depth of casing shoe (ft)
    - Well Depth TVD: True Vertical Depth of well (ft)
    - Maximum Allowable MW: Maximum Allowable Mud Weight (ppg)
    - Current MW: Current Mud Weight (ppg)
    """)

    casing_shoe_tvd = st.number_input("Casing Shoe TVD (ft)", min_value=0.0, value=5000.0)
    well_depth_tvd = st.number_input("Well Depth TVD (ft)", min_value=0.01, value=11000.0)
    max_allowable_mw = st.number_input("Maximum Allowable MW (ppg)", min_value=0.0, value=12.9)
    current_mw = st.number_input("Current MW (ppg)", min_value=0.0, value=9.8)

    ktf = None
    if st.button("Calculate Kick Tolerance Factor"):
        ktf = (casing_shoe_tvd / well_depth_tvd) * (max_allowable_mw - current_mw)
        st.success(f"**Kick Tolerance Factor: {ktf:.2f} ppg**")

    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>Maximum Formation Pressure When Shut In</h2>", unsafe_allow_html=True)
    st.markdown("""
    The maximum formation pressure that can be controlled when the well is 
    shut in refers to the highest pressure at the bottom of the well that 
    can be safely managed without risking a blowout or formation fracture 
    when the well is closed off. This value is crucial in well control 
    operations to prevent the uncontrolled release of fluids (a "kick") 
    from the formation into the wellbore.
    
    
    **Maximum formation pressure = (Kick tolerance factor + Current mud weight) × 0.052 × TVD of the well**

    - Maximum formation pressure in psi
    - Kick tolerance factor in ppg
    - Current mud weight in ppg
    - TVD of the well in ft

    This value tells you the maximum bottom hole pressure that can be controlled without breaking formation when the well is shut in.
    """)

    ktf_input = st.number_input("Kick tolerance factor (ppg)", min_value=0.0, value=1.8)
    current_mw2 = st.number_input("Current mud weight (ppg)", min_value=0.0, value=9.8)
    tvd2 = st.number_input("TVD of the well (ft)", min_value=0.0, value=9500.0)

    if st.button("Calculate Maximum Formation Pressure"):
        max_formation_pressure = (ktf_input + current_mw2) * 0.052 * tvd2
        st.success(f"**Maximum formation pressure that can be controlled when shut in: {max_formation_pressure:.0f} psi**")

    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>Maximum Surface Pressure From Kick Tolerance Factor</h2>", unsafe_allow_html=True)
    st.markdown("""
    The maximum surface pressure that can be controlled based on the kick tolerance factor is calculated as:

    **Maximum surface pressure = Kick tolerance factor × 0.052 × TVD of well**

    - Maximum surface pressure in psi
    - Kick tolerance factor in ppg
    - TVD of well in ft

    This value tells you the maximum surface pressure that can be safely managed at the surface based on your kick tolerance factor.
    """)

    ktf_surface = st.number_input("Kick tolerance factor for surface pressure (ppg)", min_value=0.0, value=1.8)
    tvd_surface = st.number_input("TVD of the well for surface pressure (ft)", min_value=0.0, value=9500.0)

    if st.button("Calculate Maximum Surface Pressure"):
        max_surface_pressure = ktf_surface * 0.052 * tvd_surface
        st.success(f"**Maximum surface pressure: {max_surface_pressure:.0f} psi**")