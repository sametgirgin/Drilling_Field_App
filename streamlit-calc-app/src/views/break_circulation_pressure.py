import streamlit as st

def break_circulation_pressure():
    st.markdown("<h2 style='text-align: center;'>Pressure Required to Break Circulation</h2>", unsafe_allow_html=True)
    st.markdown("""
    This calculator estimates the pressure required to break circulation inside the drillstring and in the annulus.

    **Inside Drillstring:**  
    P_gs= (y ÷ 300 ÷ d) × L  
    - P_gs: Pressure required to break gel strength (psi)  
    - y: 10 mm gel strength of drilling fluid (lb/100 sq ft)  
    - d: Inside diameter of drill pipe (in)  
    - L: Length of drill string (ft)  
    """)
    y_ds = st.number_input("10 mm gel strength (y, lb/100 sq ft) [Drillstring]", min_value=0.0, value=10.0, key="y_ds")
    d_ds = st.number_input("Drill pipe inside diameter (d, in)", min_value=0.01, value=4.276, key="d_ds")
    L_ds = st.number_input("Length of drill string (L, ft) [Drillstring]", min_value=0.0, value=10000.0, key="L_ds")

    if st.button("Calculate Drillstring Break Circulation Pressure"):
        pgs_inside = (y_ds / 300 / d_ds) * L_ds
        st.success(f"**Pressure required to break circulation inside drillstring:** {pgs_inside:.2f} psi")

    st.markdown("---")

    st.markdown("""
    **Inside Annulus:**  

    P_gs = y ÷ [300 × (Dh − Dp)] × L  
    - P_gs: Pressure required to break gel strength (psi)  
    - y: 10 mm gel strength of drilling fluid (lb/100 sq ft)  
    - Dh: Hole diameter (in)  
    - Dp: Pipe diameter (in)  
    - L: Length of drill string (ft)
        """)
    y_an = st.number_input("10 mm gel strength (y, lb/100 sq ft) [Annulus]", min_value=0.0, value=10.0, key="y_an")
    Dh = st.number_input("Hole diameter (Dh, in)", min_value=0.01, value=8.5, key="Dh")
    Dp = st.number_input("Pipe outside diameter (Dp, in)", min_value=0.01, value=5.0, key="Dp")
    L_an = st.number_input("Length of drill string (L, ft) [Annulus]", min_value=0.0, value=10000.0, key="L_an")

    if st.button("Calculate Annulus Break Circulation Pressure"):
        annulus_denominator = 300 * (Dh - Dp)
        if annulus_denominator != 0:
            pgs_annulus = (y_an / annulus_denominator) * L_an
            st.success(f"**Pressure required to break circulation in annulus:** {pgs_annulus:.2f} psi")
        else:
            st.error("Hole diameter must be greater than pipe diameter for annulus calculation.")