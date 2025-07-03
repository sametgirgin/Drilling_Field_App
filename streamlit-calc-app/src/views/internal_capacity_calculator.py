import streamlit as st

def internal_capacity_calculator():
    st.markdown("<h2 style='text-align: center;'>Internal Capacity Factor Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""

    Inner Capacity (bbl/ft) = (ID²) ÷ 1029.4

    Where:  
    - ID: Internal diameter (in)
    """)

    id_ = st.number_input("Internal Diameter (ID, in)", min_value=0.0, value=4.276, format ="%.3f", key="icf_id")
    inner_capacity = (id_ ** 2) / 1029.4
    st.success(f"**Inner Capacity:** {inner_capacity:.5f} bbl/ft")