import streamlit as st
from views.calculation_tab1 import calculation_tab1
from views.calculation_tab2 import calculation_tab2
from views.calculation_tab3 import calculation_tab3
from views.influx_height import influx_height
from views.estimate_influx_type import estimate_influx_type  # <-- Add this import
from views.formation_pressure import formation_pressure
from views.formation_temperature_calculator import formation_temperature_calculator
from views.gas_cut_pressure_loss import gas_cut_pressure_loss
from views.kick_penetration import kick_penetration
from views.icp_fcp import icp_fcp  # <-- Add this import
from views.kick_tolerance_factor import kick_tolerance_factor
from views.kill_mud_weight import kill_mud_weight
from views.lube_increment import lube_increment
from views.max_pit_gain import max_pit_gain
from views.max_surface_pressure import max_surface_pressure
from views.volumetric_well_control import volumetric_well_control
from views.new_stroke_pressure import new_stroke_pressure 
from views.riser_margin import riser_margin
from views.trip_margin import trip_margin
from views.tensile_capacity import tensile_capacity
from views.drill_collar_weight import drill_collar_weight
from views.equivalent_circulating_density import equivalent_circulating_density
from views.annular_volume import annular_volume
from views.pump_output import pump_output
from views.theoretical_lag_time import theoretical_lag_time
from views.spot_pill_height import spot_pill_height
from views.loss_hydrostatic_pressure import loss_hydrostatic_pressure
from views.margin_of_overpull import margin_of_overpull
from views.increase_mud_weight_due_to_cuttings import increase_mud_weight_due_to_cuttings
from views.max_rop_before_fracture import max_rop_before_fracture
from views.drill_pipe_elongation_temp import drill_pipe_elongation_temp
from views.break_circulation_pressure import break_circulation_pressure
from views.depth_of_stuck_pipe import depth_of_stuck_pipe
from views.ton_miles_calculator import ton_miles_calculator
from views.cutting_volume import cutting_volume
from views.accumulator_capacity import accumulator_capacity_tabs
from views.annular_velocity_calculator import annular_velocity_calculator
from views.buoyed_weight_casing import buoyed_weight_casing
from views.pressure_to_emw import pressure_to_emw
from views.coring_cost_per_foot import coring_cost_per_foot
from views.depth_of_washout_pipe import depth_of_washout_pipe
from views.d_exponent_calculator import d_exponent_calculator
from views.pipe_displacement_calculator import pipe_displacement_calculator
from views.drilling_cost_per_foot import drilling_cost_per_foot
from views.fit_pressure_calculator import fit_pressure_calculator
from views.hydrostatic_pressure_calculator import hydrostatic_pressure_calculator
from views.hydrostatic_pressure_decrease_pooh import hydrostatic_pressure_decrease_pooh
from views.internal_capacity_calculator import internal_capacity_calculator
from views.max_surface_pressure_calculator import max_surface_pressure_calculator
from views.slug_volume_calculator import slug_volume_calculator
from views.specific_gravity_calculator import specific_gravity_calculator
from views.angle_averaging_directional_survey import angle_averaging_directional_survey
from views.radius_of_curvature_survey import radius_of_curvature_survey
from views.balanced_tangential_survey import balanced_tangential_survey
from views.minimum_curvature_survey import minimum_curvature_survey
from views.dogleg_severity_calculator import dogleg_severity_calculator
from views.bulk_density_cuttings import bulk_density_cuttings  # <-- Add this import
from views.decrease_oil_water_ratio import decrease_oil_water_ratio
from views.oil_water_mixture_density import oil_water_mixture_density
from views.dilution_mud_system import dilution_mud_system
from views.increase_mw_formulas import increase_mw_formulas
from views.increase_oil_water_ratio import increase_oil_water_ratio
from views.mix_fluids_volume import mix_fluids_volume
from views.yp_pv_calculator import yp_pv_calculator
from views.light_weight_mud_volume import light_weight_mud_volume
from views.annular_pressure_loss import annular_pressure_loss
from views.critical_rpm_calculator import critical_rpm_calculator
from views.advanced_annular_pressure_loss_ecd import advanced_annular_pressure_loss_ecd
from views.bottom_hole_pressure_dry_gas import bottom_hole_pressure_dry_gas
from views.cci_calculator import cci_calculator
from views.cutting_slip_velocity import cutting_slip_velocity
from views.effective_viscosity import effective_viscosity_calculator
from views.hydraulic_horse_power import hydraulic_horse_power_calculator
from views.flow_behavior_index import flow_behavior_index_calculator
from views.bit_nozzle_pressure_drop import bit_nozzle_pressure_drop_calculator
from views.drill_string_pressure_loss import drill_string_pressure_loss_calculator
from views.surge_swab_pressure import surge_swab_pressure_calculator
import os
import base64

