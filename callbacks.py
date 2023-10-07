from app import app
from dash import Output, Input, State, dcc

from blueprint import generate_bar_chart, generate_card, generate_line_plot
from functions import get_chart_properties, get_friendly_metric_name
from layouts import q_layout, rb_layout, wr_layout, pc_layout
from data_manager import df
import pandas as pd


@app.callback(
    Output('login_background', 'style'),
    Input('session', 'data')
)
def update_background(data):
    if data and data.get('logged_in'):
        # If logged in, empty the style to remove the background
        return {
            'position': 'fixed',
            'top': '0',
            'left': '0',
            'height': '100%',
            'width': '100%',
            'z-index': '-1',
            'background-image': 'url("/assets/nfl_background.png")',
            'background-size': 'cover',
            'background-position': 'center',
            'background-repeat': 'no-repeat',
            'opacity': '0.001'
        }
    else:
        # If not logged in, set the background
        return {
            'position': 'fixed',
            'top': '0',
            'left': '0',
            'height': '100%',
            'width': '100%',
            'z-index': '-1',
            'background-image': 'url("/assets/nfl_background.png")',
            'background-size': 'cover',
            'background-position': 'center',
            'background-repeat': 'no-repeat',
            'opacity': '0.1'
        }


@app.callback(
    Output('main_content', 'children'),
    [Input('main_menu_id', 'value')]
)
def update_tab(tab_name):
    if tab_name == 'quarterbacks_tab':
        return q_layout
    elif tab_name == 'rb_tab':
        return rb_layout
    elif tab_name == 'wr_tab':
        return wr_layout
    elif tab_name == 'pc_tab':
        return pc_layout
    else:
        return "This tab doesn't exist."


@app.callback(
    Output('bar_plot_q', 'children'),
    Input('player_dropdown', 'value'),
    Input('q_metric_radio', 'value')
)
def render_quarterbacks_bar_plot(selected_player, selected_metric):

    selected_player_data = df[df['player'] == selected_player]
    # Get the properties
    title, color_condition, y_label = get_chart_properties(selected_player, selected_metric)

    # Generate the chart
    return generate_bar_chart(
        selected_player_data,
        x='game_id',
        y=selected_metric,
        title=title,
        color_condition=color_condition,
        y_visible=True,
        show_legend=False  # Add other parameters as needed
    )


@app.callback(
    Output('bar_plot_rb', 'children'),
    Input('player_dropdown', 'value'),
    Input('rb_metric_radio', 'value')
)
def render_rb_bar_plot(selected_player, selected_metric):

    selected_player_data = df[df['player'] == selected_player]
    # Get the properties
    title, color_condition, y_label = get_chart_properties(selected_player, selected_metric)

    # Generate the chart
    return generate_bar_chart(
        selected_player_data,
        x='game_id',
        y=selected_metric,
        title=title,
        color_condition=color_condition,
        y_visible=True,
        show_legend=False  # Add other parameters as needed
    )


@app.callback(
    Output('bar_plot_wb', 'children'),
    Input('player_dropdown', 'value'),
    Input('wr_metric_radio', 'value')
)
def render_wb_bar_plot(selected_player, selected_metric):

    selected_player_data = df[df['player'] == selected_player]
    # Get the properties
    title, color_condition, y_label = get_chart_properties(selected_player, selected_metric)

    # Generate the chart
    return generate_bar_chart(
        selected_player_data,
        x='game_id',
        y=selected_metric,
        title=title,
        color_condition=color_condition,
        y_visible=True,
        show_legend=False  # Add other parameters as needed
    )



