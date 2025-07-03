import streamlit as st
import math

def radius_of_curvature_survey():
    st.markdown("<h2 style='text-align: center;'>Directional Survey – Radius of Curvature Method</h2>", unsafe_allow_html=True)
    st.markdown("""

    The Radius of Curvature Method is one of the more accurate directional drilling 
    methods for calculating position changes (ΔNorth, ΔEast, ΔTVD) between survey stations. It assumes the wellbore follows the arc of a constant-radius circle segment between two survey points.

    Why Use It?
    
    - More accurate than Angle Averaging and Balanced Tangential methods
    - Suitable for moderate to high dogleg severity
    - Still simpler than the Minimum Curvature Method, though the latter is preferred in most modern applications
    
    This calculator finds the North, East, and TVD components between two survey points using the Radius of Curvature Method.

    **Formulas:**  
    North = ΔMD × (cos I₁ − cos I₂) × (sin A₂ − sin A₁) × [(180 / π)²] / [(I₂ − I₁)(A₂ − A₁)]  
    East = ΔMD × (cos I₁ − cos I₂) × (cos A₁ − cos A₂) × [(180 / π)²] / [(I₂ − I₁)(A₂ − A₁)]  
    TVD = ΔMD × (sin I₂ − sin I₁) × (180 / π) / (I₂ − I₁)

    Where:  
    - ΔMD = MD₂ − MD₁ (measured depth interval, ft)  
    - I₁, I₂ = Inclination at upper/lower survey (degrees)  
    - A₁, A₂ = Azimuth at upper/lower survey (degrees)
    """)

    md1 = st.number_input("Survey 1: Measured Depth (MD₁, ft)", min_value=0.0, value=7500.0, key="roc_md1")
    inc1 = st.number_input("Survey 1: Inclination (I₁, deg)", min_value=0.0, max_value=180.0, value=45.0, key="roc_inc1")
    az1 = st.number_input("Survey 1: Azimuth (A₁, deg)", min_value=0.0, max_value=360.0, value=130.0, key="roc_az1")

    md2 = st.number_input("Survey 2: Measured Depth (MD₂, ft)", min_value=0.0, value=7595.0, key="roc_md2")
    inc2 = st.number_input("Survey 2: Inclination (I₂, deg)", min_value=0.0, max_value=180.0, value=52.0, key="roc_inc2")
    az2 = st.number_input("Survey 2: Azimuth (A₂, deg)", min_value=0.0, max_value=360.0, value=139.0, key="roc_az2")

    delta_md = md2 - md1
    inc1_rad = math.radians(inc1)
    inc2_rad = math.radians(inc2)
    az1_rad = math.radians(az1)
    az2_rad = math.radians(az2)

    inc_diff = inc2 - inc1
    az_diff = az2 - az1

    # Avoid division by zero
    if inc_diff != 0 and az_diff != 0:
        factor = (180 / math.pi)
        factor2 = factor ** 2

        north = delta_md * (math.cos(inc1_rad) - math.cos(inc2_rad)) * (math.sin(az2_rad) - math.sin(az1_rad)) * factor2 / (inc_diff * az_diff)
        east = delta_md * (math.cos(inc1_rad) - math.cos(inc2_rad)) * (math.cos(az1_rad) - math.cos(az2_rad)) * factor2 / (inc_diff * az_diff)
        tvd = delta_md * (math.sin(inc2_rad) - math.sin(inc1_rad)) * factor / inc_diff

        #st.markdown(f"**ΔMD:** {delta_md:.2f} ft")
        st.success(f"**North:** {north:.2f} ft")
        st.success(f"**East:** {east:.2f} ft")
        st.success(f"**TVD:** {tvd:.2f} ft")
    else:
        st.error("Inclination and azimuth differences must not be zero for this method.")