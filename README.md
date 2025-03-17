# Energy-Consumption-Forecasting
End to End Data Science project-Energy Consumption Forecasting
Here's a structured **README.md** template tailored for your **Energy Consumption Forecasting** project — excluding the web application part. This format will highlight your project's key elements, methodologies, and results effectively on GitHub.  

---

# **Energy Consumption Forecasting 🚀**

### 📋 **Project Overview**
This project aims to predict energy consumption based on weather conditions using machine learning models like **LightGBM**, **XGBoost**, and **RandomForestRegressor**. The dataset includes features such as temperature, wind speed, and sunlight duration to improve forecasting accuracy.

---

## 📂 **Project Structure**
```
📦 Energy_Consumption_Forecasting
 ┣ 📂 data
 ┃ ┣ 📄 train.csv
 ┃ ┣ 📄 test.csv
 ┣ 📂 notebooks
 ┃ ┣ 📄 01_EDA.ipynb
 ┃ ┣ 📄 02_Feature_Engineering.ipynb
 ┃ ┣ 📄 03_Model_Training.ipynb
 ┃ ┗ 📄 04_Evaluation.ipynb
 ┣ 📂 models
 ┃ ┣ 📄 final_lightgbm_model.pkl
 ┃ ┗ 📄 final_xgboost_model.pkl
 ┣ 📜 requirements.txt
 ┣ 📄 README.md
 ┗ 📄 .gitignore
```

---

## 📊 **Dataset Description**
| Feature Name                | Description |
|:----------------------------|:------------|
| `lag_1h`                     | Energy consumption recorded 1 hour prior |
| `SunlightTime/daylength`     | Duration of daylight in hours |
| `clouds_all`                 | Cloud coverage in percentage |
| `temp`                       | Temperature in Celsius |
| `wind_speed`                 | Wind speed in m/s |

---

## ⚙️ **Data Preprocessing**
Key steps in data preprocessing:  
✅ Handling missing values  
✅ Capping extreme outliers  
✅ Creating lag features to capture temporal patterns  
✅ Encoding categorical variables  

---

## 🔍 **Model Development**
The following models were trained and evaluated:  
- **RandomForestRegressor**  
- **XGBoost**  
- **LightGBM** (Final Model)  

**Best Model:** LightGBM with parameters:  
```json
{
    "colsample_bytree": 1.0,
    "learning_rate": 0.05,
    "max_depth": 8,
    "min_child_samples": 30,
    "n_estimators": 200,
    "num_leaves": 20,
    "subsample": 0.7
}
```

---

## 📈 **Performance Metrics**
| Model   | R² Score | RMSE |
|:---------|:----------|:--------|
| **LightGBM (Final Model)** | **0.9359** | **246.09** |
| XGBoost                    | 0.9345      | 248.63      |
| RandomForestRegressor       | 0.9301      | 252.12      |

---

## 📋 **Key Insights**
✅ LightGBM outperformed other models with superior R² score and lower RMSE.  
✅ Outliers were capped instead of removed to preserve real-world energy spikes.  
✅ The model effectively captures patterns driven by temperature, sunlight, and wind speed.


---

## 📝 **Future Improvements**
🔹 Integrate additional weather features like humidity or pressure.  
🔹 Fine-tune model hyperparameters using Bayesian Optimization for improved performance.  
🔹 Deploy the model via a web interface (Flask/Django).  

---

## 🤝 **Contributing**
Contributions are welcome! Feel free to open issues or submit pull requests.

---
