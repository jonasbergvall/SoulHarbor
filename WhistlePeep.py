import streamlit as st
import pandas as pd
import datetime

# Define mood options
mood_options = ["Very Bad", "Bad", "Neutral", "Good", "Very Good"]

# Function to save user data
def save_user_data(new_entry, user_data):
    if user_data is None:
        user_data = pd.DataFrame(columns=['Date', 'Mood', 'OK_Level', 'Description'])

    user_data = user_data.append(new_entry, ignore_index=True)
    return user_data

# Main function
def main():
    # Initialize session state
    if 'user_data' not in st.session_state:
        st.session_state.user_data = None

    # Title and description
    st.title("WhistlePeep")
    st.write("Rate your mood and describe your day!")

    # Mood selection
    user_mood = st.selectbox("How is your mood today?", mood_options)

    # OK level input
    ok_level = st.slider("What is your OK level?", 0, 100, 50)

    # Description input
    user_input = st.text_area("Describe your day:")

    # Save user data on button click
    if st.button("Save"):
        new_entry = {
            'Date': datetime.datetime.now(),
            'Mood': user_mood,
            'OK_Level': ok_level,
            'Description': user_input
        }

        # Save user data
        st.session_state.user_data = save_user_data(new_entry, st.session_state.user_data)
        st.success("Data saved successfully!")

    # Display user data
    if st.session_state.user_data is not None:
        st.write("User Data:")
        st.write(st.session_state.user_data)

    # Restart for a new user button
    if st.button("Restart for a new user"):
        st.session_state.user_data = None
        st.success("App reset for a new user!")

# Run the app
if __name__ == "__main__":
    main()
