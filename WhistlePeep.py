import streamlit as st
from datetime import datetime

# Användare anger sin känsla
user_mood = st.slider('Hur mår du idag?', 0, 100, 50)

# Automatisk identifiering av dagens datum och tid
current_date_time = datetime.now()
formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

# Skapa gränssnittet
st.title('WhistlePeep - An Early Warning System for Work Environment')

# Användarens datainmatning
user_data = st.text_area('Ange din data här:', '')

# Visar dagens datum och tid
st.write(f"Dagens datum och tid: {formatted_date_time}")

# Visar användarens valda känsla
st.write(f"Din känsla idag: {user_mood}")

if st.button('Analysera'):
    # Lägg till kod för analys av användarens data här
    st.write('Analysresultat:')
