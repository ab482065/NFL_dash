import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

# Load your CSV data
df = pd.read_csv('./data/nfl_offensive_stats.csv')
df.rename(columns={'position ': 'position'}, inplace=True)

def get_player_subset_of_dataset(player: str, columns_to_isolate: list):
    PLAYER_NAME_MATCH = (df["player"] == player)
    return df[columns_to_isolate][PLAYER_NAME_MATCH]

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define a function to create the content of each tab
def create_tab_content(label, position, stat_options):
    return dbc.Tab(label=label, children=[
        dbc.Row([
            dbc.Col([
                html.P(f"Choose a {position.lower()} to view their statistics from 2019-2022."),
                dcc.Dropdown(
                    id=f'{position.lower()}-dropdown',
                    options=[{'label': player, 'value': player} for player in df[df['position'] == position]['player'].unique()],
                    value=df[df['position'] == position]['player'].iloc[0],  # Default selected player
                    multi=False,
                ),
                dcc.RadioItems(
                    id=f'{position.lower()}-stat-radio',
                    options=stat_options,
                    value=stat_options[0]['value'],  # Default selected radio item
                    labelStyle={'display': 'block'},
                ),
                dcc.Graph(id=f'{position.lower()}-stats'),
            ], width=6),
        ]),
    ])


def create_comparison_tab():
    return dbc.Tab(label="Player Comparison", children=[
        dbc.Row([
            dbc.Col([
                html.P("Select Player 1:"),
                dcc.Dropdown(
                    id='player1-dropdown',
                    options=[{'label': player, 'value': player} for player in df['player'].unique()],
                    multi=False,
                ),
            ], width=6),
            dbc.Col([
                html.P("Select Player 2:"),
                dcc.Dropdown(
                    id='player2-dropdown',
                    options=[{'label': player, 'value': player} for player in df['player'].unique()],
                    multi=False,
                ),
            ], width=6),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(id='comparison-detailed-stats', width=6),
            dbc.Col(id='comparison-detailed-viz-container', width=6),
        ], className="mt-4"),
    ])


# Define the layout of the dashboard
app.layout = dbc.Container([
    html.H1("NFL Player Statistics Dashboard", className="mt-5 text-center"),

    # Tabs for different positions
    dbc.Tabs([
        create_tab_content('Quarterbacks', 'QB', [
            {'label': 'Pass Yards', 'value': 'pass_yds'},
            {'label': 'Touchdowns', 'value': 'pass_td'},
            {'label': 'Interceptions', 'value': 'pass_int'},
        ]),
        create_tab_content('Running Backs', 'RB', [
            {'label': 'Rush Yards', 'value': 'rush_yds'},
            {'label': 'Rush Touchdowns', 'value': 'rush_td'},
            {'label': 'Rushing Attempts', 'value': 'rush_att'},
        ]),
        create_tab_content('Wide Receivers', 'WR', [
            {'label': 'Receiving Yards', 'value': 'rec_yds'},
            {'label': 'Receptions', 'value': 'rec'},
            {'label': 'Receiving Touchdowns', 'value': 'rec_td'},
        ]),
        create_comparison_tab(),
    ]),

    # Detailed statistics for selected game ID
    dbc.Row([
        dbc.Col(id='qb-detailed-stats', width=6),
        dbc.Col(id='qb-detailed-viz-container', width=6),
    ], className="mt-4"),
    dbc.Row([
        dbc.Col(id='rb-detailed-stats', width=6),
        dbc.Col(id='rb-detailed-viz-container', width=6),
    ], className="mt-4"),
    dbc.Row([
        dbc.Col(id='wr-detailed-stats', width=6),
        dbc.Col(id='wr-detailed-viz-container', width=6),
    ], className="mt-4"),

])

