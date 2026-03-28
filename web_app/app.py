# app.py

from flask import Flask, request, render_template_string
import joblib
import re
import os

# Check if model files exist
if not os.path.exists('best_model.pkl'):
    print("❌ Error: best_model.pkl not found!")
    print("Please run: python create_model.py first")
    exit()

if not os.path.exists('tfidf_vectorizer.pkl'):
    print("❌ Error: tfidf_vectorizer.pkl not found!")
    print("Please run: python create_model.py first")
    exit()

# Load model and vectorizer
print("📂 Loading model...")
model = joblib.load('best_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')
print("✅ Model loaded successfully!")

app = Flask(__name__)

def clean_text(text):
    """Clean the input text"""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def predict_spam(message):
    """Predict if message is spam or ham"""
    cleaned = clean_text(message)
    transformed = tfidf.transform([cleaned])
    pred = model.predict(transformed)[0]
    return "SPAM" if pred == 1 else "HAM"

# HTML Template
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Spam Detector</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            padding: 40px;
            max-width: 600px;
            width: 100%;
            text-align: center;
        }
        
        h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 28px;
        }
        
        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 14px;
        }
        
        textarea {
            width: 100%;
            height: 150px;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
            font-family: inherit;
            resize: vertical;
            transition: border-color 0.3s;
        }
        
        textarea:focus {
            outline: none;
            border-color: #667eea;
        }
        
        button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 16px;
            border-radius: 25px;
            cursor: pointer;
            margin-top: 20px;
            transition: transform 0.2s;
        }
        
        button:hover {
            transform: scale(1.05);
        }
        
        .result-box {
            margin-top: 30px;
            padding: 20px;
            border-radius: 10px;
            animation: fadeIn 0.5s;
        }
        
        .spam {
            background: #fee;
            border-left: 4px solid #e74c3c;
        }
        
        .ham {
            background: #e8f5e9;
            border-left: 4px solid #2ecc71;
        }
        
        .result-label {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        
        .spam .result-label {
            color: #e74c3c;
        }
        
        .ham .result-label {
            color: #2ecc71;
        }
        
        .result-message {
            font-size: 14px;
            color: #666;
            word-break: break-all;
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .examples {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
        }
        
        .examples h3 {
            color: #666;
            font-size: 14px;
            margin-bottom: 10px;
        }
        
        .example-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }
        
        .example-btn {
            background: #f0f0f0;
            color: #333;
            padding: 8px 15px;
            font-size: 12px;
            border-radius: 20px;
            cursor: pointer;
            transition: background 0.2s;
        }
        
        .example-btn:hover {
            background: #e0e0e0;
            transform: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📧 Spam Detector</h1>
        <p class="subtitle">Check if a message is SPAM or HAM (legitimate)</p>
        
        <form method="POST">
            <textarea name="message" placeholder="Type or paste your message here...">{{ message if message else '' }}</textarea>
            <br>
            <button type="submit">🔍 Check Message</button>
        </form>
        
        {% if result %}
        <div class="result-box {{ 'spam' if result == 'SPAM' else 'ham' }}">
            <div class="result-label">
                {% if result == 'SPAM' %}
                🚨 SPAM DETECTED!
                {% else %}
                ✅ HAM - Safe Message
                {% endif %}
            </div>
            <div class="result-message">
                <strong>Message:</strong> {{ message[:100] }}{% if message|length > 100 %}...{% endif %}
            </div>
        </div>
        {% endif %}
        
        <div class="examples">
            <h3>📝 Try these examples:</h3>
            <div class="example-buttons">
                <span class="example-btn" onclick="setMessage('Congratulations! You won a free iPhone! Click here to claim now!')">Spam Example</span>
                <span class="example-btn" onclick="setMessage('Hey, are we still meeting for lunch tomorrow?')">Ham Example</span>
                <span class="example-btn" onclick="setMessage('URGENT: Your account has been compromised! Verify now!')">Urgent Spam</span>
                <span class="example-btn" onclick="setMessage('Can you please send me the assignment by evening?')">Student Message</span>
            </div>
        </div>
    </div>
    
    <script>
        function setMessage(msg) {
            document.querySelector('textarea').value = msg;
        }
    </script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    message = ''
    
    if request.method == 'POST':
        message = request.form.get('message', '')
        if message:
            result = predict_spam(message)
    
    return render_template_string(HTML, result=result, message=message)

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Spam Detector Web App Starting...")
    print("="*50)
    print("📱 Open your browser and go to: http://127.0.0.1:5000")
    print("🔴 Press CTRL+C to stop the server")
    print("="*50 + "\n")
    app.run(debug=True)
