import dash_bootstrap_components as dbc
from dash import html, dcc
from data_manager import df

markdown_login = dbc.Row(
    id='markdown',
    children=[
        dbc.Col(
            children=[
                html.Div([
                    html.Img(
                        src="assets/nfl_logo.png",
                        height="200px",
                        style={'display': 'inline-block'}
                    ),
                    html.Img(
                        src="assets/logo.png",
                        height="200px",
                        style={'display': 'inline-block'}
                    ),

                ],
                style={
                    'text-align': 'center'
                }),
            ],
            width={'size': 12},
        ),
        dbc.Col(
            children=[
                dcc.Markdown(
                    children=''' # NFL Player Statistics Dashboard ''',
                    style={
                        'text-align': 'center',
                        'margin-top': '2%',
                        'margin-bottom': '2%'
                    }
                ),
            ],
            width={'size': 12},
        ),
    ],
    justify="center",  # Center horizontally
)


header = dbc.Row(id='header',
                   children=[
                       dbc.Col(
                           children=[
                               dcc.Markdown(
                                   children='''
                    ### NFL Player Statistics Dashboard
                    ''',
                                   style={'display': 'inline-block', 'line-height': '42px', 'vertical-align': 'bottom',
                                          'padding-top': '3%'}
                               ),
                           ],
                           width=2
                       ),



                       dbc.Col(
                           children=[
                               html.Img(
                                   src="assets/logo.png",
                                   height="100px",
                                   style={'display': 'inline-block'}
                               ),
                           ],
                           width=3,
                           style={'width': 'auto'}
                       )
                   ],
                   justify="between",
                   )


main_menu = html.Div(
    id='test_clicks',
    children=[
        dcc.Tabs(
            id="main_menu_id",
            value='quarterbacks_tab',
            parent_className='custom-tabs',
            className='custom-tabs-container top_padding_main_menu',
            children=[
                dcc.Tab(
                    id='quarterbacks_tab_id',
                    label='Quarterbacks',
                    value='quarterbacks_tab',
                    className='custom-tab',
                    selected_className='custom-tab--selected'
                ),
                dcc.Tab(
                    id='rb_tab_id',
                    label='Running Backs',
                    value='rb_tab',
                    className='custom-tab',
                    selected_className='custom-tab--selected'
                ),
                dcc.Tab(
                    id='wr_tab_id',
                    label='Wide Receivers',
                    value='wr_tab',
                    className='custom-tab',
                    selected_className='custom-tab--selected'
                ),
                dcc.Tab(
                    id='pc_tab_id',
                    label='Players Comparison',
                    value='pc_tab',
                    className='custom-tab',
                    selected_className='custom-tab--selected'
                ),
            ]
        )
    ]
)




q_radio = dcc.RadioItems(
    id='q_metric_radio',
    options=[
        {'label': 'Pass Yards', 'value': 'pass_yds'},
        {'label': 'Touchdowns', 'value': 'pass_td'},
        {'label': 'Interceptions', 'value': 'pass_int'},
    ],
    value='pass_yds',
    inline=True,
    className='radio'
)

rb_radio = dcc.RadioItems(
    id='rb_metric_radio',
    options=[
                    {'label': 'Rush Yards', 'value': 'rush_yds'},
                    {'label': 'Rush Touchdowns', 'value': 'rush_td'},
                    {'label': 'Rushing Attempts', 'value': 'rush_att'},
                ],
    value='rush_yds',
    inline=True,
    className='radio'
)

wr_radio = dcc.RadioItems(
    id='wr_metric_radio',
    options=[
                    {'label': 'Receiving Yards', 'value': 'rec_yds'},
                    {'label': 'Receptions', 'value': 'rec'},
                    {'label': 'Receiving Touchdowns', 'value': 'rec_td'},
                ],
    value='rec_yds',
    inline=True,
    className='radio'
)


