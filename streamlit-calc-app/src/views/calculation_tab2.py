import streamlit as st

def calculation_tab2():
    st.markdown("<h2 style='text-align: center;'>Maximum Initial Shut-In Casing Pressure (MISICP) Calculation</h2>", unsafe_allow_html=True)

    st.markdown("""
    The Maximum Initial Shut-In Casing Pressure (MISICP), also known 
    as the Maximum Allowable Shut-In Casing Pressure, refers to the 
    highest initial casing pressure that, if exceeded, would surpass the 
    formation strength at the casing shoe, potentially causing the formation 
    to fracture at that point.
                 
    MISICP (psi) = (LOT (ppg) – Current Mud Weight (ppg)) × 0.052 × TVD of shoe (ft)

    - LOT: Leak Off Test result (ppg)
    - Current Mud Weight: (ppg)
    - TVD of shoe: True Vertical Depth of casing shoe (ft)
    """)
    st.text("Enter Well Data")

    lot = st.number_input("Leak Off Test (LOT) (ppg)", min_value=0.0, value=15.0)
    mud_weight = st.number_input("Current Mud Weight (ppg)", min_value=0.0, value=10.0)
    shoe_tvd = st.number_input("Casing Shoe TVD (ft)", min_value=0.0, value=4200.0)

    if st.button("Calculate", key="calculate_tab3"):
        misicp = (lot - mud_weight) * 0.052 * shoe_tvd
        st.success(f"**MISICP:** {misicp:.2f} psi")

    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>Maximum Influx Height Calculation</h2>", unsafe_allow_html=True)
    st.markdown("""
    You can use the Maximum Allowable Shut-In Casing Pressure (MASICP) to determine the 
    maximum influx height that can be controlled in a well control situation.

    **Formula:**  
    Influx Height = MASICP ÷ (Current Mud Gradient − Influx Gradient)

    - Influx height in ft
    - MASICP in psi
    - Current mud gradient in psi/ft
    - Influx gradient in psi/ft
    """)

    masicp = st.number_input("Maximum Allowable Shut-In Casing Pressure (MASICP, psi)", min_value=0.0, value=900.0)
    mud_gradient = st.number_input("Current Mud Gradient (psi/ft)", min_value=0.0, value=0.55)
    influx_gradient = st.number_input("Influx Gradient (psi/ft)", min_value=0.0, value=0.13)

    if st.button("Calculate Maximum Influx Height"):
        denominator = mud_gradient - influx_gradient
        if denominator > 0:
            influx_height = masicp / denominator
            st.success(f"**Maximum Influx Height:** {influx_height:.0f} ft")
        else:
            st.error("Current mud gradient must be greater than influx gradient.")