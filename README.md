### Sentiment Analysis.
This project isolates the reviews column of an amazon reviews dataset, preprocesses these reviews using spaCy (splits into tokens, discards missing values, lemmatizes and removes stopwords and punctuation).
Sentiment analysis is then performed on a sample of the preprocessed reviews (the first 50 in the row).
The function prints the review followed by its polarity and corresponding sentiment.
This project also shows how to compare similarity of 2 reviews.
#### Steps in project
* Importing necessary libraries
* Reading in dataframe using pandas
* Isolating reviews column of interest
* Cleaning and preprocessing data in column
* Creating a function to calculate polarity
* Call function on first 50 rows of data
* Print review, polarity and sentiment
* Compare 2 reviews and print similarity
