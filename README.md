# 🌾 Global Crop Yield Prediction: Project "The Outliers"
**An End-to-End Machine Learning & Data Engineering Solution for Food Security**

## 👥 The Team: "The Outliers"

### Leadership & Data Engineering
- **Project Lead / Data Engineering:** [Saviour Amegayie](https://github.com/your-profile)
- **Assistant Data Lead:** [Naomi](https://github.com/assistant-profile) — *Key focus on data validation and ETL pipeline integrity.*

### Squad Leads
- **ML Squad Lead:** [Name](https://github.com/profile-link)
- **Visualization Squad Lead:** [Name](https://github.com/profile-link)
- **Delivery & Docs Lead:** [Name](https://github.com/profile-link)

### Core Contributors
- [Member Name](https://github.com/profile-link) | [Member Name](https://github.com/profile-link)
- [Member Name](https://github.com/profile-link) | [Member Name](https://github.com/profile-link)

---

## 📌 Project Overview
Food security is a critical global challenge. This project (based on **Case Study 4: Agritech**) leverages historical agricultural and climate data to predict crop yields (**hg/ha**) across various countries. By analyzing the interplay between rainfall, temperature, and pesticide usage, we provide a data-driven tool for agricultural sustainability and strategic planning.

Our goal was to move beyond simple prediction and uncover the "Biological Realities" that drive global food production.

---

## 🏗️ Data Architecture & Engineering
The foundation of this project is a high-performance **ETL (Extract, Transform, Load)** pipeline that unified four disjointed raw files into a single "Master Clean" dataset.

### 1. Data Cleaning & The "99% Rule"
* **Outlier Capping:** We applied a **99th percentile cap** (Winsorization) to the yield data. This removed "impossible" values and dirty data while preserving the signal of elite, high-performing countries.
* **Deduplication:** Successfully refined the dataset from 28,000+ to **25,932 high-quality records** for the initial merge, eventually scaling to **~45,000** for modeling.

### 2. The "Honest Model" Validation
To prevent "Data Leakage," we stress-tested our features:
* **Target Encoding:** Used to capture the productivity reputation of specific Crops and Areas.
* **One-Hot Encoding (OHE):** We re-ran all models with OHE to ensure the model wasn't "memorizing" averages. The consistency in results confirmed the model's high predictive integrity.

---

## 📊 Exploratory Data Analysis (EDA)
Our analysis discovered three critical "Sweet Spots":
* **The Temperature Ceiling:** Yields peak between **15°C and 20°C**; production significantly drops when average surface temperatures exceed 25°C.
* **The Pesticide Plateau:** Increased chemical use correlates with yield only up to a specific threshold, after which we observe diminishing returns.
* **Geographical Dominance:** Identified a "Top 10" cohort of countries (including the UK, Belgium, and Denmark) that consistently double the global average yield through superior infrastructure.

---

## 🧠 Machine Learning: The Battle of the Models
We conducted a "Model Battleground" to identify the most robust algorithm for agricultural forecasting.

| Model | $R^2$ Score | MAE (Mean Absolute Error) | Verdict |
| :--- | :--- | :--- | :--- |
| **Random Forest** | **0.9937** | **2,233 hg/ha** | **🏆 Champion** |
| **XGBoost** | 0.9631 | 10,514 hg/ha | Strong Performer |
| **Linear Regression**| 0.7538 | 30,339 hg/ha | Baseline |

### Why the Champion Won
The **Random Forest Regressor** achieved a near-perfect **99.3% accuracy**. Unlike linear models, it successfully captured non-linear biological relationships (e.g., the fact that more rain is good, but *too much* rain is catastrophic).

---

## 📈 Key Insights: The "Secret Sauce"
By analyzing **Feature Importance**, we discovered the hierarchy of what truly drives yield:
1. **Crop Identity (Item):** The single most important factor. Potatoes and Sweet Potatoes are the global yield kings.
2. **Geography (Area):** Regional efficiency and soil quality (represented by Area) are 5x more predictive than annual temperature fluctuations.
3. **Environmental Amplifiers:** Rainfall and Pesticides act as the "fine-tuners" that allow a crop to reach its maximum genetic potential.

---

## 🗺️ Strategic Implications (Case Study Fulfillment)

### 🚜 For Farmers: Decision Support
* **Input Optimization:** Our model identifies the "Pesticide Plateau," allowing farmers to reduce chemical costs without sacrificing yield.
* **Risk Assessment:** Farmers can use climate forecasts to predict if a specific crop choice is viable for the upcoming season, reducing the risk of total harvest failure.

### 🏛️ For Policy Makers: Planning & Security
* **Infrastructure Investment:** Because "Area" is a top predictor, governments should prioritize long-term irrigation and soil health over short-term subsidies.
* **Market Stabilization:** With 99% accurate yield forecasting, governments can manage food storage and export logistics months in advance to prevent price spikes.

---

## 🚀 How to Run
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/repo-name.git](https://github.com/your-username/repo-name.git)
2. **Install dependencies:**
   pip install pandas numpy matplotlib seaborn scikit-learn xgboost category_encoders
3. **Execution:**
   Run Crop_Yield_ML.ipynb to reproduce the ETL pipeline, EDA, and model training.

---

## 📝 Future Scope
* **Soil Nutrient Integration:** Adding NPK (Nitrogen, Phosphorus, Potassium) levels for localized field-level predictions.
* **Real-time Dashboard:** Developing a Streamlit or Flask app for real-time "What-If" analysis for smallholder farmers.
