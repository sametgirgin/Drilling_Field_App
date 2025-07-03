import streamlit as st

def hydraulic_horse_power_calculator():
    st.markdown("<h2 style='text-align: center;'>Hydraulic Horse Power (HHP) Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Hydraulic Horse Power is a measure of the energy per unit of time that is being expended 
    across the bit nozzles. It is commonly calculated by this equation, HHP=P*Q/1714, 
    where P stands for pressure in pounds per square in., Q stands for flow rate 
    in gallons per minute, and 1714 is a conversion factor necessary to yield HHP 
    in terms of horsepower. Bit manufacturers often recommend that fluid hydraulics 
    energy across the bit nozzles be in a particular HHP range, for example 2.0 to 7.0 HHP, 
    to ensure adequate bit tooth and bottom-of-hole cleaning (the minimum HHP) and to 
    avoid premature erosion of the bit itself (the maximum HHP).
    
    HHP = (P × Q) ÷ 1714

    Where:  
    - HHP = Hydraulic Horse Power  
    - P = Circulating pressure (psi)  
    - Q = Circulating rate (gpm)  
    - 1714 = Conversion factor
    """)

    P = st.number_input("Circulating pressure (P, psi)", min_value=0.0, value=3000.0, key="hhp_p")
    Q = st.number_input("Circulating rate (Q, gpm)", min_value=0.0, value=500.0, key="hhp_q")

    HHP = (P * Q) / 1714 if P > 0 and Q > 0 else 0

    st.markdown(f"**Hydraulic Horse Power (HHP): {HHP:.2f}**")