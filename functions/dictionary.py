import numpy as np

nss_data = {
    'timestamp': np.arange(0, 1000, 10).tolist(),  # Simulated timestamps every 10 seconds from 0 to 1000
    'thermal_neutron_flux': np.random.uniform(0.1, 5.0, 100).tolist(),  # A set of 100 random thermal neutron flux (in counts per second)
    'epithermal_neutron_flux': np.random.uniform(0.5, 10.0, 100).tolist(),  # A set of 100 random epithermal neutron flux (in counts per second)
    'hydrogen_concentration': np.random.uniform(0.01, 0.2, 100).tolist()  # A set of 100 random hydrogen concentration (in wt%)
}

rimfax_data = {
    'timestamp': np.arange(0, 1000, 10).tolist(),  # Simulated timestamps every 10 seconds
    'mode': ['surface'] * 33 + ['shallow'] * 34 + ['deep'] * 33,  # Alternating modes for simulation
    'frequency_range': {
        'surface': [150, 300],
        'shallow': [150, 300],
        'deep': [150, 300]
    },
    'reflection_amplitude': {
        'surface': np.random.uniform(0.2, 1.0, 33).tolist(),  # Simulated reflection amplitude for surface mode
        'shallow': np.random.uniform(0.3, 0.8, 34).tolist(),  # Simulated reflection amplitude for shallow mode
        'deep': np.random.uniform(0.1, 0.6, 33).tolist()  # Simulated reflection amplitude for deep mode
    },
    'depth': {
        'surface': np.random.uniform(0, 0.1, 33).tolist(),  # Simulated depth for surface mode (0-0.1m)
        'shallow': np.random.uniform(0.1, 0.5, 34).tolist(),  # Simulated depth for shallow mode (0.1-0.5m)
        'deep': np.random.uniform(0.5, 1.0, 33).tolist()  # Simulated depth for deep mode (0.5-1.0m)
    }
}

lunar_mission_data = {
    'nss': nss_data,
    'rimfax': rimfax_data
}

for key, value in lunar_mission_data.items():
    print(f"Data for {key}:")
    for subkey, subvalue in value.items():
        print(f"{subkey}: {subvalue}")