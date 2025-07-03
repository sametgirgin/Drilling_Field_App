import streamlit as st
import math

def d_exponent_calculator():
    st.markdown("<h2 style='text-align: center;'>D-Exponent Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    D exponent is an extrapolation of drilling parameters to get a trend while 
    drilling into over-pressured zones. Usually, mud logger will correct 
    all data, calculate d-exponent and plot the d exponent valve on the 
    curve. The d-exponent can be utilized to detect transition from normal 
    pressure regime to abnormal formation pressure. While drilling, 
    if the change of trend is observed, rig supervisors must be cautious 
    about this situation because this is one of the possible well control
    indications.

    d = log(R ÷ 60N) ÷ log(12W ÷ 1000D)

    Where:  
    - d: D-exponent (dimensionless)  
    - R: Penetration rate (ft/hr)  
    - N: Rotary speed (rpm)  
    - W: Weight on bit (kilo lb)  
    - D: Bit size (in)

    **Note:** This equation is valid for constant drilling fluid weight.
    """)

    R = st.number_input("Penetration rate (R, ft/hr)", min_value=0.01, value=50.0, key="dexp_R")
    N = st.number_input("Rotary speed (N, rpm)", min_value=0.01, value=120.0, key="dexp_N")
    W = st.number_input("Weight on bit (W, klb)", min_value=0.01, value=30.0, key="dexp_W")
    D = st.number_input("Bit size (D, in)", min_value=0.01, value=8.5, key="dexp_D")

    try:
        numerator = math.log(R / (60 * N))
        denominator = math.log((12 * W) / (1000 * D))
        d_exp = numerator / denominator
        st.success(f"**D-exponent (d): {d_exp:.2f}**")
    except Exception as e:
        st.error(f"Error in calculation: {e}")
        
    st.markdown("<h2 style='text-align: center;'>Corrected D-Exponent Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    The original “d” exponent is good for constant mud weight but in reality several drilling operations drill with various mud weights in hole due to weight up. In order to account for mud weight variation, so modification of d exponent, called “corrected d exponent”, has been made to correct for mud weight changes.


    dc = [log(R ÷ 60N) ÷ log(12W ÷ 1000D)] × (MW1 ÷ MW2)

    Where:  
    - dc: Corrected d-exponent (dimensionless)  
    - R: Penetration rate (ft/hr)  
    - N: Rotary speed (rpm)  
    - W: Weight on bit (kilo lb)  
    - D: Bit size (in)  
    - MW1: Initial mud weight (ppg)  
    - MW2: Actual mud weight (ppg)
    """)

    R = st.number_input("Penetration rate (R, ft/hr)", min_value=0.01, value=50.0, key="dc_R")
    N = st.number_input("Rotary speed (N, rpm)", min_value=0.01, value=120.0, key="dc_N")
    W = st.number_input("Weight on bit (W, klb)", min_value=0.01, value=30.0, key="dc_W")
    D = st.number_input("Bit size (D, in)", min_value=0.01, value=8.5, key="dc_D")
    MW1 = st.number_input("Initial mud weight (MW1, ppg)", min_value=0.01, value=10.0, key="dc_MW1")
    MW2 = st.number_input("Actual mud weight (MW2, ppg)", min_value=0.01, value=12.0, key="dc_MW2")

    try:
        numerator = math.log(R / (60 * N))
        denominator = math.log((12 * W) / (1000 * D))
        d_exp = numerator / denominator
        dc = d_exp * (MW1 / MW2)
        st.success(f"**Corrected D-exponent (dc): {dc:.2f}**")
    except Exception as e:
        st.error(f"Error in calculation: {e}")