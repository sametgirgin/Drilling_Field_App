import streamlit as st

def icp_fcp():
    st.markdown("<h2 style='text-align: center;'>Determine Initial Circulating Pressure (ICP)</h2>", unsafe_allow_html=True)
    st.markdown("""
    **ICP = SCR + SIDPP**

    - ICP: Initial Circulating Pressure (psi)
    - SCR: Slow Circulating Rate Pressure (psi)
    - SIDPP: Shut In Drill Pipe Pressure (psi)
    """)

    scr = st.number_input("Slow Circulating Rate Pressure (SCR, psi)", min_value=0.0, value=1100.0)
    sidpp = st.number_input("Shut In Drill Pipe Pressure (SIDPP, psi)", min_value=0.0, value=500.0)

    if st.button("Calculate ICP"):
        icp_value = scr + sidpp
        st.success(f"**ICP (Initial Circulating Pressure): {icp_value:.2f} psi**")

    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>Determine Final Circulating Pressure (FCP)</h2>", unsafe_allow_html=True)
    st.markdown("""
    Drill string pressure required to circulate at the selected kill-rate 
    adjusted for increase in kill drilling fluid density over the original 
    drilling fluid density; used from the time kill drilling fluid reaches 
    the bottom of the drill string until kill operations are completed or a 
    change in either kill drilling fluid density or kill-rate is effected.
                
    **FCP = SCR × KWM ÷ OMW**

    - FCP: Final Circulating Pressure (psi)
    - SCR: Slow Circulating Rate Pressure (psi)
    - KWM: Kill Weight Mud (ppg)
    - OMW: Original Mud Weight (ppg)
    """)

    scr_fcp = st.number_input("Slow Circulating Rate Pressure for FCP (SCR, psi)", min_value=0.0, value=1100.0)
    kwm = st.number_input("Kill Weight Mud (KWM, ppg)", min_value=0.0, value=12.0)
    omw = st.number_input("Original Mud Weight (OMW, ppg)", min_value=0.01, value=10.0)

    if st.button("Calculate FCP"):
        fcp = scr_fcp * kwm / omw
        st.success(f"**FCP (Final Circulating Pressure): {fcp:.2f} psi**")