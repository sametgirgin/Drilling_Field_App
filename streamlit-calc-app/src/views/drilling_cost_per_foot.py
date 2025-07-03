import streamlit as st

def drilling_cost_per_foot():
    st.markdown("<h2 style='text-align: center;'>Drilling Cost Per Foot Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Drilling cost per foot is the total drilling cost per footage drilled. 
    This value is used for evaluating drilling projects, bit performance, drilling performance, etc.
    
    CT = (B + CR × (t + T)) ÷ F

    Where:  
    - CT: Drilling cost per foot  
    - B: Bit cost ($)  
    - CR: Rig cost per hour ($/hr, including all fixed daily costs)  
    - t: Drilling time (hr)  
    - T: Round trip time (hr)  
    - F: Footage drilled (ft)

    """)

    B = st.number_input("Bit cost (B, $)", min_value=0.0, value=27000.0, key="ct_B")
    t = st.number_input("Drilling time (t, hr)", min_value=0.0, value=50.0, key="ct_t")
    CR = st.number_input("Rig cost per hour (CR, $/hr)", min_value=0.0, value=3500.0, key="ct_CR")
    T = st.number_input("Round trip time (T, hr)", min_value=0.0, value=12.0, key="ct_T")
    F = st.number_input("Footage drilled (F, ft)", min_value=0.01, value=5000.0, key="ct_F")

    CT = (B + CR * (t + T)) / F
    st.success(f"**Drilling cost per foot (CT): ${CT:.2f} per ft**")