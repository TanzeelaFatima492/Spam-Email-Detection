# 🚀 Spam Email Detection System

> A Machine Learning based classification system to detect spam emails with high accuracy (98.57%)

---

## 📋 Project Overview

This project implements a binary classification system that automatically identifies whether an email is spam or legitimate (ham). Using various machine learning algorithms, we preprocess email data, extract meaningful features, and build predictive models to classify emails accurately.

### Problem Statement
With the increasing volume of emails received daily, spam detection has become crucial for email security and user productivity. This project aims to build an automated system that can distinguish spam emails from legitimate ones with high accuracy and minimal false positives.

---

## 👥 Team Members & Contributions

| Name | Roll Number | Responsibilities | Contribution |
|------|-------------|------------------|--------------|
| **Tanzeela Fatima** | 12 | Data Preprocessing, Model Building, Evaluation, Code Implementation | 50% |
| **Atif Zaheer** | 7 | EDA, Visualization, Presentation, Panaflex Design | 50% |

### Detailed Contribution Breakdown

#### 🔹 Tanzeela Fatima (Roll No: 12) - Data Preprocessing & Model Development

| Task | Description |
|------|-------------|
| Data Collection | Sourcing and downloading the SMS Spam Collection dataset |
| Data Cleaning | Handling missing values, removing duplicates, text cleaning |
| Feature Engineering | TF-IDF vectorization, feature extraction |
| Model Implementation | Logistic Regression, Random Forest, SVM |
| Model Evaluation | Accuracy, precision, recall, F1-score |
| Report Writing | Methodology section, results section |

#### 🔹 Atif Zaheer (Roll No: 7) - EDA, Visualization & Presentation

| Task | Description |
|------|-------------|
| Data Exploration | Statistical analysis, class distribution |
| Text Analysis | Word clouds, frequent words analysis |
| Visualization | Correlation heatmaps, distribution plots |
| Flowchart Creation | System architecture and methodology flowchart |
| Presentation Design | 15-slide PowerPoint with animations |
| Panaflex Design | A1 size panaflex layout and content |
| Report Compilation | Introduction, EDA section, conclusion |

---

## 📊 Dataset Information

**Source:** SMS Spam Collection v.1 (UCI Machine Learning Repository)

| Feature | Description |
|---------|-------------|
| **label** | 'spam' or 'ham' |
| **message** | SMS text content |
| **Samples** | 5,574 messages |
| **Spam** | 747 messages (13.4%) |
| **Ham** | 4,827 messages (86.6%) |

### 🔗 Dataset Links

| Link | Description |
|------|-------------|
| [UCI Repository](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection) | Original dataset source |
| [Direct Download](https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv) | Direct TSV file link |
| [GitHub Mirror](https://github.com/justmarkham/pycon-2016-tutorial/blob/master/data/sms.tsv) | GitHub hosted version |

---

## 🛠️ Technologies Used

| Category | Tools/Libraries |
|----------|-----------------|
| Data Processing | Pandas, NumPy, re |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Development | Google Colab, Jupyter Notebook |
| Version Control | Git, GitHub |

---

## 📈 Results

### Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 98.21% | 0.9714 | 0.9524 | 0.9618 |
| Random Forest | **98.57%** | **0.9800** | 0.9524 | **0.9660** |
| SVM | 98.30% | 0.9762 | 0.9524 | 0.9641 |

**🏆 Best Model: Random Forest with 98.57% accuracy**

### Confusion Matrix - Random Forest

| | Predicted Ham | Predicted Spam |
|---|---|---|
| **Actual Ham** | 960 | 6 |
| **Actual Spam** | 7 | 142 |

- True Negatives (Ham correct): 960
- False Positives (Ham as Spam): 6
- False Negatives (Spam as Ham): 7
- True Positives (Spam correct): 142

### Key Findings
- Random Forest outperformed other algorithms with 98.57% accuracy
- Feature importance shows words like "free", "win", "click" are strong spam indicators
- TF-IDF with n-grams (1,2) performed better than unigrams alone
- Only 13 misclassifications out of 1,115 test messages

---

## 📁 Project Structure

 
---

## 🚀 How to Run

### Option 1: Google Colab (Recommended)

1. Open [Google Colab](https://colab.research.google.com)
2. Upload notebooks from `notebooks/` folder
3. Run in order:
   - `01_data_preprocessing.ipynb`
   - `02_feature_engineering.ipynb`
   - `03_model_training.ipynb`
   - `04_evaluation.ipynb`

### Option 2: Local Machine

```bash
# Clone repository
git clone https://github.com/TanzeelaFatima492/Spam-Email-Detection.git
cd Spam-Email-Detection

# Install dependencies
pip install -r requirements.txt

# Run notebooks in Jupyter
jupyter notebook notebooks/
