import streamlit as st
import pandas as pd
import datetime

# Function to save user data
def save_user_data(new_entry, user_data):
    user_data = pd.concat([user_data, pd.DataFrame([new_entry])], ignore_index=True)
    return user_data


# Main function
def main():
    st.title("WhistlePeep App")

    # User input
    user_name = st.text_input("Enter your name:")
    user_mood = st.slider("Select your mood:", 0, 100, 50)
    user_input = st.text_area("Share your thoughts:")

    # Save user data on button click
    if st.button("Save Entry"):
        new_entry = {'Date': datetime.datetime.now(), 'Mood': user_mood, 'User': user_name, 'Input': user_input}
        st.session_state.user_data = save_user_data(new_entry, st.session_state.user_data)
        st.success("Entry saved successfully!")

    # Display user data in a table
    st.subheader("Your Entries:")
    st.write(st.session_state.user_data)

    # Display mood over time using area chart
    if not st.session_state.user_data.empty:
        st.subheader("Mood Over Time")
        st.area_chart(st.session_state.user_data.set_index('Date')['Mood'], use_container_width=True).set_ylim(0, 100)

if __name__ == "__main__":
    # Check if 'user_data' is in session state, initialize if not
    if 'user_data' not in st.session_state:
        st.session_state.user_data = pd.DataFrame(columns=['Date', 'Mood', 'User', 'Input'])

    main()
