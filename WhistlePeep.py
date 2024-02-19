import streamlit as st
import pandas as pd
import plotly.express as px

# Function to get user location (you can replace this with your geolocation logic)
def get_user_location():
    # Mocking location data for demonstration purposes
    return {'latitude': 37.7749, 'longitude': -122.4194}

# Function to save user data
def save_user_data():
    # Get user input
    user_name = st.text_input("Your Name")
    user_mood = st.slider("How's your mood today?", 0, 100, 50)
    user_text = st.text_area("Write something about your day")

    # Get user location (mocked for demonstration)
    user_location = get_user_location()

    # Display user data
    st.write("### User Data:")
    st.write(f"Name: {user_name}")
    st.write(f"Mood: {user_mood}")
    st.write(f"Text: {user_text}")
    st.write(f"Location: {user_location}")

    # Save user data to a DataFrame
    user_data = pd.DataFrame({
        'Name': [user_name],
        'Mood': [user_mood],
        'Text': [user_text],
        'Latitude': [user_location['latitude']],
        'Longitude': [user_location['longitude']]
    })

    # Append user data to a CSV file
    user_data.to_csv('user_data.csv', mode='a', header=not st.session_state.data_loaded, index=False)
    st.session_state.data_loaded = True

    # Display the data
    st.write("### Compiled Data:")
    st.write(user_data)

    # Display a chart using Plotly Express
    fig = px.line(user_data, x='Name', y='Mood', title='User Mood Over Time')
    st.plotly_chart(fig)

# Run the save_user_data function when the 'Analyze' button is clicked
if st.button('Analyze'):
    save_user_data()
