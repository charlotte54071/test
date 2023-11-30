import dash
from dash import dcc, html, callback
import plotly.graph_objects as go
import pandas as pd

# Assuming the icons and texts are stored in a list of tuples as (icon_path, description)
icons_texts = [
    # ... (your icons and texts from the screenshot)
]

layout = html.Div([
    html.Div([
        dcc.Link('Back to homepage', href='/homepage', style={'fontSize': 18, 'textAlign': 'center', 'family': 'Arial, '
                                                                                                               'sans'
                                                                                                               '-serif'}),
        # add back link
        html.Br(),  # add the change line
    ]),
    html.H3('Legend'),
    html.Div([
        html.Div([
            # Looping through each icon and text to create a segment on the page
            html.Div([
                html.Img(src=icon_path, style={'height': '50px'}),  # Adjust path as necessary
                html.P(description),
            ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '10px'})
            for icon_path, description in icons_texts
        ]),
    ], style={'textAlign': 'center'})
])