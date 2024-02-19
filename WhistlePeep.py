import streamlit as st
import pandas as pd
import plotly.express as px

# Function to get user location (if available)
def get_user_location():
    # Replace this with your geolocation logic
    return {"latitude": 0, "longitude": 0}

# Function to save user data
@st.cache_data(allow_output_mutation=True)
def save_user_data(user_data, new_entry):
    user_data.append(new_entry)
    return user_data


# Set user name and date
user_name = st.text_input("User Name:")
date = st.date_input("Date:")

# Set user mood using a slider
user_mood = st.slider("How was your day?", 0, 100, 50)

# Save user data on button click
if st.button("Analyze"):
    new_entry = {
        "User": user_name,
        "Date": date,
        "Mood": user_mood,
        "Location": get_user_location(),
    }

    # Load existing user data
    user_data = st.session_state.user_data if 'user_data' in st.session_state else []

    # Append new entry to user_data
    save_user_data(user_data, new_entry)
    st.session_state.user_data = user_data

# Display user data chart
if 'user_data' in st.session_state and st.session_state.user_data:
    st.write("User Data Chart:")

    # Create a Plotly figure
    fig = px.line(st.session_state.user_data, x='Date', y='Mood', color='User', labels={'Mood': 'User Mood'})

    # Set y-axis limits
    fig.update_yaxes(range=[0, 100])

    # Show the figure
    st.plotly_chart(fig)

# Button to clear data for a new entry
if st.button("New Entry"):
    st.session_state.user_data = []
