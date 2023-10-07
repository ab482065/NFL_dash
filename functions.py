import dash_bootstrap_components as dbc

from components import markdown_login


def get_chart_properties(selected_qb, selected_stat):
    if selected_stat == 'pass_yds':
        return f"{selected_qb} Passing Yards by Game ID", 250, "Passing Yards"
    elif selected_stat == 'pass_td':
        return f"{selected_qb} Touchdowns by Game ID", 2, "Touchdowns"
    else:  # selected_stat == 'pass_int'
        return f"{selected_qb} Interceptions by Game ID", 5, "Interceptions"




def get_friendly_metric_name(metric):
    mapping = {
        'pass_yds': 'Pass Yards',
        'pass_td': 'Touchdowns',
        'pass_int': 'Interceptions',
        'rush_yds': 'Rush Yards',
        'rush_td': 'Rush Touchdowns',
        'rush_att': 'Rushing Attempts',
        'rec_yds': 'Receiving Yards',
        'rec': 'Receptions',
        'rec_td': 'Receiving Touchdowns'
    }
    return mapping.get(metric, metric)



def serve_login_form():
    return dbc.Container(
        [dbc.Row(markdown_login, className='margin_bot'),
         dbc.Form(
             [
                 dbc.Row(
                     [
                         dbc.Col(
                             dbc.Label("Username:", className="form-label"),
                             style={
                                 'display': 'flex',
                                 'justify-content': 'right',
                                 'align-items': 'end'
                             },
                             width=1
                         ),
                         dbc.Col(dbc.Input(id="username", type="text", style={'background-color': '#fcfcfc', 'color': 'black'}))
                     ],
                     style={'width': '25%'},
                     className="mb-3",
                 ),
                 dbc.Row(
                     [
                         dbc.Col(dbc.Label("Password:", className="form-label"),
                                 style={
                                     'display': 'flex',
                                     'justify-content': 'right',
                                     'align-items': 'end'
                                 },
                                 width=1
                                 ),
                         dbc.Col(dbc.Input(id="password", type="password", style={'background-color': '#fcfcfc', 'color': 'black'}))
                     ],
                     style={'width': '25%'},
                     className="mb-3",
                 ),
                 dbc.Row(
                     [
                         dbc.Col(dbc.Button("Login", id="login-button", n_clicks=0, color="black",
                                            className='login_button_cN', style={'width': '350px'})),
                         dbc.Col(dbc.Button("Sign Up", id="signup_button", n_clicks=0, color="black",
                                            className='login_button_cN', style={'width': '350px'})),
                     ]
                 ),
             ],
             style={
                 'display': 'flex',
                 'justify-content': 'flex-start',
                 'flex-direction': 'column',
                 'align-items': 'center',
                 'padding-top': '5px'
             }
             , )
         ], className='padding_top_login_page'
        , fluid=True
    )

def serve_signup_form():
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Label("Email:", className="form-label"),
                        style={
                            'display': 'flex',
                            'justify-content': 'right',
                            'align-items': 'end'
                        },
                        width=1
                    ),
                    dbc.Col(dbc.Input(id="email-signup", type="email", style={'background-color': '#fcfcfc', 'color': 'black'}))
                ],
                style={'width': '25%'},
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Label("Username:", className="form-label"),
                        style={
                            'display': 'flex',
                            'justify-content': 'right',
                            'align-items': 'end'
                        },
                        width=1
                    ),
                    dbc.Col(dbc.Input(id="username-signup", type="text", style={'background-color': '#fcfcfc', 'color': 'black'}))
                ],
                style={'width': '25%'},
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Label("Password:", className="form-label"),
                        style={
                            'display': 'flex',
                            'justify-content': 'right',
                            'align-items': 'end'
                        },
                        width=1
                    ),
                    dbc.Col(dbc.Input(id="password-signup", type="password", style={'background-color': '#fcfcfc', 'color': 'black'}))
                ],
                style={'width': '25%'},
                className="mb-3",
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Button("Register", id="register-button", n_clicks=0, color="black", className='login_button_cN', style={'width': '350px'}),

                )
            )
        ],
        style={
            'display': 'flex',
            'justify-content': 'flex-start',
            'flex-direction': 'column',
            'align-items': 'center',
            'padding-top': '300px'
        },
        className='padding_top_login_page',
        fluid=True
    )