import streamlit as st

def estimate_influx_type():
    st.markdown("<h2 style='text-align: center;'>Estimate Type of Influx (Kick)</h2>", unsafe_allow_html=True)
    st.markdown("""
    Influx weight = Current mud weight − ((SICP − SIDPP) ÷ (Influx height × 0.052))

    - Influx weight in ppg
    - Current mud weight in ppg
    - SICP: Shut In Casing Pressure (psi)
    - SIDPP: Shut In Drill Pipe Pressure (psi)
    - Influx height in ft
    """)

    mud_weight = st.number_input("Current mud weight (ppg)", min_value=0.0)
    sicp = st.number_input("Shut In Casing Pressure (SICP, psi)", min_value=0.0)
    sidpp = st.number_input("Shut In Drill Pipe Pressure (SIDPP, psi)", min_value=0.0)
    influx_height = st.number_input("Influx height (ft)", min_value=0.01)  # Avoid division by zero

    if st.button("Calculate", key="calculate_influx_type"):
        denominator = influx_height * 0.052
        if denominator > 0:
            influx_weight = mud_weight - ((sicp - sidpp) / denominator)
            st.success(f"**Estimated influx weight:** {influx_weight:.2f} ppg")

            # Determine likely influx type
            if 1 <= influx_weight < 3:
                influx_type = "Most likely gas influx."
            elif 3 <= influx_weight < 7:
                influx_type = "Most likely oil kick or combination of gas and oil."
            elif 7 <= influx_weight <= 9:
                influx_type = "Most likely water influx."
            else:
                influx_type = "Value out of typical range for influx type identification."

            st.info(f"**{influx_type}**")
        else:
            st.error("Influx height must be greater than zero.")