import streamlit as st

def increase_mw_formulas():
    st.markdown("<h2 style='text-align: center;'>Increase Mud Weight by Adding Barite/CaCO₃/Hematite</h2>", unsafe_allow_html=True)
    st.markdown("""
    In drilling operations, maintaining proper mud weight is essential for ensuring wellbore stability, controlling formation pressures, and preventing blowouts. This process—known as weighting up—involves increasing the density of the drilling fluid by adding weighting agents such as Barite, Calcium Carbonate, or Hematite.

    Each of these materials has a different specific gravity and use case. For instance, Barite is the most commonly used agent, Calcium Carbonate is preferred in horizontal or reservoir sections due to its non-damaging properties, and Hematite is selected when extremely high mud weights are required due to its higher density.

    Although the weighting up formula remains the same across these materials, the weight factor used in the calculation changes based on the specific gravity of the agent. Understanding how to correctly calculate the amount of weighting material needed is a critical skill for maintaining well control and ensuring safe drilling operations.
    """)

    # Add weighting agent selection
    agent = st.selectbox(
        "Select weighting agent:",
        ("Barite", "Calcium Carbonate", "Hematite"),
        key="weighting_agent"
    )

    # Set constants based on agent
    if agent.startswith("Barite"):
        factor = 1470
        max_weight = 35
    elif agent.startswith("Calcium Carbonate"):
        factor = 945
        max_weight = 22.5
    elif agent.startswith("Hematite"):
        factor = 1680
        max_weight = 40
    st.markdown("<u>This calculator determines the number of sacks of weighting agent required to increase mud weight.</u>", unsafe_allow_html=True)

    st.markdown(f"""
    Sacks of {agent} per 100 bbl of mud = {factor} × (W₂ − W₁) ÷ ({max_weight} − W₂)

    Where:  
    - W₁ = current mud weight (ppg)  
    - W₂ = new mud weight (ppg)  

    """)

    w1 = st.number_input("Current mud weight (W₁, ppg)", min_value=0.0, value=10.0, key="barite_w1")
    w2 = st.number_input("New mud weight (W₂, ppg)", min_value=0.0, value=13.0, key="barite_w2")
    total_vol = st.number_input("Total mud volume (bbl)", min_value=0.0, value=500.0, key="barite_vol")

    denominator = max_weight - w2
    if denominator > 0 and w2 > w1:
        sacks_per_100bbl = factor * (w2 - w1) / denominator
        total_sacks = sacks_per_100bbl * (total_vol / 100)
        st.success(f"**Sacks of {agent.split()[0]} per 100 bbl:** {sacks_per_100bbl:.1f} sacks")
        st.success(f"**Total sacks required:** {total_sacks:.0f} sacks")
    else:
        st.error(f"Ensure that new mud weight (W₂) is greater than current mud weight (W₁) and less than {max_weight} ppg.")

    st.markdown("---")
    st.markdown(f"<u>After adding {agent.split()[0].lower()} to increase mud weight, the total mud volume increases due to the volume of dry material.</u>", unsafe_allow_html=True)

    st.markdown(f"""
    **Formula:**  
    Volume increase per 100 bbl of mud = 100 × (W₂ − W₁) ÷ ({max_weight} − W₂)

    Where:  
    - W₁ = current mud weight (ppg)  
    - W₂ = new mud weight (ppg)

    **Total Volume Increase:**  
    Total volume increase = Volume increase per 100 bbl × (Total mud volume ÷ 100)
    """)

    w1_vol = st.number_input("Current mud weight for volume increase (W₁, ppg)", min_value=0.0, value=10.0, key="barite_vol_w1")
    w2_vol = st.number_input("New mud weight for volume increase (W₂, ppg)", min_value=0.0, value=13.0, key="barite_vol_w2")
    total_vol_input = st.number_input("Total mud volume for volume increase (bbl)", min_value=0.0, value=500.0, key="barite_vol_total")

    denominator_vol = max_weight - w2_vol
    if denominator_vol > 0 and w2_vol > w1_vol:
        vol_increase_per_100bbl = 100 * (w2_vol - w1_vol) / denominator_vol
        total_vol_increase = vol_increase_per_100bbl * (total_vol_input / 100)
        st.success(f"**Volume increase per 100 bbl:** {vol_increase_per_100bbl:.2f} bbl")
        st.success(f"**Total volume increase:** {total_vol_increase:.2f} bbl")
    else:
        st.error(f"Ensure that new mud weight (W₂) is greater than current mud weight (W₁) and less than {max_weight} ppg.")

    st.markdown("---")
    st.markdown(f"<u>Starting Volume of Original Mud (Weight Up with {agent.split()[0]})</u>", unsafe_allow_html=True)
    st.markdown(f"""
    If you are limited by pit volume, you may need to calculate the starting volume of original mud to achieve a predetermined final volume at the desired mud weight.

    **Formula:**  
    Starting volume (bbl) = VF × ({max_weight} − W₂) ÷ ({max_weight} − W₁)

    Where:  
    - W₁ = current mud weight (ppg)  
    - W₂ = new mud weight (ppg)  
    - VF = final volume (bbl)
    """)

    w1_start = st.number_input("Current mud weight for starting volume (W₁, ppg)", min_value=0.0, value=10.0, key="barite_start_w1")
    w2_start = st.number_input("New mud weight for starting volume (W₂, ppg)", min_value=0.0, value=13.0, key="barite_start_w2")
    vf = st.number_input("Final desired mud volume (VF, bbl)", min_value=0.0, value=100.0, key="barite_vf")

    denominator_start = max_weight - w1_start
    if denominator_start > 0 and w2_start > w1_start:
        starting_volume = vf * (max_weight - w2_start) / denominator_start
        st.success(f"**Starting volume required:** {starting_volume:.2f} bbl")
    else:
        st.error(f"Ensure that new mud weight (W₂) is greater than current mud weight (W₁) and less than {max_weight} ppg.")