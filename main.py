
import re
import pickle
from typing import Optional
from fastapi import FastAPI
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from pydantic import BaseModel


loaded_model = pickle.load(open("stock.pkl", "rb"))
tfvector = pickle.load(open("tfvector.pkl", "rb"))

app = FastAPI()

class Headline(BaseModel):
    text:str



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def predict(headline:Headline):
    new_headline = headline.text
    new_headline = re.sub('[^a-zA-Z]', ' ', new_headline)
    new_headline = new_headline.lower()
    new_headline = new_headline.split()
    lemmatizer = WordNetLemmatizer()
    new_headline = [lemmatizer.lemmatize(word) for word in new_headline if not word in stopwords.words('english')]
    new_headline = ' '.join(new_headline)
    new_corpus = [new_headline]
    new_X_test = tfvector.transform(new_corpus).toarray()
    new_y_pred = loaded_model.predict(new_X_test)
    if(new_y_pred[0]==1):
        return{"Prediction" : "the stock price increased"}
    else :
        return{"Prediction" :"the stock price stayed the same or decreased"}


     

    
        
    

