# pip install spacy textblob
# python -m spacy download en_core_web_sm

# Import necessary libraries.
import spacy 
import pandas as pd
from textblob import TextBlob

# Load the English language model from spaCy.
nlp = spacy.load('en_core_web_sm')

# Read amazon_product_reviews in as dataframe using pandas.
df = pd.read_csv('amazon_product_reviews.csv')

# Isolate reviews column of interest.
reviews_data = df['reviews.text']

# Clean data by removing missing values.
clean_data = df.dropna(subset=['reviews.text'])

# Preprocess by converting to spaCy doc and removing stop words and punctuation.
def preprocess(text):
    doc = nlp(str(text))
    return ' '.join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])

# Create a function that will preprocess input and calculate polarity.
def sentiment_analysis(x):
    preprocessed_input = preprocess(x)
    blob = TextBlob(preprocessed_input)
    polarity = blob.sentiment.polarity

    return polarity

# Call above function for the first 50 rows of reviews.
for text in reviews_data.head(50):
    polarity_score = sentiment_analysis(text)
    print (polarity_score)
# Define positive, neutral and negative sentiments.
    if polarity_score > 0:
        sentiment = 'positive'
    elif polarity_score < 0:
        sentiment = 'negative'
    else:
        semtiment = 'neutral'
# Print the review, its polarity score and its sentiment.
    print(f"Text: {text}\nPolarity score: {polarity_score}\nSentiment: {sentiment}")

# Select 2 reviews from reviews column to compare their similarity. 
my_review_of_choice = nlp(reviews_data[5])
review_to_compare = nlp(reviews_data[500])
# Calculate similarity score of these 2 reviews.
similarity_score = round(my_review_of_choice.similarity(review_to_compare), 2)
# Define what is regarded as similar and not similar using if statement.
if similarity_score >= 0.5:
    similarity = 'These 2 reviews are similar.'
else:
    similarity = 'These 2 reviews are not similar.'
# Print the similarity score and whether this is regarded as similar or not.
print(f"The similarity between review 5 and review 500 is: {similarity_score}\n{similarity}")