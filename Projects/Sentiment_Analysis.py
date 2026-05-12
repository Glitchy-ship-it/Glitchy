import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# contains 20 of each sentiment to train the model properly.

data = {
        "review" : [
        "The product quality is excellent",
        "I loved the fast delivery",
        "The customer support was very helpful",
        "Amazing value for money",
        "The packaging was neat and secure",
        "I am very happy with this purchase",
        "The service was quick and professional",
        "The product works perfectly",
        "Great experience from start to finish",
        "The staff was polite and friendly",
        "Excellent customer support and smooth service",
        "The item arrived earlier than expected",
        "Very good quality for the price",
        "Amazing product and I would definitely buy this again",
        "The product exceeded my expectations",
        "The app was easy to use",
        "The refund process was quick and smooth",
        "The seller responded very quickly",
        "The product is reliable and useful",
        "The overall experience was wonderful",

        "The delivery was late",
        "The product arrived damaged",
        "Very poor customer service",
        "Worst purchase I have made",
        "The item stopped working after one day",
        "I am not satisfied with the product",
        "The quality was disappointing",
        "The support team was rude",
        "The packaging was damaged",
        "The product is not worth the money",
        "The service was slow and frustrating",
        "I did not like the experience",
        "The product failed to meet expectations",
        "The delivery experience was terrible",
        "The item was defective",
        "The app kept crashing",
        "The refund process was very slow",
        "The seller did not respond",
        "The product description was misleading",
        "The price was too high for the quality",

        "The product is okay for the price",
        "The service was average",
        "It was neither good nor bad",
        "The delivery was normal",
        "The product works fine but nothing special",
        "The experience was decent overall",
        "The quality is acceptable",
        "The packaging was simple",
        "The product is usable",
        "It was a normal shopping experience",
        "The service was fine",
        "The item is average",
        "The purchase was satisfactory",
        "The product does the basic job",
        "The delivery time was acceptable",
        "The app works as expected",
        "The seller response was standard",
        "The product matched the description",
        "The price is reasonable",
        "The overall experience was ordinary"
    ],

    "sentiment" : [
        "positive", "positive", "positive", "positive", "positive",
        "positive", "positive", "positive", "positive", "positive",
        "positive", "positive", "positive", "positive", "positive",
        "positive", "positive", "positive", "positive", "positive",

        "negative", "negative", "negative", "negative", "negative",
        "negative", "negative", "negative", "negative", "negative",
        "negative", "negative", "negative", "negative", "negative",
        "negative", "negative", "negative", "negative", "negative",

        "neutral", "neutral", "neutral", "neutral", "neutral",
        "neutral", "neutral", "neutral", "neutral", "neutral",
        "neutral", "neutral", "neutral", "neutral", "neutral",
        "neutral", "neutral", "neutral", "neutral", "neutral"
    ]
}

dataframe = pd.DataFrame(data)

print("Business Reviews: ")
print(dataframe)

print("\nSentiment Count")
print(dataframe["sentiment"].value_counts())

x = dataframe["review"]
y = dataframe ["sentiment"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size= 0.3, random_state=10
)

vectorize = CountVectorizer()

x_train_vectorized = vectorize.fit_transform(x_train)
x_test_vectorized = vectorize.transform(x_test)

model = MultinomialNB()

model.fit(x_train_vectorized, y_train)

predictions = model.predict(x_test_vectorized)

print("\nAccuracy : ")
print(accuracy_score(y_test,predictions))

print("\nConfusion Matrix : ")
print(confusion_matrix(y_test,predictions))

print("\nClassification Report : ")
print(classification_report(y_test,predictions))

#insert new reviews to test without sentiment

new_reviews = [
    "The product quality is amazing",
    "I am very happy with the service",
    "The delivery was fast and smooth",
    "The staff was polite and helpful",
    "Excellent product and great packaging",
    "The product stopped working after one day",
    "Very bad customer support",
    "The delivery was delayed and disappointing",
    "Worst service I have received",
    "Poor quality and not worth the money",
    "The product is okay for the price",
    "The service was average",
    "It was neither good nor bad",
    "The delivery was normal",
    "The product works fine but nothing special",
    "I loved the quick response from support",
    "The item was damaged when it arrived",
    "The experience was decent overall",
    "Amazing value for money",
    "I am not satisfied with the product"
]

new_reviews_vectorized = vectorize.transform(new_reviews)
new_predictions = model.predict(new_reviews_vectorized)

print("\nNew Reviews Predictions : ")

final_table = pd.DataFrame({
    "Reviews" : new_reviews,
    "Predicted Sentiment" : new_predictions
})

print(final_table)