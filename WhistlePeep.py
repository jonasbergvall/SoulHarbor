import streamlit as st
import pandas as pd
from datetime import datetime

# Function to save user data
def save_user_data():
    # Get user input
    user_name = st.text_input("User Name")
    user_mood = st.slider("How's your mood today?", 0, 100, 50)
    user_data_input = st.text_area("Write something about your day")

    # If 'user_data' is not in session state, initialize an empty list
    if 'user_data' not in st.session_state:
        st.session_state.user_data = []

    # Save user data if Analyze button is clicked
    if st.button("Analyze"):
        # Create a new entry
        new_entry = {
            "User Name": user_name,
            "Mood": user_mood,
            "Data Input": user_data_input,
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # Append user data to the session state list
        st.session_state.user_data.append(new_entry)

# Display user data chart
if 'user_data' in st.session_state and st.session_state.user_data:
    st.write("User Data Chart:")
    df_user_data = pd.DataFrame(st.session_state.user_data)
    st.line_chart(df_user_data.set_index('Date')['Mood'])

# Save user data
save_user_data()
