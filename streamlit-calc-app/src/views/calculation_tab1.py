import streamlit as st
import math

def calculation_tab1():
    st.markdown("<h2 style='text-align: center;'>Actual Gas Migration Rate Calculation</h2>", unsafe_allow_html=True)

    st.markdown("""
    Actual gas migration rate = Increase in casing pressure (psi/hr) ÷ Pressure gradient of drilling mud (psi/ft)

    The objective of this formula is to calculate how fast gas is migrating up the wellbore (in feet per hour) 
    by observing pressure changes after shutting in the well.
    """)

    st.text("Enter Well Data")
    initial_pressure = st.number_input("Initial shut in casing pressure (psi)", min_value=0.0)
    final_pressure = st.number_input("Shut in casing pressure after half an hour (psi)", min_value=0.0)
    mud_weight = st.number_input("Current mud weight (ppg)", min_value=0.0)
    time_interval = st.selectbox("Time interval between readings", options=["30 minutes", "60 minutes"], index=0)

    if st.button("Calculate", key="calculate_tab1"):
        # Step 2: Calculate pressure increase per hour
        pressure_increase = final_pressure - initial_pressure
        if time_interval == "30 minutes":
            pressure_increase_per_hour = pressure_increase * 2
        else:
            pressure_increase_per_hour = pressure_increase

        # Step 3: Calculate mud gradient
        mud_gradient = 0.052 * mud_weight

        # Step 4: Calculate migration rate
        if mud_gradient > 0:
            migration_rate = pressure_increase_per_hour / mud_gradient
            st.success(f"**Actual gas migration rate:** {migration_rate:.2f} ft/hr")
        else:
            st.error("Mud gradient must be greater than zero.")

        # Show intermediate results
        st.markdown(f"- Pressure increase in {time_interval}: **{pressure_increase:.2f} psi**")
        st.markdown(f"- Pressure increase per hour: **{pressure_increase_per_hour:.2f} psi/hr**")
        st.markdown(f"- Mud gradient: **{mud_gradient:.2f} psi/ft**")

        # Estimated gas migration rate (Vg) calculation
        vg = 12 * math.exp(-0.37 * mud_weight)
        st.markdown("<h3 style='text-align: center;'>An Emprical Method</h2>", unsafe_allow_html=True)
        st.markdown("""
            We can estimate the gas migration rate in a shut-in well with the following equation.
            This is an empirical equation. It may be different from the actual but it can give you good 
            idea regarding how fast the gas can migrate up hole.
            """)
        st.markdown("""
            **Vg = 12 * e^(-0.37 * Mud Weight(ppg))**
            """)
        st.info(f"**Estimated gas migration rate (Vg): {vg:.4f} ft/sec**")

# Call the function to render the tab
calculation_tab1()