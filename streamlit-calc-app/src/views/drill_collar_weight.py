import streamlit as st
import math

def drill_collar_weight():
    st.markdown("<h2 style='text-align: center;'>Drill Collar Weight Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
                
    Drill collar provides weight to the bit for drilling and keep the drill 
    string from buckling. Additionally, drill pipe should not run in 
    compression because it can get seriously damaged therefore we need to 
    know weight of drill collar that is enough to provide weight to the bit.

    The following formula is used to determine required drill collar weight to obtain a 
    desired weight on bit for a well:

    **WDC = (WOB × SF) ÷ (BF × COS(θ))**

    Where the Buoyancy Factor (BF) is calculated as:  
    **BF = (65.5 – Mud Weight in ppg) ÷ 65.5**

    - WDC: Drill collar weight in air (lb)
    - WOB: Required weight on bit (lb)
    - SF: Safety factor (e.g., 1.25 for 25%)
    - Mud Weight: in ppg
    - θ: Inclination of the well (degrees)
    """)

    wob = st.number_input("Required Weight on Bit (WOB, lb)", min_value=0.0, value=50000.0)
    sf = st.number_input("Safety Factor (SF)", min_value=1.0, value=1.25)
    mud_weight = st.number_input("Mud Weight (ppg)", min_value=0.0, value=12.0)
    inclination = st.number_input("Inclination (θ, degrees)", min_value=0.0, max_value=90.0, value=30.0)

    # Calculate Buoyancy Factor
    bf = (65.5 - mud_weight) / 65.5
    st.markdown(f"**Buoyancy Factor (BF): {bf:.3f}**")

    if st.button("Calculate Drill Collar Weight"):
        try:
            wdc = (wob * sf) / (bf * math.cos(math.radians(inclination)))
            st.success(f"**Drill Collar Weight (WDC): {wdc:,.0f} lb**")
        except Exception as e:
            st.error(f"Error in calculation: {e}")

    st.markdown("""
    Note: When calculating or referencing the drill collar weight, it's important 
    to isolate it from the total Bottom Hole Assembly (BHA) weight, which 
    includes other components like:
    
    - Mud motor
    - Stabilizer
    - Logging While Drilling (LWD) tools
    - Heavy Weight Drill Pipe (HWDP)
    """)


    