from dash import Dash, html,dcc

icons_texts_left = [('/assets/Baumanteil.png','Baumanteil [%]\nAnteil von mit Bäumen besetzter Spots'),
               ('/assets/Batterie.png','Batterie [kWh]\nKapazität eines PV Stromspeichers'),
               ('/assets/Photovoltaik.png','Photovoltaik (PV) Dach [%]\nAnteil der mit PV belegten Dachfläche'),
               ('/assets/PV_Fassade_Süd.png','PV Fassade Süd [%]\nAnteil der mit PV belegten Fassadenfläche'),
               ('/assets/Kronentransparenz_Winter.png','Kronentransparenz Winter [%]\nBelaubungszustand Oktober bis März'),
               ('/assets/Kronentransparenz_Sommer.png','Kronentransparenz Sommer [%]\nBelaubungszustand April bis September'),
               ('/assets/Fassade_PV_Ost_West.png','Fassade PV Ost-West [%]\nAnteil der mit PV belegten Fassadenfläche'),
               ]

icons_texts_right = [('/assets/Fensterflächenanteil .png','Fensterflächenanteil [%]\nAnteil der Fenster an der Wandfläche'),
               ('/assets/Gesamtenergiedurchlassgrad.png','Gesamtenergiedurchlassgrad (g-Wert) [-]\nAnteil der eintretenden Solarstrahlung'),
               ('/assets/Gründachdicke.png','Gründachdicke [m]\nDicke extensiver Dachbegrünung'),
               ('/assets/Albedo_Fassade.png','Albedo Fassade [-]\nRückstrahlung Fassade, Asphalt ca. 0,15'),
               ('/assets/Kronendurchmesser .png','Kronendurchmesser [m]\nDurchmesser der Baumkrone'),
               ('/assets/Baumhöhe.png','Baumhöhe [m]\nHöhe vom Boden aus gemessen'),
               ('/assets/Straßenbreite.png','Straßenbreite [m]\nStraße zwischen Gebäuden'),
               ]

layout = html.Div([
    html.H3('Allgemeine Erläuterungen',style={'textAlign': 'center','marginTop':20}),
    html.Div([
        # Left Column
        html.Div([
            html.Div([
                html.Img(src=icon_path, style={'height': '60px'}),
                html.Div([html.Div(line, style={'marginBottom': '0px','textAlign': 'left','marginLeft':15}) for line in description.split('\n')]),
            ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '20px'})
            for icon_path, description in icons_texts_left
        ], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top','marginTop':40}),

        # Right Column
        html.Div([
            html.Div([
                html.Img(src=icon_path, style={'height': '60px'}),
                html.Div([html.Div(line, style={'marginBottom': '0px','textAlign': 'left','marginLeft':15}) for line in description.split('\n')]),
            ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '20px'})
            for icon_path, description in icons_texts_right
        ], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top','marginTop':40}),
    ], style={'textAlign': 'right'}),

    html.Div([
        dcc.Link('Back to homepage', href='/homepage', style={
            'fontSize': '18px',
            'fontFamily': 'Arial, sans-serif'
        }),
    ], style={'textAlign': 'right','marginRight':300})

])


