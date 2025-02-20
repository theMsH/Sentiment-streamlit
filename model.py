import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC


def train_model():
    df = pd.read_csv("train.csv", encoding='unicode_escape')

    # Remove null values, otherwise sklearn Pipeline will fail with ValueError
    df.dropna(inplace=True)

    # Prepare training data
    X = df['text']
    y = df['sentiment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    # Create model
    text_clf = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LinearSVC())
    ])
    text_clf.fit(X_train, y_train)

    return text_clf
