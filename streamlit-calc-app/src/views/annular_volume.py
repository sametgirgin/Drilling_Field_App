import streamlit as st

def annular_volume():
    st.markdown("<h2 style='text-align: center;'>Annular Volume Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Annular capacity  is volume of fluid between two diameter of cylindrical 
    objects per length or length per volume. This article demonstrates 
    you how to calculate annular capacity between casing or hole and 
    drill pipe, tubing, or casing. There are several formulas as shown 
    below to calculate annular capacity depending on unit of annular 
    capacity required.

    **Annular capacity (bbl/ft):**  
    Annular capacity = (Dh² – Dp²) ÷ 1029.4

    **Annular volume (bbl):**  
    Annular volume = Annular capacity (bbl/ft) × Length of annulus (ft)

    - Dh: Hole size (in)
    - Dp: Drill pipe OD (in)
    - Length of annulus: ft

    **Example:**  
    Hole size (Dh) = 6-1/8 in  
    Drill pipe OD (Dp) = 3.5 in  
    Length of annulus = 1000 ft  
    Annular capacity = (6.125² – 3.5²) ÷ 1029.4 = 0.0245 bbl/ft  
    Annular volume = 0.0245 × 1000 = 24.5 bbl
    """)

    dh = st.number_input("Hole size, Dh (in)", min_value=0.0, value=6.125)
    dp = st.number_input("Drill pipe OD, Dp (in)", min_value=0.0, value=3.5)
    length = st.number_input("Length of annulus (ft)", min_value=0.0, value=1000.0)

    annular_capacity = (dh**2 - dp**2) / 1029.4
    annular_volume = annular_capacity * length

    st.markdown(f"**Annular capacity:** {annular_capacity:.4f} bbl/ft")
    st.markdown(f"**Annular volume:** {annular_volume:.2f} bbl")