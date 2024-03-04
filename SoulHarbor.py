import streamlit as st
import pandas as pd
import networkx as nx
import plotly.graph_objects as go
import random
import numpy as np

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

# Create a dictionary of node positions for better visualization
pos = nx.spring_layout(G, k=0.5, iterations=100)

# Define a function to adjust the noise level based on the interaction frequency
def adjust_noise_level(frequency):
    max_frequency = 10  # Maximum interaction frequency
    base_noise_level = 0.1  # Base noise level for the minimum interaction frequency
    noise_reduction_factor = 0.5  # Factor by which the noise level is reduced for the maximum interaction frequency

    noise_level = base_noise_level - (frequency / max_frequency) * (base_noise_level * noise_reduction_factor)
    return noise_level

# Add random noise to the positions of the nodes based on their interaction frequency
for node in G.nodes():
    noise_level = adjust_noise_level(G.nodes[node]['Weight'])
    pos[node] = (pos[node][0] + random.uniform(-noise_level, noise_level), pos[node][1] + random.uniform(-noise_level, noise_level))

# Prepare the edges and nodes data for Plotly
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

node_x = [pos[node][0] for node in G.nodes()]
node_y = [pos[node][1] for node in G.nodes()]

# Create the Plotly figure for the collaboration network
fig = go.Figure(
    data=go.Scatter(
        x=edge_x,
        y=edge_y,
        mode='lines',
        line=dict(width=0.5, color='#888'),
        hoverinfo='none'
    ),
    layout=go.Layout(
        title='Collaboration Network',
        showlegend=False,
        hovermode='closest',
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        margin=dict(t=50, b=50, l=50, r=50),
        plot_bgcolor='white',
        paper_bgcolor='white',
    )
)

# Add nodes with names to the figure
fig.add_trace(go.Scatter(
    x=node_x,
    y=node_y,
    mode='markers+text',
    marker=dict(
        size=10,
        color=[G.nodes[node]['Weight'] for node in G.nodes()],
        colorscale='Viridis',
        showscale=True,
        line=dict(width=2, color='white')
    ),
    text=[node for node in G.nodes()],
    textposition='top center',
    textfont=dict(size=12, color='black')
))

# Display the figure in the Streamlit app
st.plotly_chart(fig)
