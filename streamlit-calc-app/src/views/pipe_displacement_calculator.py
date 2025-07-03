import streamlit as st

def pipe_displacement_calculator():
    st.markdown("<h2 style='text-align: center;'>Pipe Displacement Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Pipe displacement, normally in bbl/ft or m3/m, is steel volume  per length of steel pipe.  
    When we either pull out of hole or trip in hole for any kind of pipes such as 
    drill pipe, casing or tubing, you should know how much fluid to displace steel volume.
    For example, when we pull out of hole, a trip sheet must be monitored all time. 
    We must know how much fluid will fill the hole each stand of drill pipe 
    pulled out. If the volume of displacement less than theoretical 
    displacement value, we may have problem due to swabbing formation into wellbore.

    Pipe Displacement (bbl/ft) = (OD² − ID²) ÷ 1029.4

    Where:  
    - OD: Outside diameter of pipe (in)  
    - ID: Inside diameter of pipe (in)
    """)

    od = st.number_input("Outside diameter (OD, in)", min_value=0.0, value=5.0, format= "%.3f", key="pipe_disp_od")
    id_ = st.number_input("Inside diameter (ID, in)", min_value=0.0, value=4.276, format= "%.3f", key="pipe_disp_id")

    displacement = (od ** 2 - id_ ** 2) / 1029.4
    st.success(f"**Pipe displacement:** {displacement:.5f} bbl/ft")