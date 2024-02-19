import streamlit as st
import pandas as pd
import csv
from datetime import date

st.title('WhistlePeep')

sentiment = st.selectbox('How is your day today?', ['Very bad', 'Bad', 'Neutral', 'Good', 'Very good'])

ok_level = st.slider('Set your OK level', min_value=1, max_value=5, step=1)

if st.button('Save'):

  today = date.today().strftime('%Y-%m-%d')
  data = [today, sentiment, ok_level]  

  with open('data.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
    
  st.success('Data saved!')

# Read CSV file  
df = pd.read_csv('data.csv', names=['Date', 'Sentiment', 'OK level'])

if not df.empty:

  avg = df.pivot_table(index='OK level', values='Date', aggfunc='count').reset_index()
  st.bar_chart(avg, x='OK level', y='Date')

if st.button('Done'):
  st.legacy_caching.clear_cache()
  st.write('App reset') 
