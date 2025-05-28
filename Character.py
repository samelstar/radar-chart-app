import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Radar Chart", layout="centered")

st.title("📊 Interactive Radar Chart")

# Define the radar chart labels
categories = ['Strength', 'Speed', 'Endurance', 'Flexibility', 'Agility', 'Balance']

# Create sliders for each category
values = []
for category in categories:
    val = st.slider(f'{category}', 0, 100, 50)
    values.append(val)

# Radar charts need the data to be circular
values += values[:1]
categories += categories[:1]

# Create radar chart using Plotly
fig = go.Figure(
    data=[
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            line_color='royalblue',
        )
    ]
)

fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 100])
    ),
    showlegend=False,
)

st.plotly_chart(fig, use_container_width=True)
