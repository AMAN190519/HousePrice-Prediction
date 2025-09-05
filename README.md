\# 🏠 House Price Prediction



This project implements an \*\*end-to-end machine learning pipeline\*\* to predict house prices using the \*\*Ames Housing dataset\*\*. The pipeline includes \*\*data preprocessing, model training, and deployment-ready saving\*\*, making it easy to use in applications like Flask or Streamlit.



\## 📌 Features



\- \*\*Preprocessing\*\*

&nbsp; - Numeric features: StandardScaler

&nbsp; - Categorical features: OneHotEncoder (handle unknown categories)

\- \*\*Model\*\*

&nbsp; - XGBRegressor (tuned hyperparameters)

\- \*\*Target\*\*

&nbsp; - Log-transformed SalePrice (`SalePrice\_log`) for better regression stability

\- \*\*Output\*\*

&nbsp; - Predicted house prices converted back to original scale using `np.expm1()`



\## 🛠️ Folder Structure



HousePriceProject/

│── data/

│   └── house\_prices\_clean.csv

│── models/

│   └── final\_pipeline.pkl

│── scripts/

│   ├── final\_pipeline.py       # Training script

│   ├── app.py                  # Flask API

│   └── test\_flask\_api.py       # Test script

│── artifacts/

│   └── input\_template.json     # Example JSON input

│── requirements.txt

│── README.md



\## ⚡ How to Run



1️⃣ Train Pipeline:  

`python scripts/final\_pipeline.py`  

\- Trains the model and saves it as `models/final\_pipeline.pkl`.



2️⃣ Run Flask API:  

`python scripts/app.py`  

\- Starts a local server at `http://127.0.0.1:5000/`.



-- Open your browser and go to http://127.0.0.1:5000/

-- Upload your CSV file (must contain the same features as used during training).

-- Click Upload & Predict. The predicted house prices will appear in a table below the form.

-- When finished, stop the Flask server by pressing CTRL+C in the terminal.


\## 📝 Notes

📝 Notes
	•	templates/index.html must be present in HousePrice/templates/.
	•	CSV must contain same features used during training.
	•	Predictions are converted from log-scale to original SalePrice scale.
	•	final_pipeline.pkl includes preprocessing + model, so no separate preprocessing is needed.



\## 📈 Results



\- Model: XGBRegressor with tuned hyperparameters

\- R² Score on training/validation: ~0.89

\- RMSE: ~28,000

\- Predictions are in USD (original SalePrice scale)



\## 📌 Contact 



\- Built by: Aman  

\- LinkedIn: https://www.linkedin.com/in/aman-kumar-318a9a377/ 

\- GitHub: 

