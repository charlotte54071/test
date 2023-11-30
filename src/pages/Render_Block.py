import dash
from dash import dcc, html, callback
import plotly.graph_objects as go
import pandas as pd

# Read data from the Excel file
try:
    df = pd.read_excel('dash_visu_block.xlsx', sheet_name='Sheet1')
    if not all(column in df.columns for column in ['UTCI', 'GWP', 'LCC', 'cluster',]):
        raise ValueError("Some essential columns are missing from the Excel sheet.")
except Exception as e:
    print(f"Error reading the Excel file: {e}")
    df = pd.DataFrame()

# For Bar Chart
indicators = ['UTCI', 'GWP', 'LCC']
avg_df = df.groupby('cluster').mean()

max_values = df[indicators].max()
min_values = df[indicators].min()


def normalize(column):
    return (column - min_values[column.name]) / (max_values[column.name] - min_values[column.name])


normalized_avg_df = avg_df[indicators].apply(normalize)

# For Box Plot
parameters = df.columns[:14]
min_vals = df[parameters].min()
max_vals = df[parameters].max()
df_normalized = (df[parameters] - min_vals) / (max_vals - min_vals)
clusters = sorted(df['cluster'].unique())

# define the layout of the page
layout = html.Div([
    html.Div([
        dcc.Link('Back to homepage', href='/homepage', style={'fontSize': 18, 'textAlign': 'center', 'family': 'Arial, '
                                                                                                               'sans'
                                                                                                               '-serif'}),
        # add back link
        html.Br(),  # add the change line
    ]),
    dcc.Graph(id='3d-mesh-plot-2',
              style={'display': 'flex',
                     'justifyContent': 'center',
                     'alignItems': 'center',
                     'height': '60vh'}),
    dcc.Graph(id='bar-chart-2'),
    dcc.Dropdown(
        id='cluster-dropdown-2',
        options=[{'label': f"Cluster {cluster}", 'value': cluster} for cluster in clusters],
        value=[clusters[0]],
        multi=True,
        clearable=False,
        style={'marginBottom': '40px'}
    ),
    html.Div(id='box-plots-container-2', style={'marginBottom': '40px', 'textAlign': 'center', 'family': 'Arial, '
                                                                                                         'sans'
                                                                                                         '-serif'}),

    html.Div(children='Input your value', style={'height': '50px', 'fontSize': '24px', 'textAlign': 'center'}),

    html.Div([
        # Row containing three columns
        html.Div([
            # First column for input fields
            html.Div([
                html.Div([
                    html.Div(
                        [
                            html.Label(param, style={'fontSize': '18px', 'marginRight': '15px', 'textAlign': 'right'}),
                        ], style={'width': '40%', 'float': 'left', 'textAlign': 'right'}),
                    dcc.Input(id=f'input-{param}', type='number', step='any',
                              value=df[parameters].median()[param].round(2) if not df.empty else 0,
                              min=min_vals[param], max=max_vals[param],
                              style={'width': '15%', 'float': 'left'}),
                    html.Div(f" Choose value from {min_vals[param].round(2)} to {max_vals[param].round(2)}",
                             style={'display': 'inline-block', 'fontSize': '16px', 'marginLeft': '10px',
                                    'textAlign': 'right'})
                ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '15px'})
                for param in parameters
            ], style={'width': '40%', 'display': 'inline-block', 'textAlign': 'center'}),  # Adjust the width for column

            # Second column for button
            html.Div([
                html.Button('Find Best Cluster', id='submit-button-2',
                            style={'fontSize': '24px', 'lineHeight': '1.5', 'width': '80%', 'height': '60px'})
            ], style={'width': '30%', 'display': 'inline-block', 'textAlign': 'center','marginTop':250}),  # Adjust
            # the width for column

            # Third column for displaying results
            html.Div(id='best-cluster-output-2',
                     style={'fontSize': '20px',
                            'textAlign': 'center',
                            'width': '30%',
                            'display': 'inline-block',
                            'marginTop':260})

        ], style={'display': 'flex', 'width': '100%'}),
    ]),
    html.Div([
        dcc.Link('Back to homepage', href='/homepage', style={
            'fontSize': '18px',
            'fontFamily': 'Arial, sans-serif'
        }),
    ], style={'textAlign': 'left'})

])


# add callback of mesh diagram-> rotate the diagram
@callback(
    dash.dependencies.Output('3d-mesh-plot-2', 'figure'),
    [dash.dependencies.Input('3d-mesh-plot-2', 'relayoutData')]
)
def update_3d_mesh_plot(relayoutData):
    if df.empty:
        return {}
    # read data from file
    x = df['UTCI']
    y = df['GWP']
    z = df['LCC']

    # assign color according to the value of x, y, z
    max_x, max_y, max_z = max(x), max(y), max(z)
    colors = []

    for i, j, k in zip(x, y, z):
        r_ratio = i / max_x
        g_ratio = j / max_y
        b_ratio = k / max_z
        # （0,101,189) is Tum blue
        rgb_color = (int(0 * r_ratio), int(101 * g_ratio), int(189 * b_ratio))
        colors.append(f'rgb{rgb_color}')

    # create mesh 3d
    mesh = go.Mesh3d(x=x, y=y, z=z, vertexcolor=colors, opacity=0.7, colorscale=None)

    mesh_layout = go.Layout(
        scene=dict(

            xaxis=dict(
                title='UTCI',
                titlefont=dict(color='red')  # Red color for x-axis title
            ),
            yaxis=dict(
                title='GWP',
                titlefont=dict(color='green')  # Green color for y-axis title
            ),
            zaxis=dict(
                title='LCC',
                titlefont=dict(color='blue')  # Blue color for z-axis title
            )
        ),
        title={
            'text': 'Handlungsspielraum',
            'y': 0.9,  # define the 'y' coordinate of title
            'x': 0.5,  # in the middle
            'xanchor': 'center',
            'yanchor': 'top',

        }
    )

    fig = go.Figure(data=[mesh], layout=mesh_layout)

    fig.update_layout(
        title=dict(text='Handlungsspielraum',
                   font=dict(size=24,
                             color='black',
                             family='Arial, sans-serif',
                             )

                   )
    )

    return fig


