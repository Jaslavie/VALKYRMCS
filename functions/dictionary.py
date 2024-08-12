import numpy as np

rimfax_data = {
    'timestamp': np.arange(0, 50, 10).tolist(),  # Simulated timestamps in 10-second intervals
    'mode': ['surface'] * 17 + ['shallow'] * 17 + ['deep'] * 16,  # Simulated mode switching
    'frequency_range': {
        'surface': [150, 300],  # MHz
        'shallow': [150, 300],  # MHz
        'deep': [150, 300]  # MHz
    },
    'reflection_amplitude': {
        'surface': np.random.uniform(0.2, 1.0, 100).tolist(),  # Surface mode reflection amplitude
        'shallow': np.random.uniform(0.3, 0.8, 200).tolist(),  # Shallow mode reflection amplitude
        'deep': np.random.uniform(0.1, 0.6, 300).tolist()  # Deep mode reflection amplitude
    },
    'depth': {
        'surface': np.random.uniform(0, 0.1, 100).tolist(),  # Surface mode depth (0-0.1m)
        'shallow': np.random.uniform(0.1, 0.5, 200).tolist(),  # Shallow mode depth (0.1-0.5m)
        'deep': np.random.uniform(0.5, 1.0, 300).tolist()  # Deep mode depth (0.5-1.0m)
    }
}

nss_data = {
    'timestamp': np.arange(0, 50, 10).tolist(),  # Simulated timestamps in 10-second intervals over 177 days
    'thermal_neutron_flux': np.random.uniform(0.1, 0.3, len(np.arange(0,  50, 10))).tolist(),  # <0.3eV
    'epithermal_neutron_flux': np.random.uniform(0.3, 1000, len(np.arange(0,  50, 10))).tolist(),  # 0.3 eV to 1 keV
    'hydrogen_concentration': np.random.uniform(0.5, 5.0, len(np.arange(0,  50, 10))).tolist()  # Hydrogen concentration in wt%
}
lunar_mission_data = {
    'nss': nss_data,
    'rimfax': rimfax_data
}

for key, value in lunar_mission_data.items():
    print(f"{key.upper()} Data: ") # print instrument name
    for sub_key, sub_value in value.items():
        if isinstance(sub_value, dict):
            print(f"{sub_key.upper()}: ") # print subelement name
            for sub_sub_key, sub_sub_value in sub_value.items():
                print(f"  {sub_sub_key}: {sub_sub_value}") # print subelement values
        else:
            print(f"{sub_key}: {sub_value}") # else if not a dictionary, print the value
