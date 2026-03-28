# create_model.py - Run this first to create model files

import pandas as pd
import numpy as np
import re
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

print("="*50)
print("Creating Spam Detection Model...")
print("="*50)

# Load dataset
print("\n📂 Loading dataset...")
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

print(f"✅ Dataset loaded! Shape: {df.shape}")

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

print("\n📝 Cleaning text...")
df['cleaned_message'] = df['message'].apply(clean_text)
df['label_binary'] = df['label'].map({'spam': 1, 'ham': 0})

# Split data
X = df['cleaned_message']
y = df['label_binary']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training: {len(X_train)} samples")
print(f"Testing: {len(X_test)} samples")

# TF-IDF
print("\n📝 Applying TF-IDF...")
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

print(f"Features shape: {X_train_tfidf.shape}")

# Train Random Forest
print("\n🔹 Training Random Forest...")
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_tfidf, y_train)

# Evaluate
y_pred = rf.predict(X_test_tfidf)
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {acc:.4f}")

# Save model and vectorizer
print("\n💾 Saving model files...")
joblib.dump(rf, 'best_model.pkl')
joblib.dump(tfidf, 'tfidf_vectorizer.pkl')
print("✅ Saved: best_model.pkl")
print("✅ Saved: tfidf_vectorizer.pkl")

print("\n" + "="*50)
print("✅ Model created successfully!")
print("="*50)
print("\nNow run: python app.py")
