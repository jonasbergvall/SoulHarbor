import streamlit as st
import datetime

# Function to save user data
def save_user_data():
    user_name = st.text_input("Your Name:")
    user_mood = st.slider("How is your mood today?", 0, 100, 50)
    user_data_input = st.text_area("Write something about your day:")

    # Save data if all inputs are provided
    if user_name and user_mood is not None and user_data_input:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save user data
        user_entry = {
            "Name": user_name,
            "Mood": user_mood,
            "Data": user_data_input,
            "Time": current_time
        }

        # Display success message
        st.success("Data saved successfully!")

        return user_entry
    else:
        st.warning("Please fill in all the required information.")
        return None

# Main app
def main():
    st.title("WhistlePeep - Your Mood Tracker")
    st.write("Welcome to WhistlePeep! Track your mood and share your thoughts.")

    user_data = save_user_data()

    # Display user data
    if user_data:
        st.subheader("User Data:")
        st.write(user_data)

if __name__ == "__main__":
    main()
