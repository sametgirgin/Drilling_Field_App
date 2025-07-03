import streamlit as st
import math

def max_surface_pressure():
    st.markdown("<h2 style='text-align: center;'>Maximum Surface Pressure from Gas Influx in Water Based Mud</h2>", unsafe_allow_html=True)
    st.markdown("""
    When a well is shut in due to well control operation, the casing pressure will increase due to gas migration and gas expansion. In water based mud, you can estimate the maximum surface pressure with the following formula:

    **Max surface pressure = 0.2 × √(P × V × KWM / An)**

    - Max surface pressure: Maximum surface pressure (psi)
    - P: Expected formation pressure (psi)
    - V: Pit volume gain (bbl)
    - KWM: Kill weight mud (ppg)
    - An: Annular capacity (bbl/ft)
    """)

    formation_pressure = st.number_input("Expected formation pressure, P (psi)", min_value=0.0, value=3620.0)
    pit_gain = st.number_input("Pit volume gain, V (bbl)", min_value=0.0, value=20.0)
    kill_weight_mud = st.number_input("Kill weight mud, KWM (ppg)", min_value=0.01, value=14.5)
    annular_capacity = st.number_input("Annular capacity, An (bbl/ft)", min_value=0.01, value=0.1215)

    if st.button("Calculate Maximum Surface Pressure"):
        try:
            value = (formation_pressure * pit_gain * kill_weight_mud) / annular_capacity
            if value < 0:
                st.error("Calculation under the square root resulted in a negative number. Please check your inputs.")
            else:
                max_pressure = 0.2 * math.sqrt(value)
                st.success(f"**Maximum Surface Pressure: {max_pressure:.2f} psi**")
        except Exception as e:
            st.error(f"Error in calculation: {e}")
            
        st.markdown("""
            **WARNING:**
                We can easily estimate surface pressure in water based 
                mud because gas kick is not soluble in water based mud. 
                On the other hand, with oil based mud, you will not be able 
                to use this equation because you will not see the real 
                volume of gas kick due to gas solubility in oil.
            """) 
            
            
            
            
            
            

