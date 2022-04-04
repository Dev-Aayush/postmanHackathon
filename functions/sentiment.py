from textblob import TextBlob
# import re


def sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity == 0:
        return "Neutral"
    elif polarity > 0:
        return "Positive"
    else:
        return "Negative"


def subjectivity(text):
    analysis = TextBlob(text)
    return analysis.sentiment.subjectivity*100
