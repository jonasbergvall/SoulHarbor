import streamlit as st
import pandas as pd
import datetime
import matplotlib
from matplotlib.backends.backend_agg import RendererAgg

# Initialize the RendererAgg for Matplotlib
matplotlib.use("agg")
_lock = RendererAgg.lock

# Function to save user data
@st.cache(allow_output_mutation=True)
def save_user_data(new_entry, user_data=None):
    if user_data is None:
        user_data = pd.DataFrame(columns=['Date', 'Mood'])

    new_entry['Date'] = datetime.datetime.now()
    user_data = user_data.append(new_entry, ignore_index=True)
    return user_data

# Main function
def main():
    st.title("WhistlePeep App")
    
    # Get user input
    user_name = st.text_input("Enter your name:")
    user_mood = st.slider("Select your mood:", 0, 100, 50)
    user_input = st.text_area("Share your thoughts:")

    # Create a new entry
    new_entry = {'User': user_name, 'Mood': user_mood, 'Input': user_input}

    # Save user data
    with _lock:
        st.session_state.user_data = save_user_data(new_entry, st.session_state.user_data)

    # Display user data
    st.write("User Data:")
    st.write(st.session_state.user_data)

    # Plot user mood over time
    st.write("User Mood Over Time:")
    with _lock:
        fig, ax = matplotlib.pyplot.subplots()
        ax.plot(st.session_state.user_data['Date'], st.session_state.user_data['Mood'])
        ax.set_ylim(0, 100)
        st.pyplot(fig)

# Run the app
if __name__ == "__main__":
    main()
