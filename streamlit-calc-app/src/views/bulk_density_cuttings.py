import streamlit as st

def bulk_density_cuttings():
    st.markdown("<h2 style='text-align: center;'>Bulk Density of Cuttings Using Mud Balance</h2>", unsafe_allow_html=True)
    st.markdown("""
    Wet cutting coming over shale shakers can be used to determine cutting bulk density. 
    This calculator demonstrates you how to find bulk density (specific gravity) 
    in specific gravity of cutting using mud balance method.

    **Procedure:**  
    1. Wash cuttings free of mud (use diesel oil for oil-based mud).  
    2. Set mud balance at 8.33 ppg.  
    3. Fill mud balance with cuttings until balanced with lid in place.  
    4. Remove lid, fill cup with water (cuttings included), replace lid, dry outside.  
    5. Move counterweight to obtain new balance. This value is “Rw” (resulting weight with cuttings plus water, in ppg).

    **Formula:**  
    SG = 1 ÷ (2 − (0.12 × Rw))

    Where:  
    - SG: Specific gravity (bulk density) of cuttings  
    - Rw: Resulting weight with cuttings plus water (ppg)

    """)

    rw = st.number_input("Resulting weight with cuttings plus water (Rw, ppg)", min_value=0.0, value=14.0, key="bdc_rw")
    denominator = 2 - (0.12 * rw)
    if denominator != 0:
        sg = 1 / denominator
        st.success(f"**Specific Gravity (Bulk Density) of Cuttings: {sg:.2f}**")
    else:
        st.error("Denominator is zero. Please check your Rw value.")