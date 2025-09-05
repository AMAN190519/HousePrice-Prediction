import requests
import pandas as pd
import json
import os

# Load dataset
data_path = os.path.join("data", "house_prices_clean.csv")
df = pd.read_csv(data_path)

# Remove target columns to get only features
X = df.drop(['SalePrice','SalePrice_log'], axis=1)

# Take first row as template
template = X.iloc[0].to_dict()

# Save JSON template
artifact_path = os.path.join("artifacts", "input_template.json")
with open(artifact_path, "w") as f:
    json.dump(template, f, indent=4)
print(f"✅ JSON template saved as {artifact_path}")

# Load template for testing
with open(artifact_path, "r") as f:
    sample_input = json.load(f)

# Send POST request
url = "http://127.0.0.1:5000/predict"
response = requests.post(url, json=sample_input)

print("Flask API response:")
print(response.json())