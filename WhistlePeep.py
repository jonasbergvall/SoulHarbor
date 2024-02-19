import streamlit as st
import datetime

# Function to get user geolocation
def get_user_location():
    try:
        location = st.session_state.location
        if not location:
            st.warning("Geolocation not available. Please make sure to enable location access in your browser.")
            return None
        return location
    except AttributeError:
        st.warning("Geolocation not available. Please make sure to enable location access in your browser.")
        return None

# Function to save user data
def save_user_data():
    user_name = st.text_input("Your Name:")
    user_mood = st.slider("How is your mood today?", 0, 100, 50)
    user_data_input = st.text_area("Write something about your day:")
    
    # Get user location
    user_location = get_user_location()

    # Save data if all inputs are provided
    if user_name and user_mood is not None and user_data_input and user_location:
        # Save data to session state
        if not hasattr(st.session_state, 'user_data'):
            st.session_state.user_data = []

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save user data
        user_entry = {
            "Name": user_name,
            "Mood": user_mood,
            "Data": user_data_input,
            "Location": user_location,
            "Time": current_time
        }

        st.session_state.user_data.append(user_entry)

        # Display success message
        st.success("Data saved successfully!")

# Main app
def main():
    st.title("WhistlePeep - Your Mood Tracker")
    st.write("Welcome to WhistlePeep! Track your mood and share your thoughts.")

    save_user_data()

    # Display user data
    if hasattr(st.session_state, 'user_data') and st.session_state.user_data:
        st.subheader("User Data:")
        st.write(st.session_state.user_data)

if __name__ == "__main__":
    main()
