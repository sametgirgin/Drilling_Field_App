import streamlit as st

def max_surface_pressure_calculator():
    st.markdown("<h2 style='text-align: center;'>Maximum Surface Pressure Before Drill String Is Pushed Out</h2>", unsafe_allow_html=True)
    st.markdown("""
    Bullheading is a well control technique used to pump kill fluid directly down the wellbore (typically through the annulus or tubing), against pressure, with the intent to force formation fluids back into the reservoir or into a lower formation. It’s a non-circulating method and is often employed when circulation is not possible.

    The goal is to find out how much surface pressure can be applied before the hydraulic force overcomes the weight of the drill string, which could cause the pipe to be pushed out of the well — a serious safety risk.

    Pressure = [Drill string weight in air × ((65.5 − MW) ÷ 65.5)] ÷ [0.7857 × (Bit size)²]

    Where:  
    - Drill string weight in air: lb  
    - MW: Mud weight in hole (ppg)  
    - Bit size: in
    
    """)

    ds_weight = st.number_input("Drill string weight in air (lb)", min_value=0.0, value=45000.0, key="wcp_ds_weight")
    mw = st.number_input("Mud weight in hole (ppg)", min_value=0.0, value=12.0, key="wcp_mw")
    bit_size = st.number_input("Bit size (in)", min_value=0.01, value=8.5, key="wcp_bit_size")

    bf = (65.5 - mw) / 65.5
    buoyed_weight = ds_weight * bf
    area = 0.7857 * (bit_size ** 2)
    if area > 0:
        pressure = buoyed_weight / area
        st.markdown(f"**Buoyancy factor:** {bf:.3f}")
        st.markdown(f"**Buoyed weight of drill string:** {buoyed_weight:,.2f} lb")
        st.markdown(f"**Bit area:** {area:.2f} sq in")
        st.success(f"**Maximum surface pressure:** {pressure:.0f} psi")
    else:
        st.error("Bit size must be greater than zero.")
