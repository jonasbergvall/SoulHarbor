import streamlit as st
import pandas as pd
import csv 
from datetime import date
import plotly.express as px

st.title('WhistlePeep')

sentiment = st.selectbox('How is your day today?', ['Very bad', 'Bad', 'Neutral', 'Good', 'Very good'])
ok_level = st.slider('Set your OK level', min_value=1, max_value=5, step=1)
note = st.text_input('Notes:')

if st.button('Save'):

  today = date.today().strftime('%Y-%m-%d')
  data = [today, sentiment, ok_level, note]  

  with open('data.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)

  st.success('Data saved!')

df = pd.read_csv('data.csv', names=['Date', 'Sentiment', 'OK level', 'Notes'])

if len(df) > 0:

  df['Gap'] = df['OK level'] - df['Sentiment'].map({'Very bad':1, 'Bad':2, 'Neutral':3, 'Good':4, 'Very good':5})

  fig = px.line(df, x='Date', y='Gap', title='Mood Gap Timeline')

  fig.add_scatter(x=df['Date'], y=[df['Gap'].median()], name='Median')

  fig.add_scatter(x=[today], y=[df['Gap'].iloc[-1]], mode='markers', name='You')

else:

  fig = px.line(x=[], y=[], title='No Data')

st.write(fig)

st.write(f"Today's date: {today}")

if st.button('Done'):
  st.cache_resource.clear()
  st.write('App reset')
