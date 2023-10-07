from dash import html, dcc
import dash_bootstrap_components as dbc
from components import header, main_menu, q_radio, rb_radio, wr_radio
from blueprint import generate_card, generate_line_plot

import pandas as pd
import numpy as np

layout = html.Div([
    dcc.Location(id='url2', refresh=True),
    header,
    main_menu,
    dbc.Row(id='main_content'),
    dbc.Col(children=[
                                html.Button(
                                    html.Img(
                                        src="assets/logout_nfl.png",
                                        height="44px",
                                        id='logout_button_id'
                                    ),
                                    style={
                                        'position': 'fixed',
                                        'bottom': '0',
                                        'left': '0',
                                        'display': 'inline-block',
                                        'opacity': '0.8',
                                        'background': 'none',
                                        'border': 'none',
                                        'padding-left': '2px',
                                        'padding-bottom': '2px',
                                        'margin': '0'
                                    },
                                )
                            ]),
])

player_dropdown = dbc.Row(id='players_dropdown')
all_players_dropdown_1 = dbc.Col(id='all_players_drop_1', width=6)
all_players_dropdown_2 = dbc.Col(id='all_players_drop_2', width=6)
cards = dbc.Col([  # Cards Column
            dbc.Row(id='first_card', className='my-3'),
            dbc.Row(id='second_card', className='my-3'),
            dbc.Row(id='third_card', className='my-3'),
            dbc.Row(id='fourth_card', className='my-3'),
            dbc.Row(id='fifth_card', className='my-3')

        ], width=2, style={'padding-top':'20px'})
q_layout = html.Div([
    dbc.Row([
        dbc.Col([  # Main content Column
            dbc.Row(player_dropdown),  # Dropdown
            dbc.Row([
                q_radio
            ]),
            dbc.Row(id='bar_plot_q', className='bar_plot_container')  # Bar Plot
        ], width={'size': 10, 'offset': 0}),  # This column takes up 9/12 of the grid, and is offset by 1

        cards

        # This column takes up 2/12 of the grid
    ])
])

rb_layout = html.Div([
    dbc.Row([
        dbc.Col([  # Main content Column
            dbc.Row(player_dropdown),  # Dropdown
            dbc.Row([
                rb_radio
            ]),
            dbc.Row(id='bar_plot_rb', className='bar_plot_container')  # Bar Plot
        ], width={'size': 10, 'offset': 0}),  # This column takes up 9/12 of the grid, and is offset by 1

        cards

        # This column takes up 2/12 of the grid
    ])
])

wr_layout = html.Div([
    dbc.Row([
        dbc.Col([  # Main content Column
            dbc.Row(player_dropdown),  # Dropdown
            dbc.Row([
                wr_radio
            ]),
            dbc.Row(id='bar_plot_wb', className='bar_plot_container')  # Bar Plot
        ], width={'size': 10, 'offset': 0}),  # This column takes up 9/12 of the grid, and is offset by 1

        cards

        # This column takes up 2/12 of the grid
    ])
])

pc_layout = html.Div([
    dbc.Row([all_players_dropdown_1, all_players_dropdown_2], style={'margin-right':'41px'}),
    dbc.Row(id='players_comparison_line_plot')
])