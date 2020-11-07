import joblib
import numpy as np
from flask import Flask
from flask import jsonify
from utils import Utils
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# routes


@app.route('/predict', methods=['GET'])
def predict():
    utils = Utils()
    dataFrame1 = utils.load_from_csv('./in/dataAnimals.csv')
    dataFrame2 = utils.load_from_csv('./in/dataDataScience.csv')
    dataFrame3 = utils.load_from_csv('./in/dataEducation.csv')
    dataFrame4 = utils.load_from_csv('./in/dataFashion.csv')
    dataFrame5 = utils.load_from_csv('./in/dataPolitics.csv')
    frames = [dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5]
    alldata = pd.concat(frames)
    alldata_data = alldata.values[:, 2]
    alldata_one = alldata.values[:, 1]
    alldata_one = alldata_one[0]
    print("ALL"+alldata_one)
    vectorizer = TfidfVectorizer()
    x_train = vectorizer.fit_transform(alldata_data)
    x_test = vectorizer.transform(['where is Obama'])
    prediction = model.predict(x_test)
    return jsonify({'prediccion': list(prediction)})


# TODO Sebestian Cristian Jimmy ampliar los request para un post con mensajes
if __name__ == "__main__":
    model = joblib.load('./models/0.7865323831853058')
    app.run(port=8080)
