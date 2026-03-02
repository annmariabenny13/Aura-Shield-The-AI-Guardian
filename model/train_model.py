import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

df = pd.read_csv('../transit_safety_data.csv')
X = df[['route_deviation_meters', 'time_stopped_seconds', 'traffic_density', 'ambient_noise_db']]
y = df['is_anomaly']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')
print('Model trained and saved!')