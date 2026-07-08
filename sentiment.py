from textblob import TextBlob
from flask import Flask,request,jsonify
app=Flask(__name__)
def add_product():
    data=request.get_json()
    product_name=data[product_name]
    review=data["review"]
    analysis=TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment="Positive"

    elif polarity < 0:
        sentiment="Negative"

    else:
        sentiment="Neutral"
        return jsonify({"message":"Success"})   

    
