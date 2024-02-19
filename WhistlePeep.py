import pandas as pd
import streamlit as st
import datetime

# Function to save user data
@st.cache_data(allow_output_mutation=True)
def save_user_data(new_entry):
    user_data = st.session_state.user_data
    if user_data is None:
        user_data = pd.DataFrame(columns=['Date', 'Mood', 'OK_Level', 'Mood_Difference', 'Description'])

    # Calculate Mood_Difference
    mood_difference = new_entry['Mood'] - new_entry['OK_Level']
    new_entry['Mood_Difference'] = mood_difference

    # Append the new entry to the user_data
    user_data = pd.concat([user_data, pd.DataFrame([new_entry])], ignore_index=True)

    return user_data

# Function to display statistics
def display_statistics():
    st.write("## User Data")
    st.write(st.session_state.user_data)

    # Calculate and display statistics
    if st.session_state.user_data is not None:
        st.write("## Statistics")
        total_users = len(st.session_state.user_data)
        positive_mood_users = len(st.session_state.user_data[st.session_state.user_data['Mood_Difference'] > 0])
        negative_mood_users = len(st.session_state.user_data[st.session_state.user_data['Mood_Difference'] < 0])

        st.write(f"Total Users: {total_users}")
        st.write(f"Users with Positive Mood Difference: {positive_mood_users}")
        st.write(f"Users with Negative Mood Difference: {negative_mood_users}")

# Main function
def main():
    st.title("WhistlePeep")

    # User input section
    st.write("## How do you feel today?")
    mood_options = ['Very Bad', 'Bad', 'Neutral', 'Good', 'Very Good']
    user_mood = st.selectbox("Select your mood:", mood_options)

    ok_level = st.slider("What is your OK level?", min_value=0, max_value=100, value=50)

    description = st.text_area("Describe your day:")

    new_entry = {
        'Date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Mood': mood_options.index(user_mood) + 1,
        'OK_Level': ok_level,
        'Description': description
    }

    if st.button("Save"):
        st.session_state.user_data = save_user_data(new_entry)
        st.success("Data saved successfully!")

    # Display statistics
    display_statistics()

    # Restart button
    if st.button("Restart for a new user"):
        st.session_state.user_data = None
        st.text_area("")

if __name__ == "__main__":
    main()
