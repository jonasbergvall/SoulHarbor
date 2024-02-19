import pandas as pd
import streamlit as st

def save_user_data(new_entry):
    user_data = st.session_state.user_data
    user_data = user_data.append(new_entry, ignore_index=True)
    user_data.to_csv('user_data.csv', index=False)
    st.session_state.user_data = pd.read_csv('user_data.csv')
    return st.session_state.user_data

# rest of your code...





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

        # Plot using Plotly
        fig = px.line(st.session_state.user_data, x='Date', y='Mood', title='Mood Over Time')
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
