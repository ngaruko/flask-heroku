from worldbankapp import app
import json, plotly
from flask import render_template
from wrangling_scripts.wrangle_data import return_figures
##

import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar 
import joblib
from sqlalchemy import create_engine

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
#engine = create_engine('sqlite:///../data/DisasterResponse.db')
#df = pd.read_sql_table('messages', engine)
#print(df.columns[4:])
#
# load model
#model = joblib.load("../models/classifier.pkl")




@app.route('/')
@app.route('/index')
def index():

    # genre_counts = df.groupby('genre').count()['message']
    # genre_names = list(genre_counts.index)
    # print(genre_names)
    # category_names = df.columns[4:]
    # print(category_names)
    # category_counts =df.groupby(['request','offer','money','storm']).count()['message']

    # # create visuals
    # # TODO: Below is an example - modify to create your own visuals
    # graphs = [
    #     {
    #         'data': [
    #             Bar(
    #                 x=category_names,
    #                 y=category_counts
    #             )
    #         ],

    #         'layout': {
    #             'title': 'Distribution of Message Categories',
    #             'yaxis': {
    #                 'title': "Count"
    #             },
    #             'xaxis': {
    #                 'title': "category"
    #             }
    #         }
    #     }
    # ]
    
    # # encode plotly graphs in JSON
    # ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    # graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # # render web page with plotly graphs
    # return render_template('master.html', ids=ids, graphJSON=graphJSON)                     figuresJSON=figuresJSON)
    return "Hello Heroku 2039"