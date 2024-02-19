import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def load_user_data():
    try:
        user_data = pd.read_csv('user_data.csv')
    except FileNotFoundError:
        user_data = pd.DataFrame(columns=['Mood', 'OK_Level', 'Input'])
    return user_data

@st.cache(allow_output_mutation=True)
def save_user_data(new_entry, user_data):
    user_data = pd.concat([user_data, pd.DataFrame([new_entry])], ignore_index=True)
    user_data.to_csv('user_data.csv', index=False)
    return user_data

# Initialize session state
user_data = load_user_data()

# Mood options
mood_options = ['Very Bad', 'Bad', 'Neutral', 'Good', 'Very Good']

# OK level options
ok_level_options = ['Very Bad', 'Bad', 'Neutral', 'Good', 'Very Good']

# Assign numerical values to mood and OK levels
mood_values = {'Very Bad': 1, 'Bad': 2, 'Neutral': 3, 'Good': 4, 'Very Good': 5}
ok_level_values = {'Very Bad': 1, 'Bad': 2, 'Neutral': 3, 'Good': 4, 'Very Good': 5}

# Sidebar for user input
user_mood = st.sidebar.selectbox('How is your mood today?', mood_options, format_func=lambda x: x)
user_ok_level = st.sidebar.selectbox('What is your OK level?', ok_level_options, format_func=lambda x: x)

# Text input for describing the day
user_input = st.text_area("Describe your day:")

# Button to submit data
if st.button('Submit'):
    new_entry = {'Mood': user_mood, 'OK_Level': user_ok_level, 'Input': user_input}
    user_data = save_user_data(new_entry, user_data)

# Display user data
st.write("User Data:")
st.write(user_data)

# Calculate and display statistics
if not user_data.empty:
    num_better_than_ok = user_data[user_data['Mood'] > user_data['OK_Level']].shape[0]
    num_worse_than_ok = user_data[user_data['Mood'] < user_data['OK_Level']].shape[0]

    st.write(f"Number of people feeling better than their OK level: {num_better_than_ok}")
    st.write(f"Number of people feeling worse than their OK level: {num_worse_than_ok}")

# Button to restart for a new user
if st.button('Restart for a New User'):
    user_input = ""  # Clear the text area
    st.session_state.user_data = None
    st.experimental_rerun()
