import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
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

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''
2. Let's build a dictionary containing the parameters for our API...
'''
date_time = f"{d} {t}"
params = {
    "pickup_datetime": date_time,
    "pickup_longitude": pickup_long,
    "pickup_latitude": pickup_lat,
    "dropoff_longitude": dropoff_long,
    "dropoff_latitude": dropoff_lat,
    "passenger_count": passengers
    }

'''
3. Let's call our API using the `requests` package...
'''
response = requests.get(url, params=params).json()['fare']

'''
4. Let's retrieve the prediction from the **JSON** returned by the API...
'''

st.markdown(f"Predicted cost: {round(response, 2)}$")
