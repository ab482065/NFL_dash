import dash
from dash import Dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load your NFL player statistics data into a Pandas DataFrame
df = pd.read_csv('./data/nfl_offensive_stats.csv')

app = dash.Dash(__name__)

# Define the layout of the dashboard

app.layout = html.Div([
    html.H1("NFL Player Statistics Dashboard"),
    html.P("Choose a player from the 2022 season to view their statistics."),
    dcc.Dropdown(
        id='player-dropdown',
        options=[{'label': player, 'value': player_id} for player, player_id in zip(df['player'], df['player_id'])],
        value=df['player_id'][0],
        multi=False,
        style={'width': '50%'}
    ),
    html.P("See the top performing players by position."),
    dcc.Dropdown(
        id='unknown1',
        options=[{'label': position, 'value': player_id} for position, player_id in zip(df['position '], df['player_id'])],
        value=df['player_id'][0],
        multi=False,
        style={'width': '50%'}
    ),
    html.P("See the top performing players by stat category."),
    dcc.Dropdown(
        id='unknown432',
        options=[{'label': position, 'value': player_id} for position, player_id in zip(df['position '], df['player_id'])],
        value=df['player_id'][0],
        multi=False,
        style={'width': '50%'}
    ),
    dcc.Graph(
        id='unknown2'),
    dcc.Graph(
        id='unknown22'),
    dcc.Graph(
        id='unknown3'),
    dcc.Graph(
        id='unknown33'),
])

# @app.callback(
#     Output('player-stats-graph', 'figure'),
#     [Input('player-dropdown', 'value')]
# )
# def update_player_stats(player_id):
#     player_data = df[df['player_id'] == player_id]
#     figure = px.bar(player_data, x='StatType', y='StatValue', title='Player Statistics')
#     return figure

if __name__ == '__main__':
    app.run_server(debug=True)