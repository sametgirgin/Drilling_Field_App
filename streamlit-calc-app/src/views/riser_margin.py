import streamlit as st

def riser_margin():
    st.markdown("<h2 style='text-align: center;'>Riser Margin Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    The riser margin is the mud weight increase below the mud line to compensate 
    bottom hole pressure in case of an accidental disconnect or a failure of 
    the marine riser close to the BOP stack at the sea bed.


    ρ_rm = ((L × ρ_df) − (DW × ρ_sw) / (D − L)

    - ρ_rm: Riser margin (ppg)
    - ρ_df: Drilling fluid density equivalent to formation pressure (ppg)
    - ρ_sw: Sea water density (ppg)
    - L: Riser length from subsea BOP to rig floor (ft)
    - D: True vertical depth of the well (ft)
    - DW: Water depth (ft)
    """)

    rho_df = st.number_input("Drilling fluid density (ρ_df, ppg)", min_value=0.0, value=9.2)
    rho_sw = st.number_input("Sea water density (ρ_sw, ppg)", min_value=0.0, value=8.6)
    L = st.number_input("Riser length from BOP to rig floor (L, ft)", min_value=0.0, value=8000.0)
    D = st.number_input("True vertical depth of the well (D, ft)", min_value=0.01, value=13000.0)
    DW = st.number_input("Water depth (DW, ft)", min_value=0.0, value=8000.0)

    if st.button("Calculate Riser Margin"):
        denominator = D - L
        if denominator == 0:
            st.error("D - L cannot be zero.")
        else:
            riser_margin = ((L * rho_df) - (DW * rho_sw)) / denominator
            st.success(f"**Riser Margin: {riser_margin:.2f} ppg**")
            
    st.markdown("""
        Note: When you consider adding the riser margin, you need to make 
        sure that formation strength is sufficient. Additionally, you must 
        not add trip margin and riser margin to the system because it is way 
        over safety factor. If trip margin is higher than the riser margin, 
        you must use the trip margin.
        """)