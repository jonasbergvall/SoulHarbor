import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize session state
if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False

# Function to get user location (you can replace this with your geolocation logic)
def get_user_location():
    # Mocking location data for demonstration purposes
    return {'latitude': 37.7749, 'longitude': -122.4194}

# Function to reset data for a new user
def reset_data():
    st.session_state.data_loaded = False
    st.session_state.user_data = pd.DataFrame()

# Get user input outside the 'Analyze' button condition
user_name = st.text_input("Your Name")
user_mood = st.slider("How's your mood today?", 0, 100, 50)
user_text = st.text_area("Write something about your day")

# Display the user input
st.write("### User Input:")
st.write(f"Name: {user_name}")
st.write(f"Mood: {user_mood}")
st.write(f"Text: {user_text}")

# Run the save_user_data function when the 'Analyze' button is clicked
if st.button('Analyze'):
    # Get user location (mocked for demonstration)
    user_location = get_user_location()

    # Display user data
    st.write("### User Data:")
    st.write(f"Name: {user_name}")
    st.write(f"Mood: {user_mood}")
    st.write(f"Text: {user_text}")
    st.write(f"Location: {user_location}")

    # Save user data to a DataFrame
    new_entry = pd.DataFrame({
        'Name': [user_name],
        'Mood': [user_mood],
        'Text': [user_text],
        'Latitude': [user_location['latitude']],
        'Longitude': [user_location['longitude']]
    })

    # Append user data to the session state
    st.session_state.user_data = st.session_state.user_data.append(new_entry, ignore_index=True)

    # Display the data
    st.write("### Compiled Data:")
    st.write(st.session_state.user_data)

    # Display a chart using Plotly Express
    fig = px.line(st.session_state.user_data, x=st.session_state.user_data.index, y='Mood', title='User Mood Over Time')
    st.plotly_chart(fig)

# Button to reset data for a new user
if st.button('New Entry'):
    reset_data()
