from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import joblib
from sklearn.feature_extraction.text import CountVectorizer

# Initialize NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Initialize Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Load the logistic regression model for sentiment analysis
logistic_regression_model = joblib.load('data/Optimized_lr_model.pkl')

# Load the random forest regression model for subjectivity analysis
random_forest_model = joblib.load('data/Optimized_subjective_rf_model.pkl')

# Load the CountVectorizer used during training
count_vectorizer = joblib.load('data/count_vectorizer.pkl')

def preprocess_text(text):
    # Define the preprocess_text function
    # Step 1: Remove non-alphabetic characters and convert to lowercase
    text = re.sub("[^a-zA-Z]", " ", text.lower())

    # Step 2: Tokenize the text
    tokens = word_tokenize(text)

    # Step 3: Lemmatize tokens
    lemma = WordNetLemmatizer()
    tokens = [lemma.lemmatize(word) for word in tokens]

    # Step 4: Join tokens back into a string
    processed_text = ' '.join(tokens)

    return processed_text

def predict_sentiment_and_subjectivity(preprocessed_text):
    # Transform the preprocessed text into a numeric vector
    numeric_vector = count_vectorizer.transform([preprocessed_text])

    # Make prediction using logistic regression model for sentiment analysis
    sentiment_prediction = logistic_regression_model.predict(numeric_vector)[0]
    if sentiment_prediction == 0:
        sentiment_label = 'Positive'
    elif sentiment_prediction == 1:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    # Make prediction using random forest regression model for subjectivity analysis
    subjectivity_prediction = random_forest_model.predict(numeric_vector)[0]

    # Return the predictions
    return sentiment_label, subjectivity_prediction

# Route to handle POST requests
@app.route('/predict', methods=['POST'])
def predict():
    # Get and define the text from POST request
    text = request.json['text']

    # Preprocess the text
    preprocessed_text = preprocess_text(text)

    # Get predictions
    sentiment, subjectivity = predict_sentiment_and_subjectivity(preprocessed_text)

    # Return predictions as JSON
    return jsonify({
        'Sentimiento': sentiment,
        '% de Subjetividad': subjectivity
    })

if __name__ == '__main__':
    app.run(debug=True)
