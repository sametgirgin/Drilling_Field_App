import streamlit as st
import math

def minimum_curvature_survey():
    st.markdown("<h2 style='text-align: center;'>Directional Survey – Minimum Curvature Method</h2>", unsafe_allow_html=True)
    st.markdown("""
                
    The Minimum Curvature Method smooths two straight-line segments of the Balanced Tangential Method by using the Ratio Factor (RF).

    This calculator finds the North, East, and TVD components between two survey points using the Minimum Curvature Method.

    **Formulas:**  
    β = cos⁻¹[cos(I₂ − I₁) − (sin(I₁) × sin(I₂) × (1 − cos(A₂ − A₁)))]  
    RF = 2/β × tan(β/2)  
    North = (ΔMD / 2) × [sin(I₁) × cos(A₁) + sin(I₂) × cos(A₂)] × RF  
    East = (ΔMD / 2) × [sin(I₁) × sin(A₁) + sin(I₂) × sin(A₂)] × RF  
    TVD = (ΔMD / 2) × [cos(I₁) + cos(I₂)] × RF

    Where:  
    - ΔMD = MD₂ − MD₁ (measured depth interval, ft)  
    - I₁, I₂ = Inclination at upper/lower survey (degrees)  
    - A₁, A₂ = Azimuth at upper/lower survey (degrees)
    - β = dogleg angle (radians)
    - RF = Ratio Factor
    """)

    md1 = st.number_input("Survey 1: Measured Depth (MD₁, ft)", min_value=0.0, value=3500.0, key="mc_md1")
    inc1 = st.number_input("Survey 1: Inclination (I₁, deg)", min_value=0.0, max_value=180.0, value=15.0, key="mc_inc1")
    az1 = st.number_input("Survey 1: Azimuth (Az₁, deg)", min_value=0.0, max_value=360.0, value=20.0, key="mc_az1")

    md2 = st.number_input("Survey 2: Measured Depth (MD₂, ft)", min_value=0.0, value=3600.0, key="mc_md2")
    inc2 = st.number_input("Survey 2: Inclination (I₂, deg)", min_value=0.0, max_value=180.0, value=25.0, key="mc_inc2")
    az2 = st.number_input("Survey 2: Azimuth (Az₂, deg)", min_value=0.0, max_value=360.0, value=45.0, key="mc_az2")

    delta_md = md2 - md1
    inc1_rad = math.radians(inc1)
    inc2_rad = math.radians(inc2)
    az1_rad = math.radians(az1)
    az2_rad = math.radians(az2)

    # Calculate dogleg angle β
    cos_beta = math.cos(inc2_rad - inc1_rad) - (math.sin(inc1_rad) * math.sin(inc2_rad) * (1 - math.cos(az2_rad - az1_rad)))
    # Clamp cos_beta to [-1, 1] to avoid math domain error
    cos_beta = max(min(cos_beta, 1), -1)
    beta = math.acos(cos_beta)

    # Calculate Ratio Factor (RF)
    if beta != 0:
        rf = (2 / beta) * math.tan(beta / 2)
    else:
        rf = 1.0

    north = (delta_md / 2) * (math.sin(inc1_rad) * math.cos(az1_rad) + math.sin(inc2_rad) * math.cos(az2_rad)) * rf
    east = (delta_md / 2) * (math.sin(inc1_rad) * math.sin(az1_rad) + math.sin(inc2_rad) * math.sin(az2_rad)) * rf
    tvd = (delta_md / 2) * (math.cos(inc1_rad) + math.cos(inc2_rad)) * rf

    st.markdown(f"**ΔMD:** {delta_md:.2f} ft")
    st.markdown(f"**Dogleg angle (β):** {math.degrees(beta):.4f}°")
    st.markdown(f"**Ratio Factor (RF):** {rf:.6f}")
    st.success(f"**North:** {north:.2f} ft")
    st.success(f"**East:** {east:.2f} ft")
    st.success(f"**TVD:** {tvd:.2f} ft")