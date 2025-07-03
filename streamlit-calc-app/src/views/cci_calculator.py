import streamlit as st
import math

def cci_calculator():
    st.markdown("<h2 style='text-align: center;'>Cutting Carrying Index (CCI) Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Hole cleaning is a critical aspect of successful drilling operations, ensuring the efficient removal of drilled rock cuttings from the wellbore. Inadequate hole cleaning can lead to significant problems, impacting drilling efficiency, safety, and cost. The Cutting Carrying Index (CCI) is a valuable tool used by drilling engineers to assess the effectiveness of hole cleaning.

    The Cutting Carrying Index (CCI) is an empirical relationship derived from real-world drilling data that provides a quantitative measure of how effectively drilling fluid is transporting cuttings out of the wellbore.

    Purpose of CCI:
    - Assess Hole Cleaning Efficiency: The primary purpose of CCI is to provide a quick and simple indicator of the quality of hole cleaning during drilling operations.
    - Prevent Downhole Problems: By identifying poor hole cleaning conditions early, engineers can take proactive measures to prevent common drilling issues such as:
        - Increased torque and drag on the drill string.
        - Pipe sticking.
        - Premature drill bit wear.
        - Wellbore instability.
        - Lost circulation.
    - Optimize Drilling Performance: Good hole cleaning contributes to:
        - Smoother drilling operations.
        - Enhanced rate of penetration (ROP).
        - Reduced non-productive time (NPT).
        - Improved wellbore integrity.
              
    This calculator determines the Cutting Carrying Index (CCI) for hole cleaning assessment.

    **Formulas:**  
    1. n = 3.322 × log₁₀[(2 × PV + YP) / (PV + YP)]  
    2. K = (511^(1−n)) × (PV + YP)  
    3. CCI = (K × AV × MW) ÷ 400,000

    Where:  
    - AV = Annular velocity (ft/min)  s
    - MW = Mud weight (ppg)  
    - PV = Plastic viscosity (cP)  
    - YP = Yield point (lb/100 ft²)

    **CCI Interpretation:**  
    - CCI ≤ 0.5: Poor hole cleaning  
    - CCI ≥ 1.0: Good hole cleaning
    """)

    mw = st.number_input("Mud Weight (MW, ppg)", min_value=0.0, value=9.2, key="cci_mw")
    av = st.number_input("Annular Velocity (AV, ft/min)", min_value=0.0, value=140.0, key="cci_av")
    pv = st.number_input("Plastic Viscosity (PV, cP)", min_value=0.0, value=17.0, key="cci_pv")
    yp = st.number_input("Yield Point (YP, lb/100 ft²)", min_value=0.0, value=15.0, key="cci_yp")

    denominator = pv + yp
    if denominator > 0:
        n = 3.322 * math.log10((2 * pv + yp) / denominator)
        K = (511 ** (1 - n)) * denominator
        cci = (K * av * mw) / 400000
        st.markdown(f"**n:** {n:.5f}")
        st.markdown(f"**K:** {K:.2f}")
        st.markdown(f"**CCI:** {cci:.2f}")

        if cci <= 0.5:
            st.error("CCI ≤ 0.5: Poor hole cleaning. Hole problems may be seen.")
        elif cci >= 1.0:
            st.success("CCI ≥ 1.0: Good hole cleaning.")
        else:
            st.warning("CCI between 0.5 and 1.0: Marginal hole cleaning.")
    else:
        st.error("PV + YP must be greater than zero.")
