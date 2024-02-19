import streamlit as st
import pandas as pd
import datetime

# Initialize session state
if 'user_data' not in st.session_state:
    st.session_state.user_data = pd.DataFrame(columns=['Date', 'Mood'])

# Function to save user data
def save_user_data(new_entry):
    st.session_state.user_data = st.session_state.user_data.append(new_entry, ignore_index=True)

# Main function
def main():
    user_mood = st.slider('Select your mood:', 0, 100, 50)
    user_name = st.text_input('Enter your name:')
    user_input = st.text_area('Share your thoughts:')
    
    new_entry = {'Date': datetime.datetime.now(), 'Mood': user_mood, 'User': user_name, 'Input': user_input}
    
    # Save user data
    save_user_data(new_entry)
    
    # Display user data
    st.dataframe(st.session_state.user_data)

# Run the app
if __name__ == '__main__':
    main()