# Callbacks to update the graphs based on user input
@app.callback(
    Output('qb-stats', 'figure'),
    Output('qb-detailed-stats', 'children'),
    Output('qb-detailed-viz-container', 'children'),
    Input('qb-dropdown', 'value'),
    Input('qb-stat-radio', 'value'),
    Input('qb-stats', 'clickData')
)
def update_qb_stats(selected_qb, selected_stat, click_data):

    if selected_qb:
        qb_data = get_player_subset_of_dataset(selected_qb, ["game_id", "player", selected_stat])

        if selected_stat == 'pass_yds':
            title = f"{selected_qb} Passing Yards by Game ID"
            color_condition = 250
            y_label = "Passing Yards"
        elif selected_stat == 'pass_td':
            title = f"{selected_qb} Touchdowns by Game ID"
            color_condition = 2
            y_label = "Touchdowns"
        else:  # selected_stat == 'pass_int'
            title = f"{selected_qb} Interceptions by Game ID"
            color_condition = 5
            y_label = "Interceptions"

        fig = px.bar(qb_data, x='game_id', y=selected_stat, title=title)
        fig.update_traces(marker=dict(color=['green' if y > color_condition else 'red' for y in qb_data[selected_stat]]))
        fig.update_xaxes(title_text="Game ID")
        fig.update_yaxes(title_text=y_label)


        detailed_stats = None
        detailed_viz_container = None
        if click_data is not None:
            selected_game_id = click_data['points'][0]['x']
            game_stats = df[(df['player'] == selected_qb) & (df['game_id'] == selected_game_id)]
            if not game_stats.empty:
                detailed_stats = html.Div([
                    html.H3(f"Detailed Statistics for Game ID: {selected_game_id}"),
                    html.Table([
                        html.Tr([html.Th("Pass Yards"), html.Td(game_stats['pass_yds'].values[0])]),
                        html.Tr([html.Th("Pass Attempts"), html.Td(game_stats['pass_att'].values[0])]),
                        html.Tr([html.Th("Pass Completions"), html.Td(game_stats['pass_cmp'].values[0])]),
                        html.Tr([html.Th("Interceptions"), html.Td(game_stats['pass_int'].values[0])]),
                        html.Tr([html.Th("Touchdowns"), html.Td(game_stats['pass_td'].values[0])]),
                    ]),
                ])

                detailed_viz_container = dbc.Container([
                    html.H3(f"Visualization Options for {selected_qb}"),
                    dcc.RadioItems(
                        id='qb-detailed-viz-radio',
                        options=[
                            {'label': 'Bar Chart', 'value': 'bar'},
                            {'label': 'Line Chart', 'value': 'line'},
                            {'label': 'Scatter Plot', 'value': 'scatter'},
                        ],
                        value='bar',
                        labelStyle={'display': 'block'},
                    ),
                    dcc.Graph(id='qb-detailed-viz'),
                ])
        return fig, detailed_stats, detailed_viz_container

@app.callback(
    Output('rb-stats', 'figure'),
    Output('rb-detailed-stats', 'children'),
    Output('rb-detailed-viz-container', 'children'),
    Input('rb-dropdown', 'value'),
    Input('rb-stat-radio', 'value'),
    Input('rb-stats', 'clickData')
)
def update_rb_stats(selected_rb, selected_stat, click_data):

    if selected_rb:
        rb_data = get_player_subset_of_dataset(selected_rb, ["game_id", "player", selected_stat])

        # Update the title, color condition, and y-axis label based on selected_stat
        if selected_stat == 'rush_yds':
            title = f"{selected_rb} Rushing Yards by Game ID"
            color_condition = 75
            y_label = "Rushing Yards"
        elif selected_stat == 'rush_td':
            title = f"{selected_rb} Rush Touchdowns by Game ID"
            color_condition = 1
            y_label = "Rush Touchdowns"
        else:  # selected_stat == 'rush_att'
            title = f"{selected_rb} Rushing Attempts by Game ID"
            color_condition = 15
            y_label = "Rushing Attempts"

        fig = px.bar(rb_data, x='game_id', y=selected_stat, title=title)
        fig.update_traces(marker=dict(color=['green' if y > color_condition else 'red' for y in rb_data[selected_stat]]))
        fig.update_xaxes(title_text="Opponent")
        fig.update_yaxes(title_text=y_label)


        detailed_stats = None
        detailed_viz_container = None
        if click_data is not None:
            selected_game_id = click_data['points'][0]['x']
            game_stats = df[(df['player'] == selected_rb) & (df['game_id'] == selected_game_id)]
            if not game_stats.empty:
                detailed_stats = html.Div([
                    html.H3(f"Detailed Statistics for Game ID: {selected_game_id}"),
                    html.Table([
                        html.Tr([html.Th("Rush Yards"), html.Td(game_stats['rush_yds'].values[0])]),
                        html.Tr([html.Th("Rush Attempts"), html.Td(game_stats['rush_att'].values[0])]),
                        html.Tr([html.Th("Rushing Touchdowns"), html.Td(game_stats['rush_td'].values[0])]),
                        html.Tr([html.Th("Longest Rush"), html.Td(game_stats['rush_long'].values[0])])
                    ]),
                ])

                detailed_viz_container = dbc.Container([
                    html.H3(f"Visualization Options for {selected_rb}"),
                    dcc.RadioItems(
                        id='rb-detailed-viz-radio',
                        options=[
                            {'label': 'Bar Chart', 'value': 'bar'},
                            {'label': 'Line Chart', 'value': 'line'},
                            {'label': 'Scatter Plot', 'value': 'scatter'},
                        ],
                        value='bar',
                        labelStyle={'display': 'block'},
                    ),
                    dcc.Graph(id='rb-detailed-viz'),
                ])
        return fig, detailed_stats, detailed_viz_container

