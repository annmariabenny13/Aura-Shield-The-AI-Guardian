import pandas as pd
import numpy as np

np.random.seed(42)
TOTAL_ROWS = 1000

data = {
    'route_deviation_meters': np.random.randint(0, 3000, TOTAL_ROWS),
    'time_stopped_seconds': np.random.randint(0, 1500, TOTAL_ROWS),
    'traffic_density': np.random.choice([0, 1], TOTAL_ROWS), # 0=Low, 1=High
    'ambient_noise_db': np.random.randint(40, 110, TOTAL_ROWS)
}
df = pd.DataFrame(data)

def determine_anomaly(row):
    if row['time_stopped_seconds'] > 600 and row['traffic_density'] == 0:
        return 1
    if row['route_deviation_meters'] > 1000:
        return 1
    return 0

df['is_anomaly'] = df.apply(determine_anomaly, axis=1)
df.to_csv('transit_safety_data.csv', index=False)
print('Dataset generated successfully!')