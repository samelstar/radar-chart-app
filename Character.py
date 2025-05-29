import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Radar Chart", layout="centered")

st.title("📊 Interactive Radar Chart")

# Define the radar chart labels
categories = ['Vitality', 'Stamina', 'Dexterity', 'Flexibility', 'Intellect', 'Personality']

# Initialize default values in session state if not already present
for cat in categories:
    if cat not in st.session_state:
        st.session_state[cat] = 50  # default slider value

# Create sliders using session_state
values = []
for cat in categories:
    val = st.slider(cat, 0, 100, st.session_state[cat], key=cat)
    values.append(val)

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

# Correctly indented layout update
fig.update_layout(
    polar=dict(
        bgcolor='black',
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            gridcolor='white',
            linecolor='white',
            tickfont=dict(color='white'),
        ),
        angularaxis=dict(
            gridcolor='white',
            linecolor='white',
            tickfont=dict(color='yellow'),
        ),
    ),
    showlegend=False,
    paper_bgcolor='black',
    plot_bgcolor='black',
)

st.plotly_chart(fig, use_container_width=True)
