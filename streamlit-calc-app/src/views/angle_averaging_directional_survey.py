import streamlit as st
import math

def angle_averaging_directional_survey():
    st.markdown("<h2 style='text-align: center;'>Directional Survey – Angle Averaging Method</h2>", unsafe_allow_html=True)
    st.markdown("""
                
    The Angle Averaging Method is a simple technique used in directional drilling to calculate the change in position (North, East, and True Vertical Depth – TVD) between two measured depth (MD) stations. It assumes that the inclination (I) and azimuth (Az) angles vary linearly between two survey points.

    Assumptions:
    
    - Well path between two points is approximated by a straight segment.
    - The inclination and azimuth angles are averaged between the two stations.
    - Suitable for slight doglegs (small changes in direction).
    
    ✅ When to Use:
    - Quick computations when well path curvature is low.
    - Preliminary planning or real-time estimation.
    - Easy to implement in Excel or simple software.

    ⚠️ Limitations:
    - Not accurate for large dogleg severity (rapid changes in direction).
    - Does not account for actual curvature like the Minimum Curvature Method.
    - Errors can accumulate over long intervals or in highly deviated wells.

    This calculator finds the North, East, and TVD components between two survey points using the Angle Averaging Method.

    **Formulas:**  
    ΔNorth = ΔMD × sin((I₁ + I₂) / 2) × cos((Az₁ + Az₂) / 2)  
    ΔEast = ΔMD × sin((I₁ + I₂) / 2) × sin((Az₁ + Az₂) / 2)  
    ΔTVD = ΔMD × cos((I₁ + I₂) / 2)

    Where:  
    - ΔMD = MD₂ − MD₁ (measured depth interval, ft)  
    - I₁, I₂ = Inclination at upper/lower survey (degrees)  
    - Az₁, Az₂ = Azimuth at upper/lower survey (degrees)
    """)

    md1 = st.number_input("Survey 1: Measured Depth (MD₁, ft)", min_value=0.0, value=7500.0, key="dd_md1")
    inc1 = st.number_input("Survey 1: Inclination (I₁, deg)", min_value=0.0, max_value=180.0, value=45.0, key="dd_inc1")
    az1 = st.number_input("Survey 1: Azimuth (Az₁, deg)", min_value=0.0, max_value=360.0, value=130.0, key="dd_az1")

    md2 = st.number_input("Survey 2: Measured Depth (MD₂, ft)", min_value=0.0, value=7595.0, key="dd_md2")
    inc2 = st.number_input("Survey 2: Inclination (I₂, deg)", min_value=0.0, max_value=180.0, value=52.0, key="dd_inc2")
    az2 = st.number_input("Survey 2: Azimuth (Az₂, deg)", min_value=0.0, max_value=360.0, value=139.0, key="dd_az2")

    delta_md = md2 - md1
    avg_inc_rad = math.radians((inc1 + inc2) / 2)
    avg_az_rad = math.radians((az1 + az2) / 2)

    delta_north = delta_md * math.sin(avg_inc_rad) * math.cos(avg_az_rad)
    delta_east = delta_md * math.sin(avg_inc_rad) * math.sin(avg_az_rad)
    delta_tvd = delta_md * math.cos(avg_inc_rad)

    #st.markdown(f"**ΔMD:** {delta_md:.2f} ft")
    st.success(f"**ΔNorth:** {delta_north:.2f} ft")
    st.success(f"**ΔEast:** {delta_east:.2f} ft")
    st.success(f"**ΔTVD:** {delta_tvd:.2f} ft")