def main():
    #st.image("/Users/sametgirgin/Drilling App/images/RePathLogo.png", use_container_width=True)

    main_tabs = [
        "Home",
        "Basic Drilling Formulas",
        "Applied Drilling Formulas",
        "Drill String Formulas",
        "Hydraulic Formulas",
        "Drilling Fluid Formulas",
        "Well Control Formulas",
        "Directional Drilling Calculation"
    ]

    selected_main = st.sidebar.selectbox("Main Menu", main_tabs)

    if selected_main == "Home":
        st.title("Drilling Formula Calculator")
        # Read and format content.txt
        import os
        content_path = os.path.join(os.path.dirname(__file__), "content.txt")
        with open(content_path, "r") as f:
            lines = f.readlines()

        formatted = ""
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#"):
                # Make section header (remove # and add Markdown header)
                formatted += f"\n\n### {stripped.lstrip('#').strip()}\n"
            elif stripped:
                # Make bullet point
                formatted += f"- {stripped}\n"
            else:
                formatted += "\n"

        st.markdown(formatted)
    elif selected_main == "Applied Drilling Formulas":
        sub_tabs = [
            "Drill Collar Weight",
            "Equivalent Circulating Density (ECD)",
            "Annular Volume",
            "Pump Output",
            "Theoretical Lag Time",
            "Spot Pill Height",
            "Loss of Hydrostatic Pressure",
            "Margin of Overpull",
            "Increase in MW Due to Cuttings",
            "Maximum ROP Before Fracture Formation",
            "Drill Pipe Elongation Due to Temperature",
            "Pressure Required to Break Circulation",
            "Depth of Stuck Pipe",
            "Ton-Miles",
            "Volume of Cutting Generated"
        ]
        selected_sub = st.sidebar.radio("Applied Drilling Formulas", sub_tabs)
        if selected_sub == "Drill Collar Weight":
            drill_collar_weight()
        elif selected_sub == "Equivalent Circulating Density (ECD)":
            equivalent_circulating_density()
        elif selected_sub == "Annular Volume":
            annular_volume()
        elif selected_sub == "Pump Output":
            pump_output()
        elif selected_sub == "Theoretical Lag Time":
            theoretical_lag_time()
        elif selected_sub == "Spot Pill Height":
            spot_pill_height()
        elif selected_sub == "Loss of Hydrostatic Pressure":
            loss_hydrostatic_pressure()
        elif selected_sub == "Margin of Overpull":
            margin_of_overpull()
        elif selected_sub == "Increase in MW Due to Cuttings":
            increase_mud_weight_due_to_cuttings()
        elif selected_sub == "Maximum ROP Before Fracture Formation":
            max_rop_before_fracture()
        elif selected_sub == "Drill Pipe Elongation Due to Temperature":
            drill_pipe_elongation_temp()
        elif selected_sub == "Pressure Required to Break Circulation":
            break_circulation_pressure()
        elif selected_sub == "Depth of Stuck Pipe":
            depth_of_stuck_pipe()
        elif selected_sub == "Ton-Miles":
            ton_miles_calculator()
        elif selected_sub == "Volume of Cutting Generated":
            cutting_volume()
    elif selected_main == "Basic Drilling Formulas":
        sub_tabs = [
            "Accumulator Capacity",
            "Annular Velocity",
            "Buoyed Weight of Casing",
            "Convert Pressure to EMW",
            "Coring Cost Per Foot",
            "Depth of Washout Pipe",
            "D-Exponent",
            "Pipe Displacement",
            "Drilling Cost Per Foot",
            "FIT Pressure",
            "Formation Temperature",
            "Hydrostatic Pressure",
            "Hydrostatic Pressure Decrease When POOH",
            "Internal Capacity Factor",
            "Slug Volume",
            "Specific Gravity"
        ]
        selected_sub = st.sidebar.radio("Basic Drilling Formulas", sub_tabs)
        if selected_sub == "Accumulator Capacity":
            accumulator_capacity_tabs()
        elif selected_sub == "Annular Velocity":
            annular_velocity_calculator()
        elif selected_sub == "Buoyed Weight of Casing":
            buoyed_weight_casing()
        elif selected_sub == "Convert Pressure to EMW":
            pressure_to_emw()
        elif selected_sub == "Coring Cost Per Foot":
            coring_cost_per_foot()
        elif selected_sub == "Depth of Washout Pipe":
            depth_of_washout_pipe()
        elif selected_sub == "D-Exponent":
            d_exponent_calculator()
        elif selected_sub == "Pipe Displacement":
            pipe_displacement_calculator()
        elif selected_sub == "Drilling Cost Per Foot":
            drilling_cost_per_foot()
        elif selected_sub == "FIT Pressure":
            fit_pressure_calculator()
        elif selected_sub == "Formation Temperature":
            formation_temperature_calculator()
        elif selected_sub == "Hydrostatic Pressure":
            hydrostatic_pressure_calculator()
        elif selected_sub == "Hydrostatic Pressure Decrease When POOH":
            hydrostatic_pressure_decrease_pooh()
        elif selected_sub == "Internal Capacity Factor":
            internal_capacity_calculator()
        elif selected_sub == "Slug Volume":
            slug_volume_calculator()
        elif selected_sub == "Specific Gravity":
            specific_gravity_calculator()
    elif selected_main == "Well Control Formulas":
        sub_tabs = [
            "Actual Gas Migration Rate",
            "MISICP",
            "Adjusted MASICP",
            "Influx Height",
            "Estimate Type of Influx (Kick)",
            "Formation Pressure from Kick Analysis",
            "Hydrostatic Pressure Loss Due to Gas Cut Mud",
            "Kick Penetration For Stripping Operation",
            "Initial & Final Circulating Pressure (ICP & FCP)",
            "Kick Tolerance Factor",
            "Kill Mud Weight",
            "Lube Increment",
            "Maximum Pit Gain from Gas Kick",
            "Maximum Surface Pressure from Gas Influx",  # <-- Add this line
            "Volumetric Well Control Method",
            "New Pressure Loss with New Strokes",  # <-- Add this line
            "Riser Margin",
            "Trip Margin",
            "Max Surface Pressure (Bullheading)"
        ]
        selected_sub = st.sidebar.radio("Well Control Formulas", sub_tabs)
        if selected_sub == "Actual Gas Migration Rate":
            calculation_tab1()
        elif selected_sub == "MISICP":
            calculation_tab2()
        elif selected_sub == "Adjusted MASICP":
            calculation_tab3()
        elif selected_sub == "Influx Height":
            influx_height()
        elif selected_sub == "Estimate Type of Influx (Kick)":
            estimate_influx_type()
        elif selected_sub == "Formation Pressure from Kick Analysis":
            formation_pressure()
        elif selected_sub == "Gas Cut Pressure Loss":
            gas_cut_pressure_loss()
        elif selected_sub == "Hydrostatic Pressure Loss Due to Gas Cut Mud":
            gas_cut_pressure_loss()
        elif selected_sub == "Kick Penetration For Stripping Operation":
            kick_penetration()  # <-- Add this line
        elif selected_sub == "Initial & Final Circulating Pressure (ICP & FCP)":
            icp_fcp()
        elif selected_sub == "Kick Tolerance Factor":
            kick_tolerance_factor()
        elif selected_sub == "Kill Mud Weight":  # <-- Add this line
            kill_mud_weight()  # <-- Add this line
        elif selected_sub == "Lube Increment":  # <-- Add this line
            lube_increment()  # <-- Add this line
        elif selected_sub == "Maximum Pit Gain from Gas Kick":  # <-- Add this line
            max_pit_gain()  # <-- Add this line
        elif selected_sub == "Max Surface Pressure":  # <-- Add this line
            max_surface_pressure()  # <-- Add this line
        elif selected_sub == "Maximum Surface Pressure from Gas Influx":
            max_surface_pressure()
        elif selected_sub == "Volumetric Well Control Method":
            volumetric_well_control()
        elif selected_sub == "New Pressure Loss with New Strokes":  # <-- Add this line
            new_stroke_pressure()  # <-- Add this line
        elif selected_sub == "Riser Margin":
            riser_margin()  # <-- Add this line
        elif selected_sub == "Trip Margin":
            trip_margin()
        elif selected_sub == "Max Surface Pressure (Bullheading)":
            max_surface_pressure_calculator()
    elif selected_main == "Drill String Formulas":
        sub_tabs = [
            "Tensile Capacity of Drill Pipe"]
        selected_sub = st.sidebar.radio("Drill String Formulas", sub_tabs)
        if selected_sub == "Tensile Capacity of Drill Pipe":
            tensile_capacity()
    elif selected_main == "Directional Drilling Calculation":
        sub_tabs = [
            "Angle Averaging Survey",
            "Radius of Curvature Survey",
            "Balanced Tangential Survey",
            "Minimum Curvature Survey",
            "Dogleg Severity"
        ]
        selected_sub = st.sidebar.radio("Directional Drilling Calculation", sub_tabs)
        if selected_sub == "Angle Averaging Survey":
            angle_averaging_directional_survey()
        elif selected_sub == "Radius of Curvature Survey":
            radius_of_curvature_survey()
        elif selected_sub == "Balanced Tangential Survey":
            balanced_tangential_survey()
        elif selected_sub == "Minimum Curvature Survey":
            minimum_curvature_survey()
        elif selected_sub == "Dogleg Severity":
            dogleg_severity_calculator()
    elif selected_main == "Drilling Fluid Formulas":
        sub_tabs = [
            "Bulk Density of Cuttings",
            "Decrease Oil/Water Ratio",
            "Increase Oil/Water Ratio",
            "Oil/Water Mixture Density",
            "Dilution of Mud System (Base Fluid)",
            "Dilution of Mud System (By Adding Mud)",
            "Barite Formulas",
            "Barite Volume Increase",
            "Mix Fluids Volume (Pit Limit)",
            "Mix Fluids Volume (No Limit)",
            "YP & PV Calculator",
            "Light Weight Mud Volume"
        ]
        selected_sub = st.sidebar.radio("Drilling Fluid Formulas", sub_tabs)
        if selected_sub == "Bulk Density of Cuttings":
            bulk_density_cuttings()
        elif selected_sub == "Decrease Oil/Water Ratio":
            decrease_oil_water_ratio()
        elif selected_sub == "Increase Oil/Water Ratio":
            increase_oil_water_ratio()
        elif selected_sub == "Oil/Water Mixture Density":
            oil_water_mixture_density()
        elif selected_sub == "Dilution of Mud System":
            dilution_mud_system()
        elif selected_sub == "Increase Mud Weight Formulas":
            increase_mw_formulas()
        elif selected_sub == "Mix Fluids Volume (Pit Limit)":
            mix_fluids_volume()
        elif selected_sub == "Mix Fluids Volume (No Limit)":
            mix_fluids_volume()
        elif selected_sub == "YP & PV Calculator":
            yp_pv_calculator()
        elif selected_sub == "Light Weight Mud Volume":
            light_weight_mud_volume()
    elif selected_main == "Hydraulic Formulas":
        sub_tabs = [
            "Annular Pressure Loss",
            "Drill String Pressure Loss",
            "Bit Nozzle Pressure Drop",
            "Hydraulic Horse Power",
            "Surge & Swab Pressure",
            "Cutting Slip Velocity",
            "Cutting Carrying Index (CCI)",
            "Effective Viscosity",
            "Critical RPM",
            "Advanced Annular Pressure Loss & ECD",
            "Bottom Hole Pressure (Dry Gas Well)",
            "Flow Behavior Index & Consistency Factor"
        ]
        selected_sub = st.sidebar.radio("Hydraulic Formulas", sub_tabs)
        if selected_sub == "Annular Pressure Loss":
            annular_pressure_loss()
        elif selected_sub == "Critical RPM":
            critical_rpm_calculator()
        elif selected_sub == "Advanced Annular Pressure Loss & ECD":
            advanced_annular_pressure_loss_ecd()
        elif selected_sub == "Bottom Hole Pressure (Dry Gas Well)":
            bottom_hole_pressure_dry_gas()
        elif selected_sub == "Cutting Carrying Index (CCI)":
            cci_calculator()
        elif selected_sub == "Cutting Slip Velocity":
            cutting_slip_velocity()
        elif selected_sub == "Effective Viscosity":
            effective_viscosity_calculator()
        elif selected_sub == "Hydraulic Horse Power":
            hydraulic_horse_power_calculator()
        elif selected_sub == "Flow Behavior Index & Consistency Factor":
            flow_behavior_index_calculator()
        elif selected_sub == "Bit Nozzle Pressure Drop":
            bit_nozzle_pressure_drop_calculator()
        elif selected_sub == "Drill String Pressure Loss":
            drill_string_pressure_loss_calculator()
        elif selected_sub == "Surge & Swab Pressure":
            surge_swab_pressure_calculator()

    st.markdown("---")
    
    #st.image("streamlit-calc-app/images/RePathLogo.png", width=160, use_column_width=False)
    
    #image_path = os.path.join(os.path.dirname(__file__), '..', '..', 'images', 'RePathLogo.png')
    #st.image(image_path, width=600)
    
    #st.image("../images/RePathLogo.png", width=160)

    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'RePathLogo.png')
    img_base64 = get_base64_image(image_path)
    st.markdown(
    f"""
    <div style='text-align: right;'>
        <img src='data:image/png;base64,{img_base64}' width='160'>
    </div>
    """,
    unsafe_allow_html=True
)
if __name__ == "__main__":
    main()
    
    
