import streamlit as st
import pandas as pd
import graphviz as gv

# Hämta data från CSV-fil
samarbete_data = pd.read_csv("samarbetsdata.csv")

# Ange deltagare och ID för visualisering
deltagare = st.sidebar.selectbox("Välj deltagare", samarbete_data.index)
id = samarbete_data.loc[deltagare, "ID"]

# Visa information om vald deltagare
st.header(f"Samarbetsdata för {deltagare} (ID: {id})")

# Skapa Graphviz-kod för nätverksgraf
dot = """
digraph G {
  node [shape=circle, fontsize=12];
"""

# Lägg till noder till Graphviz-kod
for deltagare in samarbete_data.columns:
    dot += f"  {deltagare};\n"

# Lägg till kanter till Graphviz-kod
for i in range(samarbete_data.shape[0]):
    for j in range(samarbete_data.shape[1]):
        if samarbete_data.iloc[i, j] == 1:
            dot += f"  {samarbete_data.columns[i]} -> {samarbete_data.columns[j]};\n"

dot += "}"

# Generera PNG-bild från Graphviz-kod
png = gv.render(dot, format='png').pipe(lambda x: x.decode('utf-8'))

# Visa information om samarbeten
st.markdown(f"- Samarbeten med:")
for i in range(samarbete_data.shape[0]):
    for j in range(samarbete_data.shape[1]):
        if samarbete_data.iloc[i, j] == 1:
            st.markdown(f"    - {samarbete_data.columns[j]}")

# Visa nätverksgraf
st.image(png)

# Visa detaljerad information om samarbeten
nya_samarbeten = []
for i in range(samarbete_data.shape[0]):
    for j in range(samarbete_data.shape[1]):
        if samarbete_data.iloc[i, j] == 1 and samarbete_data.loc[samarbete_data.columns[i], f"Samarbete{j+1}"] == 0:
            nya_samarbeten.append((samarbete_data.columns[i], samarbete_data.columns[j]))

if nya_samarbeten:
    st.header("Nya samarbeten")
    for samarbeten in nya_samarbeten:
        st.markdown(f"- {samarbeten[0]} och {samarbeten[1]}")
