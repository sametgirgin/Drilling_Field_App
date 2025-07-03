import streamlit as st

def influx_height():
    st.markdown("<h2 style='text-align: center;'>Influx Height Calculation</h2>", unsafe_allow_html=True)

    st.markdown("""
    Influx Height refers to the vertical distance (in feet) that an undesired 
    fluid influx (kick) occupies inside the wellbore. This influx is 
    usually a result of formation fluids (gas, oil, or water) entering 
    the well when formation pressure exceeds the wellbore pressure.           
                
                
    - Annular capacity (bbl/ft) = (Hole size² - Pipe OD²) ÷ 1029.4
    - Annular volume (bbl) = Annular capacity × Length (ft)
    - Influx above BHA (bbl) = Total pit gain – Annular volume between hole and BHA
    - Height of influx (ft) = Influx above BHA (bbl) ÷ Annular capacity (bbl/ft) for DP
    - Total influx height = Height of influx + BHA length
    """)

    st.text("Enter Required Data")
    pit_gain = st.number_input("Pit gain (bbl)", min_value=0.0, value=25.0)
    hole_size = st.number_input("Hole size (inch)", min_value=0.0, value=8.5)
    bha_od = st.number_input("BHA OD (inch)", min_value=0.0, value=6.0)
    bha_length = st.number_input("BHA length (ft)", min_value=0.0, value=420.0)
    dp_od = st.number_input("Drill pipe OD (inch)", min_value=0.0, value=5.0)

    if st.button("Calculate", key="calculate_influx_height"):
        # Annular capacity between BHA and hole
        ann_cap_bha = (hole_size**2 - bha_od**2) / 1029.4
        ann_vol_bha = bha_length * ann_cap_bha

        # Influx above BHA
        influx_above_bha = pit_gain - ann_vol_bha

        # Annular capacity between DP and hole
        ann_cap_dp = (hole_size**2 - dp_od**2) / 1029.4

        # Height of influx above BHA
        if ann_cap_dp > 0:
            height_above_bha = influx_above_bha / ann_cap_dp
        else:
            height_above_bha = 0

        # Total influx height
        total_influx_height = height_above_bha + bha_length

        st.markdown(f"- Annular capacity (BHA): **{ann_cap_bha:.4f} bbl/ft**")
        st.markdown(f"- Annular volume (BHA): **{ann_vol_bha:.2f} bbl**")
        st.markdown(f"- Influx above BHA: **{influx_above_bha:.2f} bbl**")
        st.markdown(f"- Annular capacity (DP): **{ann_cap_dp:.4f} bbl/ft**")
        st.markdown(f"- Height of influx above BHA: **{height_above_bha:.2f} ft**")
        st.success(f"**Total influx height: {total_influx_height:.2f} ft**")