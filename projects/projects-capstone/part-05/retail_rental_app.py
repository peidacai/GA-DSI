import flask
app = flask.Flask(__name__)

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pickle

with open('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/assets/taxi_ref_df.pkl', 'r') as f:
    taxi_ref_df = pickle.load(f)

with open('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/assets/full_yelp_ref_df.pkl', 'r') as f:
    yelp_ref_df = pickle.load(f)

with open('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/assets/model.pkl', 'r') as f:
    model = pickle.load(f)

with open('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/assets/x_scaler.pkl', 'r') as f:
    ss_x = pickle.load(f)

with open('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/assets/y_scaler.pkl', 'r') as f:
    ss_y = pickle.load(f)

with open('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/assets/x_zip.pkl', 'r') as f:
    x_zip = pickle.load(f)



# def set_zip(zipcode, zip_df):
#     if zipcode == '10001':
#         return zip_df
#     else:
#         try:
#             for i in zip_df.columns:
#                 new_i = i.replace('Zip__', '')
#                 if new_i == zipcode:
#                     zip_df.loc[0, i] = 1
#                     return zip_df
#                 else:
#                     return zip_df
#         except:
#             return zip_df

@app.route("/page")
def page():
    with open('page.html', 'r') as viz_file:
        return viz_file.read()

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    if flask.request.method == 'POST':

        inputs = flask.request.form

      
        # zipcode = inputs['zipcode']

        # area = inputs['area']

        # taxi = taxi_ref_df.loc[:, ['dropoff_hr_0600_1200', 'dropoff_hr_1200_1800', 'dropoff_hr_1800_2359', 'dropoff_hr_2359_0600']]
        # floor_area = pd.Series([area], index = ['SF_avail'])
        # yelp = yelp_ref_df.loc[zipcode, :]

        # comb = pd.DataFrame(pd.concat([floor_area, yelp, taxi], axis = 0))
        # comb = comb.T

        # scale_comb = pd.DataFrame(ss_x.transform(comb), columns = inp.columns)
        # inp_x = pd.concat([scale_comb, set_zip(str(zipcode), x_zip)], axis = 1)

        # y_pred = round(ss_y.inverse_transform(model.predict(inp_x))[0],2)


        return 'heehaw'




if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = '4000'
    app.run(HOST, PORT)
