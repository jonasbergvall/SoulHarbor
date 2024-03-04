import pandas as pd
import streamlit as st

# Hämta demografisk data
demo_data = pd.read_csv("SHdata.csv")

# Hämta samarbetsdata
samarbete_data = pd.read_csv("SamData.csv")

# Visa information om deltagarna
st.header("Deltagare")
st.table(demo_data)

# Visa information om samarbeten
st.header("Samarbeten")
st.table(samarbete_data)

# Visualisera nätverket av samarbeten
# Använd verktyg som Gephi eller NodeXL för att skapa en visualisering
# Visa visualiseringen i Streamlit-appen

# Filtrera och analysera data
# Använd Streamlits widgetar för att låta användare filtrera och analysera data

# Slutsatser och insikter
# Presentera slutsatser och insikter baserat på analysen

