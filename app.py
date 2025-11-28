import streamlit as st
import datetime
import requests
import pandas as pd

'''
# Get a not so solid estimate of your NY taxifare.
#### You should walk anymay.


'''

st.markdown('''
Just fill the fields and move on bro
''')

passengers = st.text_input('Passenger_count', '1')

d = st.date_input("Date", datetime.date(2019, 7, 6))

t = st.time_input('Time', datetime.time(8, 45))

pickup_long = st.text_input('Pickup_longitude', '41')

pickup_lat = st.text_input('Pickup_latitude', '-72')

dropoff_long = st.text_input('Dropoff_longitude', '41')

dropoff_lat = st.text_input('Dropoff_latitude', '-72')

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


def get_map_data():

    # return pd.DataFrame(
    #         [50, 50] + [37.76, -122.4],
    #         columns=['lat', 'lon']

    return pd.DataFrame({
        'lat': [-74.3, -73.7],
        'lon': [40.5, 40.9]
        })

df = get_map_data()

st.map(df, longitude = 'long', latitude = 'lat')


date_time = f"{d} {t}"
params = {
    "pickup_datetime": date_time,
    "pickup_longitude": pickup_long,
    "pickup_latitude": pickup_lat,
    "dropoff_longitude": dropoff_long,
    "dropoff_latitude": dropoff_lat,
    "passenger_count": passengers
    }

response = requests.get(url, params=params).json()['fare']


if st.button('Estimate!'):
    # print is visible in the server output, not in the page
    st.markdown(f"## Predicted cost: {round(response, 2)}$")
