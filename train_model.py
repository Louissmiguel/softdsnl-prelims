import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'temperature': [30, 22, 35, 18, 25, 27, 32, 15, 20, 28],
    'humidity':    [70, 90, 40, 95, 65, 55, 50, 100, 85, 60],
    'wind_speed':  [5, 2, 7, 1, 4, 6, 3, 0, 2, 5],
    'condition':   ['Sunny', 'Rainy', 'Sunny', 'Foggy', 'Windy', 'Windy', 'Sunny', 'Foggy', 'Rainy', 'Windy']
}

df = pd.DataFrame(data)

# Features & labels
X = df[['temperature', 'humidity', 'wind_speed']]
y = df['condition']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model to file
joblib.dump(model, 'weather_model.pkl')
print("✅ Model trained and saved as weather_model.pkl")

# Visualize relationships
sns.pairplot(df, hue='condition')  # <- fixed line here
plt.tight_layout()
plt.show()
