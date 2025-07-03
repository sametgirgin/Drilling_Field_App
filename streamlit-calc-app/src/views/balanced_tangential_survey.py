import streamlit as st
import math

def balanced_tangential_survey():
    st.markdown("<h2 style='text-align: center;'>Directional Survey – Balanced Tangential Method</h2>", unsafe_allow_html=True)
    st.markdown("""
    
    The Balanced Tangential Method improves upon the simple Tangential Method by averaging the inclination and azimuth over the survey interval, producing more accurate results, especially in curved sections of the wellbore.
    
    Why Use It?

    - More accurate than the Tangential Method (which uses only the start angle)
    - Easier to compute than Minimum Curvature
    - Assumes changes between survey points occur symmetrically, i.e., linearly over the interval         
    
    This calculator finds the North, East, and TVD components between two survey points using the Balanced Tangential Method.

    **Formulas:**  
    North = (ΔMD / 2) × [sin(I₁) × cos(Az₁) + sin(I₂) × cos(Az₂)]  
    East = (ΔMD / 2) × [sin(I₁) × sin(Az₁) + sin(I₂) × sin(Az₂)]  
    TVD = (ΔMD / 2) × [cos(I₁) + cos(I₂)]

    Where:  
    - ΔMD = MD₂ − MD₁ (measured depth interval, ft)  
    - I₁, I₂ = Inclination at upper/lower survey (degrees)  
    - Az₁, Az₂ = Azimuth at upper/lower survey (degrees)
    """)

    md1 = st.number_input("Survey 1: Measured Depth (MD₁, ft)", min_value=0.0, value=3500.0, key="bt_md1")
    inc1 = st.number_input("Survey 1: Inclination (I₁, deg)", min_value=0.0, max_value=180.0, value=15.0, key="bt_inc1")
    az1 = st.number_input("Survey 1: Azimuth (Az₁, deg)", min_value=0.0, max_value=360.0, value=20.0, key="bt_az1")

    md2 = st.number_input("Survey 2: Measured Depth (MD₂, ft)", min_value=0.0, value=3600.0, key="bt_md2")
    inc2 = st.number_input("Survey 2: Inclination (I₂, deg)", min_value=0.0, max_value=180.0, value=25.0, key="bt_inc2")
    az2 = st.number_input("Survey 2: Azimuth (Az₂, deg)", min_value=0.0, max_value=360.0, value=45.0, key="bt_az2")

    delta_md = md2 - md1
    inc1_rad = math.radians(inc1)
    inc2_rad = math.radians(inc2)
    az1_rad = math.radians(az1)
    az2_rad = math.radians(az2)

    north = (delta_md / 2) * (math.sin(inc1_rad) * math.cos(az1_rad) + math.sin(inc2_rad) * math.cos(az2_rad))
    east = (delta_md / 2) * (math.sin(inc1_rad) * math.sin(az1_rad) + math.sin(inc2_rad) * math.sin(az2_rad))
    tvd = (delta_md / 2) * (math.cos(inc1_rad) + math.cos(inc2_rad))

    #st.markdown(f"**ΔMD:** {delta_md:.2f} ft")
    st.success(f"**North:** {north:.2f} ft")
    st.success(f"**East:** {east:.2f} ft")
    st.success(f"**TVD:** {tvd:.2f} ft")