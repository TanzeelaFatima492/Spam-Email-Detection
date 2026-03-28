
# 🚀 Spam Email Detection System

A Machine Learning based classification system to detect spam emails with high accuracy (98.57%)

---

## 📋 Project Overview

This project implements a binary classification system that automatically identifies whether an email is spam or legitimate (ham). Using various machine learning algorithms, we preprocess email data, extract meaningful features, and build predictive models to classify emails accurately.

### Problem Statement
With the increasing volume of emails received daily, spam detection has become crucial for email security and user productivity. This project aims to build an automated system that can distinguish spam emails from legitimate ones with high accuracy and minimal false positives.

---

## 👥 Team Members & Contributions

| Name | Roll Number | Responsibilities | Contribution |
|------|-------------|------------------|--------------|
| Tanzeela Fatima | 12 | Data Preprocessing, Model Building, Evaluation, Code Implementation | 50% |
| Atif Zaheer | 7 | EDA, Visualization, Presentation, Panaflex Design | 50% |

---

## 📊 Dataset Information

**Source:** SMS Spam Collection v.1 (UCI Machine Learning Repository)

| Feature | Description |
|---------|-------------|
| label | 'spam' or 'ham' |
| message | SMS text content |
| Samples | 5,574 messages |
| Spam | 747 messages (13.4%) |
| Ham | 4,827 messages (86.6%) |

### 🔗 Dataset Links

- **UCI Repository:** https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
- **Direct Download:** https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv

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

```
Spam-Email-Detection/
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_evaluation.ipynb
│
├── README.md
└── requirements.txt
```

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
```

---

## 📝 Conclusion

The Random Forest model achieved the best performance with **98.57% accuracy**, correctly identifying 142 out of 149 spam messages and 960 out of 966 ham messages.

---

## 🔗 Links

- **GitHub Repository:** https://github.com/TanzeelaFatima492/Spam-Email-Detection
- **Dataset:** https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

---

## 🙏 Acknowledgments

- **Mam Naila** – Course Instructor
- **Atif Zaheer** – Project Partner

---

## 📧 Contact

| Name | Roll Number |
|------|-------------|
| Tanzeela Fatima | 12 |
| Atif Zaheer | 7 |

---

**Course:** Machine Learning  
**Submission Date:** 20-04-26  
**Supervisor:** Mam Naila

---

⭐ Star this repository if you found it helpful!
