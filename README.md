# 🌾 Global Crop Yield Prediction: Project "The Outliers"
**An End-to-End Machine Learning & Data Engineering Solution for Food Security**

## 👥 The Team: "The Outliers"

### Leadership & Data Engineering
- **Project Lead:** [Saviour Amegayie](https://github.com/Delkay-byte)
- **Assistant Lead:** [Yakubu Naomi Idiakheua](https://github.com/Naomi123-creator)
### Core Contributors
- [Sule Gideon Adinoyi ](https://github.com/GIDEON-1960)
- [Iroanya David](https://github.com/son-of-man47)
- [Umazayi Success Adinoyi](https://github.com/Success007T)
- [Mariam Morohunfola](https://github.com/Mojisolar)
- [Habiba Adamu Abdulkadir](https://github.com/bebo-bee)
  
---

🏗️ Project Architecture
The following flowchart illustrates the technical journey from raw data ingestion to high-precision forecasting.

![Flowchart illustrating the technical journey from raw data ingestion to high-precision forecasting](path/to/your/image.png)
    
---

## 📌 Project Overview
Food security is a critical global challenge. This project leverages historical agricultural and climate data to predict crop yields (hg/ha) across multiple countries. By analysing the interplay among rainfall, temperature, and pesticide use, we provide a data-driven tool to support agricultural sustainability and strategic planning.

Our goal was to move beyond simple prediction and uncover the "Biological Realities" that drive global food production.

---

🏗️ Data Architecture & Engineering
The foundation of this project is a high-performance ETL (Extract, Transform, Load) pipeline that unified four disjointed raw files into a single, high-integrity "Master Clean" dataset.

### 1. The Data Evolution (Refinement Pipeline)
To ensure the model learned from truth rather than noise, we moved the data through a multi-stage validation funnel:

* **Raw Ingestion:** Merged four independent sources (Rainfall, Temperature, Pesticides, and Yield), resulting in an initial "Dirty Master" set of ~28,000 records.

* **Deduplication & Quality Control:** Identified and removed over 2,000 redundant entries and overlapping data points, refining the set to 25,932 unique, high-quality records.

* **Final Expansion:** Through final feature engineering and the inclusion of the complete historical cycle, the pipeline delivered a robust 45,540 records for the champion model training.

### 2. Data Cleaning & The "99% Rule"
* **Outlier Capping:** We applied a **99th percentile cap** (Winsorization) to the yield data. This removed "impossible" values and dirty data while preserving the signal of elite, high-performing countries.
* **Deduplication:** Successfully refined the dataset from 52,252  to **45,540 high-quality records**.

### 3. The "Honest Model" Validation
To prevent "Data Leakage," we stress-tested our features:
* **Target Encoding:** Used to capture the productivity reputation of specific Crops and Areas.
* **One-Hot Encoding (OHE):** We re-ran all models with OHE to ensure the model wasn't "memorising" averages. Consistent results confirmed the model's strong predictive performance.

---

## 📊 Exploratory Data Analysis (EDA)
Our analysis discovered three critical "Sweet Spots":
* **The Temperature Ceiling:** Yields peak between **15°C and 20°C**; production significantly drops when average surface temperatures exceed 25°C.
* **The Pesticide Plateau:** Increased chemical use correlates with yield only up to a specific threshold, after which we observe diminishing returns.
* **Geographical Dominance:** Identified a "Top 10" cohort of countries (including the UK, Belgium, and Denmark) that consistently double the global average yield through superior infrastructure even in varied climates.

---

## 🧠 Machine Learning: The Battle of the Models
We conducted a "Model Battleground" to identify the most robust algorithm for agricultural forecasting.

| Model | $R^2$ Score | MAE (Mean Absolute Error) | Verdict |
| :--- | :--- | :--- | :--- |
| **Random Forest** | **0.9913** | **2,261 hg/ha** | **🏆 Champion** |
| **Decision Tree** | 0.9814 | 3,233 hg/ha | Strong Performer |
| **XGBoost** | 0.9850 | 10,655 hg/ha | Good Performer |
| **Linear Regression**| 0.7300 | 30,339 hg/ha | Baseline |

### Why Random Forest Won
The **Random Forest Regressor** achieved a near-perfect **99.1% accuracy**. Unlike linear models, it successfully captured nonlinear biological relationships (e.g., that more rain is beneficial but too much rain is catastrophic).

---

## 📈 Key Insights: The "Secret Sauce"
By analysing **Feature Importance**, we discovered the hierarchy of what truly drives yield:
1. **Crop Identity (Item):** The single most important factor. Potatoes, Sweet Potatoes, and Cassava are the primary drivers of yield weight.
2. **Geography (Area):** Regional efficiency and soil quality (represented by Area) are 5x more predictive than annual temperature fluctuations.
3. **The "Human-Nature" Balance:** Rainfall and Pesticides act as the "fine-tuners" that allow a crop to reach its maximum genetic potential. The pesticide usage and rainfall carry nearly equal importance, proving human inputs are now as decisive as the climate.

---

## 🗺️ Strategic Implications

### 🚜 For Farmers: Decision Support
* **Input Optimisation:** Our model identifies the "Pesticide Plateau," allowing farmers to potentially reduce chemical costs by 15% without sacrificing yield by optimising application timing.
* **Risk Assessment:** Farmers can use climate forecasts to predict if a specific crop choice is viable for the upcoming season, reducing the risk of total harvest failure.

### 🏛️ For Policy Makers: Planning & Security
* **Infrastructure over Subsidies:** Because "Area" is a top predictor, governments should prioritise long-term irrigation and soil health over short-term subsidies. The stability of the "Belgium Model" is more sustainable than reactive weather subsidies.
* **Market Stabilisation:** With 99% accurate yield forecasting, governments can manage food storage and export logistics months in advance to prevent price spikes.

---

## 🚀 How to Run
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Delkay-byte/Predictive-Agriculture-Analysis.git](https://github.com/Delkay-byte/Predictive-Agriculture-Analysis.git)
2. **Install dependencies:**
   !pip install pandas numpy matplotlib seaborn scikit-learn xgboost category_encoders
3. **Execution:**
   Run *Predictive_Agriculture_Analysis.ipynb* to reproduce the ETL pipeline, EDA, and model training.

---

## 📝 Future Scope
* **Soil Nutrient Integration:** Adding NPK (Nitrogen, Phosphorus, Potassium) levels for localised field-level predictions.
* **Real-time Dashboard:** Developing a Streamlit or Flask app for real-time "What-If" analysis for smallholder farmers.
