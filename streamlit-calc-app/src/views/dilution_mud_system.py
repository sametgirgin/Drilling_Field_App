import streamlit as st

def dilution_mud_system():
    st.markdown("<h2 style='text-align: center;'>Dilution of Mud System to Control Low Gravity Solids</h2>", unsafe_allow_html=True)
    st.markdown("""

    ## 1- Dilution by Adding Base Fluid or Water ##
    
    By adding bbl of base fluid required, dilution of mud can help control Low Gravity Solid (LGS) in mud system.
    
    This calculator determines the barrels of dilution fluid (water or base fluid) required to achieve the desired low gravity solids (LGS) in a mud system.

    **Formula:**  
    V_wm = V_m × (F_ct − F_cop) ÷ F_cop

    Where:  
    - V_wm: Barrels of dilution fluid needed  
    - V_m: Total barrels of mud in circulating system  
    - F_ct: Percent low gravity solids in system  
    - F_cop: Percent total low gravity solids desired

    """)

    vm = st.number_input("Total barrels of mud in system (Vm, bbl)", min_value=0.0, value=2000.0, key="dms_vm")
    fct = st.number_input("Percent low gravity solids in system (Fct, %)", min_value=0.0, value=7.0, key="dms_fct")
    fcop = st.number_input("Percent total low gravity solids desired (Fcop, %)", min_value=0.01, value=3.5, key="dms_fcop")

    if fcop > 0:
        vwm = vm * (fct - fcop) / fcop
        st.success(f"**Barrels of dilution fluid required: {vwm:.0f} bbl**")
    else:
        st.error("Desired LGS percent (Fcop) must be greater than zero.")
    
    st.markdown("---")
    st.markdown("""

    ## 2- Dilution by Adding Drilling Fluid ##
    
    Adding barrels of drilling fluid can help control low gravity solids (LGS) in the mud system.  
    Unlike adding base fluid, the mud added contains some LGS, so this must be accounted for in the calculation.
    
    V_wm = V_m × (F_ct − F_cop) ÷ (F_cop - F_ca

    Where:  
    - V_wm: Barrels of dilution fluid needed  
    - V_m: Total barrels of mud in circulating system  
    - F_ct: Percent low gravity solids in system  
    - F_cop: Percent total low gravity solids desired
    - F_ca: Percent low gravity solids in added mud

    """)

    vm = st.number_input("Total barrels of mud in system (Vm, bbl)", min_value=0.0, value=2000.0, key="dmsbm_vm")
    fct = st.number_input("Percent low gravity solids in system (Fct, %)", min_value=0.0, value=7.0, key="dmsbm_fct")
    fcop = st.number_input("Percent total low gravity solids desired (Fcop, %)", min_value=0.01, value=3.5, key="dmsbm_fcop")
    fca = st.number_input("Percent low gravity solids in added mud (Fca, %)", min_value=0.0, value=2.0, key="dmsbm_fca")

    denominator = fcop - fca
    if denominator > 0:
        vwm = vm * (fct - fcop) / denominator
        st.success(f"**Barrels of drilling fluid to add: {vwm:.0f} bbl**")
    else:
        st.error("Fcop (desired LGS %) must be greater than Fca (LGS % in added mud).")