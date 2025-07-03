import streamlit as st

def kill_mud_weight():
    st.markdown("<h2 style='text-align: center;'>Kill Mud Weight Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    After kick has been circulated out of the well, the mud pumps can be shut down 
    and the well must be secured. While shutting down the pumps, it is a good practice 
    to gradually close the choke instead of suddenly shut in.
    You must keep in mind that while shutting down pumps, you must keep casing pressure constant 
    achieved by manipulating the choke. This procedure is to ensure that constant bottom hole 
    pressure is maintained during the shutdown.
    The shut-in casing pressure and the shut-in drill pipe pressure should be equal after complete 
    the first circulation of the driller’s method. After shutdown pumps, the Shut In Casing Pressure (SICP) and the Shut In Drill pipe Pressure (SIDP) should be equal to the initial shut-in drill pipe pressure observed at the first time. If SICP and SIDP are the same but they are more than the initial shut-in drill pipe pressure, there is possibly trapped pressure on top of SICP.

    
    Kill mud weight = Original mud weight + (Initial Shut In Drill Pipe Pressure ÷ (0.052 × TVD of the well))

    - Kill mud weight in ppg
    - Original mud weight in ppg
    - Initial Shut In Drill Pipe Pressure (SIDPP) in psi
    - TVD of the well in ft
    """)

    original_mw = st.number_input("Original mud weight (ppg)", min_value=0.0, value=10.0)
    sidpp = st.number_input("Initial Shut In Drill Pipe Pressure (SIDPP, psi)", min_value=0.0, value=300.0)
    tvd = st.number_input("TVD of the well (ft)", min_value=0.01, value=8000.0)

    if st.button("Calculate Kill Mud Weight"):
        kill_mw = original_mw + (sidpp / (0.052 * tvd))
        st.success(f"**Kill mud weight: {kill_mw:.2f} ppg**")