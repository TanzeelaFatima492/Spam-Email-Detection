# 🚀 Spam Email Detection System

> A Machine Learning based classification system to detect spam emails with high accuracy

---

## 📋 Project Overview

This project implements a binary classification system that automatically identifies whether an email is spam or legitimate (ham). Using various machine learning algorithms, we preprocess email data, extract meaningful features, and build predictive models to classify emails accurately.

### Problem Statement
With the increasing volume of emails received daily, spam detection has become crucial for email security and user productivity. This project aims to build an automated system that can distinguish spam emails from legitimate ones with high accuracy and minimal false positives.

---

## 👥 Team Members & Contributions

| Name | Roll Number | Responsibilities | Contribution |
|------|-------------|------------------|--------------|
| **Tanzeela Fatima** | 12 | Data Preprocessing, Model Selection, Evaluation Metrics, Report Writing | 50% |
| **Atif Zaheer** | 7 | EDA, Visualization, Presentation, Panaflex Design | 50% |

### Detailed Contribution Breakdown

#### 🔹 Tanzeela Fatima (Roll No: 12) - Data Preprocessing & Model Development

| Task | Description | Deliverables |
|------|-------------|--------------|
| Data Collection | Sourcing and downloading the SMS Spam Collection dataset | `data/raw/` folder |
| Data Cleaning | Handling missing values, removing duplicates, text cleaning | `notebooks/01_data_cleaning.ipynb` |
| Feature Engineering | TF-IDF vectorization, feature extraction | `notebooks/03_feature_engineering.ipynb` |
| Model Implementation | Logistic Regression, Random Forest, SVM, XGBoost | `src/models.py` |
| Hyperparameter Tuning | GridSearchCV optimization for all models | `notebooks/04_hyperparameter_tuning.ipynb` |
| Model Evaluation | Accuracy, precision, recall, F1-score, ROC-AUC | `notebooks/05_evaluation.ipynb` |
| Report Writing | Methodology section, results section | `docs/report/methodology.md` |

#### 🔹 Atif Zaheer (Roll No: 7) - EDA, Visualization & Presentation

| Task | Description | Deliverables |
|------|-------------|--------------|
| Data Exploration | Statistical analysis, class distribution | `notebooks/01_eda.ipynb` |
| Text Analysis | Word clouds, frequent words analysis | `notebooks/02_text_analysis.ipynb` |
| Visualization | Correlation heatmaps, distribution plots | `notebooks/03_visualizations.ipynb` |
| Flowchart Creation | System architecture and methodology flowchart | `docs/flowchart.png` |
| Presentation Design | 15-slide PowerPoint with animations | `presentation/Project_Presentation.pptx` |
| Panaflex Design | A1 size panaflex layout and content | `panaflex/panaflex_design.ai` |
| Demo Setup | Live demo environment and explanation | `demo/` folder |
| Report Compilation | Introduction, EDA section, conclusion | `docs/report/introduction.md` |

---

## 📁 Project Structure with Owner Labels

spam-email-detection/
│
├── README.md # [Both] Project documentation
├── requirements.txt # [Tanzeela] Dependencies
│
├── data/
│ ├── raw/ # [Tanzeela] Original dataset
│ │ └── spam.csv
│ ├── processed/ # [Tanzeela] Cleaned data
│ │ └── spam_processed.csv
│ └── features/ # [Tanzeela] Extracted features
│ └── tfidf_features.npz
│
├── notebooks/
│ ├── 01_data_cleaning.ipynb # [Tanzeela]
│ ├── 02_eda.ipynb # [Atif]
│ ├── 03_feature_engineering.ipynb # [Tanzeela]
│ ├── 04_model_training.ipynb # [Tanzeela]
│ ├── 05_evaluation.ipynb # [Tanzeela]
│ └── 06_visualizations.ipynb # [Atif]
│
├── src/
│ ├── preprocess.py # [Tanzeela]
│ ├── features.py # [Tanzeela]
│ ├── models.py # [Tanzeela]
│ └── visualize.py # [Atif]
│
├── docs/
│ ├── report/
│ │ ├── 01_introduction.md # [Atif]
│ │ ├── 02_methodology.md # [Tanzeela]
│ │ ├── 03_results.md # [Tanzeela]
│ │ ├── 04_conclusion.md # [Both]
│ │ └── project_report.pdf # [Both]
│ ├── flowchart.png # [Atif]
│ └── methodology_diagram.pptx # [Atif]
│
├── presentation/ # [Atif]
│ ├── Project_Presentation.pptx
│ └── presentation_notes.md
│
├── panaflex/ # [Atif]
│ ├── panaflex_design.ai
│ └── panaflex_final.pdf
│
├── models/ # [Tanzeela]
│ ├── logistic_regression.pkl
│ ├── random_forest.pkl
│ ├── svm.pkl
│ └── xgboost_best.pkl
│
└── results/ # [Both]
├── confusion_matrix.png
├── roc_curves.png
├── feature_importance.png
└── model_comparison.csv



---

## 📊 Dataset Information

**Source:** SMS Spam Collection v.1 (UCI Machine Learning Repository)

| Feature | Description |
|---------|-------------|
| **v1** | Label: 'spam' or 'ham' |
| **v2** | Email message text |
| **Samples** | 5,574 messages |
| **Spam** | 747 messages (13.4%) |
| **Ham** | 4,827 messages (86.6%) |

---

## 🛠️ Technologies Used

| Category | Tools/Libraries | Responsible |
|----------|-----------------|-------------|
| Data Processing | Pandas, NumPy, re | Tanzeela |
| Visualization | Matplotlib, Seaborn, WordCloud | Atif |
| Machine Learning | Scikit-learn, XGBoost | Tanzeela |
| Model Evaluation | Scikit-learn metrics | Tanzeela |
| Presentation | PowerPoint, Canva | Atif |
| Report Writing | LaTeX/Markdown | Both |

---

## 📈 Results

### Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 98.2% | 0.97 | 0.95 | 0.96 | 0.99 |
| Random Forest | 98.5% | 0.98 | 0.96 | 0.97 | 0.99 |
| SVM | 98.3% | 0.97 | 0.95 | 0.96 | 0.99 |
| **XGBoost (Best)** | **98.7%** | **0.98** | **0.97** | **0.97** | **0.99** |

### Key Findings (By Atif's Visualization)
- XGBoost achieved the highest accuracy of 98.7%
- Feature importance shows that words like "free", "win", "click" are strong spam indicators
- TF-IDF with n-grams (1,2) performed better than unigrams alone

---

## 📝 Conclusion

The spam detection system successfully classifies emails with high accuracy. The XGBoost model outperformed other algorithms, achieving 98.7% accuracy with minimal false positives. This system can be integrated into email clients for real-time spam filtering.

---

## 📧 Contact

| Name | Roll Number | Email | GitHub |
|------|-------------|-------|--------|
| **Tanzeela Fatima** | 12 | tanzeela.fatima@university.edu | github.com/tanzeela |
| **Atif Zaheer** | 7 | atif.zaheer@university.edu | github.com/atif |

---

**Course:** Machine Learning  
**Submission Date:** 20-04-26  
**Supervisor:** Mam Naila
