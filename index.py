import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import Input, Output
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
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[
                dbc.themes.BOOTSTRAP])

# Quarterbacks tab layout
qb_layout = dbc.Row([
    dbc.Col([
        html.H5(f"Choose a QB to view their statistics from 2019-2022.",
                style={'margin-top': '20px', 'font-weight': 'bold'}),
        dcc.Dropdown(
            id='qb-dropdown',
            options=[{'label': player, 'value': player}
                     for player in df[df['position'] == 'QB']['player'].unique()],
            # Default selected player
            value=df[df['position'] == 'QB']['player'].iloc[0],
            multi=False,
        ),
        dcc.RadioItems(
            id='qb-stat-radio',
            options=[
                {'label': 'Pass Yards', 'value': 'pass_yds'},
                {'label': 'Touchdowns', 'value': 'pass_td'},
                {'label': 'Interceptions', 'value': 'pass_int'},
            ],
            value='pass_yds',
            labelStyle={'display': 'inline', 'margin-left': '70px'},
            style={'margin-top': '20px',
                   'font-weight': 'bold', 'font-size': '14px'},
            inputStyle={"margin-right": "10px"}
        ),
        dcc.Graph(id='qb-stats',
                  className='graph-div', style={'margin-top': '20px'}),
    ], width=6),
    dbc.Col([
        html.H5('Detailed Statistics of a Player for a Game',
                style={'font-weight': 'bold', 'text-align': 'center'}),
        html.Div(id='qb-detailed-stats', children=[],
                 style={'margin-top': '45px'})
    ], width=6, style={'margin-top': '80px'}),
], style={'margin-bottom': '30px'}),


# Running backs tab layout
rb_layout = dbc.Row([
    dbc.Col([
        html.H5(f"Choose a RB to view their statistics from 2019-2022.",
                style={'margin-top': '20px', 'font-weight': 'bold'}),
        dcc.Dropdown(
            id='rb-dropdown',
            options=[{'label': player, 'value': player}
                     for player in df[df['position'] == 'RB']['player'].unique()],
            # Default selected player
            value=df[df['position'] == 'RB']['player'].iloc[0],
            multi=False,
        ),
        dcc.RadioItems(
            id='rb-stat-radio',
            options=[
                {'label': 'Rushing Yards', 'value': 'rush_yds'},
                {'label': 'Rush Touchdowns', 'value': 'rush_td'},
                {'label': 'Rushing Attempts', 'value': 'rush_att'},
            ],
            value='rush_yds',
            labelStyle={'display': 'inline', 'margin-left': '70px'},
            style={'margin-top': '20px',
                   'font-weight': 'bold', 'font-size': '14px'},
            inputStyle={"margin-right": "10px"}
        ),
        dcc.Graph(id='rb-stats',
                  className='graph-div', style={'margin-top': '20px'}),
    ], width=6),
    dbc.Col([
        html.H5('Detailed Statistics of a Player for a Game',
                style={'font-weight': 'bold', 'text-align': 'center'}),
        html.Div(id='rb-detailed-stats', children=[],
                 style={'margin-top': '45px'})
    ], width=6, style={'margin-top': '80px'}),
], style={'margin-bottom': '30px'}),


# Wide Receivers tab layout
wr_layout = dbc.Row([
    dbc.Col([
        html.H5(f"Choose a WR to view their statistics from 2019-2022.",
                style={'margin-top': '20px', 'font-weight': 'bold'}),
        dcc.Dropdown(
            id='wr-dropdown',
            options=[{'label': player, 'value': player}
                     for player in df[df['position'] == 'WR']['player'].unique()],
            # Default selected player
            value=df[df['position'] == 'WR']['player'].iloc[0],
            multi=False,
        ),
        dcc.RadioItems(
            id='wr-stat-radio',
            options=[
                {'label': 'Receiving Yards', 'value': 'rec_yds'},
                {'label': 'Receptions', 'value': 'rec'},
                {'label': 'Receiving Touchdowns', 'value': 'rec_td'},
            ],
            value='rec_yds',
            labelStyle={'display': 'inline', 'margin-left': '70px'},
            style={'margin-top': '20px',
                   'font-weight': 'bold', 'font-size': '14px'},
            inputStyle={"margin-right": "10px"}
        ),
        dcc.Graph(id='wr-stats',
                  className='graph-div', style={'margin-top': '20px'}),
    ], width=6),
    dbc.Col([
        html.H5('Detailed Statistics of a Player for a Game',
                style={'font-weight': 'bold', 'text-align': 'center'}),
        html.Div(id='wr-detailed-stats', children=[],
                 style={'margin-top': '45px'})
    ], width=6, style={'margin-top': '80px'}),
], style={'margin-bottom': '30px'}),


