import jinja2
from flask import Flask, render_template, request
app = Flask(__name__)
#app._static_folder = '/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/'

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pickle
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


# Reference dataframe with taxi information indexed by zipcodes
with open('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/assets/taxi_ref_df.pkl', 'r') as f:
    taxi_ref_df = pickle.load(f)

# Reference dataframe with yelp review information indexed by zipcodes
with open('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/assets/full_yelp_ref_df.pkl', 'r') as f:
    yelp_ref_df = pickle.load(f)

# Prediction RandomForest regressor ML model
with open('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/assets/model.pkl', 'r') as f:
    model = pickle.load(f)

# StandardScaler fitted to training X data, used to transform continuous data of x
with open('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/assets/x_scaler.pkl', 'r') as f:
    ss_x = pickle.load(f)

# StandardScaler fitted to training y data, used to inverse transform predict y
with open('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/assets/y_scaler.pkl', 'r') as f:
    ss_y = pickle.load(f)

# Empty X input dataframe for zipcodes
with open('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/assets/x_zip.pkl', 'r') as f:
    x_zip = pickle.load(f)

# Function to populate respective cell in zipcode dataframe
def set_zip(zipcode, zip_df):
    if zipcode == '10001':
        return zip_df
    else:
        try:
            for i in zip_df.columns:
                new_i = i.replace('Zip__', '')
                if new_i == zipcode:
                    zip_df.loc[0, i] = 1
                    return zip_df
                else:
                    return zip_df
        except:
            return zip_df

@app.route("/page")
def page():
    with open('page.html', 'r') as viz_file:
        return viz_file.read()

@app.route('/magic_predictions', methods = ['POST', 'GET'])

