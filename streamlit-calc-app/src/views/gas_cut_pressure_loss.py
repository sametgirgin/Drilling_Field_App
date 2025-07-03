import streamlit as st

def gas_cut_pressure_loss():
    st.markdown("<h2 style='text-align: center;'>Hydrostatic Pressure Loss Due to Gas Cut Mud</h2>", unsafe_allow_html=True)
    st.markdown("""
    When gas is mixed into your drilling mud, it lowers the mud weight, 
    leading to a decrease in hydrostatic pressure. To calculate this 
    pressure reduction, you can use the pit gain method. The hydrostatic 
    pressure loss can be determined using the following equation.

    Hydrostatic pressure decrease = (Mud gradient ÷ Annular Capacity) × Pit volume gain

    - Hydrostatic pressure decrease in psi
    - Mud gradient in psi/ft (Mud gradient = 0.052 × Mud weight)
    - Annular Capacity in bbl/ft (Annular Capacity = (Hole size² – BHA OD²) ÷ 1029.4)
    - Pit volume gain in bbl
    """)

    mud_weight = st.number_input("Mud weight (ppg)", min_value=0.0, value=13.0)
    bha_od = st.number_input("BHA diameter (inch)", min_value=0.0, value=6.0)
    hole_diameter = st.number_input("Hole diameter (inch)", min_value=0.0, value=8.5)
    pit_gain = st.number_input("Pit volume gain (bbl)", min_value=0.0, value=15.0)

    if st.button("Calculate", key="calculate_gas_cut_pressure_loss"):
        mud_gradient = 0.052 * mud_weight
        annular_capacity = (hole_diameter**2 - bha_od**2) / 1029.4

        if annular_capacity > 0:
            pressure_loss = (mud_gradient / annular_capacity) * pit_gain
            st.success(f"**Hydrostatic pressure decrease:** {pressure_loss:.2f} psi")
            st.markdown(f"- Mud gradient: **{mud_gradient:.4f} psi/ft**")
            st.markdown(f"- Annular capacity: **{annular_capacity:.4f} bbl/ft**")
        else:
            st.error("Annular capacity must be greater than zero.")