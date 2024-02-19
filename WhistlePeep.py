import streamlit as st
from datetime import datetime
import pandas as pd

# Funktion för att spara data till fil
@st.cache(persist=True)
def save_data(user_data):
    # Läs befintlig data från filen om det finns
    try:
        existing_data = pd.read_csv('user_data.csv')
    except FileNotFoundError:
        existing_data = pd.DataFrame(columns=['Date', 'Mood', 'User Data'])

    # Lägg till ny data
    current_date_time = datetime.now()
    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame([[formatted_date_time, user_mood, user_data]],
                             columns=['Date', 'Mood', 'User Data'])
    updated_data = pd.concat([existing_data, new_entry], ignore_index=True)

    # Spara till fil
    updated_data.to_csv('user_data.csv', index=False)

    return updated_data

# Användare anger sin känsla
user_mood = st.slider('Hur mår du idag?', 0, 100, 50)

# Automatisk identifiering av dagens datum och tid
current_date_time = datetime.now()
formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

# Skapa gränssnittet
st.title('WhistlePeep - An Early Warning System for Work Environment')

# Användarens datainmatning
user_data = st.text_area('Skriv något om dagen:', '')

# Visar dagens datum och tid
st.write(f"Dagens datum och tid: {formatted_date_time}")

# Visar användarens valda känsla
st.write(f"Din känsla idag: {user_mood}")

if st.button('Analysera'):
    # Spara användarens data
    save_data(user_data)
    st.write('Analysresultat sparad!')

# Visa sammanställd data
st.subheader('Sammanställd data:')
compiled_data = save_data(user_data)
st.write(compiled_data)
