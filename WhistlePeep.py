import streamlit as st
import plotly.express as px
import pandas as pd
import datetime

# Function to get user geolocation
def get_user_location():
    location = st.session_state.location
    if not location:
        st.warning("Geolocation not available. Please make sure to enable location access in your browser.")
        return None
    return location

# Function to save user data
def save_user_data():
    user_name = st.session_state.user_name
    user_mood = st.slider("How's your mood today?", 0, 100, 50)
    user_text = st.text_area("Write something about your day")
    user_location = get_user_location()

    # Get current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save data to session_state
    if 'user_data' not in st.session_state:
        st.session_state.user_data = pd.DataFrame(columns=["Date", "Time", "User Name", "Mood", "Text", "Location"])

    st.session_state.user_data = st.session_state.user_data.append({
        "Date": current_datetime.split()[0],
        "Time": current_datetime.split()[1],
        "User Name": user_name,
        "Mood": user_mood,
        "Text": user_text,
        "Location": user_location
    }, ignore_index=True)

# Load saved user data
if 'user_data' not in st.session_state:
    st.session_state.user_data = pd.DataFrame(columns=["Date", "Time", "User Name", "Mood", "Text", "Location"])

# Main app
st.title("WhistlePeep - Your Mood Tracker")

# User input
st.session_state.user_name = st.text_input("Enter your name:")
save_button = st.button("Save my data")

# Save data when the "Save my data" button is clicked
if save_button:
    save_user_data()

# Display saved data
if not st.session_state.user_data.empty:
    st.subheader("Your Saved Data:")
    st.write(st.session_state.user_data)

# Plot mood over time
if st.checkbox("Show Mood Over Time"):
    fig = px.line(st.session_state.user_data, x="Date", y="Mood", title="Mood Over Time", markers=True)
    st.plotly_chart(fig)
