import streamlit as st

def trip_margin():
    st.markdown("<h2 style='text-align: center;'>Trip Margin Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Trip margin is an increment of drilling mud density to provide overbalance so as to compensate the swabbing effect while pulling out of hole.

    **Formula:**  
    Trip Margin = Mud Yield Point ÷ [11.7 × (Hole diameter − Drill pipe diameter)]

    - Trip Margin in ppg (pound per gallon)
    - Mud Yield Point in lb/100 sq ft
    - Hole diameter in inch
    - Drill pipe diameter in inch
    """)

    yield_point = st.number_input("Mud Yield Point (lb/100 sq ft)", min_value=0.0, value=12.0)
    hole_diameter = st.number_input("Hole diameter (in)", min_value=0.01, value=10.0)
    dp_diameter = st.number_input("Drill pipe diameter (in)", min_value=0.0, value=5.0)

    if st.button("Calculate Trip Margin"):
        denominator = 11.7 * (hole_diameter - dp_diameter)
        if denominator <= 0:
            st.error("Hole diameter must be greater than drill pipe diameter.")
        else:
            trip_margin = yield_point / denominator
            st.success(f"**Trip Margin: {trip_margin:.3f} ppg**")