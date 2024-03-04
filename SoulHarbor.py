import streamlit as st
import pandas as pd
import networkx as nx
import pyvis
import pyvis.network as net
import random

st.title('SoulHarbor: Collaboration Network Visualization')

individuals = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy', 'Kevin', 'Lily']

# Set the number of time steps
time_steps = 5

# Create an empty DataFrame to store the collaboration data for each time step
data = pd.DataFrame(columns=['Time', 'Source', 'Target', 'Weight'])

# Generate random interaction frequencies between individuals for each time step
for t in range(time_steps):
    for i in range(len(individuals)):
        for j in range(i+1, len(individuals)):
            weight = random.randint(1, 10)
            new_data = pd.DataFrame({'Time': [t], 'Source': [individuals[i]], 'Target': [individuals[j]], 'Weight': [weight]})
            data = pd.concat([data, new_data], ignore_index=True)

# Make the DataFrame symmetric, assuming interactions are bidirectional
data = pd.concat([data, data.rename(columns={'Source': 'Target', 'Target': 'Source'})], ignore_index=True)

# Add a timeline (slider) to select the time step
selected_time = st.slider('Select a time step:', min_value=0, max_value=time_steps - 1, value=0)

# Filter the DataFrame based on the selected time step
filtered_data = data[data['Time'] == selected_time]

# Create a NetworkX graph from the filtered DataFrame
G = nx.from_pandas_edgelist(filtered_data, 'Source', 'Target', edge_attr='Weight')

# Set node attributes for interaction frequency
for node in G.nodes():
    G.nodes[node]['Weight'] = sum([G[node][neighbor]['Weight'] for neighbor in G.neighbors(node)])

# Create a Pyvis network object
pyvis_net = net.Network(height="750px", width="100%", directed=False, bgcolor="white", font_color="black")

# Set the physics layout options
pyvis_net.barnes_hut()

# Add nodes and edges to the Pyvis network
for node in G.nodes():
    pyvis_net.add_node(node, label=node, title=f"{node}\nInteraction Frequency: {G.nodes[node]['Weight']}")

for edge in G.edges():
    pyvis_net.add_edge(edge[0], edge[1], value=G[edge[0]][edge[1]]['Weight'])

# Update the network layout and display options
pyvis_net.force_atlas_2based()
pyvis_net.show_buttons(filter_=["physics"])

# Display the Pyvis network in the Streamlit app
st.pyvis_chart(pyvis_net)
