import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
import os

os.makedirs("./model", exist_ok=True)
os.makedirs("./results", exist_ok=True)
os.makedirs("./app/artifacts", exist_ok=True)

# Load dataset
df = pd.read_csv("./data/wine_quality.csv")
X = df.drop(["quality","Unnamed: 0"], axis=1)
y = df["quality"]

# Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Model
model = Lasso(alpha=0.1)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse}")
print(f"R2 Score: {r2}")

# Save model
joblib.dump(model, "./model/model.pkl")

results = {
    "MSE": mse,
    "R2": r2,
    "accuracy": r2  # Using R2 score as accuracy metric for regression
}

with open("./app/artifacts/metrics.json", "w") as f:
    json.dump(results, f, indent=4)
