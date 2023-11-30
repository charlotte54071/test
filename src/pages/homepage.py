# apps/homepage.py
from dash import Dash, html

table_style = {
    'borderCollapse': 'collapse',
    'margin': '10px auto',  # auto margins for horizontal centering
    'textAlign': 'left'     # align text to the left within cells
}

cell_style = {
    'border': '1px solid black',
    'padding': '5px',
    'fontFamily': 'Arial, sans-serif',
    'textAlign': 'left'  # align text to the left within cells
}

header_style = {
    'border': '1px solid black',
    'padding': '5px',
    'fontFamily': 'Arial, sans-serif',
    'fontWeight': 'bold',
    'textAlign': 'left'  # align text to the left within cells
}

# create layout for the homepage
layout = html.Div([
    html.H3('Welcome to UrbanCide',style={'textAlign': 'center','marginTop':20}),
    html.Div([
        html.Div([
            html.A(html.Img(src='/assets/Render_Block.png', style={'height': '280px', 'margin': '10px'}), href='/app2'),
            html.Table([
                html.Tr([html.Td("Bebauungstyp", style=header_style), html.Td("Blockbebauung", style=cell_style)]),
                html.Tr([html.Td("Baujahr", style=header_style), html.Td("1949 – 1957", style=cell_style)]),
                html.Tr([html.Td("Standort", style=header_style), html.Td("München", style=cell_style)]),
                html.Tr([html.Td("Energieträger", style=header_style), html.Td("Wärmepumpe", style=cell_style)]),
                html.Tr([html.Td("Sanierungszustand", style=header_style), html.Td("Passivhaus", style=cell_style)])
            ], style=table_style)
        ], style={'display': 'inline-block','verticalAlign': 'middle', 'width': '30%'}),
        html.Div([
            html.A(html.Img(src='/assets/Render_Punkt.png', style={'height': '280px', 'margin': '10px'}), href='/app3'),
            html.Table([
                html.Tr([html.Td("Bebauungstyp", style=header_style), html.Td("Punktbebauung", style=cell_style)]),
                html.Tr([html.Td("Baujahr", style=header_style), html.Td("1969 – 1978", style=cell_style)]),
                html.Tr([html.Td("Standort", style=header_style), html.Td("München", style=cell_style)]),
                html.Tr([html.Td("Energieträger", style=header_style), html.Td("Wärmepumpe", style=cell_style)]),
                html.Tr([html.Td("Sanierungszustand", style=header_style), html.Td("Passivhaus", style=cell_style)])
            ], style=table_style)

        ], style={'display': 'inline-block', 'verticalAlign': 'middle','width': '30%'}),
        html.Div([
            html.A(html.Img(src='/assets/Render_Zeile.png', style={'height': '280px', 'margin': '10px'}), href='/app4'),
            html.Table([
                html.Tr([html.Td("Bebauungstyp", style=header_style), html.Td("Zeilenbebauung", style=cell_style)]),
                html.Tr([html.Td("Baujahr", style=header_style), html.Td("1919 – 1948", style=cell_style)]),
                html.Tr([html.Td("Standort", style=header_style), html.Td("München", style=cell_style)]),
                html.Tr([html.Td("Energieträger", style=header_style), html.Td("Wärmepumpe", style=cell_style)]),
                html.Tr([html.Td("Sanierungszustand", style=header_style), html.Td("Passivhaus", style=cell_style)])
            ], style=table_style)
        ], style={'display': 'inline-block','verticalAlign': 'middle', 'width': '30%'})
    ], style={'textAlign': 'center','marginBottom':30}),
    html.Div(
        [
            html.A(
                "Allgemeine Erläuterungen",
                href='/app5',
                style={
                    'display': 'block',
                    'textAlign': 'center',
                    'fontSize': '24px',
                    'fontFamily': 'Arial, sans-serif',
                    'fontWeight': 'bold'
                }
            ),
        ]
    )

])
