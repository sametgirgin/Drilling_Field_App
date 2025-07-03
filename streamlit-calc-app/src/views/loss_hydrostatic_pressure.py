import streamlit as st

def loss_hydrostatic_pressure():
    st.markdown("<h2 style='text-align: center;'>Loss of Hydrostatic Pressure When Filling Hole with Water or Lighter Mud</h2>", unsafe_allow_html=True)
    st.markdown("""
    In case of totally lost return, the annulus must be fully filled with fluid, normally water, 
    as fast as we can. Water filled in annulus causes loss of hydrostatic pressure 
    in the wellbore. This article demonstrates how to determine hydrostatic pressure 
    reduction when water or other light fluid is used to fully fill the hole.
    
    This tool calculates the loss of hydrostatic pressure and equivalent mud weight (EMW) when filling the hole with water or a lighter mud.

    **Formulas:**
    - Height of liquid added (ft) = Liquid added (bbl) ÷ Annular capacity (bbl/ft)
    - BHP decrease (psi) = (Current mud weight (ppg) − Weight of lighter liquid (ppg)) × 0.052 × Height of liquid added (ft)
    - EMW (ppg) = Current mud weight (ppg) − (BHP decrease (psi) ÷ 0.052 ÷ TVD (ft))

    **Note:** For high-angle wells, use actual TVD from survey data for more accurate results.
    """)

    mud_weight = st.number_input("Current mud weight (ppg)", min_value=0.0, value=13.0)
    liquid_added = st.number_input("Liquid added (bbl)", min_value=0.0, value=140.0)
    lighter_weight = st.number_input("Weight of lighter liquid (ppg)", min_value=0.0, value=8.6)
    annular_capacity = st.number_input("Annular capacity (bbl/ft)", min_value=0.0001, value=0.1422)
    tvd = st.number_input("Hole TVD (ft)", min_value=0.0, value=6000.0)

    height_added = liquid_added / annular_capacity
    st.markdown(f"**Height of liquid added:** {height_added:.0f} ft")

    bhp_decrease = (mud_weight - lighter_weight) * 0.052 * height_added
    st.markdown(f"**BHP decrease:** {bhp_decrease:.1f} psi")

    emw = mud_weight - (bhp_decrease / 0.052 / tvd) if tvd > 0 else 0
    st.markdown(f"**Equivalent Mud Weight (EMW) at TD:** {emw:.2f} ppg")