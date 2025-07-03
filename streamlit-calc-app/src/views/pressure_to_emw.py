import streamlit as st

def pressure_to_emw():
    st.markdown("<h2 style='text-align: center;'>Convert Pressure into Equivalent Mud Weight (EMW)</h2>", unsafe_allow_html=True)
    st.markdown("""
    **Formula:**  
    Equivalent Mud Weight (ppg) = Pressure (psi) ÷ 0.052 ÷ True Vertical Depth (TVD, ft)
    """)

    pressure = st.number_input("Pressure (psi)", min_value=0.0, value=5000.0, key="emw_pressure")
    tvd = st.number_input("True Vertical Depth (TVD, ft)", min_value=0.01, value=8000.0, key="emw_tvd")

    emw = pressure / 0.052 / tvd
    st.success(f"**Equivalent Mud Weight (EMW): {emw:.2f} ppg**")