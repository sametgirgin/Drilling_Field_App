import streamlit as st

def coring_cost_per_foot():
    st.markdown("<h2 style='text-align: center;'>Coring Cost Per Footage Drilled Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""

    Cc = (Cb + Cs + Cr × (tt + tc + trc)) ÷ (L × Rc)

    Where:  
    - C_c: Coring cost per foot  
    - C_b: Cost of core bit (USD)  
    - C_s: Cost of coring service (USD)  
    - C_r: Rig day rate (USD/hour)  
    - t_t: Trip time (hr)  
    - t_c: Core recovering time (hr)  
    - t_rc: Core barrel handling time (hr)  
    - L: Length of core recovered (ft)  
    - R_c: Percentage of core recovery (as a decimal, e.g., 0.95 for 95%)
    """)

    cb = st.number_input("Cost of core bit (USD)", min_value=0.0, value=5000.0, key="cb")
    cs = st.number_input("Cost of coring service (USD)", min_value=0.0, value=15000.0, key="cs")
    cr = st.number_input("Rig day rate (USD/hr)", min_value=0.0, value=1000.0, key="cr")
    tt = st.number_input("Trip time (hr)", min_value=0.0, value=8.0, key="tt")
    tc = st.number_input("Core recovering time (hr)", min_value=0.0, value=6.0, key="tc")
    trc = st.number_input("Core barrel handling time (hr)", min_value=0.0, value=2.0, key="trc")
    L = st.number_input("Length of core recovered (ft)", min_value=0.01, value=100.0, key="L")
    Rc = st.number_input("Percentage of core recovery (e.g., 0.95 for 95%)", min_value=0.01, max_value=1.0, value=0.95, key="Rc")

    numerator = cb + cs + cr/24 * (tt + tc + trc)
    denominator = L * Rc
    cc = numerator / denominator

    st.success(f"**Coring cost per foot (Cc): ${cc:.2f} per ft**")