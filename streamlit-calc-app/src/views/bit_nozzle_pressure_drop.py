import streamlit as st

def bit_nozzle_pressure_drop_calculator():
    st.markdown("<h2 style='text-align: center;'>Bit Nozzle Pressure Drop Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    The pressure drop across a bit occurs when drilling mud passes through the jet nozzles. This pressure drop is crucial for hydraulic optimization and effective hole cleaning.

    **Formula:**  
    Pb = (Q² × W) ÷ (12031 × A²)

    Where:  
    - Pb = Pressure drop across bit (psi)  
    - Q = Flow rate (gpm)  
    - W = Mud weight (ppg)  
    - A = Total flow area (in²)
    """)

    Q = st.number_input("Flow rate (Q, gpm)", min_value=0.0, value=800.0, key="bitpd_q")
    W = st.number_input("Mud weight (W, ppg)", min_value=0.0, value=9.0, key="bitpd_w")
    A = st.number_input("Total flow area (A, in²)", min_value=0.01, value=0.3728, key="bitpd_a")  # Avoid zero

    if A > 0:
        Pb = (Q ** 2 * W) / (12031 * (A ** 2))
        st.success(f"**Pressure drop across bit (Pb): {Pb:,.0f} psi**")
    else:
        st.error("Total flow area (A) must be greater than zero.")