# comparison tab layout
comparison_layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col([
                html.P("Select Player 1:"),
                dcc.Dropdown(
                    id='player1-dropdown',
                    options=[{'label': player, 'value': player}
                             for player in df['player'].unique()],
                    value=df['player'][0],
                ),
            ], width=6),
            dbc.Col([
                html.P("Select Player 2:"),
                dcc.Dropdown(
                    id='player2-dropdown',
                    options=[{'label': player, 'value': player}
                             for player in df['player'].unique()],
                    value=df['player'][1],
                ),
            ], width=6),
        ]
    ),
    dbc.Row([
        dbc.Col([
            html.Div(id='player-graph-one', children=[])
        ], width=6),
        dbc.Col([
            html.Div(id='player-graph-two', children=[])
        ], width=6),
    ], className="mt-4", style={'margin-bottom': '30px'}),
    dbc.Row([
        dbc.Col([
            html.Div(id='player1-detailed-stats', children=[])
        ], width=6),
        dbc.Col([
            html.Div(id='player2-detailed-stats', children=[])
        ], width=6)
    ]),
    html.Br()

])


app_tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Quarterbacks", tab_id="tab-one",
                        label_style={"color": "#00AEF9",
                                     'font-weight': 'bold', 'font-size': '18px'},
                        tab_style={"marginLeft": "140px"},
                        active_tab_style={"textTransform": "uppercase"},
                        activeTabClassName="fw-bold fst-italic"),
                dbc.Tab(label="Running Backs", tab_id="tab-two",
                        label_style={"color": "#00AEF9",
                                     'font-weight': 'bold', 'font-size': '18px'},
                        tab_style={"marginLeft": "140px"},
                        active_tab_style={"textTransform": "uppercase"},
                        activeTabClassName="fw-bold fst-italic"),
                dbc.Tab(label="Wide Receivers", tab_id="tab-three",
                        label_style={"color": "#00AEF9",
                                     'font-weight': 'bold', 'font-size': '18px'},
                        tab_style={"marginLeft": "140px"},
                        active_tab_style={"textTransform": "uppercase"},
                        activeTabClassName="fw-bold fst-italic"),
                dbc.Tab(label="Players Comparison", tab_id="tab-four",
                        label_style={"color": "#00AEF9",
                                     'font-weight': 'bold', 'font-size': '18px'},
                        tab_style={"marginLeft": "140px"},
                        active_tab_style={"textTransform": "uppercase"},
                        activeTabClassName="fw-bold fst-italic"),
            ],
            id="tabs",
            active_tab="tab-one",
        ),
    ], className="mt-3"
)


app.layout = dbc.Container([
    dbc.Row(
        dbc.Col([
            html.H1("NFL Player Statistics Dashboard", className='title-div')
        ]),
    ),
    dbc.Row(dbc.Col(app_tabs, width=12), className="mb-3"),
    html.Div(id='content', children=[])

])


# navigating through tabs
@app.callback(
    Output("content", "children"),
    [Input("tabs", "active_tab")]
)
def switch_tab(tab_chosen):
    if tab_chosen == "tab-one":
        return qb_layout
    elif tab_chosen == "tab-two":
        return rb_layout
    elif tab_chosen == "tab-three":
        return wr_layout
    elif tab_chosen == "tab-four":
        return comparison_layout
    return html.P("This shouldn't be displayed for now...")


