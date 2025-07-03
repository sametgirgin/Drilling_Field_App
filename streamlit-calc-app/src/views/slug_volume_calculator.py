import streamlit as st
import os

def slug_volume_calculator():
    st.markdown("<h2 style='text-align: center;'>Slug Volume Calculator for Dry Pipe</h2>", unsafe_allow_html=True)
    st.markdown("""
                
    What is a Slug?
    A slug is a small volume of heavy-weighted drilling fluid (mud) pumped into the drill pipe 
    to displace lighter mud downward. It is used to prevent wet pipe trips by pushing mud 
    below the pipe before pulling out of hole (POOH).
    
    When Do We Use a Slug?
    - To avoid mud spillover at the rig floor during trips.
    - Typically used when pipe becomes wet during tripping.
    - Helps in clean and safe pipe handling at surface.
    
    Rule of Thumb:
    - Slug weight = 1.5 to 2.0 PPG higher than current mud weight
        Example: If mud weight = 10.0 PPG → Slug weight = 11.5 to 12.0 PPG
        
    
    This calculator determines the required slug volume to achieve a desired length of dry pipe.

    **Step 1:**  
    Hydrostatic Pressure (psi) = Mud weight (ppg) × 0.052 × Desired dry pipe length (ft)

    **Step 2:**  
    Pressure gradient difference (psi/ft) = (Slug weight (ppg) − Mud weight (ppg)) × 0.052

    **Step 3:**  
    Slug length (ft) = Hydrostatic Pressure (psi) ÷ Pressure gradient difference (psi/ft)

    **Step 4:**  
    Slug volume (bbl) = Slug length (ft) × Drill pipe capacity (bbl/ft)

    """)
    #st.image("/Users/sametgirgin/Drilling App/images/slug.jpg", use_container_width=True)

    image_path = os.path.join(os.path.dirname(__file__), '..', '..', 'images', 'slug.jpg')
    st.image(image_path, width=600)

    dry_pipe_length = st.number_input("Desired length of dry pipe (ft)", min_value=0.0, value=200.0, key="slug_dry_pipe")
    dp_capacity = st.number_input("Drill pipe capacity (bbl/ft)", min_value=0.0, value=0.016, format="%.3f", key="slug_dp_capacity")
    mud_weight = st.number_input("Mud weight (ppg)", min_value=0.0, value=10.0, key="slug_mud_weight")
    slug_weight = st.number_input("Slug weight (ppg)", min_value=0.0, value=11.5, key="slug_slug_weight")

    # Step 1
    hydrostatic_pressure = mud_weight * 0.052 * dry_pipe_length
    # Step 2
    pressure_gradient_diff = (slug_weight - mud_weight) * 0.052
    # Step 3
    if pressure_gradient_diff > 0:
        slug_length = hydrostatic_pressure / pressure_gradient_diff
    else:
        slug_length = 0
    # Step 4
    slug_volume = slug_length * dp_capacity

    st.markdown(f"**Step 1:** Hydrostatic Pressure = {hydrostatic_pressure:.2f} psi")
    st.markdown(f"**Step 2:** Pressure gradient difference = {pressure_gradient_diff:.3f} psi/ft")
    st.markdown(f"**Step 3:** Slug length = {slug_length:.0f} ft")
    st.success(f"**Step 4: Slug volume required = {slug_volume:.2f} bbl**")
    
    st.markdown("<h2 style='text-align: center;'>Slug Weight Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    You can determine how much slug weight required in order to achieve desired length of dry pipe with certain slug volume that you will use.

    This calculator determines the slug weight required for a desired length of dry pipe with a set slug volume.

    **Step 1:**  
    Length of slug in drill pipe (ft) = Slug volume (bbl) ÷ Drill pipe capacity (bbl/ft)

    **Step 2:**  
    Hydrostatic Pressure (psi) = Mud weight (ppg) × 0.052 × Desired length of dry pipe (ft)

    **Step 3:**  
    Slug weight (ppg) = [Hydrostatic Pressure (psi) ÷ 0.052 ÷ Slug length (ft)] + Mud weight (ppg)
    """)

    dry_pipe_length = st.number_input("Desired length of dry pipe (ft)", min_value=0.0, value=200.0, key="sw_dry_pipe")
    mud_weight = st.number_input("Mud weight in hole (ppg)", min_value=0.0, value=12.0, key="sw_mud_weight")
    dp_capacity = st.number_input("Drill pipe capacity (bbl/ft)", min_value=0.0001, value=0.016, format="%.3f", key="sw_dp_capacity")
    slug_volume = st.number_input("Slug volume (bbl)", min_value=0.0, value=20.0, key="sw_slug_volume")

    # Step 1
    slug_length = slug_volume / dp_capacity if dp_capacity > 0 else 0
    # Step 2
    hydrostatic_pressure = mud_weight * 0.052 * dry_pipe_length
    # Step 3
    if slug_length > 0:
        slug_weight = (hydrostatic_pressure / 0.052 / slug_length) + mud_weight
    else:
        slug_weight = 0

    st.markdown(f"**Step 1:** Slug length in drill pipe = {slug_length:.0f} ft")
    st.markdown(f"**Step 2:** Hydrostatic Pressure = {hydrostatic_pressure:.2f} psi")
    st.success(f"**Step 3: Slug weight required = {slug_weight:.2f} ppg**")