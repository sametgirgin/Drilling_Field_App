import streamlit as st

def hydrostatic_pressure_decrease_pooh():
    st.markdown("<h2 style='text-align: center;'>Hydrostatic Pressure Decrease When POOH</h2>", unsafe_allow_html=True)
    st.markdown("""
                
    When pulling out of hole, volume of steel will be out of hole and mud volume will replace the steel volume.  If we don’t fill hole, hydrostatic pressure will decrease.  This topic shows you how to calculate hydrostatic pressure loss while pulling out of hole without filling the wellbore.  Moreover, there is the Excel sheet for calculating pressure decrease due to pulling out of hole.

    This calculator estimates the hydrostatic pressure decrease when pulling out of hole (POOH).

    ---
    #### Step 1: Total Volume of Steel Out of Hole

    Total Volume (bbl) = Length of pipe pulled out × ((OD_p² − ID_p²) ÷ 1029.4)

    - OD_p: Drill pipe OD (in)
    - ID_p: Drill pipe ID (in)
    - Length: Pipe pulled out (ft)
    
    #### Step 2: Hydrostatic Pressure Decrease
    Hydrostatic Pressure Decrease (psi) =  
    [((OD_p² − ID_p²) ÷ 1029.4) × L_dp × 0.052 × Mud Weight] ÷ [(ID_casing² ÷ 1029.4) − ((OD_p² − ID_p²) ÷ 1029.4)]

    - L_dp: Length of pipe pulled out (ft)
    - Mud Weight: ppg
    - ID_casing: Casing ID (in)
    """)

    od_p = st.number_input("Drill pipe OD (in)", min_value=0.0, value=5.0, format="%.3f", key="pooh_od_p")
    id_p = st.number_input("Drill pipe ID (in)", min_value=0.0, value=4.276,format="%.3f", key="pooh_id_p")
    length_pulled = st.number_input("Length of pipe pulled out (ft)", min_value=0.0, value=1000.0, key="pooh_length")
    mud_weight = st.number_input("Mud weight (ppg)", min_value=0.0, value=12.0, key="pooh_mw")
    id_casing = st.number_input("Casing ID (in)", min_value=0.0, value=8.5, format="%.3f", key="pooh_id_casing")

    pipe_disp = (od_p ** 2 - id_p ** 2) / 1029.4
    total_vol_steel = length_pulled * pipe_disp


    annular_capacity = (id_casing ** 2) / 1029.4
    numerator = total_vol_steel * 0.052 * mud_weight
    denominator = annular_capacity - pipe_disp

    if denominator > 0:
        hp_decrease = numerator / denominator
        st.success(f"**Hydrostatic Pressure Decrease:** {hp_decrease:.2f} psi")
    else:
        st.error("Denominator must be greater than zero for a valid calculation.")