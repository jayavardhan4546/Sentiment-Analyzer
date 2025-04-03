from flask import Flask, render_template, request
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import matplotlib.pyplot as plt
from collections import Counter
import os

nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

app = Flask(__name__)

# Load emotions from file
emotion_dict = {}
with open('emotions.txt', 'r') as file:
    for line in file:
        clean_line = line.strip().replace(",", "").replace("'", "")
        if ":" in clean_line:
            word, emotion = clean_line.split(":")
            emotion_dict[word.strip()] = emotion.strip()

# Function to clean and tokenize text
def clean_text(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    words = [WordNetLemmatizer().lemmatize(word) for word in words if word not in stopwords.words('english')]
    return words

# Sentiment Analysis Function
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    if score['compound'] >= 0.05:
        return "Positive"
    elif score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Emotion Detection Function
def analyze_emotions(text):
    words = clean_text(text)
    detected_emotions = [emotion_dict[word] for word in words if word in emotion_dict]
    return detected_emotions

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        if text:
            sentiment = analyze_sentiment(text)
            emotions = analyze_emotions(text)

            # Count emotions and plot
            emotion_counts = Counter(emotions)
            if emotion_counts:
                plt.figure(figsize=(6, 4))
                plt.bar(emotion_counts.keys(), emotion_counts.values(), color='skyblue')
                plt.xlabel("Emotions")
                plt.ylabel("Count")
                plt.title("Emotion Analysis")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig("static/graph.png")
                plt.close()

            return render_template("result.html", text=text, sentiment=sentiment, emotions=emotions)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