# add callback->show different colors of selected clusters
@callback(
    dash.dependencies.Output('bar-chart-2', 'figure'),
    [dash.dependencies.Input('cluster-dropdown-2', 'value')]
)
def update_bar_chart(selected_clusters):
    bar_data = []

    indicator_colors = {
        'UTCI': 'red',
        'GWP': 'green',
        'LCC': 'blue'
    }

    bar_width = 0.2
    offset = bar_width * len(indicators) / 2

    legend_added = {indicator: False for indicator in indicators}

    for cluster in normalized_avg_df.index:
        for i, indicator in enumerate(indicators):
            show_legend = not legend_added[indicator]
            color = indicator_colors[indicator] if cluster in selected_clusters else 'rgba(204, 204, 204, 0.7)'
            x_position = cluster - offset + (i + 0.5) * bar_width
            bar_data.append(
                go.Bar(
                    x=[x_position],
                    y=[normalized_avg_df.loc[cluster, indicator]],
                    name=indicator,
                    marker_color=color,
                    showlegend=show_legend,
                    width=bar_width
                )
            )
            legend_added[indicator] = True

    return {
        'data': bar_data,
        'layout': {
            'title': {'text': 'Einordnung der cluster',
                      'font':
                          {
                              'size': 24,
                              'color': 'black',
                              'family': 'Arial, sans-serif',
                              'weight': 'bold'
                          }},
            'xaxis': {'title': 'Cluster', 'tickvals': list(normalized_avg_df.index),
                      'ticktext': [f'Cluster {i + 1}' for i in range(len(normalized_avg_df.index))]},
            'yaxis': {
                'title': 'Ereignis der Aspekte',
                'tickvals': [0, 0.5, 1],
                'ticktext': ['Gut', 'Mittel', 'Schlecht']
            },
            'barmode': 'group',
            'bargap': 0,
            'bargroupgap': 0,

        }
    }


# add callbacks which is related to the 'box plot' and 'input'
@callback(
    [dash.dependencies.Output('box-plots-container-2', 'children'),
     dash.dependencies.Output('best-cluster-output-2', 'children')],
    [dash.dependencies.Input('cluster-dropdown-2', 'value'),
     dash.dependencies.Input('submit-button-2', 'n_clicks')],
    [dash.dependencies.State(f'input-{param}', 'value') for param in parameters]
)
def combined_callback(selected_clusters, n_clicks, *values):
    # callback_context is a Dash object that gets information about which input has triggered the callback
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update, dash.no_update

    # find and store which callback is triggered
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    button_clicked = n_clicks and n_clicks > 0

    # Processing and normalizing user input
    input_values = {param: value for param, value in zip(parameters, values)}
    all_values_provided = all(value is not None for value in input_values.values())

    # Normalize user inputs or set to zero if not provided
    normalized_input_values = {
        param: (value - min_vals[param]) / (max_vals[param] - min_vals[param]) if value is not None else 0 for
        param, value in input_values.items()} if button_clicked else {}

    # check which callback is triggered, if triggered->calculate to get the best cluster
    if trigger_id == 'submit-button-2' and button_clicked:
        if not all_values_provided or df.empty:
            return dash.no_update, "Please ensure all fields are filled before clicking 'Find Best Cluster'."

        differences = df[parameters].apply(lambda row: sum((row - pd.Series(input_values)) ** 2), axis=1)
        best_cluster = df.loc[differences.idxmin(), 'cluster']
        best_cluster_output = f'The closest cluster for your inputs is: Cluster {best_cluster}'
    else:
        best_cluster_output = dash.no_update

    # Update Box Plot chart
    filtered_df = df_normalized[df['cluster'].isin(selected_clusters)]
    traces = []
    for parameter in parameters:
        traces.append(go.Box(y=filtered_df[parameter], name=parameter, boxpoints='all', jitter=0.3, pointpos=-1.8))
        # Add red dots to denote the normalized values of user input if the submit button has been clicked at least once
        if button_clicked:
            # get normalized input, if no input ,get 0
            user_input_normalized = normalized_input_values.get(parameter, 0)
            traces.append(
                go.Scatter(x=[parameter], y=[user_input_normalized], mode='markers', marker=dict(color='red', size=10)))

    box_plot = dcc.Graph(
        figure={
            'data': traces,
            'layout': go.Layout(
                title=dict(text="Box Plots for Selected Clusters",
                           font={'size': 24, 'color': "black", 'family': "Arial, sans-serif"}),
                yaxis=dict(title="Normalized Value", tickvals=[0, 0.5, 1], ticktext=['Low', 'Medium', 'High']),
                xaxis=dict(title="Parameters"),
                showlegend=False,
                margin=dict(l=80, r=40, t=40, b=120),  # Fixed margins
                height=600,  # Fixed height
                width=1350  # Fixed width
            )
        }
    )
    return box_plot, best_cluster_output
