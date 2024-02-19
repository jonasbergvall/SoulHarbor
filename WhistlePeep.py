import streamlit as st
import pandas as pd
import plotly.express as px

# Function to get user location (if available)
def get_user_location():
    # Replace this with your geolocation logic
    return {"latitude": 0, "longitude": 0}

# Function to save user data
def save_user_data():
    new_entry = {
        "User": st.session_state.user_name,
        "Date": st.session_state.date,
        "Mood": st.session_state.user_mood,
        "Location": get_user_location(),
    }

    # Create DataFrame if not exists
    if 'user_data' not in st.session_state:
        st.session_state.user_data = pd.DataFrame(columns=["User", "Date", "Mood", "Location"])

    # Append new entry to user_data
    st.session_state.user_data = st.session_state.user_data.append(new_entry, ignore_index=True)

# Set user name and date
st.session_state.user_name = st.text_input("User Name:")
st.session_state.date = st.date_input("Date:")

# Set user mood using a slider
st.session_state.user_mood = st.slider("How was your day?", 0, 100, 50)

# Save user data on button click
if st.button("Analyze"):
    save_user_data()

# Display user data chart
if 'user_data' in st.session_state and not st.session_state.user_data.empty:
    st.write("User Data Chart:")
    
    # Create a Plotly figure
    fig = px.line(st.session_state.user_data, x='Date', y='Mood', color='User', labels={'Mood': 'User Mood'})

    # Set y-axis limits
    fig.update_yaxes(range=[0, 100])

    # Show the figure
    st.plotly_chart(fig)
