import streamlit as st
import os

def yp_pv_calculator():
    st.markdown("<h2 style='text-align: center;'>Yield Point (YP) & Plastic Viscosity (PV) Calculator</h2>", unsafe_allow_html=True)
    image_path = os.path.join(os.path.dirname(__file__), '..', '..', 'images', 'PV.jpg')
    st.image(image_path, width=600)

    st.markdown("""
    Yield Point (YP) is resistance of initial flow of fluid or the stress required in order to move the fluid. It can be simply stated that the Yield Point (YP) is the attractive force among colloidal particles in drilling fluid. As per Bingham plastic model, YP is the shear stress extrapolated to a shear rate of zero.

    Yield point can be calculated by the following formula.
    - Yield Point (YP) = Reading at 300 rpm – Plastic Viscosity (PV)

    You can determine the Plastic Viscosity (PV) by this formula.
    - Plastic Viscosity (PV) = Reading at 600 rpm – Reading at 300 rpm

    - Plastic Viscosity (PV) = Reading at 600 rpm − Reading at 300 rpm  
    - Yield Point (YP) = Reading at 300 rpm − PV  
    - PV unit: cP  
    - YP unit: lb/100 ft²
    """)

    reading_600 = st.number_input("Viscometer Reading at 600 rpm", min_value=0.0, value=56.0, key="yp_pv_600")
    reading_300 = st.number_input("Viscometer Reading at 300 rpm", min_value=0.0, value=35.0, key="yp_pv_300")

    pv = reading_600 - reading_300
    yp = reading_300 - pv

    st.success(f"**Plastic Viscosity (PV): {pv:.2f} cP**")
    st.success(f"**Yield Point (YP): {yp:.2f} lb/100 ft²**")