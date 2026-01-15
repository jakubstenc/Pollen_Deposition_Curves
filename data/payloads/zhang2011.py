flat_data_table = [
    # --- Global Traits ---
    # Total Pollen per flower used for conversion: 24,166 (Mean)

    # --- Figure 1: Pollen Removal (Converted from %) ---
    {
        "bibtex_nick": "Zhang2011",
        "Species": "Glechoma longituba",
        "Family": "Lamiaceae",
        "breeding_system": "Protandrous, self-compatible, predominantly outcrossing",
        "life_form": "Perennial herb",
        "total_longevity": "Female phase approx 24h", # Inferred from text
        "ovule_number": 4, # Standard for Lamiaceae (4 nutlets)
        "pollen_number": 24166, # Explicitly stated in Results
        "methods_notes": "Fig 1: Dynamics of pollen removal and deposition. Converted from % to absolute grains using N=24,166.",
        "source_figure": "Figure 1",
        "image_path": "Data_images/zhang2011/zhang2011dynamics.pdf", # Placeholder
        "series_name": "Pollen Removal (Cumulative)",
        "time_point_h": 2.0, # 2 hours after anthesis
        "variable": "pollen_removed_grains",
        "value": 1208.0, # ~5% of 24,166
        "variation_value": 483.0, # ~2% converted SE
        "variation_type": "SE"
    },
    {
        "bibtex_nick": "Zhang2011",
        "Species": "Glechoma longituba",
        "Family": "Lamiaceae",
        "breeding_system": "Protandrous, self-compatible, predominantly outcrossing",
        "life_form": "Perennial herb",
        "total_longevity": "Female phase approx 24h",
        "ovule_number": 4,
        "pollen_number": 24166,
        "methods_notes": "Fig 1: Dynamics of pollen removal and deposition. Converted from % to absolute grains using N=24,166.",
        "source_figure": "Figure 1",
        "image_path": "Data_images/zhang2011/zhang2011dynamics.pdf",
        "series_name": "Pollen Removal (Cumulative)",
        "time_point_h": 4.0,
        "variable": "pollen_removed_grains",
        "value": 6041.0, # ~25%
        "variation_value": 725.0,
        "variation_type": "SE"
    },
    {
        "bibtex_nick": "Zhang2011",
        "Species": "Glechoma longituba",
        "Family": "Lamiaceae",
        "breeding_system": "Protandrous, self-compatible, predominantly outcrossing",
        "life_form": "Perennial herb",
        "total_longevity": "Female phase approx 24h",
        "ovule_number": 4,
        "pollen_number": 24166,
        "methods_notes": "Fig 1: Dynamics of pollen removal and deposition. Converted from % to absolute grains using N=24,166.",
        "source_figure": "Figure 1",
        "image_path": "Data_images/zhang2011/zhang2011dynamics.pdf",
        "series_name": "Pollen Removal (Cumulative)",
        "time_point_h": 6.0,
        "variable": "pollen_removed_grains",
        "value": 14500.0, # ~60%
        "variation_value": 1208.0,
        "variation_type": "SE"
    },
    {
        "bibtex_nick": "Zhang2011",
        "Species": "Glechoma longituba",
        "Family": "Lamiaceae",
        "breeding_system": "Protandrous, self-compatible, predominantly outcrossing",
        "life_form": "Perennial herb",
        "total_longevity": "Female phase approx 24h",
        "ovule_number": 4,
        "pollen_number": 24166,
        "methods_notes": "Fig 1: Dynamics of pollen removal and deposition. Converted from % to absolute grains using N=24,166.",
        "source_figure": "Figure 1",
        "image_path": "Data_images/zhang2011/zhang2011dynamics.pdf",
        "series_name": "Pollen Removal (Cumulative)",
        "time_point_h": 8.0,
        "variable": "pollen_removed_grains",
        "value": 20541.0, # ~85%
        "variation_value": 966.0,
        "variation_type": "SE"
    },
    {
        "bibtex_nick": "Zhang2011",
        "Species": "Glechoma longituba",
        "Family": "Lamiaceae",
        "breeding_system": "Protandrous, self-compatible, predominantly outcrossing",
        "life_form": "Perennial herb",
        "total_longevity": "Female phase approx 24h",
        "ovule_number": 4,
        "pollen_number": 24166,
        "methods_notes": "Fig 1: Dynamics of pollen removal and deposition. Converted from % to absolute grains using N=24,166.",
        "source_figure": "Figure 1",
        "image_path": "Data_images/zhang2011/zhang2011dynamics.pdf",
        "series_name": "Pollen Removal (Cumulative)",
        "time_point_h": 10.0,
        "variable": "pollen_removed_grains",
        "value": 22957.0, # ~95%
        "variation_value": 483.0,
        "variation_type": "SE"
    },

    # --- Figure 1: Pollen Deposition (Converted from % of assumed Total Capacity/Transfer) ---
    # Note: Assuming the relative % refers to percentage of maximum pollen grains observed (approx 400-500 based on typical Lamiaceae/Glechoma data).
    # IF the graph is % of Total Production (24,166), the values would be massive (thousands), which is unlikely for deposition.
    # It is highly probable the "100%" for deposition refers to a Saturation Point.
    # Text mentions "stigmatic pollen deposition... was 389 ± 24 grains" at saturation/natural max.
    # Therefore, I will use **389** as the conversion factor for the right axis.
    {
        "bibtex_nick": "Zhang2011",
        "Species": "Glechoma longituba",
        "Family": "Lamiaceae",
        "breeding_system": "Protandrous, self-compatible, predominantly outcrossing",
        "life_form": "Perennial herb",
        "total_longevity": "Female phase approx 24h",
        "ovule_number": 4,
        "pollen_number": 24166,
        "methods_notes": "Fig 1: Deposition converted using Mean Max Pollen Load = 389 grains (from text).",
        "source_figure": "Figure 1",
        "image_path": "Data_images/zhang2011/zhang2011dynamics.pdf",
        "series_name": "Pollen Deposition",
        "time_point_h": 2.0,
        "variable": "pollen_deposited_grains",
        "value": 19.5, # ~5% of 389
        "variation_value": 7.8,
        "variation_type": "SE"
    },
    {
        "bibtex_nick": "Zhang2011",
        "Species": "Glechoma longituba",
        "Family": "Lamiaceae",
        "breeding_system": "Protandrous, self-compatible, predominantly outcrossing",
        "life_form": "Perennial herb",
        "total_longevity": "Female phase approx 24h",
        "ovule_number": 4,
        "pollen_number": 24166,
        "methods_notes": "Fig 1: Deposition converted using Mean Max Pollen Load = 389 grains (from text).",
        "source_figure": "Figure 1",
        "image_path": "Data_images/zhang2011/zhang2011dynamics.pdf",
        "series_name": "Pollen Deposition",
        "time_point_h": 4.0,
        "variable": "pollen_deposited_grains",
        "value": 77.8, # ~20% of 389
        "variation_value": 15.6,
        "variation_type": "SE"
    },
    {
        "bibtex_nick": "Zhang2011",
        "Species": "Glechoma longituba",
        "Family": "Lamiaceae",
        "breeding_system": "Protandrous, self-compatible, predominantly outcrossing",
        "life_form": "Perennial herb",
        "total_longevity": "Female phase approx 24h",
        "ovule_number": 4,
        "pollen_number": 24166,
        "methods_notes": "Fig 1: Deposition converted using Mean Max Pollen Load = 389 grains (from text).",
        "source_figure": "Figure 1",
        "image_path": "Data_images/zhang2011/zhang2011dynamics.pdf",
        "series_name": "Pollen Deposition",
        "time_point_h": 6.0,
        "variable": "pollen_deposited_grains",
        "value": 233.4, # ~60% of 389
        "variation_value": 38.9,
        "variation_type": "SE"
    },
    {
        "bibtex_nick": "Zhang2011",
        "Species": "Glechoma longituba",
        "Family": "Lamiaceae",
        "breeding_system": "Protandrous, self-compatible, predominantly outcrossing",
        "life_form": "Perennial herb",
        "total_longevity": "Female phase approx 24h",
        "ovule_number": 4,
        "pollen_number": 24166,
        "methods_notes": "Fig 1: Deposition converted using Mean Max Pollen Load = 389 grains (from text).",
        "source_figure": "Figure 1",
        "image_path": "Data_images/zhang2011/zhang2011dynamics.pdf",
        "series_name": "Pollen Deposition",
        "time_point_h": 8.0,
        "variable": "pollen_deposited_grains",
        "value": 350.1, # ~90% of 389
        "variation_value": 19.5,
        "variation_type": "SE"
    },
    {
        "bibtex_nick": "Zhang2011",
        "Species": "Glechoma longituba",
        "Family": "Lamiaceae",
        "breeding_system": "Protandrous, self-compatible, predominantly outcrossing",
        "life_form": "Perennial herb",
        "total_longevity": "Female phase approx 24h",
        "ovule_number": 4,
        "pollen_number": 24166,
        "methods_notes": "Fig 1: Deposition converted using Mean Max Pollen Load = 389 grains (from text).",
        "source_figure": "Figure 1",
        "image_path": "Data_images/zhang2011/zhang2011dynamics.pdf",
        "series_name": "Pollen Deposition",
        "time_point_h": 10.0,
        "variable": "pollen_deposited_grains",
        "value": 389.0, # ~100% (Saturation)
        "variation_value": 11.7,
        "variation_type": "SE"
    }
]
