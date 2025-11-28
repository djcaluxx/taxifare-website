import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

d = st.date_input(
    "Date:",
    datetime.date(2019, 7, 6))

t = st.time_input('Time', datetime.time(8, 45))

pickup_long = st.text_input('Pickup_longitude', 'longitude')

pickup_lat = st.text_input('Pickup_latitude', 'latitude')

dropoff_long = st.text_input('Dropoff_longitude', 'longitude')

dropoff_lat = st.text_input('Dropoff_latitude', 'latitude')

passengers = st.text_input('Passenger_count', '2')


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

st.markdown(f"Predicted cost: {round(response, 2)}")
## Finally, we can display the prediction to the user
