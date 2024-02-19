import streamlit as st
import pandas as pd
import datetime

# Initialize session state
if 'user_data' not in st.session_state:
    st.session_state.user_data = None

def save_user_data(new_entry):
    user_data = st.session_state.user_data
    if user_data is None:
        user_data = pd.DataFrame(columns=['Date', 'Mood', 'User', 'Input'])

    user_data = user_data.append(new_entry, ignore_index=True)
    user_data.to_csv('user_data.csv', index=False)

    st.session_state.user_data = user_data
    return user_data

def main():
    st.title("WhistlePeep App")

    user_name = st.text_input("Enter your name:")
    user_mood = st.slider("Rate your mood (0-100):", 0, 100)
    user_input = st.text_area("Anything you want to share?")

    if st.button("Submit"):
        new_entry = {
            'Date': datetime.datetime.now(),
            'Mood': user_mood,
            'User': user_name,
            'Input': user_input
        }

        st.write("Your data has been submitted!")
        st.session_state.user_data = save_user_data(new_entry)

        st.line_chart(st.session_state.user_data.set_index('Date')['Mood'], use_container_width=True)

if __name__ == "__main__":
    main()
