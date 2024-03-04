import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Hämta demografisk data
demo_data = pd.read_csv("demodata.csv")

# Hämta samarbetsdata
samarbete_data = pd.read_csv("samarbetsdata.csv")

# Visa information om deltagarna
st.header("Deltagare")
st.table(demo_data)

# Visa information om samarbeten
st.header("Samarbeten")
st.table(samarbete_data)

# Visualisera nätverket av samarbeten
fig, ax = plt.subplots(figsize=(10, 10))

# Noder
for i in range(samarbete_data.shape[0]):
    ax.plot(i, i, "o", color="blue")

# Kanter
for i in range(samarbete_data.shape[0]):
    for j in range(i + 1, samarbete_data.shape[0]):
        if samarbete_data["Samarbete"][i, j] == 1:
            ax.plot([i, j], [i, j], "-", color="gray")

# Lägg till etiketter
for i in range(samarbete_data.shape[0]):
    ax.annotate(samarbete_data["Deltagare"][i], (i, i))

st.pyplot(fig)

# Filtrera och analysera data
# Använd Streamlits widgetar för att låta användare filtrera och analysera data

# Slutsatser och insikter
# Presentera slutsatser och insikter baserat på analysen

