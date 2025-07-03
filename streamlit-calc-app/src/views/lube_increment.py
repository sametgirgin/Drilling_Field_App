import streamlit as st

def lube_increment():
    st.markdown("<h2 style='text-align: center;'>Lube Increment Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    In some well control cases, when you will not be able to circulate kick 
    out of the well and the kick is brought up to the surface by using the 
    Volume Metric Method. 
    
    This is the time that we must perform a special well control procedure 
    called “Lubricate and Bleed”. Lubricate and bleed procedure is the 
    way to remove the gas when the circulation is impossible to conduct. 
    The basic theory is the same as Volumetric Well Control Method but 
    it is just a reverse process. Surface pressure will be replaced 
    with hydrostatic pressure by pumping drilling fluid into the wellbore. 
    The gas and drilling mud are allowed to swap the places and amount 
    of surface pressure will be bled off later.

    If you use the current mud weight to perform the lubricate and bleed 
    procedure, the well will not be killed and there is remaining surface 
    casing pressure. Only surface casing pressure will be decreased to where 
    it balances to formation pressure. In many cases, it is sometimes 
    desirable to pump heavier mud in to the wellbore and hopefully it will 
    kill the well too.
    
    The lubricate and bleed procedure is listed in the following steps:

                
    **Step 1: Calculate Annular Capacity (ACF) in bbl/ft**  
    Annular Capacity = (Dh² – Dp²) ÷ 1029.4

    - Dh: Hole size (in)
    - Dp: Drill pipe OD (in)

    **Step 2: Calculate Lube Increment (LI) in bbl**  
    LI = PI × ACF ÷ (0.052 × MW)

    - LI: Lube Increment (bbl)
    - PI: Pressure Increment (psi)
    - ACF: Annular Capacity Factor (bbl/ft)
    - MW: Mud Weight (ppg)
    
    **Step 3: Lubricate**  
    Slowly pump a desired volume into the well. The amount of volume depends 
    on well conditions and it may change during the process. Increasing 
    in surface pressure can be estimated by utilizing Boyle’s Laws (P1V1 = P1V2) 
    and every one bbl of mud pumped into the well, the gas size is reduced by one bbl.
    During lubricating, surface casing pressure will be definitely increase. 
    The amount of pressure increase will depend on the volume of gas being compressed. 
    Small pressure increase indicates large volume of gas. Additionally, Maximum Allowable 
    Surface Casing Pressure (MAASCP) will reduce because the increase in hydrostatic pressure during lubrication.
    
    **Step 4: Wait**  
    Wait for a while to allow gas and mud swapping out. Drilling mud 
    properties as mud weight and rheology affects on this step. You need 
    to be patient.
    
    **Step 5: Bleed off pressure**
    Bleeding gas from the surface until the amount of pressure is equal to 
    hydrostatic pressure of mud pumped in hole. If you know that you lubricate
    in 50 psi, only 50 psi of gas must be bled off. It is very important to 
    bleed only gas. During this process if you see mud on surface, you must stop 
    and allow gas to swap out. For instant, you plan to bleed a total of 50 psi 
    but you observe mud coming out when you bleed only 30 psi, you stop the 
    bleeding process and shut the well in. Then, you continue bleeding the remaining 20 psi later. If the mud is accidentally allowed to come out during this bleeding process, the bottom hole pressure will reduce resulting in more influx coming into the wellbore.

    **Step 6: Repeat 3-5**

    Repeat step 3 – 5 until you get the gas out of the well or the desired 
    surface casing pressure is reached. 
    
    Source: https://wellcontrol.blog/tag/lubricate-and-bleed/
    """)

    dh = st.number_input("Hole size, Dh (in)", min_value=0.0, value=6.125)
    dp = st.number_input("Drill pipe OD, Dp (in)", min_value=0.0, value=3.5)
    pi = st.number_input("Pressure Increment, PI (psi)", min_value=0.0, value=100.0)
    mw = st.number_input("Mud Weight, MW (ppg)", min_value=0.01, value=14.0)

    # Calculate Annular Capacity
    acf = (dh**2 - dp**2) / 1029.4
    st.markdown(f"**Annular Capacity (ACF): {acf:.4f} bbl/ft**")

    li = None
    if st.button("Calculate Lube Increment"):
        li = pi * acf / (0.052 * mw)
        st.success(f"**Lube Increment (LI): {li:.4f} bbl**")