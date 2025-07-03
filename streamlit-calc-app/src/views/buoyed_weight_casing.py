import streamlit as st
import math

def buoyed_weight_casing():
    st.markdown("<h2 style='text-align: center;'>Buoyed Weight of Casing Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""Buoyancy Factor is the factor that is used to compensate loss of weight 
                due to immersion in drilling fluid.
                At different stage of the well, you may have different buoyed weight 
                depending on density of fluid inside and outside of the component 
                and it is not always that buoyed weight is less than air weight.""")
    
    st.markdown("#### 1. Buoyed Weight in Drilling Mud")
    st.markdown("""
    - Buoyancy Factor (BF) = 1 − MW / 65.4  
    - Buoyed weight = BF × Air Weight of Casing

    Where:  
    - MW: Mud weight (ppg)  
    - Air Weight of Casing: lb
    """)
    mw1 = st.number_input("Mud weight (MW, ppg)", min_value=0.0, value=9.5, key="mud_weight_1")
    air_weight1 = st.number_input("Air Weight of Casing (lb)", min_value=0.0, value=100000.0, key="air_weight_1")

    bf1 = 1 - mw1 / 65.4
    buoyed_weight1 = bf1 * air_weight1
    st.success(f"**Buoyancy Factor (BF): {bf1:.4f}**")
    st.success(f"**Buoyed Weight in Mud:** {buoyed_weight1:,.2f} lb")

    st.markdown("---")
    st.markdown("#### 2. Buoyed Weight during Cement Operation")
    st.markdown("""
    - Ao = π × (OD)² ÷ 4  
    - Ai = π × (ID)² ÷ 4  
    - BF_in = [Ao × (1 − ρo/65.4) − Ai × (1 − ρi/65.4)] ÷ (Ao − Ai)  
    - Buoyed weight = BF_in × Air Weight of Casing

    Where:  
    - OD: Outside diameter of casing (in)  
    - ID: Inside diameter of casing (in)  
    - ρo: Mud weight in annulus (ppg)  
    - ρi: Cement weight inside casing (ppg)  
    - Air Weight of Casing: lb
    """)
    od = st.number_input("Casing outside diameter (OD, in)", min_value=0.0, value=9.625, key="od")
    id_ = st.number_input("Casing inside diameter (ID, in)", min_value=0.0, value=8.835, key="id")
    mw = st.number_input("Mud weight (ρo, ppg)", min_value=0.0, value=9.5, key="rho_o")
    cement_weight = st.number_input("Cement weight inside casing (ρi, ppg)", min_value=0.0, value=14.0, key="rho_i")
    air_weight2 = st.number_input("Air Weight of Casing (lb) [Cement]", min_value=0.0, value=100000.0, key="air_weight_2")

    ao = math.pi * (od ** 2) / 4
    ai = math.pi * (id_ ** 2) / 4
    if ao - ai != 0:
        bf_in = (ao * (1 - mw / 65.4) - ai * (1 - cement_weight / 65.4)) / (ao - ai)
        buoyed_weight2 = bf_in * air_weight2
        #st.success(f"**Ao (sq in): {ao:.2f}**")
        #st.success(f"**Ai (sq in): {ai:.2f}**")
        st.markdown(f"**Buoyed weight of casing when cement is inside casing and drilling mud is outside casing**")
        st.success(f"**Buoyancy Factor (BF_in): {bf_in:.3f}**")
        st.success(f"**Buoyed Weight (Cement in, Mud out): {buoyed_weight2:,.2f} lb**")
        bf_out = (ao * (1 - cement_weight / 65.4) - ai * (1 - mw / 65.4)) / (ao - ai)
        buoyed_weight2 = bf_out * air_weight2
        st.markdown(f"**Buoyed weight of casing when cement is outside casing and drilling mud is inside casing**")
        st.success(f"**Buoyancy Factor (BF_out): {bf_out:.3f}**")
        st.success(f"**Buoyed Weight (Cement out, Mud in): {buoyed_weight2:,.2f} lb**")
    else:
        st.error("Ao - Ai must not be zero.")