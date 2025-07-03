import streamlit as st

def depth_of_stuck_pipe():
    st.markdown("<h2 style='text-align: center;'>Depth of Stuck Pipe Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    Stuck pipe is one of serious situations that sometimes happen on the rig. 
    People put a lot of effort to free stuck pipe; however, when they reach 
    the point that they can not free the pipe anymore, they may need to know 
    where the stuck point is in order to plan to cut or back off drill pipe. 


    This calculator estimates the free point constant (FPC) and the depth at which the pipe is stuck.

    **Step 1: Free Point Constant (FPC)**
    - FPC = As × 2500
    - As = (OD² − ID²) × 0.7854
    - OD: Outside diameter (in)
    - ID: Inside diameter (in)

    **Step 2: Depth of Stuck Pipe**
    - Depth of stuck pipe (ft) = (Pipe stretch in inch × FPC) ÷ Pull force (klbf)
    """)

    od = st.number_input("Pipe outside diameter (OD, in)", min_value=0.0, value=3.5)
    id_ = st.number_input("Pipe inside diameter (ID, in)", min_value=0.0, value=2.992)
    stretch = st.number_input("Pipe stretch (inches)", min_value=0.0, value=20.0)
    pull_force = st.number_input("Pull force (klbf)", min_value=0.01, value=25.0)

    as_area = (od**2 - id_**2) * 0.7854
    fpc = as_area * 2500
    st.markdown(f"**Free Point Constant (FPC): {fpc:.1f}**")

    depth_stuck = (stretch * fpc) / pull_force
    st.success(f"**Depth of stuck pipe: {depth_stuck:,.0f} ft**")
    
    st.markdown("""
    ### Drill Pipe Stretch Table

| ID (in.) | Nominal Weight (lb/ft) | ID (in.) | Wall Area (sq.in.) | Stretch Constant (in/1000lb/1000ft) | Free Point Constant |
|----------|-------------------------|----------|---------------------|--------------------------------------|----------------------|
| 2-3/8    | 4.85                    | 1.995    | 1.304               | 0.30675                              | 3260.0               |
|          | 6.65                    | 1.815    | 1.843               | 0.21704                              | 4607.0               |
| 2-7/8    | 6.85                    | 2.241    | 1.812               | 0.22075                              | 4530.0               |
|          | 10.40                   | 2.125    | 2.858               | 0.13996                              | 7145.0               |
| 3-1/2    | 9.50                    | 2.992    | 2.590               | 0.15444                              | 6475.0               |
|          | 13.30                   | 2.764    | 3.621               | 0.11047                              | 9052.0               |
|          | 15.50                   | 2.602    | 4.061               | 0.09844                              | 10760.0              |
| 4.0      | 11.85                   | 3.476    | 3.077               | 0.13000                              | 7692.5               |
|          | 14.00                   | 3.340    | 3.805               | 0.10512                              | 9512.5               |
| 4-1/2    | 13.75                   | 3.958    | 3.600               | 0.11111                              | 9000.0               |
|          | 16.60                   | 3.826    | 4.038               | 0.09076                              | 11017.0              |
|          | 18.10                   | 3.754    | 4.836               | 0.08275                              | 12090.0              |
|          | 20.00                   | 3.640    | 5.498               | 0.07275                              | 13745.0              |
| 5.0      | 16.25                   | 4.408    | 4.374               | 0.09145                              | 10935.0              |
|          | 19.50                   | 4.276    | 5.275               | 0.07583                              | 13187.0              |
| 5-1/2    | 21.90                   | 4.778    | 5.828               | 0.06863                              | 14570.0              |
|          | 24.70                   | 4.670    | 6.630               | 0.06033                              | 16575.0              |
| 6-5/8    | 25.20                   | 5.965    | 6.526               | 0.06129                              | 16315.0              |
    """)