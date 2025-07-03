import streamlit as st

def depth_of_washout_pipe():
    st.markdown("<h2 style='text-align: center;'>Depth of Washout Pipe Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Washout in drill string can cause big problem later such as parted drill string. When we see stand pipe pressure decrease without changing any parameters as flow rate, mud properties, etc, you may need to consider following items before you decide to pull out of hole for washout.

    1. Check surface line: You may need to close stand pipe valves or IBOP and then pressure up to see leaking in the surface. If you see pressure drop, you can fix the surface problem. Anyway you still need to test system again.

    2. Check drillstring: You may pump the same flow rate and see how your MWD tool down hole response. If y MWD tool response gets weaker signal so it means that you have washout somewhere above MWD tool. If not, you may have washout below that such as bit, mud motor, etc.
     
    This tool provides two methods to estimate the depth of a washout in the drill pipe.

    ---
    ### Method 1: Based on Pressure Increase After Plugging Material
    
    The concept of this method is to pump plugging material to plug the wash out. We will count how many strokes pump till pump pressure increases then we can calculate back where the washout is by applying internal capacity concept and pump output concept.



    Depth of washout (ft) = (Strokes × Pump output (bbl/stk)) ÷ [(D_pins²) ÷ 1029.4]

    - Strokes: Number of strokes until pressure increase
    - Pump output: bbl/stk
    - D_pin: Drill pipe inside diameter (in)
    """)

    st.markdown("##### Method 1 Input")
    strokes1 = st.number_input("Strokes until pressure increase", min_value=0.0, value=100.0, key="strokes1")
    pump_output1 = st.number_input("Pump output (bbl/stk)", min_value=0.0, value=0.005, format="%.5f", key="pump_output1")
    d_pin1 = st.number_input("Drill pipe inside diameter (in)", min_value=0.0, value=4.276, format="%.3f", key="d_pin1")
    
    dp_capacity1 = (d_pin1 ** 2) / 1029.4
    if dp_capacity1 > 0:
        depth1 = (strokes1 * pump_output1) / dp_capacity1
        st.success(f"**Drill Pipe Capacity: {dp_capacity1:.5f} ft**")
        st.success(f"**Depth of washout (Method 1): {depth1:.2f} ft**")
    else:
        st.error("Drill pipe inside diameter must be greater than zero.")

    st.markdown("---")
    st.markdown("""
    ### Method 2: Based on Material Observed at Surface
    
    The concept of this method is to pump material that can be easily observed from drill pipe pass through wash out into annulus and over the surface. We can calculate the depth of washout bases on the combination volume of internal drill pipe volume and annulus volume.
    The materials can be easily observed when it comes across the shakers are as follows: carbide, corn starch, glass beads, bright colored paint, etc.

    - Drill pipe capacity (bbl/ft) = (D<sub>pin</sub>²) ÷ 1029.4  
    - Annular capacity (bbl/ft) = (Dh² − Dp<sub>out</sub>²) ÷ 1029.4  
    - Depth of washout (ft) = (Strokes × Pump output (bbl/stk)) ÷ [Drill pipe capacity + Annular capacity]

    - D_pin: Drill pipe inside diameter (in)
    - Dh: Hole size (in)
    - Dp_out: Drill pipe outside diameter (in)
    """)

    st.markdown("##### Method 2 Input")
    strokes2 = st.number_input("Strokes until material observed at surface", min_value=0.0, value=120.0, key="strokes2")
    pump_output2 = st.number_input("Pump output (bbl/stk) [Method 2]", min_value=0.0, value=0.05, format="%.5f",key="pump_output2")
    d_pin2 = st.number_input("Drill pipe inside diameter (D_pin, in) [Method 2]", min_value=0.0, value=4.276, key="d_pin2")
    dh = st.number_input("Hole size (Dh, in)", min_value=0.0, value=8.5, key="dh")
    dp_out = st.number_input("Drill pipe outside diameter (Dp_out, in)", min_value=0.0, value=5.0, key="dp_out")
    to_shale_shaker_capacity = st.number_input("Volume from bell nipple to shale shaker (bbl)", min_value=0.0, value=0.1, key="to_shale_shaker_capacity")
    dp_capacity2 = (d_pin2 ** 2) / 1029.4
    annular_capacity = (dh ** 2 - dp_out ** 2) / 1029.4
    total_capacity = dp_capacity2 + annular_capacity

    if total_capacity > 0:
        depth2 = (strokes2 * pump_output2 -to_shale_shaker_capacity) / total_capacity
        st.success(f"**Annular Capacity: {annular_capacity:.5f} bbl/ft**")
        st.success(f"**Depth of washout (Method 2): {depth2:.2f} ft**")
    else:
        st.error("Sum of drill pipe and annular capacities must be greater than zero.")