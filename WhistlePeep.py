import streamlit as st
import pandas as pd
import datetime

# Initialize session state
if 'user_data' not in st.session_state:
    st.session_state.user_data = pd.DataFrame(columns=['Date', 'Mood', 'OK Level', 'Description'])

# Title and user input
st.title('WhistlePeep App')
mood_options = ["Very bad", "Bad", "Neutral", "Good", "Excellent"]
user_mood = st.selectbox("Select your mood today:", mood_options)

ok_level = st.slider("On a scale of 0 to 10, how OK are you?", 0, 10, 5)

user_input = st.text_area("Describe your day:")

# Save user data
if st.button("Save"):
    new_entry = {'Date': datetime.datetime.now(), 'Mood': user_mood, 'OK Level': ok_level, 'Description': user_input}
    st.session_state.user_data = st.session_state.user_data.append(new_entry, ignore_index=True)

# Display average mood
average_mood = st.session_state.user_data['Mood'].map(mood_options.index).mean()
st.write(f"Average Mood: {mood_options[round(average_mood)]}")

# Display user data table
st.write("User Data:")
st.write(st.session_state.user_data)
