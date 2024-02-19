import pandas as pd
import streamlit as st
import datetime

# Function to save user data
def save_user_data(new_entry):
    try:
        user_data = pd.read_csv('user_data.csv') if 'user_data' in st.session_state else pd.DataFrame(columns=['Date', 'Mood'])
    except FileNotFoundError:
        user_data = pd.DataFrame(columns=['Date', 'Mood'])

    if isinstance(new_entry, pd.DataFrame):
        user_data = user_data.append(new_entry, ignore_index=True)
    elif isinstance(new_entry, dict):
        user_data = user_data.append(new_entry, ignore_index=True)
    else:
        st.warning("Invalid data format. Please provide data in the form of a DataFrame or a dictionary.")
        return user_data

    user_data.to_csv('user_data.csv', index=False)
    st.session_state.user_data = user_data
    st.session_state.data_loaded = True  # New line to indicate data has been loaded
    return user_data




# Main function
def main():
    st.title("WhistlePeep")

    # User input for mood and additional data
    user_name = st.text_input("Your Name:")
    user_mood = st.slider("How do you feel today?", 0, 100, 50)
    user_input = st.text_area("Write something about your day:")

    if st.button("Analyze"):
        # Save user data
        new_entry = {'Date': datetime.datetime.now(), 'Mood': user_mood, 'User': user_name, 'Input': user_input}
        save_user_data(new_entry)

        # Display user data
        st.write("Your data has been recorded.")
        st.write("Name:", user_name)
        st.write("Mood:", user_mood)
        st.write("Input:", user_input)

        # Display aggregated data
        st.write("Aggregated Data:")
        st.line_chart(st.session_state.user_data.set_index('Date')['Mood'], use_container_width=True).set_ylim(0, 100)

# Run the app
if __name__ == "__main__":
    main()
