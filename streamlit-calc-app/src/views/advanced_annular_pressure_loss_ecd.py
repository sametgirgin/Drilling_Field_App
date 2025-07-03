import streamlit as st
import math

def advanced_annular_pressure_loss_ecd():
    st.markdown("<h2 style='text-align: center;'>Advanced Annular Pressure Loss & ECD Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    This calculator uses rheological properties and geometry for a more accurate annular pressure loss and ECD calculation.

    **Inputs:**  
    - θ_300: Viscometer reading at 300 rpm  
    - θ_600: Viscometer reading at 600 rpm  
    - Q: Flow rate (gpm)  
    - Dh: Hole diameter (in)  
    - Dp: Drill pipe/OD (in)  
    - L: Length (ft)  
    - MW: Mud weight (ppg)  
    - TVD: True vertical depth (ft)

    **Steps:**  
    1. Determine n  
    2. Determine K  
    3. Annular velocity (v, ft/min)  
    4. Critical velocity (Vc, ft/min)  
    5. Pressure loss for laminar flow (Ps, psi)  
    6. Pressure loss for turbulent flow (Ps, psi)  
    7. Equivalent circulating density (ECD, ppg)
    """)

    mw = st.number_input("Mud weight (MW, ppg)", min_value=0.0, value=13.2, key="adv_mw")
    theta_300 = st.number_input("θ300 (Viscometer at 300 rpm)", min_value=0.0, value=47.0, key="adv_theta300")
    theta_600 = st.number_input("θ600 (Viscometer at 600 rpm)", min_value=0.0, value=80.0, key="adv_theta600")
    q = st.number_input("Flow rate (Q, gpm)", min_value=0.0, value=165.0, key="adv_q")
    dh = st.number_input("Hole diameter (Dh, in)", min_value=0.0, value=6.35, key="adv_dh")
    dp = st.number_input("Drill pipe/OD (Dp, in)", min_value=0.0, value=4.0, key="adv_dp")
    l_dp = st.number_input("Drill pipe length (L_dp, ft)", min_value=0.0, value=12276.0, key="adv_l_dp")
    dc = st.number_input("Drill collar/OD (Dc, in)", min_value=0.0, value=5.0, key="adv_dc")
    l_dc = st.number_input("Drill collar length (L_dc, ft)", min_value=0.0, value=100.0, key="adv_l_dc")
    tvd = st.number_input("True vertical depth (TVD, ft)", min_value=0.0, value=10000.0, key="adv_tvd")

    pv = theta_600 - theta_300  # Plastic Viscosity

    # Step 1: n
    if theta_300 > 0 and theta_600 > theta_300:
        n = 3.32 * math.log10(theta_600 / theta_300)
    else:
        n = 1.0
    st.markdown(f"**Flow behavior index (n):** {n:.3f}")

    # Step 2: K
    K = (theta_300) / (511 ** n)
    st.markdown(f"**Consistency index (K):** {K:.3f}")

    # Step 3: Annular velocity (v, ft/min) in dp
    annular_area_dp = (dh ** 2 - dp ** 2)
    if annular_area_dp > 0:
        v_dp = (24.5 * q) / annular_area_dp
    else:
        v_dp = 0
    st.markdown(f"**Annular velocity around drill pipe (v):** {v_dp:.2f} ft/min")
    
    # Step 3: Annular velocity (v, ft/min) in dc
    annular_area_dc = (dh ** 2 - dc ** 2)
    if annular_area_dc > 0:
        v_dc = (24.5 * q) / annular_area_dc
    else:
        v_dc = 0
    st.markdown(f"**Annular velocity around drill collar (v):** {v_dc:.2f} ft/min")

    # Step 4: Critical velocity (Vc, ft/min)-around dp
    if n > 0:
        vc_dp =((3.878e4 * K / mw) ** (1 / (2 - n)))*(((2.4 / (dh - dp)) * ((2 * n + 1) / (3 * n))) ** (n / (2 - n)))
        #vc_dp = ((3.878 * 10000 * K / mw) ** (1 /(2-n))) * (((2.4 / (dh - dp)) **((2*n+1)/(3*n)))**(n/(2-n)))
    else:
        vc_dp = 0
    st.markdown(f"**Critical velocity around drill pipe (Vc):** {vc_dp:.2f} ft/min")
    
    # Step 4: Critical velocity (Vc, ft/min) -around dc
    if n > 0:
        vc_dc =((3.878e4 * K / mw) ** (1 / (2 - n)))*(((2.4 / (dh - dc)) * ((2 * n + 1) / (3 * n))) ** (n / (2 - n)))
        #vc_dc = ((3.878*10000*K/mw) ** (1 / (2-n))) * (((2.4/(dh - dc)) **((2*n+1)/(3*n)))**(n/(2-n)))
    else:
        vc_dc = 0
    st.markdown(f"**Critical velocity around drill collar(Vc):** {vc_dc:.2f} ft/min")


    # Step 5: Pressure loss for laminar flow (Ps, psi) -- around dp
    if v_dp < vc_dp and annular_area_dp > 0:
        Ps_lam_dp = (((2.4*v_dp*(2*n+1))/((dh - dp)*3*n))**n)*((K * l_dp) / (300*(dh-dp)))
        st.markdown(f"**Pressure loss for laminar flow around drill pipe annulus (Ps):** {Ps_lam_dp:.2f} psi")
    else:
        Ps_lam_dp = None
        
    # Step 5: Pressure loss for laminar flow (Ps, psi) -- around dc
    if v_dc < vc_dc and annular_area_dc > 0:
        Ps_lam_dc = (((2.4*v_dc*(2*n+1))/((dh - dc)*3*n))**n)*((K * l_dc) / (300*(dh-dc)))
        st.markdown(f"**Pressure loss for laminar flow around drill collar annulus(Ps):** {Ps_lam_dc:.2f} psi")
    else:
        Ps_lam_dc = None

    # Step 6: Pressure loss for turbulent flow (Ps, psi) --around dp
    if v_dp >= vc_dp and annular_area_dp > 0:
        Ps_turb_dp = (7.7*(10**-5)*(mw**(0.8))*(q**(1.8))*(pv**(0.2))*l_dp)/(((dh-dp)**3)*((dh+dp)**(1.8)))
        st.markdown(f"**Pressure loss for turbulent flow around drill pipe annulus (Ps):** {Ps_turb_dp:.2f} psi")
    else:
        Ps_turb_dp= None
        
    # Step 6: Pressure loss for turbulent flow (Ps, psi) --around dc
    if v_dc >= vc_dc and annular_area_dc > 0:
        Ps_turb_dc = (7.7*(10**-5)*(mw**(0.8))*(q**(1.8))*(pv**(0.2))*l_dc)/(((dh-dc)**3)*((dh+dc)**(1.8)))
        st.markdown(f"**Pressure loss for turbulent flow around drill collar annulus (Ps):** {Ps_turb_dc:.2f} psi")
    else:
        Ps_turb_dc = None


    # Step 7: ECD
    # Use whichever pressure loss is valids
    Ps_dp = Ps_lam_dp if Ps_lam_dp is not None else (Ps_turb_dp if Ps_turb_dp is not None else 0)
    Ps_dc = Ps_lam_dc if Ps_lam_dc is not None else (Ps_turb_dc if Ps_turb_dc is not None else 0)
    annular_loss = Ps_dp + Ps_dc 
    st.markdown(f"**Total Annular Pressure loss :** {annular_loss:.1f} psi")
    if tvd > 0:
        ecd = mw + (annular_loss / (0.052 * tvd))
        st.markdown(f"**Equivalent Circulating Density (ECD):** {ecd:.2f} ppg")
    else:
        st.markdown("**Equivalent Circulating Density (ECD):** TVD must be greater than zero.")