@app.callback(
    Output('qb-stats', 'figure'),
    Input('qb-dropdown', 'value'),
    Input('qb-stat-radio', 'value'),
)
def update_qb_stats(selected_qb, selected_stat):

    if selected_qb:
        qb_data = get_player_subset_of_dataset(
            selected_qb, ["game_id", "player", selected_stat, 'Opponent_abbrev'])

        if selected_stat == 'pass_yds':
            title = f"<b>{selected_qb}</b> Passing Yards against <b>Opponents</b>"
            color_condition = 250
            y_label = "Passing Yards"
        elif selected_stat == 'pass_td':
            title = f"<b>{selected_qb}</b> Touchdowns against <b>Opponents</b>"
            color_condition = 2
            y_label = "Touchdowns"
        else:  # selected_stat == 'pass_int'
            title = f"<b>{selected_qb}</b> Interceptions against <b>Opponents</b>"
            color_condition = 5
            y_label = "Interceptions"
        try:
            fig = px.bar(qb_data, x='Opponent_abbrev', y=selected_stat,
                         title=title, custom_data=['game_id'])
            fig.update_traces(marker=dict(color=['#3a5a40' if y > color_condition else '#c1121f' for y in qb_data[selected_stat]]),
                              marker_line_color='rgb(8,48,107)', marker_line_width=1, opacity=0.8,)
            fig.update_xaxes(title_text="<b>Opponents</b>")
            fig.update_yaxes(title_text=f'<b>{y_label}</b>')
            fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
        except:
            fig = px.bar(qb_data, x='Opponent_abbrev', y=selected_stat,
                         title=title, custom_data=['player'])
            fig.update_traces(marker=dict(color=['#3a5a40' if y > color_condition else '#c1121f' for y in qb_data[selected_stat]]),
                              marker_line_color='rgb(8,48,107)', marker_line_width=1, opacity=0.8,)
            fig.update_xaxes(title_text="<b>Opponents</b>")
            fig.update_yaxes(title_text=f'<b>{y_label}</b>')
            fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
        return fig


@app.callback(
    Output('qb-detailed-stats', 'children'),
    Input('qb-dropdown', 'value'),
    Input('qb-stats', 'clickData'),
    prevent_initial_call=True
)
def update_qb_detailed_stats(selected_qb, click_data):
    if click_data is not None:
        selected_game_id = click_data['points'][0]['customdata'][0]
        game_stats = df[(df['player'] == selected_qb) &
                        (df['game_id'] == selected_game_id)]
        if not game_stats.empty:
            game_stats = game_stats[['pass_yds',
                                     'pass_att', 'pass_cmp', 'pass_int', 'pass_td']]
            game_stats = game_stats.T
            game_stats = game_stats.rename(
                columns={game_stats.columns[0]: 'Count'})
            fig = px.pie(game_stats, values=game_stats.Count, names=game_stats.index,
                         hole=.3, title=f'Stats of <b>{selected_qb}</b> for game <b>{selected_game_id}</b>')
            # fig.update_traces(hoverinfo='label+percent', textinfo='value')
            return dcc.Graph(figure=fig, className='graph-div')


@app.callback(
    Output('rb-stats', 'figure'),
    Input('rb-dropdown', 'value'),
    Input('rb-stat-radio', 'value'),
)
def update_rb_stats(selected_rb, selected_stat):

    if selected_rb:
        rb_data = get_player_subset_of_dataset(
            selected_rb, ["game_id", "player", selected_stat, 'Opponent_abbrev'])

        if selected_stat == 'rush_yds':
            title = f"<b>{selected_rb}</b> Rushing Yards against <b>Opponents</b>"
            color_condition = 75
            y_label = "Rushing Yards"
        elif selected_stat == 'rush_td':
            title = f"<b>{selected_rb}</b> Rush Touchdowns against <b>Opponents</b>"
            color_condition = 1
            y_label = "Rush Touchdowns"
        else:  # selected_stat == 'rush_att'
            title = f"<b>{selected_rb}</b> Rushing Attempts against <b>Opponents</b>"
            color_condition = 15
            y_label = "Rushing Attempts"
        try:
            fig = px.bar(rb_data, x='Opponent_abbrev', y=selected_stat,
                         title=title, custom_data=['game_id'])
            fig.update_traces(marker=dict(color=['#3a5a40' if y > color_condition else '#c1121f' for y in rb_data[selected_stat]]),
                              marker_line_color='rgb(8,48,107)', marker_line_width=1, opacity=0.8,)
            fig.update_xaxes(title_text="<b>Opponents</b>")
            fig.update_yaxes(title_text=f'<b>{y_label}</b>')
            fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
        except:
            fig = px.bar(rb_data, x='Opponent_abbrev', y=selected_stat,
                         title=title, custom_data=['player'])
            fig.update_traces(marker=dict(color=['#3a5a40' if y > color_condition else '#c1121f' for y in rb_data[selected_stat]]),
                              marker_line_color='rgb(8,48,107)', marker_line_width=1, opacity=0.8,)
            fig.update_xaxes(title_text="<b>Opponents</b>")
            fig.update_yaxes(title_text=f'<b>{y_label}</b>')
            fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
        return fig


