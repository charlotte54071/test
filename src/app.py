'''
 # @ Create Time: 2023-11-23 11:07:50.092603
'''

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc,callback
from dash.dependencies import Input, Output
import pages.homepage, pages.Render_Punkt, pages.Render_Zeile, pages.Render_Block

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], title="test")
app.config.suppress_callback_exceptions = True
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    try:
        if pathname == '/app1':
            return pages.homepage.layout
        elif pathname == '/app2':
            return pages.Render_Block.layout
        elif pathname == '/app3':
            return pages.Render_Punkt.layout
        elif pathname == '/app4':
            return pages.Render_Zeile.layout
        else:
            return pages.homepage.layout  # default 'app1'
    except Exception as e:
        return html.Div([
            html.H3("Error"),
            html.P(str(e))
        ])


if __name__ == "__main__":
    app.run_server(debug=True)
