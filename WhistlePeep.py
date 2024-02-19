import streamlit as st
st.title('WhistlePeep - An Early Warning System for Work Environment')

user_data = st.text_area('Enter your data here:', '')

if st.button('Analyze'):
    # Lägg till kod för analys av användarens data här
    st.write('Analysis Results:')
