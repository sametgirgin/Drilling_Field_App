import streamlit as st

def ton_miles_calculator():
    st.markdown("<h2 style='text-align: center;'>Ton-Miles Calculator</h2>", unsafe_allow_html=True)

    st.markdown("""
    All types of ton-mile service should be calculated and recorded 
    in order to obtain a true picture of the total service received from 
    the rotary drilling line. There are several types of ton miles as 
    follows;

    1. Round trip ton-miles
    2. Drilling or “connection” ton-miles
    3. Coring ton-miles
    4. Ton-miles setting casing
    5. Short-trip ton-miles

    """)
    st.markdown("""
    **1. Round Trip Ton-Miles (RTTM) Calculator**
    
    This calculator estimates the ton-miles for a round trip operation.

    RTTM = [wp × BF × D × (Lp + D) + (2 × D) × (2 × Wb + (w_dc × L_dc + w_hwdp × L_hwdp + W_bha) × BF)] ÷ (5280 × 2000)

    Where:  
    - RTTM: Round Trip Ton-Miles  
    - BF: Buoyancy Factor = (65.5 − MW) ÷ 65.5  
    - wp: Weight of drill pipe (lb/ft)  
    - D: Hole measured depth (ft)  
    - Lp: Average length per stand of drill pipe (ft)  
    - Wb: Weight of traveling block (lb)  
    - w_dc: Weight of drill collar (lb/ft)  
    - L_dc: Length of drill collar (ft)  
    - w_hwdp: Weight of heavy weight drill pipe (lb/ft)  
    - L_hwdp: Length of heavy weight drill pipe (ft)  
    - W_bha: BHA weight from directional driller (lb)  
    - MW: Mud weight (ppg)
    """)

    mw = st.number_input("Mud weight (ppg)", min_value=0.0, value=10.0)
    D = st.number_input("Hole measured depth (ft)", min_value=0.0, value=5500.0)
    wp = st.number_input("Weight of drill pipe (lb/ft)", min_value=0.0, value=13.3)
    w_dc = st.number_input("Weight of drill collar (lb/ft)", min_value=0.0, value=85.0)
    L_dc = st.number_input("Length of drill collar (ft)", min_value=0.0, value=120.0)
    w_hwdp = st.number_input("Weight of HWDP (lb/ft)", min_value=0.0, value=49.0)
    L_hwdp = st.number_input("Length of HWDP (ft)", min_value=0.0, value=450.0)
    W_bha = st.number_input("BHA weight (lb)", min_value=0.0, value=8300.0)
    L_bha = st.number_input("Length of BHA (ft)", min_value=0.0, value=94.0)
    Wb = st.number_input("Weight of traveling block (lb)", min_value=0.0, value=95000.0)
    Lp = st.number_input("Average length per stand of drill pipe (ft)", min_value=0.0, value=94.0)

    BF = (65.5 - mw) / 65.5

    # Calculate RTTM
    bha_weight = (w_dc * L_dc + w_hwdp * L_hwdp + W_bha)* BF - ((L_dc + L_hwdp+ L_bha) * wp * BF)
    numerator = (wp * BF * D * (Lp + D)) + (2 * D) * (2 * Wb + bha_weight)
    RTTM = numerator / (5280 * 2000)
    st.markdown(f"**Buoyancy Factor (BF): {BF:.4f}**")
    st.markdown(f"**Weight of BHA (after buoyancy): {bha_weight:.2f} lb**")
    st.success(f"**Round Trip Ton-Miles (RTTM): {RTTM:.2f} ton-miles**")
    
    
    st.markdown("---")

    st.markdown("**2. Drilling or Connection Ton-Miles**")

    st.markdown("""
    This calculator estimates the ton-miles of work for drilling or making a connection.

    Td = 3 × (T2 − T1)

    Where:  
    - Td: Ton-miles for drilling/connection  
    - T2: Ton-miles for one round trip at last depth before coming out of hole  
    - T1: Ton-miles for one round trip at first depth where drilling started
    """)

    t2 = st.number_input("Ton-miles for trip at last depth (T2)", min_value=0.0, value=230.0)
    t1 = st.number_input("Ton-miles for trip at first depth (T1)", min_value=0.0, value=195.0)

    td = 3 * (t2 - t1)
    st.success(f"**Drilling/Connection Ton-Miles (Td): {td:.2f} ton-miles**")
    
    st.markdown("---")

    st.markdown("**3. Ton-miles for coring operation**")
    
    
    st.markdown("""
    This calculator estimates the ton-miles for a coring operation.

    Tc = 2 × (T4 − T3)

    Where:  
    - Tc: Ton-miles for coring operation  
    - T4: Ton-miles for one round trip at depth where coring operation stopped  
    - T3: Ton-miles for one round trip at depth where coring started

    """)

    t4 = st.number_input("Ton-miles at end of coring (T4)", min_value=0.0, value=200.0)
    t3 = st.number_input("Ton-miles at start of coring (T3)", min_value=0.0, value=190.0)

    tc = 2 * (t4 - t3)
    st.success(f"**Coring Operation Ton-Miles (Tc): {tc:.2f} ton-miles**")
    
    st.markdown("---")

    st.markdown("**4. Ton-Miles for Setting Casing**")
    
    st.markdown("""
    This calculator estimates the ton-miles for setting casing.

    Tc = {Wcsg × BF × D × (Lcs + D) + D × Wb} × 0.5 ÷ (5280 × 2000)

    Where:  
    - Tc: Ton-miles for setting casing  
    - Wcsg: Weight of casing (lb/ft)  
    - BF: Buoyancy Factor = (65.5 − MW) ÷ 65.5  
    - D: Depth of casing (ft)  
    - Lcs: Length of one joint of casing (ft)  
    - Wb: Weight of traveling block assembly (lb)  
    - MW: Mud weight (ppg)
    """)

    mw = st.number_input("Mud weight (MW, ppg)", min_value=0.0, value=10.0)
    wcsg = st.number_input("Weight of casing (Wcsg, lb/ft)", min_value=0.0, value=25.0)
    D = st.number_input("Depth of casing (D, ft)", min_value=0.0, value=5200.0)
    lcs = st.number_input("Length of one joint of casing (Lcs, ft)", min_value=0.0, value=42.0)
    wb = st.number_input("Weight of traveling block assembly (Wb, lb)", min_value=0.0, value=95000.0)

    BF = (65.5 - mw) / 65.5
    numerator = (wcsg * BF * D * (lcs + D) + D * wb) * 0.5
    Tc = numerator / (5280 * 2000)

    st.success(f"**Ton-Miles for Setting Casing (Tc): {Tc:.2f} ton-miles**")
    
    st.markdown("---")

    st.markdown("**5. Ton-miles while making short trip**")
    
    st.markdown("""
    This calculator estimates the ton-miles for a short trip.

    Tst = T6 − T5

    Where:  
    - Tst: Ton-miles for short trip  
    - T6: Ton-miles for one round trip at the deeper depth  
    - T5: Ton-miles for one round trip at the shallower depth
    """)

    t6 = st.number_input("Ton-miles at deeper depth (T6)", min_value=0.0, value=150.0)
    t5 = st.number_input("Ton-miles at shallower depth (T5)", min_value=0.0, value=100.0)

    tst = t6 - t5
    st.success(f"**Ton-Miles for Short Trip (Tst): {tst:.2f} ton-miles**")