import streamlit as st
import pandas as pd
import datetime

# Function to get user location (dummy data for illustration purposes)
def get_user_location():
    return "Dummy Location"

# Function to save user data
@st.cache(allow_output_mutation=True)
def save_user_data(new_entry, user_data):
    user_data = user_data.append(new_entry, ignore_index=True)
    return user_data.copy()

# Main Streamlit app
def main():
    st.title("WhistlePeep - Employee Well-being Tracker")

    # Get or create user data DataFrame
    if 'user_data' not in st.session_state:
        st.session_state.user_data = pd.DataFrame(columns=['Date', 'Mood', 'Location'])

    # Get user name
    user_name = st.text_input("Enter your name:")

    # Get user mood
    user_mood = st.slider("How is your mood today?", 0, 100, 50)

    # Get user location (dummy data for illustration purposes)
    user_location = get_user_location()

    # Create a new entry
    new_entry = {'Date': datetime.datetime.now(), 'Mood': user_mood, 'Location': user_location}

    # Save user data
    st.session_state.user_data = save_user_data(new_entry, st.session_state.user_data)

    # Display user data
    st.write("User Data:")
    st.write(st.session_state.user_data)

    # Display mood chart
    st.line_chart(st.session_state.user_data['Mood'], use_container_width=True).set_ylim(0, 100)

# Run the app
if __name__ == "__main__":
    main()
