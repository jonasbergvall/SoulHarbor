import streamlit as st
from datetime import datetime
import pandas as pd

# Funktion för att spara data till fil
def save_data(user_mood, user_data):
    # Läs befintlig data från filen om det finns
    try:
        existing_data = pd.read_csv('user_data.csv')
    except FileNotFoundError:
        existing_data = pd.DataFrame(columns=['Date', 'Mood', 'User Data'])

    # Lägg till ny data endast om användaren klickade på Analysera
    if st.button('Analysera'):
        # Automatisk identifiering av dagens datum och tid
        current_date_time = datetime.now()
        formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

        # Lägg till ny data
        new_entry = pd.DataFrame([[formatted_date_time, user_mood, user_data]],
                                 columns=['Date', 'Mood', 'User Data'])
        updated_data = pd.concat([existing_data, new_entry], ignore_index=True)

        # Spara till fil
        updated_data.to_csv('user_data.csv', index=False)

        st.write('Analysresultat sparad!')

# Användare anger sin känsla
user_mood = st.slider('Hur mår du idag?', 0, 100, 50)

# Skapa gränssnittet
st.title('WhistlePeep - An Early Warning System for Work Environment')

# Användarens datainmatning
user_data = st.text_area('Skriv något om dagen:', '')

# Visa sammanställd data
st.subheader('Sammanställd data:')
save_data(user_mood, user_data)
compiled_data = pd.read_csv('user_data.csv')
st.write(compiled_data)
