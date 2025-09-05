import os
from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import joblib

# ------------------------------
# Define paths (robust for scripts/ folder)
# ------------------------------
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # HousePrice folder
template_dir = os.path.join(base_dir, 'templates')
model_path = os.path.join(base_dir, 'models', 'final_pipeline.pkl')

# ------------------------------
# Initialize Flask
# ------------------------------
app = Flask(__name__, template_folder=template_dir)

# Load trained pipeline
pipeline = joblib.load(model_path)

# ------------------------------
# Flask routes
# ------------------------------
@app.route("/", methods=["GET", "POST"])
def upload_file():
    tables = None
    if request.method == "POST":
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file:
            df = pd.read_csv(file)
            # Predict log SalePrice
            pred_log = pipeline.predict(df)
            pred_original = np.expm1(pred_log)
            df['Predicted_SalePrice'] = np.round(pred_original, 2)
            tables = df.to_html(classes='data', header="true", index=False)
    return render_template("index.html", tables=tables)

# ------------------------------
# Run app
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)