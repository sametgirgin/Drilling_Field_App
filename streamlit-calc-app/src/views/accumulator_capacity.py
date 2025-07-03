import streamlit as st

def accumulator_capacity_surface():
    st.markdown("<h3>Accumulator Capacity – Usable Volume per Bottle (Surface Stack)</h3>", unsafe_allow_html=True)
    st.markdown("""
    **Step 1:**  
    V₁ = (P_precharge × V_bottle) ÷ P_min_system  
    **Step 2:**  
    V₂ = (P_precharge × V_bottle) ÷ P_operating  
    **Step 3:**  
    Usable fluid volume = V₁ − V₂
    """)
    V_bottle = st.number_input("Bottle volume (gallons)", min_value=0.0, value=15.0, key="surface_bottle_vol")
    P_precharge = st.number_input("Precharge pressure (psi)", min_value=0.01, value=1000.0, key="surface_precharge")
    P_min_system = st.number_input("Minimum system pressure (psi)", min_value=0.01, value=1200.0, key="surface_min_sys")
    P_operating = st.number_input("Operating (initial) system pressure (psi)", min_value=0.01, value=3000.0, key="surface_operating")

    V1 = (P_precharge * V_bottle) / P_min_system
    V2 = (P_precharge * V_bottle) / P_operating
    usable_volume = V1 - V2

    st.markdown(f"**Step 1:** V₁ = {V1:.2f} gallons")
    st.markdown(f"**Step 2:** V₂ = {V2:.2f} gallons")
    st.success(f"**Usable fluid volume per bottle:** {usable_volume:.2f} gallons")

def accumulator_capacity_subsea():
    st.markdown("<h3>Accumulator Capacity – Usable Volume per Bottle (Subsea BOP)</h3>", unsafe_allow_html=True)
    st.markdown("""
    **Step 1:** Adjust all pressures for hydrostatic pressure of the hydraulic fluid:  
    - Subsea Pre-charge pressure = Pre-charge pressure + (Hydraulic fluid pressure gradient × Water depth)
    - Subsea Minimum system pressure = Minimum system pressure + (Hydraulic fluid pressure gradient × Water depth)
    - Subsea Operating pressure = Operating pressure + (Hydraulic fluid pressure gradient × Water depth)

    **Step 2:**  
    V₂ = Subsea Pre-charge pressure × V_bottle ÷ Subsea Minimum system pressure

    **Step 3:**  
    V₁ = Subsea Pre-charge pressure × V_bottle ÷ Subsea Operating pressure

    **Step 4:**  
    Usable volume per bottle = V₂ − V₁
    """)
    V_bottle = st.number_input("Bottle volume (gallons)", min_value=0.0, value=15.0, key="subsea_bottle_vol")
    P_precharge = st.number_input("Pre-charge pressure (psi)", min_value=0.0, value=1000.0, key="subsea_precharge")
    P_min_system = st.number_input("Minimum system pressure (psi)", min_value=0.0, value=1200.0, key="subsea_min_sys")
    P_operating = st.number_input("Operating (initial) system pressure (psi)", min_value=0.0, value=3000.0, key="subsea_operating")
    fluid_grad = st.number_input("Hydraulic fluid pressure gradient (psi/ft)", min_value=0.0, value=0.433, key="subsea_grad")
    water_depth = st.number_input("Water depth (ft)", min_value=0.0, value=5000.0, key="subsea_depth")

    subsea_precharge = P_precharge + (fluid_grad * water_depth)
    subsea_min_system = P_min_system + (fluid_grad * water_depth)
    subsea_operating = P_operating + (fluid_grad * water_depth)

    V2 = subsea_precharge * V_bottle / subsea_min_system if subsea_min_system > 0 else 0
    V1 = subsea_precharge * V_bottle / subsea_operating if subsea_operating > 0 else 0
    usable_volume = V2 - V1

    #st.markdown(f"**Subsea Pre-charge pressure:** {subsea_precharge:.2f} psi")
    #st.markdown(f"**Subsea Minimum system pressure:** {subsea_min_system:.2f} psi")
    #st.markdown(f"**Subsea Operating pressure:** {subsea_operating:.2f} psi")
    #st.markdown(f"**Step 2:** V₂ = {V2:.2f} gallons")
    #st.markdown(f"**Step 3:** V₁ = {V1:.2f} gallons")
    st.success(f"**Usable fluid volume per bottle:** {usable_volume:.2f} gallons")
    
    st.markdown("""
                
    The accumulator bottle capacity calculation for subsea Blowout Preventer (BOP) systems is based on understanding how gas compresses when hydraulic fluid enters the bottle. This principle is crucial in well control, where hydraulic systems must operate reliably at great depths.

    Conceptual Background: Subsea BOP systems use accumulators (bottles filled with nitrogen gas) to store energy in the form of compressed gas. This energy is released when hydraulic fluid is needed to activate BOP components, such as rams or annular preventers. Because nitrogen gas is compressible, it follows Boyle’s Law:
    Boyle’s Law: P_1 × V_1 = P_2 × V_2 (at constant temperature)

    This means that when pressure increases, gas volume decreases, and vice versa. This behavior allows hydraulic fluid to be stored in the bottle by compressing the gas.

    🧪 Key Definitions:
    - Pre-charge pressure: Initial nitrogen pressure in the bottle before any fluid enters (usually around 1000 psi).
    - Minimum system pressure: The minimum pressure required to operate the BOP system effectively.
    - Operating pressure: Normal working pressure for the BOP system (e.g., 3000 psi).
    - Dead volume: The volume of fluid required to reach the minimum system pressure — this fluid is not considered "usable."
    - Usable volume: The fluid that can be delivered above the minimum pressure to perform work (e.g., closing a ram).
    """)


def accumulator_capacity_tabs():
    st.markdown("<h2 style='text-align: center;'>Accumulator Capacity – Usable Volume per Bottle</h2>", unsafe_allow_html=True)
    tab = st.radio(
        "Select Stack Type",
        ["Surface Stack", "Subsea BOP"],
        horizontal=True  # This makes the radio buttons appear laterally
    )
    if tab == "Surface Stack":
        accumulator_capacity_surface()
    else:
        accumulator_capacity_subsea()
    