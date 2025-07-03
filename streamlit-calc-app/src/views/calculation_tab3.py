import streamlit as st

def calculation_tab3():
    st.markdown("<h2 style='text-align: center;'>Adjusted Maximum Allowable Shut-in Casing Pressure (MASICP) Calculation</h2>", unsafe_allow_html=True)

    st.markdown("""    
    Once you drill deeper, you may increase mud weight. With new mud 
    weight, you are not able to use the MASICP calculated by the initial
    weight because higher mud weight will reduce the MASCIP. 
    The formula below demonstrates you how to adjust the MASICP 
    with new mud weight.
    
    Adjusted MASICP = Leak off pressure – [Shoe TVD × (MW2 – MW1)] × 0.052

    - Leak off pressure: pressure from leak off test (psi)
    - Shoe TVD: true vertical depth of casing shoe (ft)
    - MW2: current mud weight (ppg)
    - MW1: original mud weight (ppg)
    """)
    
    st.text("Enter Well Data")

    leak_off_pressure = st.number_input("Leak off pressure (psi)", min_value=0.0, value=1000.0)
    shoe_tvd = st.number_input("Shoe TVD (ft)", min_value=0.0, value=4500.0)
    mw2 = st.number_input("Current mud weight, MW2 (ppg)", min_value=0.0, value=12.0)
    mw1 = st.number_input("Original mud weight, MW1 (ppg)", min_value=0.0, value=9.5)

    if st.button("Calculate", key="calculate_tab2"):
        adjusted_mascip = leak_off_pressure - (shoe_tvd * (mw2 - mw1)) * 0.052
        st.success(f"**Adjusted MASICP:** {adjusted_mascip:.2f} psi")


if __name__ == "__main__":
    calculation_tab2()