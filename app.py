import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Load your CSV data
df = pd.read_csv('./data/nfl_offensive_stats.csv')

# Rename the 'position ' column to 'position'
df.rename(columns={'position ': 'position'}, inplace=True)

def get_player_subset_of_dataset(player: str, 
                                columns_to_isolate: list):
    # Filter data for a specific player
    PLAYER_NAME_MATCH = (df["player"] == player)
    return df[columns_to_isolate][PLAYER_NAME_MATCH]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("NFL Player Statistics Dashboard"),
    
    # Section for passing stats
    html.Div([
        html.P("Choose a quarterback to view their passing statistics from 2019-2022."),
        
        # Dropdown to select a quarterback for passing stats
        dcc.Dropdown(
            id='pass-qb-dropdown',
            options=[{'label': player, 'value': player} for player in df[df['position'] == 'QB']['player'].unique()],
            value="Aaron Rodgers",  # Default selected quarterback
            multi=False,
            style={'width': '50%'}
        ),
        
        # Graph to display passing stats
        dcc.Graph(id='pass-stats'),
    ]),
    
    # Section for rushing stats
    html.Div([
        html.P("Choose a running back to view their rushing statistics from 2019-2022."),
        
        # Dropdown to select a running back for rushing stats
        dcc.Dropdown(
            id='rush-rb-dropdown',
            options=[{'label': player, 'value': player} for player in df[df['position'] == 'RB']['player'].unique()],
            value=df[df['position'] == 'RB']['player'].iloc[0],  # Default selected running back
            multi=False,
            style={'width': '50%'}
        ),
        
        # Graph to display rushing stats
        dcc.Graph(id='rush-stats'),
    ]),
])

# Callback to update the passing stats graph based on selected quarterback
@app.callback(
    dash.dependencies.Output('pass-stats', 'figure'),
    [dash.dependencies.Input('pass-qb-dropdown', 'value')]
)
def update_pass_stats(selected_qb):
    # Get subset of data for the selected quarterback
    pass_data = get_player_subset_of_dataset(selected_qb, ["game_id", "player", "pass_yds"])
    
    # Create a bar graph for passing stats
    fig = px.bar(pass_data, x='game_id', y='pass_yds', title=f"{selected_qb} Passing Yards by Game ID")
    
    # Customize bar colors based on pass yards value (green if > 250, red otherwise)
    fig.update_traces(marker=dict(color=['green' if y > 250 else 'red' for y in pass_data['pass_yds']]))
    
    # Update x and y labels
    fig.update_xaxes(title_text="Game ID")
    fig.update_yaxes(title_text="Passing Yards")
    
    return fig

# Callback to update the rushing stats graph based on selected running back
@app.callback(
    dash.dependencies.Output('rush-stats', 'figure'),
    [dash.dependencies.Input('rush-rb-dropdown', 'value')]
)
def update_rush_stats(selected_rb):
    # Get subset of data for the selected running back
    rush_data = get_player_subset_of_dataset(selected_rb, ["game_id", "player", "rush_yds"])
    
    # Create a bar graph for rushing stats
    fig = px.bar(rush_data, x='game_id', y='rush_yds', title=f"{selected_rb} Rushing Yards per Game")
    
    # Customize bar colors based on rush yards value (green if > 75, red otherwise)
    fig.update_traces(marker=dict(color=['green' if y > 75 else 'red' for y in rush_data['rush_yds']]))
    
    # Update x and y labels
    fig.update_xaxes(title_text="Game ID")
    fig.update_yaxes(title_text="Rushing Yards")
    
    return fig

# Run the app if the script is executed
if __name__ == '__main__':
    app.run_server(debug=True)
