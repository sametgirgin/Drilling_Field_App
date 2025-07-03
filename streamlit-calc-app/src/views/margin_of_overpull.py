import streamlit as st

def margin_of_overpull():
    st.markdown("<h2 style='text-align: center;'>Margin of Overpull in Drillstring Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Margin of overpull is additional tension to be applied when pulling the stuck drill string without breaking the tensile limit of the drill string. This is the difference between maximum allowable tensile load of drill string and hook load.

    There are several factors when consider about the margin of over pull as listed below;
    
    - Overall drilling conditions
    - Hole drag
    - Likelihood of getting stuck
    - Dynamic loading


    **Formulas:**
    - Buoyancy Factor (BF) = (65.5 − MW) ÷ 65.5
    - Weight of string = (Ldp × Wdp) + (Ldc × Wdc) + (Lhwdp × Whwdp) + (Lbha × Wbha)
    - Th (Hook load) = Weight of string × BF
    - Margin of Overpull = Ta − Th
    - Safety Factor (SF) = Ta ÷ Th

    Where:
    - Ta: Maximum allowable tensile strength (lb)
    - MW: Mud weight (ppg)
    - Ldp: Length of drill pipe (ft)
    - Wdp: Weight per foot of drill pipe (lb/ft)
    - Ldc: Length of drill collar (ft)
    - Wdc: Weight per foot of drill collar (lb/ft)
    - Lhwdp: Length of HWDP (ft)
    - Whwdp: Weight per foot of HWDP (lb/ft)
    - Lbha: Length of BHA (ft)
    - Wbha: Weight per foot of BHA (lb/ft)
    """)

    ta = st.number_input("Maximum allowable tensile strength, Ta (lb)", min_value=0.0, value=400000.0)
    mw = st.number_input("Mud weight (MW, ppg)", min_value=0.0, value=12.0)
    ldp = st.number_input("Length of drill pipe, Ldp (ft)", min_value=0.0, value=10000.0)
    wdp = st.number_input("Weight/ft of drill pipe, Wdp (lb/ft)", min_value=0.0, value=19.5)
    ldc = st.number_input("Length of drill collar, Ldc (ft)", min_value=0.0, value=800.0)
    wdc = st.number_input("Weight/ft of drill collar, Wdc (lb/ft)", min_value=0.0, value=50.0)
    lhwdp = st.number_input("Length of HWDP, Lhwdp (ft)", min_value=0.0, value=500.0)
    whwdp = st.number_input("Weight/ft of HWDP, Whwdp (lb/ft)", min_value=0.0, value=26.0)
    lbha = st.number_input("Length of BHA, Lbha (ft)", min_value=0.0, value=200.0)
    wbha = st.number_input("Weight/ft of BHA, Wbha (lb/ft)", min_value=0.0, value=75.0)

    bf = (65.5 - mw) / 65.5
    st.markdown(f"**Buoyancy Factor (BF): {bf:.3f}**")

    weight_string = (ldp * wdp) + (ldc * wdc) + (lhwdp * whwdp) + (lbha * wbha)
    th = weight_string * bf
    margin = ta - th
    sf = ta / th if th > 0 else 0

    st.markdown(f"**Weight of string:** {weight_string:,.0f} lb")
    st.markdown(f"**Hook load (Th):** {th:,.0f} lb")
    st.success(f"**Margin of Overpull:** {margin:,.0f} lb")
    st.success(f"**Safety Factor (SF):** {sf:.2f}")