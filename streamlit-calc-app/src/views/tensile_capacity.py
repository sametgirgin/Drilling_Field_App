import streamlit as st
import math
import os

def tensile_capacity():
    st.markdown("<h2 style='text-align: center;'>Tensile Capacity of Drill String Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
        ## Young’s Modulus (Modulus of Elasticity): 
        Young’s modulus (the tensile modulus or elastic modulus) is a ratio of stress and strain along the axis and we can write into the following equation.

        Young’s modulus = Stress (σ) ÷ Strain (ε) = (F x L) ÷ (∆L x A)
        Where;
        
        Stress (σ) equals to force divided by cross sectional area of the material (F/A). For our case, we will discuss about only stress in tensile because the drill pipe is almost always designed to work in a tensile condition.
        Strain (ε) is a change of material per an original length.

        F is pulling force.
        L is an original length of pipe.
        ∆L is an amount by which the length of the pipe changes.
        A is a cross sectional area of object.

        The Young’s Modulus of material represents the factor of proportional in Hook’s Law therefore it will valid under the elastic zone.  There are several units for Young’s Modulus as N/m2 (Newton), Maga Pascal (N/mm2) and Pound per Square Inch (psi).
        """)
    
    st.markdown("""
        ## Stress-Strain Curve
        A stress-strain curve is a graph derived from Stress (σ) 
        versus Strain (ε) for a sample of a material. The nature of 
        the curve varies from material to material. The following curve 
        shows a behavior of metal.
        
        Yield Point or Yield strength, is defined as the stress at which a material 
        begins to plastically deform. Before the yield point the material will deform 
        elastically and it will return to its original shape when the stress is released. 
        If the tension applied is over the yield point, the deformation will be permanent and non-reversible.
        Ultimate strength is the maximum stress applied before the material is completely parted.
        
        Young’s Modulus (modulus of elasticity) is the slope of the Stress-Strain curve within the e
        lastic limit. It means that once tensile is less than Yield Point, the Young’s 
        Modulus is valid for the calculation.
        
        In drilling operation, we must operate within Yield point because 
        the metal will become the original shape. For example, if you get 
        stuck, the maximum tension applied to free the stuck drillstring must be 
        always under yield point with a designed safety factor for the operation.
        """)
    
    image_path = os.path.join(os.path.dirname(__file__), '..', '..', 'images', 'Stress-Strain Curve.png')
    if os.path.exists(image_path):
        st.image(image_path, width=600)
    else:
        st.warning("Image 'kick_casing_pressure.jpg' not found at the specified path.")
      
    st.markdown("""
    ## Tensile Capacity of Drill Pipe
    The tensile capacity of drill pipe is the maximum tension applied before the elastic limit is reached.

    - Cross Sectional Area = π × (OD² − ID²) ÷ 4  
    - Tensile Capacity = Cross Sectional Area × Yield Strength

    - Tensile Capacity: in lb
    - Cross Sectional Area: in square inch
    - Yield Strength: in psi
    - OD: Outside diameter (in)
    - ID: Inside diameter (in)
    """)

    st.markdown("""
    API Drill Pipe Grade (US Customary Unit)

    | Grade      | Yield Strength (psi)  | Tensile Strength (psi) |
    |------------|-----------------------|------------------------|
    | Grade E    | 75,000  – 105,000     | ≥ 100,000              |
    | Grade X    | 95,000  – 125,000     | ≥ 105,000              |
    | Grade G    | 105,000 – 135,000     | ≥ 115,000              |
    | Grade S    | 135,000 – 165,000     | ≥ 145,000              |
    | Tool joint | 120,000 – 165,000     | ≥ 140,000              |
    """)

    od = st.number_input("Outside Diameter (OD, in)", min_value=0.0, value=5.0)
    id_ = st.number_input("Inside Diameter (ID, in)", min_value=0.0, value=4.276)
    yield_strength = st.number_input("Yield Strength (psi)", min_value=0.0, value=95000.0)

    if st.button("Calculate Tensile Capacity"):
        area = math.pi * (od**2 - id_**2) / 4
        tensile_capacity = area * yield_strength
        st.markdown(f"**Cross Sectional Area:** {area:.2f} in²")
        st.success(f"**Tensile Capacity:** {tensile_capacity:,.0f} lb")

    