@app.callback(
    Output('players_dropdown', 'children'),
    [Input('main_menu_id', 'value')]
)
def render_players_dropdown(tab_name):
    # Define a mapping from tab names to positions
    tab_to_position = {
        'quarterbacks_tab': 'QB',
        'rb_tab': 'RB',
        'wr_tab': 'WR',
        'pc_tab': 'PC'
    }

    # Get the corresponding position from the selected tab
    position = tab_to_position.get(tab_name, None)

    if position is not None:
        # Filter the DataFrame based on the position
        filtered_df = df[df['position'] == position]

        # Create a Dropdown component with the filtered players
        players_dropdown = dcc.Dropdown(
            id='player_dropdown',
            options=[{'label': player, 'value': player} for player in filtered_df['player']],
            value=filtered_df['player'].iloc[0] if not filtered_df.empty else None,
            className='players_dropdown'
        )

        return players_dropdown

    return None  # Return None if no tab matches


@app.callback(
    Output('all_players_drop_1', 'children'),
    Output('all_players_drop_2', 'children'),
    [Input('main_menu_id', 'value')]
)
def render_players_dropdown(tab_name):


        # Create a Dropdown component with the filtered players
        players_dropdown_1 = dcc.Dropdown(
            id='all_player_dropdown_1',
            options=[{'label': player, 'value': player} for player in df['player']],
            value=df['player'].iloc[0] if not df.empty else None,
            className='players_dropdown'
        )

        players_dropdown_2 = dcc.Dropdown(
            id='all_player_dropdown_2',
            options=[{'label': player, 'value': player} for player in df['player']],
            value=df['player'].iloc[0] if not df.empty else None,
            className='players_dropdown'
        )

        return players_dropdown_1, players_dropdown_2



@app.callback(
    Output('first_card', 'children', allow_duplicate=True),
    Output('second_card', 'children', allow_duplicate=True),
    Output('third_card', 'children', allow_duplicate=True),
    Output('fourth_card', 'children', allow_duplicate=True),
    Output('fifth_card', 'children', allow_duplicate=True),
    Input('player_dropdown', 'value'),
    Input('q_metric_radio', 'value')
)
def render_q_cards(selected_player, selected_metric):

    selected_player_data = df[df['player'] == selected_player]
    max_metric_for_player = selected_player_data[selected_player_data[selected_metric] == selected_player_data[selected_metric].max()][selected_metric].iloc[0]
    min_metric_for_player = selected_player_data[selected_player_data[selected_metric] == selected_player_data[selected_metric].min()][selected_metric].iloc[0]
    avg_metric_for_player = int(selected_player_data[selected_metric].mean())
    max_metric_game = selected_player_data[selected_player_data[selected_metric] == selected_player_data[selected_metric].max()]['game_id'].iloc[0]
    total_metric_for_player = int(selected_player_data[selected_metric].sum())
    friendly_metric_name = get_friendly_metric_name(selected_metric)

    # Generate the chart
    return (generate_card('Best Game', max_metric_game, colour_left='grey', width=330),
            generate_card(f'Highest {friendly_metric_name}', max_metric_for_player, colour_left='grey', width=330),
            generate_card(f'Lowest {friendly_metric_name}', min_metric_for_player, colour_left='grey', width=330),
            generate_card(f'Average {friendly_metric_name}', avg_metric_for_player, colour_left='grey', width=330),
            generate_card(f'Total {friendly_metric_name}', total_metric_for_player, colour_left='grey', width=330))


@app.callback(
    Output('first_card', 'children', allow_duplicate=True),
    Output('second_card', 'children', allow_duplicate=True),
    Output('third_card', 'children', allow_duplicate=True),
    Output('fourth_card', 'children', allow_duplicate=True),
    Output('fifth_card', 'children', allow_duplicate=True),
    Input('player_dropdown', 'value'),
    Input('rb_metric_radio', 'value')
)
def render_rb_cards(selected_player, selected_metric):

    selected_player_data = df[df['player'] == selected_player]
    max_metric_for_player = selected_player_data[selected_player_data[selected_metric] == selected_player_data[selected_metric].max()][selected_metric].iloc[0]
    min_metric_for_player = selected_player_data[selected_player_data[selected_metric] == selected_player_data[selected_metric].min()][selected_metric].iloc[0]
    avg_metric_for_player = int(selected_player_data[selected_metric].mean())
    max_metric_game = selected_player_data[selected_player_data[selected_metric] == selected_player_data[selected_metric].max()]['game_id'].iloc[0]
    total_metric_for_player = int(selected_player_data[selected_metric].sum())
    friendly_metric_name = get_friendly_metric_name(selected_metric)

    # Generate the chart
    return (generate_card('Best Game', max_metric_game, colour_left='grey', width=330),
            generate_card(f'Highest {friendly_metric_name}', max_metric_for_player, colour_left='grey', width=330),
            generate_card(f'Lowest {friendly_metric_name}', min_metric_for_player, colour_left='grey', width=330),
            generate_card(f'Average {friendly_metric_name}', avg_metric_for_player, colour_left='grey', width=330),
            generate_card(f'Total {friendly_metric_name}', total_metric_for_player, colour_left='grey', width=330))




