# Sentiment Analysis Website  

## Overview  

This project is a web-based sentiment analysis tool that classifies text as **positive, negative, or neutral** using **Natural Language Processing (NLP)** techniques. It processes user-inputted text and determines the sentiment score based on the words and phrases used.  

## Features  

- Analyzes text sentiment using **NLTK’s VADER Sentiment Analyzer**.  
- Processes text in **real-time** and classifies sentiment as **positive, negative, or neutral**.  
- Uses **Flask** to provide a web interface for easy interaction.  
- Displays **percentage-based sentiment scores** for better understanding.  

## Files in the Project  

- **app.py** – The main Flask application that handles text processing.  
- **templates/index.html** – The HTML frontend for user interaction.  
- **templates/result.html** – The HTML frontend for giving result.
- **requirements.txt** – Lists all necessary Python dependencies.  

## How It Works  

### **Step 1: User Input**  
- The user enters a text passage in the provided input field on the website.  
- This text is then sent to the Flask backend for processing.  

### **Step 2: Preprocessing the Text**  
- The application **cleans the input** by removing:  
  - Special characters  
  - Punctuation  
  - Extra spaces  
- The text is **converted to lowercase** for uniform analysis.  
- The words are **tokenized** (split into individual words for analysis).  

### **Step 3: Sentiment Analysis**  
- The cleaned text is processed using **NLTK’s VADER Sentiment Analyzer**.  
- The analyzer assigns sentiment scores:  
  - **Positive Score** – Represents positive words in the text.  
  - **Negative Score** – Represents negative words in the text.  
  - **Neutral Score** – Represents words with neutral meaning.  
- The overall sentiment is determined based on the highest score.  

### **Step 4: Displaying the Results**  
- The computed sentiment scores are converted into percentages.  
- The sentiment classification (**Positive, Negative, or Neutral**) is displayed.  
- The results are sent back to the frontend and shown to the user.  

## Example Processing  

### **Input Text:**  
*"I love this product! It's amazing and works perfectly."*  

### **Preprocessed Text:**  
`['love', 'product', 'amazing', 'works', 'perfectly']`  

### **Sentiment Scores:**  
- Positive: **85%**  
- Neutral: **10%**  
- Negative: **5%**  

### **Final Output:**  
- **Sentiment: Positive**  
- **Displayed Message:** "Your text expresses a positive sentiment!"  

---

### **Input Text:**  
*"This is the worst experience ever. I hate it!"*  

### **Preprocessed Text:**  
`['worst', 'experience', 'hate']`  

### **Sentiment Scores:**  
- Positive: **5%**  
- Neutral: **15%**  
- Negative: **80%**  

### **Final Output:**  
- **Sentiment: Negative**  
- **Displayed Message:** "Your text expresses a negative sentiment!"  

---

## Future Enhancements  

- **Support for multiple languages** using advanced NLP models.  
- **Integration with social media APIs** (Twitter, Reddit) for live sentiment tracking.  
- **Machine Learning-based classification** to improve accuracy.  
- **Graphical representation of sentiment trends** for visualization.  

## License  

This project is open-source. Feel free to use, modify, and improve it.  
