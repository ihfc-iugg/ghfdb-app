
ROCK_GROUPS = ( ('M','metamorphic'),
                ('I','igneous'),
                ('S','sedimentary'),
                ('MI','meta-igneous'),
                ('MS','meta-sedimentary'),)
ROCK_ORIGIN = ( ('P','plutonic'),
                ('V','volcanic'),)

# ========== FIELD SETS ==============
SITE_FIELDS = [
                'name',
                'lat',
                'lng',
                'elevation',
                'well_depth',
                'year_drilled',
                
                'seamount_distance',
                'sediment_thickness',
                'sediment_thickness_type',
                'crustal_thickness',
                # 'surface_temp',
                'bottom_water_temp',
                'cruise',
                ]   

HEAT_FLOW_FIELDS = [
            'q_top',
            'q_bot',
            'tilt',
            'num_temp',
            'temp_method',

            'heat_flow_corrected',
            'heat_flow_corrected_uncertainty',
            'heat_flow_uncorrected',
            'heat_flow_uncorrected_uncertainty',

            'gradient_corrected',
            'gradient_corrected_uncertainty',
            'gradient_uncorrected',
            'gradient_uncorrected_uncertainty',

            'tc_mean',
            'cond_unc',
            'num_cond',
            'cond_method',
            'comment',
            ]

HEAT_FLOW_FIELDS_BASIC = [
            'q_top',
            'q_bot',
            'heatflow_corrected',
            'heatflow_uncorrected',
            'gradient_corrected',
            'gradient_uncorrected',
            'thermal_conductivity',
            'comment',
            ]

CONDUCTIVITY_FIELDS = [
            'sample_name',
            'conductivity',
            'uncertainty',
            'orientation',
            'sample_thickness',
            'sample_length',
            'sample_width',
            'sample_diameter',
            'method',
            'formation',
            'rock_type',
            'depth',
            'year_logged',
            'operator',
            'comment',
            'source',
            'source_id',    
            'log_id',
            ]

HEAT_GEN_FIELDS = [
            'heat_production',
            'uncertainty',
            'k_pc',
            'th_ppm',
            'u_ppm',
            'method',
            'formation',
            'rock_type',
            'depth',
            'year_logged',
            'operator',
            'comment',
            'source',
            'source_id',    
            'log_id',
            ]

TEMPERATURE_FIELDS = [
            'temperature',
            'uncertainty',
            'depth',
            'method',

            'log_id',
            'year_logged',
            'circ_time',
            'lag_time',
            'correction',
            'formation',

            'operator',
            'comment',  
            'source',
            'source_id',         
            ]

# ========== IMPORT SETS ==============

heat_flow = gradient = SITE_FIELDS + HEAT_FLOW_FIELDS
conductivity = SITE_FIELDS + CONDUCTIVITY_FIELDS
heat_production = SITE_FIELDS + HEAT_GEN_FIELDS
temperature = SITE_FIELDS + TEMPERATURE_FIELDS


# Can write these in html
UNITS = dict(
    elevation='m',
    age_min='Ma',
    age_max='Ma',
    tectonothermal_min='Ma',
    tectonothermal_max='Ma',
    juvenile_age_min='Ma',
    juvenile_age_max='Ma',
    seamount_distance='km',
    outcrop_distance='km',
    sediment_thickness='km',
    crustal_thickness='km',
    # surface_temp='&deg;C',
    well_depth='m',






)