import streamlit as st
import pandas as pd

# Initialize session state
if 'user_data' not in st.session_state:
    st.session_state.user_data = pd.DataFrame(columns=['Mood', 'OK_Level', 'Input'])

# Mood options
mood_options = ['Very Bad', 'Bad', 'Neutral', 'Good', 'Excellent']

# OK level options
ok_level_options = ['Very Bad', 'Bad', 'Neutral', 'Good', 'Excellent']

# Sidebar for user input
user_mood = st.sidebar.selectbox('How is your mood today?', mood_options)
user_ok_level = st.sidebar.selectbox('What is your OK level?', ok_level_options)

# Text input for describing the day
user_input = st.text_area("Describe your day:")

# Button to submit data
if st.button('Submit'):
    new_entry = {'Mood': user_mood, 'OK_Level': user_ok_level, 'Input': user_input}
    st.session_state.user_data = pd.concat([st.session_state.user_data, pd.DataFrame([new_entry])], ignore_index=True)

# Display user data
st.write("User Data:")
st.write(st.session_state.user_data)

# Calculate and display statistics
if not st.session_state.user_data.empty:
    num_better_than_ok = st.session_state.user_data[st.session_state.user_data['Mood'] > st.session_state.user_data['OK_Level']].shape[0]
    num_worse_than_ok = st.session_state.user_data[st.session_state.user_data['Mood'] < st.session_state.user_data['OK_Level']].shape[0]

    st.write(f"Number of people feeling better than their OK level: {num_better_than_ok}")
    st.write(f"Number of people feeling worse than their OK level: {num_worse_than_ok}")
