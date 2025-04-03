# 🎭 Sentiment Analysis Website  

## 📌 Overview  

This project is a **web-based sentiment analysis tool** that classifies text as **positive, negative, or neutral** using **Natural Language Processing (NLP)**.  

## ✨ Features  

- Analyzes text sentiment using **NLTK’s VADER Sentiment Analyzer**.  
- Processes text in **real-time** and classifies sentiment.  
- Uses **Flask** to provide a web interface.  
- Displays **percentage-based sentiment scores**.  

## 📂 Files in the Project  

- `app.py` – The main Flask application.  
- `templates/index.html` – Frontend interface.  
- `static/style.css` – CSS styling.  
- `requirements.txt` – Lists dependencies.  

## 🔍 How It Works  

1️⃣ The user **enters text** in the input field.  
2️⃣ The application **cleans** the text (removes punctuation, converts to lowercase).  
3️⃣ The text is analyzed using **NLTK’s VADER Sentiment Analyzer**.  
4️⃣ The sentiment scores (**Positive, Negative, Neutral**) are **calculated**.  
5️⃣ The result is **displayed** on the website.  

## 📊 Example  

**Input:** `"I love this product! It's amazing."`  
**Sentiment Output:** ✅ **Positive (85%)**  

---

**Input:** `"This is the worst experience ever."`  
**Sentiment Output:** ❌ **Negative (80%)**  

## 🚀 Future Enhancements  

- **Support for multiple languages**.  
- **Social media sentiment analysis**.  
- **Machine Learning-based improvements**.  

## 📜 License  

This project is **open-source**. Feel free to use and modify it. 🎉  