@app.callback(
    Output('wr-stats', 'figure'),
    Output('wr-detailed-stats', 'children'),
    Output('wr-detailed-viz-container', 'children'),
    Input('wr-dropdown', 'value'),
    Input('wr-stat-radio', 'value'),
    Input('wr-stats', 'clickData')
)

def update_wr_stats(selected_wr, selected_stat, click_data):

    if selected_wr:
        wr_data = get_player_subset_of_dataset(selected_wr, ["game_id", "player", selected_stat])

        # Update the title, color condition, and y-axis label based on selected_stat
        if selected_stat == 'rec_yds':
            title = f"{selected_wr} Receiving Yards by Game ID"
            color_condition = 70
            y_label = "Receiving Yards"
        elif selected_stat == 'rec':
            title = f"{selected_wr} Receptions by Game ID"
            color_condition = 5
            y_label = "Receptions"
        else:  # selected_stat == 'rec_td'
            title = f"{selected_wr} Receiving Touchdowns by Game ID"
            color_condition = 1
            y_label = "Receiving Touchdowns"

        fig = px.bar(wr_data, x='game_id', y=selected_stat, title=title)
        fig.update_traces(marker=dict(color=['green' if y > color_condition else 'red' for y in wr_data[selected_stat]]))
        fig.update_xaxes(title_text="Opponent")
        fig.update_yaxes(title_text=y_label)


        detailed_stats = None
        detailed_viz_container = None
        if click_data is not None:
            selected_game_id = click_data['points'][0]['x']
            game_stats = df[(df['player'] == selected_wr) & (df['game_id'] == selected_game_id)]
            if not game_stats.empty:
                detailed_stats = html.Div([
                    html.H3(f"Detailed Statistics for Game ID: {selected_game_id}"),
                    html.Table([
                        html.Tr([html.Th("Receiving Yards"), html.Td(game_stats['rec_yds'].values[0])]),
                        html.Tr([html.Th("Targets"), html.Td(game_stats['targets'].values[0])]),
                        html.Tr([html.Th("Receiving Touchdowns"), html.Td(game_stats['rec_td'].values[0])]),
                        html.Tr([html.Th("Longest Reception"), html.Td(game_stats['rec_long'].values[0])])
                    ]),
                ])

                detailed_viz_container = dbc.Container([
                    html.H3(f"Visualization Options for {selected_wr}"),
                    dcc.RadioItems(
                        id='wr-detailed-viz-radio',
                        options=[
                            {'label': 'Compare to', 'value': 'bar'},
                            {'label': 'Line Chart', 'value': 'line'},
                            {'label': 'Scatter Plot', 'value': 'scatter'},
                        ],
                        value='bar',
                        labelStyle={'display': 'block'},
                    ),
                    dcc.Graph(id='wr-detailed-viz'),
                ])
        return fig, detailed_stats, detailed_viz_container

@app.callback(
    Output('comparison-detailed-stats', 'children'),
    Output('comparison-detailed-viz-container', 'children'),
    Input('player1-dropdown', 'value'),
    Input('player2-dropdown', 'value')
)
def update_comparison_stats(player1, player2):
    detailed_stats = None
    detailed_viz_container = None
    
    if player1 and player2:
        player1_stats = get_player_subset_of_dataset(player1, ["game_id", "player", "pass_yds", "pass_td", "pass_int", "rush_yds", "rush_td", "rush_att", "rec_yds", "rec", "rec_td"])
        player2_stats = get_player_subset_of_dataset(player2, ["game_id", "player", "pass_yds", "pass_td", "pass_int", "rush_yds", "rush_td", "rush_att", "rec_yds", "rec", "rec_td"])

        # Calculate statistics and visualizations for player comparison
        # (You can add your logic here)
        
        detailed_stats = html.Div([
            html.H3("Detailed Statistics Comparison"),
            # ... (Display comparison statistics here)
        ])

        detailed_viz_container = dbc.Container([
            html.H3("Visualization Options for Comparison"),
            dcc.RadioItems(
                id='comparison-detailed-viz-radio',
                options=[
                    {'label': 'Bar Chart', 'value': 'bar'},
                    {'label': 'Line Chart', 'value': 'line'},
                    {'label': 'Scatter Plot', 'value': 'scatter'},
                ],
                value='bar',
                labelStyle={'display': 'block'},
            ),
            dcc.Graph(id='comparison-detailed-viz'),
        ])
    
    return detailed_stats, detailed_viz_container

# Run the app if the script is executed
if __name__ == '__main__':
    app.run_server(debug=True)