import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''



date = st.date_input(
    "Selecciona la fecha",
    datetime.date(2024, 7, 12))

# Input de hora
time = st.time_input(
    "Selecciona la hora",
    datetime.time(14, 0))

# Combinar fecha y hora
datetime_combined = datetime.datetime.combine(date, time)

st.write('La fecha y hora seleccionadas son:', datetime_combined)

'''
# Ejemplo desde Times square a Central park:
1. Pickup (Times Square)

Latitud: 40.758896
Longitud: -73.985130
2. Dropoff (Central Park)

Latitud: 40.785091
Longitud: -73.968285
'''

# Input para pickup longitude
pickup_longitude = st.number_input('Ingrese la longitud de pickup', format="%.6f")

# Input para pickup latitude
pickup_latitude = st.number_input('Ingrese la latitud de pickup', format="%.6f")

# Input para dropoff longitude
dropoff_longitude = st.number_input('Ingrese la longitud de destino', format="%.6f")

# Input para dropoff latitude
dropoff_latitude = st.number_input('Ingrese la latitud de destino', format="%.6f")

st.write('Longitud de pickup:', pickup_longitude)
st.write('Latitud de pickup:', pickup_latitude)
st.write('Longitud de destino:', dropoff_longitude)
st.write('Latitud de destino:', dropoff_latitude)


number = st.number_input('Seleccione número de pasajeros', step=1, min_value=1)

st.write('Número de pasajeros:', int(number))



URL = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

    # st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''

api_params = {
    "pickup_datetime": datetime_combined.strftime("%Y-%m-%d %H:%M:%S"),
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": int(number)
}

if st.button('Obtener predicción'):
    try:
        response = requests.get(URL, params=api_params, timeout=10)

        # Paso 4: Recuperar la predicción del JSON devuelto por la API
        if response.status_code == 200:
            prediction = response.json()
            st.write('Predicción de la tarifa:', prediction['fare'])
        else:
            st.write('Error en la llamada a la API:', response.status_code)
    except requests.exceptions.Timeout:
        st.write('Error: La solicitud a la API ha superado el tiempo de espera.')
    except requests.exceptions.RequestException as e:
        st.write('Error en la solicitud a la API:', str(e))