@app.callback(
    Output('rb-detailed-stats', 'children'),
    Input('rb-dropdown', 'value'),
    Input('rb-stats', 'clickData'),
    prevent_initial_call=True
)
def update_qb_detailed_stats(selected_rb, click_data):
    if click_data is not None:
        selected_game_id = click_data['points'][0]['customdata'][0]
        game_stats = df[(df['player'] == selected_rb) &
                        (df['game_id'] == selected_game_id)]
        if not game_stats.empty:
            game_stats = game_stats[['rush_yds',
                                     'rush_att', 'rush_td', 'rush_long']]
            game_stats = game_stats.T
            game_stats = game_stats.rename(
                columns={game_stats.columns[0]: 'Count'})
            fig = px.pie(game_stats, values=game_stats.Count, names=game_stats.index,
                         hole=.3, title=f'Stats of <b>{selected_rb}</b> for game <b>{selected_game_id}</b>')
            # fig.update_traces(hoverinfo='label+percent', textinfo='value')
            return dcc.Graph(figure=fig, className='graph-div')


@app.callback(
    Output('wr-stats', 'figure'),
    Input('wr-dropdown', 'value'),
    Input('wr-stat-radio', 'value'),
)
def update_wr_stats(selected_wr, selected_stat):

    if selected_wr:
        wr_data = get_player_subset_of_dataset(
            selected_wr, ["game_id", "player", selected_stat, 'Opponent_abbrev'])

        if selected_stat == 'rec_yds':
            title = f"<b>{selected_wr}</b> Receiving Yards against <b>Opponents</b>"
            color_condition = 70
            y_label = "Receiving Yards"
        elif selected_stat == 'rec':
            title = f"<b>{selected_wr}</b> Receptions against <b>Opponents</b>"
            color_condition = 5
            y_label = "Receptions"
        else:  # selected_stat == 'rec_td'
            title = f"<b>{selected_wr}</b> Receiving Touchdowns against <b>Opponents</b>"
            color_condition = 1
            y_label = "Receiving Touchdowns"
        try:
            fig = px.bar(wr_data, x='Opponent_abbrev', y=selected_stat,
                         title=title, custom_data=['game_id'])
            fig.update_traces(marker=dict(color=['#3a5a40' if y > color_condition else '#c1121f' for y in wr_data[selected_stat]]),
                              marker_line_color='rgb(8,48,107)', marker_line_width=1, opacity=0.8,)
            fig.update_xaxes(title_text="<b>Opponents</b>")
            fig.update_yaxes(title_text=f'<b>{y_label}</b>')
            fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
        except:
            fig = px.bar(wr_data, x='Opponent_abbrev', y=selected_stat,
                         title=title, custom_data=['player'])
            fig.update_traces(marker=dict(color=['#3a5a40' if y > color_condition else '#c1121f' for y in wr_data[selected_stat]]),
                              marker_line_color='rgb(8,48,107)', marker_line_width=1, opacity=0.8,)
            fig.update_xaxes(title_text="<b>Opponents</b>")
            fig.update_yaxes(title_text=f'<b>{y_label}</b>')
            fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
        return fig


@app.callback(
    Output('wr-detailed-stats', 'children'),
    Input('wr-dropdown', 'value'),
    Input('wr-stats', 'clickData'),
    prevent_initial_call=True
)
def update_qb_detailed_stats(selected_wr, click_data):
    if click_data is not None:
        selected_game_id = click_data['points'][0]['customdata'][0]
        game_stats = df[(df['player'] == selected_wr) &
                        (df['game_id'] == selected_game_id)]
        if not game_stats.empty:
            game_stats = game_stats[['rec_yds',
                                     'targets', 'rec_td', 'rec_long']]
            game_stats = game_stats.T
            game_stats = game_stats.rename(
                columns={game_stats.columns[0]: 'Count'})
            fig = px.pie(game_stats, values=game_stats.Count, names=game_stats.index,
                         hole=.3, title=f'Stats of <b>{selected_wr}</b> for game <b>{selected_game_id}</b>')
            # fig.update_traces(hoverinfo='label+percent', textinfo='value')
            return dcc.Graph(figure=fig, className='graph-div')


