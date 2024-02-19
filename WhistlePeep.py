import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg




# Function to save user data
@st.cache(allow_output_mutation=True)
def save_user_data(new_entry, user_data):
    user_data = user_data.append(new_entry, ignore_index=True)
    return user_data

# Main function
def main():
    # Load or create user data
    user_data = pd.read_csv('user_data.csv') if 'user_data' in st.session_state else pd.DataFrame(columns=['Date', 'Mood'])

    # Get user input
    user_name = st.text_input("Enter your name:")
    user_mood = st.slider("Select your mood:", 0, 100)
    user_input = st.text_area("Leave a comment:")

    # Create a new entry
    new_entry = {'Date': datetime.datetime.now(), 'Mood': user_mood, 'User': user_name, 'Input': user_input}

    # Save user data
    st.session_state.user_data = save_user_data(new_entry, user_data)

    # Display the line chart
    st.line_chart(st.session_state.user_data.set_index('Date')['Mood'], use_container_width=True)

# Run the app
if __name__ == "__main__":
    main()
