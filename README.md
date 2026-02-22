# 🌾 Global Crop Yield Prediction
**An End-to-End Machine Learning & Data Engineering Project**

## 👥 The Team: "The Outliers"

### Leadership & Data Engineering
- **Project Lead / Data Engineering:** [Deladem](https://github.com/your-profile)
- **Assistant Data Lead:** [Name](https://github.com/assistant-profile) — *Key focus on data validation and ETL pipeline integrity.*

### Squad Leads
- **ML Squad Lead:** [Name](https://github.com/profile-link)
- **Visualization Squad Lead:** [Name](https://github.com/profile-link)
- **Delivery & Docs Lead:** [Name](https://github.com/profile-link)

### Core Contributors
- [Member Name](https://github.com/profile-link)
- [Member Name](https://github.com/profile-link)
- [Member Name](https://github.com/profile-link)
- [Member Name](https://github.com/profile-link)

---

## 📌 Project Overview
Food security is a critical global challenge. This project leverages historical agricultural and climate data to predict crop yields (**hg/ha**) across various countries. By analyzing the interplay between rainfall, temperature, and pesticide usage, we provide a data-driven tool for agricultural sustainability and planning.

---

## 🏗️ Data Architecture
As the foundation of this project, we performed an extensive **ETL (Extract, Transform, Load)** process to move from four disjointed raw files into an integrated unified pipeline—a single "Master Clean" dataset. The data is sourced from **FAOSTAT** (Food and Agriculture Organization of the UN).



### 1. Data Sources
* **Yield Data:** Historical crop output per hectare ($hg/ha$).
* **Rainfall Data:** Average annual precipitation ($mm/year$).
* **Pesticide Data:** Annual usage in tonnes of active ingredients.
* **Temperature Data:** Average annual surface temperatures (°C).

### 2. Preprocessing & Engineering
Our pipeline ensures high-quality data through:
* **Standardization:** Unified naming conventions (e.g., converting 'country' and 'year' keys to match across all sources).
* **Cleaning:** Removal of leading whitespaces in headers and conversion of object-type weather data into numerical formats.
* **Integration:** Performed a multi-key `Inner Join` on `Year` and `Area`.
* **Deduplication:** Successfully identified and dropped redundant records, refining the dataset from 28,000+ to **25,932 high-quality records**.

---

## 📊 Exploratory Data Analysis (EDA)
> **Status:** *In Progress*
* **Objective:** Identify correlation patterns between environmental factors and yield.
* **Key Visualizations:**
    * Global yield distribution per crop type.
    * Temperature vs. Yield correlation heatmaps.
    * *[Placeholder: Insert visualization of pesticide impact over time]*

---

## 🧠 Machine Learning Modeling
> **Status:** *In Progress*
* **Target Variable ($y$):** `hg/ha_yield`
* **Features ($X$):** `Area`, `Item`, `Year`, `average_rain_fall_mm_per_year`, `pesticides_tonnes`, `avg_temp`.
* **Planned Algorithms:**
    1.  Linear Regression (Baseline)
    2.  Random Forest Regressor
    3.  XGBoost
* **Evaluation Metrics:** R-Squared ($R^2$), Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).



---

## 🚀 How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/repo-name.git](https://github.com/your-username/repo-name.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```
3.  **Execution:**
    Run `Crop_Yield_Main.ipynb` in a Jupyter environment to reproduce the preprocessing and training workflow.

---

## 📈 Results & Findings
> **Status:** *Placeholder*
* Final model performance metrics will be summarized here by the ML Squad.
* Analysis of the most influential factors (Feature Importance) affecting global crop production will follow.

---

## 📝 Future Scope
* Integration of soil quality and irrigation data.
* Expansion into real-time climate monitoring for predictive alerts.
* Development of a web-based dashboard for farmer decision support.
