import streamlit as st

def volumetric_well_control():
    st.markdown("<h2 style='text-align: center;'>Performing Volumetric Well Control Method</h2>", unsafe_allow_html=True)
    st.markdown("""
    **Step 1 – Calculation**

    Three calculations must be determined before conducting volumetric well control:

    1. **Safety Factor (SF):**  
       The increase in bottom hole pressure allowed during gas influx migration with the well shut in.  
       - Typical values: 50–200 psi.  
       - If the initial shut-in casing pressure is close to the maximum allowable surface pressure, select a small safety factor to prevent fracturing formation.

    2. **Pressure Increment (PI):**  
       The working pressure used during volumetric well control.  
       - This is the pressure equivalent to the hydrostatic pressure of the mud bled during each step.

    3. **Mud Increment (MI):**  
       The volume of mud bled off from the annulus to reduce hydrostatic pressure by the Pressure Increment.  
       - **Formula:**  
         Mud Increment = PI × ACF ÷ (0.052 × MW)
       - MI: Mud Increment (bbl)
       - PI: Pressure Increment (psi)
       - ACF: Annular Capacity Factor (bbl/ft)
       - MW: Mud Weight (ppg)
    """)

    st.markdown("#### Calculate Mud Increment (MI)")
    pi = st.number_input("Pressure Increment (PI, psi)", min_value=0.0, value=50.0)
    acf = st.number_input("Annular Capacity Factor (ACF, bbl/ft)", min_value=0.0, value=0.1275)
    mw = st.number_input("Mud Weight (MW, ppg)", min_value=0.01, value=14.0)

    if st.button("Calculate Mud Increment (MI)"):
        mi = pi * acf / (0.052 * mw)
        st.success(f"**Mud Increment (MI): {mi:.4f} bbl**")
        
    st.markdown("""
    **Step 2 – Allow Casing Pressure To Increase To Safety Factor Plus Pressure Increment**

    After the first step is completed, the 2nd step is to wait until casing pressure increases 
    by an amount equal to Safety Factor (SF) plus Pressure Increment (PI). At this stage, 
    the bottom hole pressure will increase by surface pressure but hydrostatic pressure is still the same.

    For example, if SF is 100 psi and PI is 100 psi, we need to wait until casing pressure increase by 200 psi.
    
    
    **Step 3 – Hold Casing Pressure Constant While Mud Increment Is Bled Off**
    Since we have the overbalance in step-2, in order to keep raising casing 
    pressure due to gas migration, hydrostatic pressure must be taken out by 
    bleeding off mud volume. This step will bleed off amount of mud equal to 
    mud increment. Bleeding mud with constant casing pressure is performed to
    ensure that the bottom hole pressure is decreased by a loss of hydrostatic pressure only. Failure to keep casing pressure constant while bleeding off mud results in reduction of the bottom hole pressure. This can lead to more severe well control problem.

    Every bleed off volume (mud increment) will reduce the bottom hole 
    pressure by the amount of Pressure Increment. Once the bleed off is complete,
    the bottom hole pressure will be over balance by the safety factor.

    **Step 4 – Wait For Casing Pressure To Increase By Pressure Increment**
    At this step, we must wait to gas to migrate up until the surface casing pressure increase by Pressure Increment. When this step finishes, the bottom hole pressure will increase by the amount of Pressure Increment therefore the bottom hole pressure will be over balance by the amount of Safety Factor plug Pressure Increment.

    **Step 5 – Repeat Step 3 and Step 4 Until The Gas Migrates To Surface**
    The rest of volumetric well control is to repeat step#3 and step#4 until the gas finally migrates all the way to surface. During each step of bleeding off, the gas bubble expands and its pressure decreases. By the time, the gas reach at surface, the gas pressure will greatly reduce and its volume increases according to Boyles’ Laws.
    """)