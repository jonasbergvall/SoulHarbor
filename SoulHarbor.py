import streamlit as st
import pandas as pd

# Hämta data från CSV-fil
samarbete_data = pd.read_csv("samarbetsdata.csv", index_col="ID")

# Ange deltagare och ID för visualisering
deltagare = st.sidebar.selectbox("Välj deltagare", samarbete_data.index)
id = samarbete_data.loc[deltagare, "ID"]

# Visa information om vald deltagare
st.header(f"Samarbetsdata för {deltagare} (ID: {id})")

# Skapa matris för visuell representation av samarbeten
samarbete_matris = samarbete_data.iloc[:, 2:].values

# Visa matrisen
st.table(samarbete_matris)

# Loopa igenom deltagare och samarbeten
for i in range(samarbete_matris.shape[0]):
    for j in range(samarbete_matris.shape[1]):
        # Visa detaljerad information om samarbete
        if samarbete_matris[i, j] == 1:
            st.markdown(f"- Samarbete med {samarbete_data.index[j]}")

# Visa information om eventuella nya samarbeten
nya_samarbeten = []
for i in range(samarbete_matris.shape[0]):
    for j in range(samarbete_matris.shape[1]):
        if samarbete_matris[i, j] == 1 and samarbete_data.loc[samarbete_data.index[i], f"Samarbete{j+1}"] == 0:
            nya_samarbeten.append((samarbete_data.index[i], samarbete_data.index[j]))

if nya_samarbeten:
    st.header("Nya samarbeten")
    for samarbeten in nya_samarbeten:
        st.markdown(f"- {samarbeten[0]} och {samarbeten[1]}")

