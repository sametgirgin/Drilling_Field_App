import streamlit as st

def cutting_volume():
    st.markdown("<h2 style='text-align: center;'>Volume of Cutting Generated While Drilling</h2>", unsafe_allow_html=True)
    st.markdown("""
    While drilling, cuttings are generated every footage drilled and this topic will demonstrate how to determine volume of cutting entering into the wellbore.


    This calculator estimates the volume of cuttings generated while drilling.

    Vc = (1 − Ø) × D² × ROP ÷ 1029.4

    Where:  
    - Vc: Volume of cuttings (bbl/hr)  
    - Ø: Formation porosity (as a decimal, e.g., 0.20 for 20%)  
    - D: Wellbore diameter (in)  
    - ROP: Rate of penetration (ft/hr)
    """)

    porosity = st.number_input("Formation porosity (Ø, as decimal, e.g., 0.20 for 20%)", min_value=0.0, max_value=1.0, value=0.20)
    diameter = st.number_input("Wellbore diameter (D, in)", min_value=0.0, value=8.5)
    rop = st.number_input("Rate of penetration (ROP, ft/hr)", min_value=0.0, value=50.0)

    vc = (1 - porosity) * (diameter ** 2) * rop / 1029.4
    st.success(f"**Volume of cuttings generated (Vc): {vc:.2f} bbl/hr**")