def predict():
    if request.method == 'POST':

        # Getting the user inputs on the form
        inputs = request.form

        # Setting zipcode variable (Integer)
        z = int(inputs['zipcode'])

        # Setting area variable (Integer)
        a = int(inputs['area'])

        # Get the respective row on taxi df based on zipcode
        taxi = taxi_ref_df.loc[z, ['dropoff_hr_0600_1200', 
                                    'dropoff_hr_1200_1800', 
                                    'dropoff_hr_1800_2359', 
                                    'dropoff_hr_2359_0600']]

        # Create taxi dropoff plot
        sub_df = taxi_ref_df.loc[z,
                ['dropoff_hour_0', 'dropoff_hour_1', 'dropoff_hour_2', 
                 'dropoff_hour_3', 'dropoff_hour_4', 'dropoff_hour_5', 
                 'dropoff_hour_6', 'dropoff_hour_7', 'dropoff_hour_8', 
                 'dropoff_hour_9', 'dropoff_hour_10', 'dropoff_hour_11', 
                 'dropoff_hour_12', 'dropoff_hour_13', 'dropoff_hour_14', 
                 'dropoff_hour_15', 'dropoff_hour_16', 'dropoff_hour_17', 
                 'dropoff_hour_18', 'dropoff_hour_19', 'dropoff_hour_20', 
                 'dropoff_hour_21', 'dropoff_hour_22', 'dropoff_hour_23', 
                ]]
        # Getting NYC average hourly dropoff
        taxi_avg = taxi_ref_df[['dropoff_hour_0', 'dropoff_hour_1', 'dropoff_hour_2', 
                 'dropoff_hour_3', 'dropoff_hour_4', 'dropoff_hour_5', 
                 'dropoff_hour_6', 'dropoff_hour_7', 'dropoff_hour_8', 
                 'dropoff_hour_9', 'dropoff_hour_10', 'dropoff_hour_11', 
                 'dropoff_hour_12', 'dropoff_hour_13', 'dropoff_hour_14', 
                 'dropoff_hour_15', 'dropoff_hour_16', 'dropoff_hour_17', 
                 'dropoff_hour_18', 'dropoff_hour_19', 'dropoff_hour_20', 
                 'dropoff_hour_21', 'dropoff_hour_22', 'dropoff_hour_23', 
                ]].mean()

        fig, ax = plt.subplots(1,1, figsize=(10,6))
        hr = np.arange(0, len(sub_df))
        count = sub_df.values
        width = 0.6
        ax.bar(hr, count, width = width, color='#F2E51D', label = 'Current zipcode')
        ax.set_xticklabels(np.arange(0,24))
        ax.set_xticks(hr + width-0.3)
        plt.plot((hr+(width/2.)), taxi_avg.values, 'xr-', linewidth = 2, markersize = 5, label = 'NYC average')
        ax.legend(loc = 'best', fontsize = 10)

        ax.tick_params(axis = 'both', labelsize = 14)
        ax.set_xlim(0,24)
        ax.set_xlabel('Hour of day', fontsize = 14)
        ax.set_ylabel('Passenger dropoff count (100s)', fontsize = 14)
        fig.tight_layout()
        fig.savefig('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/static/taxi_dropoff.png')

        # Dropoff by day of week
        dow_df = taxi_ref_df.loc[z,
                        ['day_0', 'day_1', 'day_2', 
                         'day_3', 'day_4', 'day_5', 
                         'day_6' 
                        ]]

        # Dropoff by day of week average
        dow_avg = taxi_ref_df.loc[:,
                ['day_0', 'day_1', 'day_2', 
                 'day_3', 'day_4', 'day_5', 
                 'day_6' 
                ]].mean()

        # Create taxi day of week dropoff plot
        fig4, ax4 = plt.subplots(1,1, figsize=(10,6))
        hr = np.arange(0, len(dow_df))
        count = dow_df.values
        width = 0.4
        ax4.bar(hr, count, width = width, color='#F2E51D', label = 'Current zipcode')
        ax4.set_xticklabels(['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat'])
        ax4.set_xticks(hr + width-0.2)
        ax4.plot((hr+(width/2.)), dow_avg.values, 'xr-', linewidth = 2, markersize = 5, label = 'NYC average')
        ax4.legend(loc = 'best', fontsize = 10)

        ax4.tick_params(axis = 'both', labelsize = 14)
        ax4.set_xlim(-.5,7)
        ax4.set_ylabel('Passenger dropoff count (100s)', fontsize = 14)
        fig4.tight_layout()
        fig4.savefig('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/static/dow_dropoff.png')

        # Create Yelp review count plot
        a_rev = yelp_ref_df.loc[z, 'Review_mean']
        fig1, ax1 = plt.subplots(1,1, figsize=(8,5))
        ax1.hist(yelp_ref_df['Review_mean'], bins = 10, color = '#c41200', label = 'Rest of NYC')
        ax1.vlines(a_rev, 0, 90, colors= 'orange', label = 'Current zipcode')
        ax1.tick_params(axis = 'both', labelsize = 14)
        ax1.set_xlabel('Average number of Yelp user reviews for nearby businesses', fontsize =14)
        ax1.set_ylabel('Number of businesses', fontsize =14)
        ax1.legend(loc = 'best', fontsize = 10)
        fig1.tight_layout()
        fig1.savefig('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/static/yelp_revcount.png')

        # Create Yelp "$" plot
        a_cost = yelp_ref_df.loc[z, 'Cost_mean']
        fig2, ax2 = plt.subplots(1,1, figsize=(8,5))
        ax2 .hist(yelp_ref_df['Cost_mean'], bins = 10, color = '#c41200', label = 'Rest of NYC')
        ax2.vlines(a_cost, 0, 45, colors= 'orange', label = 'Current zipcode')
        ax2.tick_params(axis = 'both', labelsize = 14)
        ax2.set_xlabel('Average number of "$" for nearby businesses', fontsize = 14)
        ax2.set_ylabel('Number of businesses', fontsize =14)
        ax2.legend(loc = 'best', fontsize = 10)
        fig2.tight_layout()
        fig2.savefig('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/static/yelp_cost.png')


        #Create Yelp review stars plot
        a_rate = yelp_ref_df.loc[z, 'Rate_mean']
        fig3, ax3 = plt.subplots(1,1, figsize=(8,5))
        ax3.hist(yelp_ref_df['Rate_mean'], bins = 10, color = '#c41200', label = 'Rest of NYC')
        ax3.vlines(a_rate, 0, 60, colors= 'orange', label = 'Current zipcode')
        ax3.tick_params(axis = 'both', labelsize = 14)
        ax3.set_xlabel('Average number of stars for nearby businesses', fontsize = 14)
        ax3.set_ylabel('Number of businesses', fontsize =14)
        ax3.legend(loc = 'best', fontsize = 10)
        fig3.tight_layout()
        fig3.savefig('/Users/peidacai/GA-DSI/projects/projects-capstone/part-05/static/yelp_star.png')

        # Create floor area into a pandas series
        floor_area = pd.Series([a], index = ['SF_avail'])

        # Get the respective row on yelp df based on zipcode
        yelp = yelp_ref_df.loc[z, :]

        comb = pd.DataFrame(pd.concat([floor_area, yelp, taxi], axis = 0))
        comb = comb.T

        scale_comb = pd.DataFrame(ss_x.transform(comb), columns = comb.columns)
        inp_x = pd.concat([scale_comb, set_zip(str(z), x_zip)], axis = 1)

        y_pred = round(ss_y.inverse_transform(model.predict(inp_x))[0],2)

        #return 'Predicted price per sqft per year = $' +  str(y_pred)
        z = str(z)
        a = str(a)
        rent_yr = y_pred * int(a)
        rent_mth = round(rent_yr / 12., 2)
        y_pred = str(y_pred)


        return render_template('magic_predictions.html', z=z, a=a, y_pred=y_pred, rent_yr= str(rent_yr), rent_mth = str(rent_mth))

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    #response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    return response

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = '4000'
    app.run(debug=True)