@app.callback(
    Output('player-graph-one', 'children'),
    Output('player-graph-two', 'children'),
    Input('player1-dropdown', 'value'),
    Input('player2-dropdown', 'value')
)
def update_comparison_stats(player1, player2):

    player1_stats = df[df['player'] == player1]
    player2_stats = df[df['player'] == player2]

    fig1 = px.bar(player1_stats, x='Opponent_abbrev', y=["pass_yds", "pass_td", "pass_int", "rush_yds", "rush_td", "rush_att", "rec_yds", "rec", "rec_td"],
                  title=f'Stats for <b>{player1}</b>', custom_data=['game_id'])
    fig1.update_traces(marker_line_color='rgb(8,48,107)',
                       marker_line_width=1, opacity=0.8,)
    fig1.update_xaxes(title_text="<b>Player</b>")
    fig1.update_yaxes(title_text='<b>All STATs</b>')
    fig1.update_layout(plot_bgcolor='rgba(0,0,0,0)')

    fig2 = px.bar(player2_stats, x='Opponent_abbrev', y=["pass_yds", "pass_td", "pass_int", "rush_yds", "rush_td", "rush_att", "rec_yds", "rec", "rec_td"],
                  title=f'Stats for <b>{player2}</b>', custom_data=['game_id'])
    fig2.update_traces(marker_line_color='rgb(8,48,107)',
                       marker_line_width=1, opacity=0.8,)
    fig2.update_xaxes(title_text="<b>Player</b>")
    fig2.update_yaxes(title_text='<b>All STATs</b>')
    fig2.update_layout(plot_bgcolor='rgba(0,0,0,0)')

    return [
        dcc.Graph(id='player1-graph', figure=fig1, className='graph-div'),
        dcc.Graph(id='player2-graph', figure=fig2, className='graph-div')
    ]


@app.callback(
    Output('player1-detailed-stats', 'children'),
    Input('player1-graph', 'clickData'),
    Input('player1-dropdown', 'value'),
    prevent_initial_call=True
)
def update_comparison_detailed_stats(click_data_one, player1):
    if click_data_one is not None:
        selected_game_id = click_data_one['points'][0]['customdata'][0]
        game_stats = df[(df['game_id'] == selected_game_id)]
        if not game_stats.empty:
            game_stats = game_stats[["pass_yds", "pass_td", "pass_int",
                                     "rush_yds", "rush_td", "rush_att", "rec_yds", "rec", "rec_td"]]
            game_stats = game_stats.T
            game_stats = game_stats.rename(
                columns={game_stats.columns[0]: 'Count'})
            fig = go.Figure(
                data=[go.Pie(labels=game_stats.index, values=game_stats.Count, hole=.3, rotation=-90)])
            fig.update_layout(
                title_text=f'Stats of <b>{player1}</b> for game <b>{selected_game_id}</b>')
            # fig.update_traces(hoverinfo='label+percent', textinfo='value')
            return dcc.Graph(figure=fig, className='graph-div')


@app.callback(
    Output('player2-detailed-stats', 'children'),
    Input('player2-graph', 'clickData'),
    Input('player2-dropdown', 'value'),
    prevent_initial_call=True
)
def update_comparison_detailed_stats(click_data_one, player2):
    if click_data_one is not None:
        selected_game_id = click_data_one['points'][0]['customdata'][0]
        game_stats = df[(df['game_id'] == selected_game_id)]
        if not game_stats.empty:
            game_stats = game_stats[["pass_yds", "pass_td", "pass_int",
                                     "rush_yds", "rush_td", "rush_att", "rec_yds", "rec", "rec_td"]]
            game_stats = game_stats.T
            game_stats = game_stats.rename(
                columns={game_stats.columns[0]: 'Count'})
            fig = go.Figure(
                data=[go.Pie(labels=game_stats.index, values=game_stats.Count, hole=.3, rotation=-90)])
            fig.update_layout(
                title_text=f'Stats of <b>{player2}</b> for game <b>{selected_game_id}</b>')
            # fig.update_traces(hoverinfo='label+percent', textinfo='value')
            return dcc.Graph(figure=fig, className='graph-div')


# Run the app if the script is executed
if __name__ == '__main__':
    app.run_server(debug=True)
