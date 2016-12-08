import flask
app = flask.Flask(__name__)

#-------- MODEL GOES HERE -----------#
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


from sklearn.linear_model import LinearRegression
import pickle


with open("tips_model.pkl", "r") as f:
    PREDICTOR2 = pickle.load(f)

with open("spd_model.pkl", "r") as f:
    PREDICTOR = pickle.load(f)    

with open("X_dow_dum.pkl", "r") as f:
    X_dow_dum = pickle.load(f)

with open("X_hour_dum.pkl", "r") as f:
    X_hour_dum = pickle.load(f)
    
with open("X_zip_dum.pkl", "r") as f:
    X_zip_dum = pickle.load(f)    

with open("small_df.pkl.txt", "r") as f:
    df2 = pickle.load(f)        

#-------- FUNCTION GOES HERE -----------#
def dummy_dow(dow_t):
    for i, j in enumerate(X_dow_dum.index):
        if str(dow_t) == j.split("_") [1]:
            X_dow_dum.iloc[i] = 1
        else: 
            X_dow_dum.iloc[i] = 0
    return X_dow_dum  

def dummy_hour(hour_t):
    for i, j in enumerate(X_hour_dum.index):
        if str(hour_t) == j.split("_") [1]:
            X_hour_dum.iloc[i] = 1
        else: 
            X_hour_dum.iloc[i] = 0
    return X_hour_dum        
    
def dummy_zip(zipcod_t):
    for i, j in enumerate(X_zip_dum.index):
        if str(zipcod_t) == j.split("_") [1]:
            X_zip_dum.iloc[i] = 1
        else: 
            X_zip_dum.iloc[i] = 0
    return X_zip_dum    

 # function to return mean features from dataframe based on user input

def mean_features(zipp, dow, hour):
    
    # spit out mean speed, mean trip distance, mean fare, mean tips percent
    # Filtering to subset dataframe
    dfo = df2[df2['zipcode'] == int(zipp)]
    dfo = dfo[dfo['pickup_hour'] == int(hour)]
    dfo = dfo[dfo['day_of_week'] == int(dow)]
    
    outdict = {}
    
    outdict['Avg_spd'] = round(dfo['Avg_spd'].mean(), 2)
    outdict['tip_amount'] = round(dfo['tip_percent'].mean(), 2)
    outdict['total_amount'] = round(dfo['total_amount'].mean(), 2)
    outdict['trip_distance'] = round(dfo['trip_distance'].mean(),2)
    outlist = []
    outlist.append(outdict)
        
    return outlist   


#-------- ROUTES GO HERE -----------#

# This method takes input via an HTML page
@app.route('/page')
def page():
   with open("page_taxi.html", 'r') as viz_file:
       return viz_file.read()

# @app.route("/predict", methods=["GET"])
# def predict():
#     pclass = flask.request.args['pclass']
#     sex = flask.request.args['sex']
#     age = flask.request.args['age']
#     fare = flask.request.args['fare']
#     sibsp = flask.request.args['sibsp']

#     item = [pclass, sex, age, fare, sibsp]
#     score = PREDICTOR.predict_proba(item)
#     results = {'survival chances': score[0,1], 'death chances': score[0,0]}
#     return flask.jsonify(results)

@app.route('/result', methods=['POST', 'GET'])
def result():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':

       inputs = flask.request.form

      
       X_zip_dum = dummy_zip(inputs['zipcode'])

       X_dow_dum = dummy_dow(inputs['day'])
    
       X_hour_dum = dummy_hour(inputs['hour'])

       avg = mean_features(inputs['zipcode'], inputs['day'], inputs['hour'])

       item2 = pd.concat([X_hour_dum, X_dow_dum, X_zip_dum])
       score2 = PREDICTOR2.predict(item2)

       spd = PREDICTOR.predict(item2)

       score2 = round(score2[0], 2)

       spd = round(spd[0], 2)

       results = [{'Predicted Tip': score2, 'Predicted Speed': spd}]

       results = results + avg

       return flask.jsonify(results)


if __name__ == '__main__':
    '''Connects to the server'''

    HOST = '127.0.0.1'
    PORT = '4000'
    app.run(HOST, PORT)