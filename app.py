from dotenv import load_dotenv
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from dash import Dash, html, dcc, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import dash
from components import markdown_login
import logging
# from users import create_connection_and_table
import sqlite3
import os
from connection import DB

load_dotenv()

# logging.basicConfig(level=logging.WARNING)
logging.getLogger('werkzeug').setLevel(logging.WARNING)

server = Flask(__name__)
server.secret_key = 'your-secret-key'

app = Dash(__name__, server=server, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.UNITED],
           prevent_initial_callbacks='initial_duplicate')
app.title = 'NFL Player Statistics Dashboard'


app.layout = html.Div([
    html.Div(
        id='login_background',
        style={
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
    ),
    dcc.Location(id='url', refresh=False),
    dbc.Container(id='content_app', fluid=True, className='container-no-padding'),
    dcc.Store(id='session', storage_type='session'),
    html.Div(id='registration_status')

])

login_manager = LoginManager()
login_manager.init_app(server)


class User(UserMixin):
    def __init__(self, username, password):
        self.id = username
        self.password = password




@login_manager.user_loader
def load_user(username):
    # conn = sqlite3.connect('user_data.db')
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    # row = cursor.fetchone()
    db = DB()
    conn = db.getConnection()
    conn.cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    row = conn.cursor.fetchone()
    conn.close()

    if row:
        print(row)
        return User(row[0], row[2])  # username, hashed_password
    return None



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


@app.callback(
    Output('registration_status', 'children'),
    Input('register-button', 'n_clicks'),
    [State('email-signup', 'value'),
     State('username-signup', 'value'),
     State('password-signup', 'value')],
    prevent_initial_call=True
)
def register_user(n, email, username, password):
    if n:
        try:
            # conn = sqlite3.connect('user_data.db')
            # cursor = conn.cursor()

            # hashed_password = generate_password_hash(password)
            # cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            #                (username, email, hashed_password))
            # conn.commit()
            conn = DB().getConnection()

            hashed_password = generate_password_hash(password)
            conn.cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                           (username, email, hashed_password))
            print(conn.cursor.rowcount)
            # conn.commit()
            conn.close()

            return 'User registered successfully!'
        except Exception as e:
            return f'Error: {e}'


@app.callback(
    Output("content_app", "children"),
    Input("signup_button", "n_clicks"),
    prevent_initial_call=True,
)
def switch_to_signup(n):
    if n:
        return serve_signup_form()
    else:
        return serve_login_form()

@app.callback(Output('session', 'data'),
              Output('url', 'pathname'),
              Input('login-button', 'n_clicks'),
              [State('username', 'value'),
               State('password', 'value')],
              prevent_initial_call=True)
def login(n, username, password):
    user = load_user(username)
    if user and check_password_hash(user.password, password):
        return {'logged_in': True, 'username': username}, '/app'
    else:
        return {'logged_in': False, 'username': username}, dash.no_update



@app.callback(Output('content_app', 'children', allow_duplicate=True),
              Output('session', 'data', allow_duplicate=True),
              Input('url', 'pathname'),
              State('session', 'data'))
def serve_page(pathname, data):

    if data and data.get('logged_in'):
        current_username = data.get('username')  # retrieve the username from the session data
        if pathname == '/logout':
            return dcc.Location(pathname='/login', id='url-logout-redirect'), {'logged_in': False, 'username': ''},

        elif pathname == '/app':
            from layouts import layout
            return layout, dash.no_update

        else:
            return serve_login_form(), dash.no_update
    else:
        return serve_login_form(), dash.no_update


from callbacks import *

if __name__ == "__main__":
    # create_connection_and_table()
    app.run_server(debug=False)
