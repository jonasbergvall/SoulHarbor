import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import random

# Title of the app
st.title('SoulHarbor: Collaboration Network Visualization')

# List of hypothetical individuals
individuals = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy', 'Kevin', 'Lily']

# Create an empty DataFrame
data = pd.DataFrame(columns=['Source', 'Target', 'Weight'])

# Generate random interaction frequencies
for i in range(len(individuals)):
    for j in range(i+1, len(individuals)):
        weight = random.randint(1, 10)
        data = data.append({'Source': individuals[i], 'Target': individuals[j], 'Weight': weight}, ignore_index=True)

# Make the DataFrame symmetric (assuming interactions are bidirectional)
data = pd.concat([data, data.rename(columns={'Source': 'Target', 'Target': 'Source'})], ignore_index=True)

# Create a NetworkX graph
G = nx.from_pandas_edgelist(data, 'Source', 'Target', edge_attr='Weight')

# Create a dictionary of node positions for better visualization
pos = nx.spring_layout(G, k=0.5)

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

# Create the Plotly figure
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

# Add nodes to the figure
fig.add_trace(go.Scatter(
    x=node_x,
    y=node_y,
    mode='markers',
    marker=dict(
        size=10,
        color=[G.nodes[node]['Weight'] for node in G.nodes()],
        colorscale='Viridis',
        showscale=True,
        line=dict(width=2, color='white')
    ),
    hoverinfo='text',
    text=[f'{node}<br>Interaction Frequency: {G.nodes[node]["Weight"]}' for node in G.nodes()]
))

# Display the figure in Streamlit
st.plotly_chart(fig)
