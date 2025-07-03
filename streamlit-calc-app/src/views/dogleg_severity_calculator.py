import streamlit as st
import math

def dogleg_severity_calculator():
    st.markdown("<h2 style='text-align: center;'>Dogleg Severity (DLS) Calculator</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: left;'>Radius of Curvature Method</h3>", unsafe_allow_html=True)
    st.markdown("""
    Dogleg severity (DLS) is a normalized estimation, normally described in degrees per 100 feet or degree per 30 meters, of the overall well bore curvature between two consecutive directional surveys. Regarding a planned well path, dogleg severity may be synonymous about build and/or turn. The following formula provides dogleg severity in degrees/100 ft  based on the Radius of Curvature Method.
    
    DLS = {cos⁻¹[(cos I₁ × cos I₂) + (sin I₁ × sin I₂ × cos(Az₂ − Az₁))]} × (100 ÷ MD)

    Where:  
    - DLS: Dogleg severity (degrees/100 ft)  
    - MD: Measured Depth interval (ft)  
    - I₁, I₂: Inclination at upper/lower survey (degrees)  
    - Az₁, Az₂: Azimuth at upper/lower survey (degrees)

    **Example:**  
    Survey 1: Depth = 7500 ft, Inclination = 45°, Azimuth = 130°  
    Survey 2: Depth = 7595 ft, Inclination = 52°, Azimuth = 139°  
    DLS = 10.22°/100 ft
    """)

    md1 = st.number_input("Survey 1: Measured Depth (MD₁, ft)", min_value=0.0, value=7500.0, key="dls_md1")
    inc1 = st.number_input("Survey 1: Inclination (I₁, deg)", min_value=0.0, max_value=180.0, value=45.0, key="dls_inc1")
    az1 = st.number_input("Survey 1: Azimuth (Az₁, deg)", min_value=0.0, max_value=360.0, value=130.0, key="dls_az1")

    md2 = st.number_input("Survey 2: Measured Depth (MD₂, ft)", min_value=0.0, value=7595.0, key="dls_md2")
    inc2 = st.number_input("Survey 2: Inclination (I₂, deg)", min_value=0.0, max_value=180.0, value=52.0, key="dls_inc2")
    az2 = st.number_input("Survey 2: Azimuth (Az₂, deg)", min_value=0.0, max_value=360.0, value=139.0, key="dls_az2")

    delta_md = md2 - md1
    inc1_rad = math.radians(inc1)
    inc2_rad = math.radians(inc2)
    az1_rad = math.radians(az1)
    az2_rad = math.radians(az2)

    # DLS calculation
    cos_dls = (math.cos(inc1_rad) * math.cos(inc2_rad)) + (math.sin(inc1_rad) * math.sin(inc2_rad) * math.cos(az2_rad - az1_rad))
    # Clamp to [-1, 1] to avoid math domain error
    cos_dls = max(min(cos_dls, 1), -1)
    dls_rad = math.acos(cos_dls)
    if delta_md > 0:
        dls = math.degrees(dls_rad) * (100 / delta_md)
        st.markdown(f"**ΔMD:** {delta_md:.2f} ft")
        st.success(f"**Dogleg Severity (DLS): {dls:.2f}°/100 ft**")
    else:
        st.error("Measured Depth interval (ΔMD) must be greater than zero.")
        
    st.markdown("---")
    
    st.markdown("<h3 style='text-align: left;'>Tangential Method</h2>", unsafe_allow_html=True)
    st.markdown("""
    This calculator estimates dogleg severity (DLS) in degrees/100 ft using the Tangential Method.

    **Formula:**  
    DLS = 100 ÷ [MD × ((sin I₁ × sin I₂) × (sin Az₁ × sin Az₂ + cos Az₁ × cos Az₂) + (cos I₁ × cos I₂))]

    Where:  
    - DLS: Dogleg severity (degrees/100 ft)  
    - MD: Measured depth interval (ft)  
    - I₁, I₂: Inclination at upper/lower survey (degrees)  
    - Az₁, Az₂: Azimuth at upper/lower survey (degrees)
    """)

    md1 = st.number_input("Survey 1: Measured Depth (MD₁, ft)", min_value=0.0, value=7500.0, key="dlst_md1")
    inc1 = st.number_input("Survey 1: Inclination (I₁, deg)", min_value=0.0, max_value=180.0, value=45.0, key="dlst_inc1")
    az1 = st.number_input("Survey 1: Azimuth (Az₁, deg)", min_value=0.0, max_value=360.0, value=130.0, key="dlst_az1")

    md2 = st.number_input("Survey 2: Measured Depth (MD₂, ft)", min_value=0.0, value=7595.0, key="dlst_md2")
    inc2 = st.number_input("Survey 2: Inclination (I₂, deg)", min_value=0.0, max_value=180.0, value=52.0, key="dlst_inc2")
    az2 = st.number_input("Survey 2: Azimuth (Az₂, deg)", min_value=0.0, max_value=360.0, value=139.0, key="dlst_az2")

    delta_md = md2 - md1
    inc1_rad = math.radians(inc1)
    inc2_rad = math.radians(inc2)
    az1_rad = math.radians(az1)
    az2_rad = math.radians(az2)

    # Tangential method denominator
    denominator = delta_md * (
        (math.sin(inc1_rad) * math.sin(inc2_rad)) *
        (math.sin(az1_rad) * math.sin(az2_rad) + math.cos(az1_rad) * math.cos(az2_rad)) +
        (math.cos(inc1_rad) * math.cos(inc2_rad))
    )

    if denominator != 0:
        dls = 100 / denominator
        st.markdown(f"**ΔMD:** {delta_md:.2f} ft")
        st.success(f"**Dogleg Severity (DLS): {dls:.2f}°/100 ft**")
    else:
        st.error("Denominator is zero. Please check your input values.")