@app.callback(
    Output('first_card', 'children', allow_duplicate=True),
    Output('second_card', 'children', allow_duplicate=True),
    Output('third_card', 'children', allow_duplicate=True),
    Output('fourth_card', 'children', allow_duplicate=True),
    Output('fifth_card', 'children', allow_duplicate=True),
    Input('player_dropdown', 'value'),
    Input('wr_metric_radio', 'value')
)
def render_wr_cards(selected_player, selected_metric):

    selected_player_data = df[df['player'] == selected_player]
    max_metric_for_player = selected_player_data[selected_player_data[selected_metric] == selected_player_data[selected_metric].max()][selected_metric].iloc[0]
    min_metric_for_player = selected_player_data[selected_player_data[selected_metric] == selected_player_data[selected_metric].min()][selected_metric].iloc[0]
    avg_metric_for_player = int(selected_player_data[selected_metric].mean())
    max_metric_game = selected_player_data[selected_player_data[selected_metric] == selected_player_data[selected_metric].max()]['game_id'].iloc[0]
    total_metric_for_player = int(selected_player_data[selected_metric].sum())
    friendly_metric_name = get_friendly_metric_name(selected_metric)

    # Generate the chart
    return (generate_card('Best Game', max_metric_game, colour_left='grey', width=330),
            generate_card(f'Highest {friendly_metric_name}', max_metric_for_player, colour_left='grey', width=330),
            generate_card(f'Lowest {friendly_metric_name}', min_metric_for_player, colour_left='grey', width=330),
            generate_card(f'Average {friendly_metric_name}', avg_metric_for_player, colour_left='grey', width=330),
            generate_card(f'Total {friendly_metric_name}', total_metric_for_player, colour_left='grey', width=330))


@app.callback(
    Output('players_comparison_line_plot', 'children'),
    [Input('all_player_dropdown_1', 'value'),
     Input('all_player_dropdown_2', 'value')]
)
def render_players_dropdown(selected_player_1, selected_player_2):
    if selected_player_1 and selected_player_2:
        key_metrics = ['pass_yds', 'rush_yds', 'rec_yds', 'pass_td', 'rush_td', 'rec_td']

        filtered_df = df[df['player'].isin([selected_player_1, selected_player_2])]

        title = f"Comparison between {selected_player_1} and {selected_player_2}"
        filtered_df['game_date'] = pd.to_datetime(filtered_df['game_date'])
        filtered_df = filtered_df.sort_values(by='game_date')
        filtered_df['game_date'] = filtered_df['game_date'].astype(str)
        plot = generate_line_plot(
            df=filtered_df,
            x='game_date',
            metrics=key_metrics,
            players=[selected_player_1, selected_player_2],
            title=title,
            height=620,  # Adjust height and width as needed
            percentage_y_axis=False  # Set to True or False based on your preference
        )

        return plot



@app.callback(
    Output('url2', 'pathname', allow_duplicate=True),
    Input('logout_button_id', 'n_clicks'),
    prevent_initial_call=True
)
def logout(n_clicks):
    if n_clicks is not None and n_clicks > 0:
        return '/logout'