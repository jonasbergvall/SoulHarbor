import streamlit as st
import pandas as pd
from datetime import date

# Initialize variables
data = pd.DataFrame(columns=['Date', 'Sentiment', 'OK level'])

st.title('WhistlePeep') 

# Get user input
sentiment = st.selectbox('How is your day today?', ['Very bad', 'Bad', 'Neutral', 'Good', 'Very good'])

ok_level = st.slider('Set your OK level', min_value=1, max_value=5, step=1)

# Save data
if st.button('Save'):
    today = date.today().strftime('%Y-%m-%d')
    new_data = pd.DataFrame({'Date': [today], 'Sentiment': [sentiment], 'OK level': [ok_level]})
    data = data.append(new_data, ignore_index=True)
    st.success('Data saved!')

# Show pivot chart  
if not data.empty:
   avg = data.pivot_table(index='OK level', values='Date', aggfunc='count').reset_index()
   st.bar_chart(avg, x='OK level', y='Date')
   
# Reset app
if st.button('Done'):
    data = pd.DataFrame(columns=['Date', 'Sentiment', 'OK level']) 
    st.legacy_caching.clear_cache()
    st.write('App reset')
