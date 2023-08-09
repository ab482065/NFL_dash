import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Load your CSV data
df = pd.read_csv('./data/nfl_offensive_stats.csv')
df.rename(columns={'position ': 'position'}, inplace=True)

def get_player_subset_of_dataset(player: str, columns_to_isolate: list):
    PLAYER_NAME_MATCH = (df["player"] == player)
    return df[columns_to_isolate][PLAYER_NAME_MATCH]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("NFL Player Statistics Dashboard"),
    
    # Tabs for different positions
    dcc.Tabs([
        dcc.Tab(label='Quarterbacks', children=[
            html.Div([
                html.P("Choose a quarterback to view their passing statistics from 2019-2022."),
                dcc.Dropdown(
                    id='qb-dropdown',
                    options=[{'label': player, 'value': player} for player in df[df['position'] == 'QB']['player'].unique()],
                    value="Aaron Rodgers",  # Default selected quarterback
                    multi=False,
                    style={'width': '50%'}
                ),
                dcc.Graph(id='qb-stats'),
            ]),
        ]),
        
        dcc.Tab(label='Running Backs', children=[
            html.Div([
                html.P("Choose a running back to view their rushing statistics from 2019-2022."),
                dcc.Dropdown(
                    id='rb-dropdown',
                    options=[{'label': player, 'value': player} for player in df[df['position'] == 'RB']['player'].unique()],
                    value=df[df['position'] == 'RB']['player'].iloc[0],  # Default selected running back
                    multi=False,
                    style={'width': '50%'}
                ),
                dcc.Graph(id='rb-stats'),
            ]),
        ]),
        
        dcc.Tab(label='Wide Receivers', children=[
            html.Div([
                html.P("Choose a wide receiver to view their receiving statistics from 2019-2022."),
                dcc.Dropdown(
                    id='wr-dropdown',
                    options=[{'label': player, 'value': player} for player in df[df['position'] == 'WR']['player'].unique()],
                    value=df[df['position'] == 'WR']['player'].iloc[0],  # Default selected wide receiver
                    multi=False,
                    style={'width': '50%'}
                ),
                dcc.Graph(id='wr-stats'),
            ]),
        ]),
    ]),
])

# Callback to update the quarterback stats graph
@app.callback(
    Output('qb-stats', 'figure'),
    Input('qb-dropdown', 'value')
)
def update_qb_stats(selected_qb):
    if selected_qb:
        pass_data = get_player_subset_of_dataset(selected_qb, ["game_id", "player", "pass_yds"])
        fig = px.bar(pass_data, x='game_id', y='pass_yds', title=f"{selected_qb} Passing Yards by Game ID")
        fig.update_traces(marker=dict(color=['green' if y > 250 else 'red' for y in pass_data['pass_yds']]))
        fig.update_xaxes(title_text="Game ID")
        fig.update_yaxes(title_text="Passing Yards")
        return fig

# Callback to update the running back stats graph
@app.callback(
    Output('rb-stats', 'figure'),
    Input('rb-dropdown', 'value')
)
def update_rb_stats(selected_rb):
    if selected_rb:
        rush_data = get_player_subset_of_dataset(selected_rb, ["game_id", "player", "rush_yds"])
        fig = px.bar(rush_data, x='game_id', y='rush_yds', title=f"{selected_rb} Rushing Yards per Game")
        fig.update_traces(marker=dict(color=['green' if y > 75 else 'red' for y in rush_data['rush_yds']]))
        fig.update_xaxes(title_text="Game ID")
        fig.update_yaxes(title_text="Rushing Yards")
        return fig

# Callback to update the wide receiver stats graph
@app.callback(
    Output('wr-stats', 'figure'),
    Input('wr-dropdown', 'value')
)
def update_wr_stats(selected_wr):
    if selected_wr:
        rec_data = get_player_subset_of_dataset(selected_wr, ["game_id", "player", "rec_yds"])
        fig = px.bar(rec_data, x='game_id', y='rec_yds', title=f"{selected_wr} Receiving Yards per Game")
        fig.update_traces(marker=dict(color=['green' if y > 70 else 'red' for y in rec_data['rec_yds']]))
        fig.update_xaxes(title_text="Game ID")
        fig.update_yaxes(title_text="Receiving Yards")
        return fig

# Run the app if the script is executed
if __name__ == '__main__':
    app.run_server(debug=True)
