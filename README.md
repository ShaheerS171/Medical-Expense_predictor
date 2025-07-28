# 🧠 Medical Charges Prediction with Machine Learning

This project predicts individual medical insurance charges based on features like age, BMI, smoking status, region, and more. The aim is to build a reliable regression model that can help insurance companies estimate future charges for new clients.

---

## 📌 Dataset

- **Source**: [Kaggle - Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Features**:
  - `age`: Age of primary beneficiary
  - `sex`: Gender
  - `bmi`: Body Mass Index
  - `children`: Number of children covered by health insurance
  - `smoker`: Smoking status
  - `region`: Residential area
  - `charges`: Medical costs billed (target variable)

---

## 🔍 Exploratory Data Analysis (EDA)

- Checked for null values and duplicates
- Visualized distributions of `charges`, `age`, `bmi`
- Used boxplots and histograms to detect outliers
- Explored relationships between categorical features and charges using bar plots and swarm plots

---

## 📊 Data Preprocessing

- Label Encoding & One-Hot Encoding applied where necessary
- Used `StandardScaler` to scale numerical features (only selected columns)
- Handled feature transformation using `PolynomialFeatures` where needed

---

## 🤖 Models Used

1. **Linear Regression** (baseline)
2. **Random Forest Regressor** (final model)

- Evaluated using:
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - R² Score

---

## 🧪 Best Model (Random Forest with GridSearchCV)

- Tuned hyperparameters: `n_estimators`, `max_depth`, `min_samples_split`
- Best Performance:
  - **MAE**: 2620.14
  - **RMSE**: 4436.48
  - **R² Score**: 0.873

---

## 💡 Future Improvements

- Integrate more advanced models like XGBoost or LightGBM
- Add polynomial interaction terms between features like `age` × `bmi`
- Perform feature selection to reduce dimensionality
- Add cross-validation visualization and learning curves
- Deploy the model using **Streamlit** (in progress 🔧)
- Add a frontend UI for user input
- Add API endpoints using Flask or FastAPI for scalability

---

## 🚀 How to Run

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
