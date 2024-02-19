import streamlit as st
import pandas as pd

# Function to save user data
def save_user_data(new_entry):
    user_data = pd.read_csv('user_data.csv') if st.session_state.user_data is None else st.session_state.user_data
    user_data = user_data.append(new_entry, ignore_index=True)
    user_data.to_csv('user_data.csv', index=False)
    st.session_state.user_data = user_data
    return user_data

# Main function
def main():
    # Get user input
    user_mood = st.slider("Select your mood:", 0, 100, 50)
    user_name = st.text_input("Enter your name:")
    user_input = st.text_area("Share your thoughts:")

    # Create a new entry
    new_entry = {'Date': pd.to_datetime('now'), 'Mood': user_mood, 'User': user_name, 'Input': user_input}

    # Save user data
    st.session_state.user_data = save_user_data(new_entry)

    # Display area chart
    st.area_chart(st.session_state.user_data.set_index('Date')['Mood'], use_container_width=True, key='user_data_chart')

# Run the app
if __name__ == "__main__":
    main()
