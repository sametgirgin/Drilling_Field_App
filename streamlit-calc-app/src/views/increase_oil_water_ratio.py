import streamlit as st

def increase_oil_water_ratio():
    st.markdown("<h2 style='text-align: center;'>Increase Oil/Water Ratio Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
                
    The concept of increase oil water ratio is to increase oil volume in the system without any changes in water to meet new oil water ratio.

    This calculator determines the amount of oil to add to increase the oil/water ratio by increasing oil volume (water volume remains constant).

    **Inputs:**  
    - Initial mud volume (bbl)  
    - % by volume oil (from retort analysis)  
    - % by volume water (from retort analysis)  
    - Desired water ratio (e.g., 15 for 85/15)

    """)

    oil_pct = st.number_input("Oil (% by volume)", min_value=0.0, max_value=100.0, value=56.0, key="iowr_oil_pct")
    water_pct = st.number_input("Water (% by volume)", min_value=0.0, max_value=100.0, value=14.0, key="iowr_water_pct")
    solids_pct = st.number_input("Solids (% by volume)", min_value=0.0, max_value=100.0, value=100-oil_pct-water_pct, key="iowr_solids_pct")

    if abs(oil_pct + water_pct + solids_pct - 100) > 0.01:
        st.warning("Warning: The sum of oil, water, and solids percentages should be equal to 100%. Please check your inputs.")
    
    new_oil_ratio = st.number_input("Desired oil ratio (e.g., 85 for 85/15)", min_value=1.0, max_value=99.0, value=85.0, key="iowr_desired_ratio")

    original_oil_in_liquid = oil_pct * 100 / (oil_pct + water_pct)
    original_water_in_liquid = water_pct * 100 / (oil_pct + water_pct)
    
    if new_oil_ratio <= original_oil_in_liquid:
        st.warning(f"Desired oil ratio ({new_oil_ratio:.2f}%) must be greater than the original oil in liquid ({original_oil_in_liquid:.2f}%).")

    new_liquid_volume = water_pct * 100/(100-new_oil_ratio)
    oil_added_100 = new_liquid_volume - (oil_pct + water_pct)

    st.markdown(f"**Percent of Original oil in liquid:** {original_oil_in_liquid:.2f} %")
    st.markdown(f"**Percent of Original water in liquid:** {original_water_in_liquid:.2f} %")
    st.success(f"**Oil added for 100 bbl system:** {oil_added_100:.2f} bbl")
