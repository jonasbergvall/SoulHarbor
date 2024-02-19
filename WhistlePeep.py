import streamlit as st
from datetime import datetime
import pandas as pd

# Function to save data to a file
def save_data(user_name, user_mood, user_data):
    # Read existing data from the file if it exists
    try:
        existing_data = pd.read_csv('user_data.csv')
    except FileNotFoundError:
        existing_data = pd.DataFrame(columns=['Date', 'User Name', 'Mood', 'User Data'])

    # Add new data only if the user clicked on Analyze
    if st.button('Analyze'):
        # Automatic identification of the current date and time
        current_date_time = datetime.now()
        formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

        # Add new data
        new_entry = pd.DataFrame([[formatted_date_time, user_name, user_mood, user_data]],
                                 columns=['Date', 'User Name', 'Mood', 'User Data'])
        updated_data = pd.concat([existing_data, new_entry], ignore_index=True)

        # Save to file
        updated_data.to_csv('user_data.csv', index=False)

        st.write('Analysis result saved!')

# User inputs
user_name = st.text_input('Enter your name:', 'Anonymous')
user_mood = st.slider('How are you feeling today?', 0, 100, 50)

# Create the interface
st.title('WhistlePeep - An Early Warning System for Work Environment')

# User's data input
user_data = st.text_area('Write something about your day:', '')

# Display compiled data
st.subheader('Compiled data:')
save_data(user_name, user_mood, user_data)
compiled_data = pd.read_csv('user_data.csv')
st.write(compiled_data)
