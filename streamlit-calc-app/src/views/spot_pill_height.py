import streamlit as st

def spot_pill_height():
    st.markdown("<h2 style='text-align: center;'>Light Weight Spot Pill Height Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""
    When differential sticking occurs, one possible solution is to spot 
    a lightweight fluid to lessen the force caused by the pressure 
    difference between the wellbore mud and the formation pressure. 
    However, it is critical to accurately calculate the volume of 
    lightweight fluid to be added, ensuring that the formation pressure 
    is not unintentionally underbalanced.

    **Step 1:**  
    Difference in pressure gradient (psi/ft) = (Current mud weight (ppg) − Spot pill weight (ppg)) × 0.052

    **Step 2:**  
    Height of spot pill (ft) = Overbalance pressure (psi) ÷ Difference in pressure gradient (psi/ft)

    """)

    mud_weight = st.number_input("Current mud weight (ppg)", min_value=0.0, value=13.0)
    spot_weight = st.number_input("Light weight spot pill (ppg)", min_value=0.0, value=8.3)
    overbalance = st.number_input("Overbalance pressure (psi)", min_value=0.0, value=300.0)

    diff_grad = (mud_weight - spot_weight) * 0.052
    st.markdown(f"**Difference in pressure gradient:** {diff_grad:.4f} psi/ft")

    height = overbalance / diff_grad if diff_grad > 0 else 0
    st.markdown(f"**Required spot pill height:** {height:.0f} ft")