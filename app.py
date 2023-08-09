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
                html.P("Choose a quarterback to view their statistics from 2019-2022."),
                dcc.Dropdown(
                    id='qb-dropdown',
                    options=[{'label': player, 'value': player} for player in df[df['position'] == 'QB']['player'].unique()],
                    value="Aaron Rodgers",  # Default selected quarterback
                    multi=False,
                    style={'width': '50%'}
                ),
                
                # Radio items to select the type of statistics
                dcc.RadioItems(
                    id='qb-stat-radio',
                    options=[
                        {'label': 'Pass Yards', 'value': 'pass_yds'},
                        {'label': 'Touchdowns', 'value': 'pass_td'},
                        {'label': 'Interceptions', 'value': 'pass_int'}
                    ],
                    value='pass_yds',  # Default selected radio item
                    labelStyle={'display': 'block'}
                ),
                
                dcc.Graph(id='qb-stats'),
            ]),
        ]),
        
        dcc.Tab(label='Running Backs', children=[
            html.Div([
                html.P("Choose a running back to view their statistics from 2019-2022."),
                dcc.Dropdown(
                    id='rb-dropdown',
                    options=[{'label': player, 'value': player} for player in df[df['position'] == 'RB']['player'].unique()],
                    value=df[df['position'] == 'RB']['player'].iloc[0],  # Default selected running back
                    multi=False,
                    style={'width': '50%'}
                ),
                
                # Radio items to select the type of statistics
                dcc.RadioItems(
                    id='rb-stat-radio',
                    options=[
                        {'label': 'Rush Yards', 'value': 'rush_yds'},
                        {'label': 'Rush Touchdowns', 'value': 'rush_td'},
                        {'label': 'Rushing Attempts', 'value': 'rush_att'}
                    ],
                    value='rush_yds',  # Default selected radio item
                    labelStyle={'display': 'block'}
                ),
                
                dcc.Graph(id='rb-stats'),
            ]),
        ]),
        
        dcc.Tab(label='Wide Receivers', children=[
            html.Div([
                html.P("Choose a wide receiver to view their statistics from 2019-2022."),
                dcc.Dropdown(
                    id='wr-dropdown',
                    options=[{'label': player, 'value': player} for player in df[df['position'] == 'WR']['player'].unique()],
                    value=df[df['position'] == 'WR']['player'].iloc[0],  # Default selected wide receiver
                    multi=False,
                    style={'width': '50%'}
                ),
                
                # Radio items to select the type of statistics
                dcc.RadioItems(
                    id='wr-stat-radio',
                    options=[
                        {'label': 'Receiving Yards', 'value': 'rec_yds'},
                        {'label': 'Receptions', 'value': 'rec'},
                        {'label': 'Receiving Touchdowns', 'value': 'rec_td'}
                    ],
                    value='rec_yds',  # Default selected radio item
                    labelStyle={'display': 'block'}
                ),
                
                dcc.Graph(id='wr-stats'),
            ]),
        ]),
        
    ]),
])

# Callback to update the quarterback stats graph based on selected radio item
@app.callback(
    Output('qb-stats', 'figure'),
    Input('qb-dropdown', 'value'),
    Input('qb-stat-radio', 'value')
)
def update_qb_stats(selected_qb, selected_stat):
    if selected_qb:
        qb_data = get_player_subset_of_dataset(selected_qb, ["game_id", "player", selected_stat])
        
        if selected_stat == 'pass_yds':
            title = f"{selected_qb} Passing Yards by Game ID"
            color_condition = 250
            y_label = "Passing Yards"
        elif selected_stat == 'pass_td':
            title = f"{selected_qb} Touchdowns by Game ID"
            color_condition = 1
            y_label = "Touchdowns"
        else:  # selected_stat == 'pass_int'
            title = f"{selected_qb} Interceptions by Game ID"
            color_condition = 1
            y_label = "Interceptions"
        
        fig = px.bar(qb_data, x='game_id', y=selected_stat, title=title)
        fig.update_traces(marker=dict(color=['green' if y > color_condition else 'red' for y in qb_data[selected_stat]]))
        fig.update_xaxes(title_text="Game ID")
        fig.update_yaxes(title_text=y_label)
        return fig

# Callback to update the running back stats graph based on selected radio item
@app.callback(
    Output('rb-stats', 'figure'),
    Input('rb-dropdown', 'value'),
    Input('rb-stat-radio', 'value')
)
def update_rb_stats(selected_rb, selected_stat):
    if selected_rb:
        rb_data = get_player_subset_of_dataset(selected_rb, ["game_id", "player", selected_stat])
        
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
            color_condition = 10
            y_label = "Rushing Attempts"
        
        fig = px.bar(rb_data, x='game_id', y=selected_stat, title=title)
        fig.update_traces(marker=dict(color=['green' if y > color_condition else 'red' for y in rb_data[selected_stat]]))
        fig.update_xaxes(title_text="Game ID")
        fig.update_yaxes(title_text=y_label)
        return fig

# Callback to update the wide receiver stats graph based on selected radio item
@app.callback(
    Output('wr-stats', 'figure'),
    Input('wr-dropdown', 'value'),
    Input('wr-stat-radio', 'value')
)
def update_wr_stats(selected_wr, selected_stat):
    if selected_wr:
        wr_data = get_player_subset_of_dataset(selected_wr, ["game_id", "player", selected_stat])
        
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
        fig.update_xaxes(title_text="Game ID")
        fig.update_yaxes(title_text=y_label)
        return fig

# Run the app if the script is executed
if __name__ == '__main__':
    app.run_server(debug=True)
