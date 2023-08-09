import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Load your CSV data
df = pd.read_csv('./data/nfl_offensive_stats.csv')

def get_player_subset_of_dataset(player: str = "Aaron Rodgers", 
                                columns_to_isolate: list = ["game_id", "player", "pass_yds"]):
    # Filter data for a specific player
    PLAYER_NAME_MATCH = (df["player"] == player)
    return df[columns_to_isolate][PLAYER_NAME_MATCH]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("NFL Player Statistics Dashboard"),
    html.P("Choose a player to view their statistics from 2019-2022."),
    
    # Dropdown to select a player
    dcc.Dropdown(
        id='player-dropdown',
        options=[{'label': player, 'value': player} for player in df['player'].unique()],
        value="Aaron Rodgers",  # Default selected player
        multi=False,
        style={'width': '50%'}
    ),
    
    # Graph to display player statistics
    dcc.Graph(id='player-stats'),
])

# Callback to update the graph based on selected player
@app.callback(
    dash.dependencies.Output('player-stats', 'figure'),
    [dash.dependencies.Input('player-dropdown', 'value')]
)
def update_player_stats(selected_player):
    # Get subset of data for the selected player
    player_data = get_player_subset_of_dataset(selected_player, ["game_id", "player", "pass_yds"])

    # Create a bar graph using Plotly Express
    fig = px.bar(player_data, x='game_id', y='pass_yds', title=f"{selected_player} Pass Yards by Game ID")

    # Customize bar colors based on pass yards value
    fig.update_traces(marker=dict(color=['green' if y > 250 else 'red' for y in player_data['pass_yds']]))

    fig.update_yaxes(title_text="Pass Yards")
    fig.update_xaxes(title_text="Opponent")

    return fig

# Run the app if the script is executed
if __name__ == '__main__':
    app.run_server(debug=True)
