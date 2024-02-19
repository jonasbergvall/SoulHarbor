import streamlit as st
import pandas as pd
from datetime import datetime

# Function to get user's geolocation
def get_user_location():
    try:
        location = st.session_state.location
        return location
    except AttributeError:
        return None

# Function to save user data
def save_user_data():
    # Get user input
    user_name = st.text_input("User Name", key="user_name")
    user_mood = st.slider("How's your mood today?", 0, 100, 50, key="user_mood")
    user_data_input = st.text_area("Write something about your day", key="user_data_input")
    
    # Get geolocation
    user_location = get_user_location()

    # Save user data if Analyze button is clicked
    if st.button("Analyze"):
        # Create a new entry
        new_entry = {
            "User Name": user_name,
            "Mood": user_mood,
            "Data Input": user_data_input,
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Location": user_location,
        }

        # If 'user_data' is not in session state, initialize an empty DataFrame
        if 'user_data' not in st.session_state:
            st.session_state.user_data = pd.DataFrame()

        # Append user data to the session state
        st.session_state.user_data = st.session_state.user_data.append(new_entry, ignore_index=True)

# Display user data chart
if 'user_data' in st.session_state and not st.session_state.user_data.empty:
    st.write("User Data Chart:")
    st.line_chart(st.session_state.user_data.set_index('Date')['Mood'])

# Save user data
save_user_data()
