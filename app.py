import dash
from dash import Dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load your NFL player statistics data into a Pandas DataFrame
df = pd.read_csv('./data/nfl_offensive_stats.csv')

def get_player_subset_of_dataset(player: str = "Aaron Rodgers", 
                                 columns_to_isolate: list = ["game_id", "player", "pass_yds"], ):
    PLAYER_NAME_MATCH = (df["player"] == player)
    print(f"Player is `{player}`.")
    return df[columns_to_isolate][PLAYER_NAME_MATCH]

app = dash.Dash(__name__)

# Define the layout of the dashboard

app.layout = html.Div([
    html.H1("NFL Player Statistics Dashboard"),
    html.P("Choose a player to view their statistics from 2019- 2022."),
    dcc.Dropdown(
        id='player-dropdown',
        options=[{'label': player, 'value': player_id} for player, player_id in zip(df['player'], df['player_id'])],
        value=df['player_id'][0],
        multi=False,
        style={'width': '50%'}
    ),
    dcc.Graph(
        id='player-stats'),
])

@app.callback(
    Output('player-stats', 'figure'),
    [Input('player-dropdown', 'value')]
)
def update_graph(selected_player_id):
    selected_player_data = df[df['player_id'] == selected_player_id]
    fig = px.bar(selected_player_data, x='stat_category', y='stat_value', title="Player Statistics")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
