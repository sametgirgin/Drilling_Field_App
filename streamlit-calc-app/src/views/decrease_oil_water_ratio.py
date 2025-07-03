import streamlit as st

def decrease_oil_water_ratio():
    st.markdown("<h2 style='text-align: center;'>Decrease Oil/Water Ratio Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    This calculator determines the amount of water to add to decrease the oil/water ratio by increasing water volume (oil volume remains constant).
    
    The concept of decrease oil water ratio is to increase water volume in the system without any changes in oil volume to meet new oil water ratio.
    
    **Inputs:**  
    - Initial mud volume (bbl)  
    - % by volume oil (from retort analysis)  
    - % by volume water (from retort analysis)  
    - Desired oil/water ratio (e.g., 70 for 70/30)

    **Steps:**  
    1. Calculate initial oil and water volumes.  
    2. Calculate new total liquid volume so oil is the desired % of the new system.  
    3. Water added = new total liquid volume − original liquid volume  
    4. For different total mud volumes, scale water added accordingly.
    """)

    oil_pct = st.number_input("Oil (% by volume)", min_value=0.0, max_value=100.0, value=56.0, key="owr_oil_pct")
    water_pct = st.number_input("Water (% by volume)", min_value=0.0, max_value=100.0, value=14.0, key="owr_water_pct")
    solids_pct = st.number_input("Solids (% by volume)", min_value=0.0, max_value=100.0, value=30.0, key="owr_solids_pct")
    #initial_mud_vol = st.number_input("Initial mud volume (bbl)", min_value=1.0, value=100.0, key="owr_mud_vol")

    desired_oil_ratio = st.number_input("Desired oil ratio (e.g., 70 for 70/30)", min_value=1.0, max_value=99.0, value=70.0, key="owr_desired_ratio")
    total_mud_vol = st.number_input("Total mud volume for scaling (bbl)", min_value=1.0, value=300.0, key="owr_total_mud_vol")

    # Step 1: New total liquid volume for desired oil ratio
    oil_in_liquid = oil_pct *100 / (oil_pct+ water_pct) 
    water_in_liquid = water_pct *100 / (oil_pct + water_pct)
    
    # Step 3: Water to add the system
    water_added= ((oil_pct * 100 / desired_oil_ratio)- (oil_pct+water_pct) )* (total_mud_vol / 100)

    st.markdown(f"**Percent original oil in liquid:** {oil_in_liquid:.2f} bbl")
    st.markdown(f"**Percent original water in liquid:** {water_in_liquid:.2f} bbl")
    
    st.markdown(f"**Total volume of water added into the system:** {water_added:.2f} bbl")

