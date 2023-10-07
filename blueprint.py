from dash import dcc, html
import plotly.graph_objects as go



def generate_bar_chart(
        df,
        x,
        y,
        title,
        color_condition=None,
        height=500,
        width=None,
        margin_l=30,
        margin_r=30,
        margin_t=40,
        margin_b=150,
        y_visible=False,
        show_legend=True
):
    bar_trace = go.Bar(
        x=df[x],
        y=df[y],
        text=df[y],
        textposition="auto",
        hoverinfo="none"
    )

    if color_condition is not None:
        bar_trace.marker = dict(
            color=['#386641' if val > color_condition else '#6d1b1f' for val in df[y]],
            opacity=0.7,
            # line=dict(color="#FFFFFF", width=1.5)
        )

    layout = go.Layout(
        title=dict(
            text=title,
            font=dict(size=24, color="#ffc812"),
            x=0.1,
            y=0.97
        ),
        xaxis=dict(tickangle=-45, gridcolor='rgba(128, 128, 128, 0)', gridwidth=0),
        yaxis=dict(title=y, domain=[0.15, 1], visible=y_visible, gridcolor='rgba(128, 128, 128, 0.3)', gridwidth=0.5),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#fcfcfc"),
        margin=dict(l=margin_l, r=margin_r, t=margin_t, b=margin_b),
        height=height,
        width=width,
        uniformtext=dict(mode="hide", minsize=12),
        barmode='group',
        showlegend=show_legend
    )

    fig = go.Figure(data=[bar_trace], layout=layout)
    return dcc.Graph(
        figure=fig,
        config={'displayModeBar': False, 'showLink': False, 'displaylogo': False},
        style={'height': '500px'}
    )

def generate_card(title,
                         value,
                         font_color='#fff',
                         colour_left='#63baa9',
                         colour_right='#3e3e3e',
                         title_font_size='1.5em',
                         value_font_size='1em',
                         width='auto',
                         height='auto',
                         margin='0',
                         padding='20px'):
    """
    Create a tile component for Dash apps.

    Parameters:
    - title (str): Title of the KPI.
    - value (str/int/float): Value of the KPI.
    - font_color (str, optional): Color of the font for the text in the tile.
    - colour_left, colour_right (str, optional): Gradient colors for the tile's background.
    - title_font_size, value_font_size (str, optional): Font sizes for the title and value respectively.
    - width, height, margin, padding (str, optional): Styling dimensions for the KPI tile.

    Returns:
    - html.Div: A Dash HTML Div component styled as a KPI tile.
    """
    return html.Div(
        className='kpi-tile',
        style={
            'width': width,
            'height': height,
            'color': font_color,
            'background': f'linear-gradient(to right, {colour_left}, {colour_right})',
            'margin': margin,
            'padding': padding
        },
        children=[
            html.H3(title, className='kpi-title', style={'font-size': title_font_size}),
            html.P(value, className='kpi-value', style={'font-size': value_font_size})
        ]
    )



def generate_line_plot(
        df,
        metrics,
        x,
        y=None,
        title='Title',
        players=None,
        height=900,
        width=None,
        margin_l=30,
        margin_r=30,
        margin_t=40,
        margin_b=150,
        colors=None,
        show_horizontal_grid=False,
        show_vertical_grid=False,
        x_label=None,
        y_label=None,
        horizontal_grid_color="#D3D3D3",
        vertical_grid_color="#D3D3D3",
        percentage_y_axis=True
):



    if colors is None:
        colors = [
            "#ea592e",
            "#f28f7f",
            "#6561a9",
            "#0f5153",
            "#3e3e3e",
            "#f8ac33",
            "#f9c5af",
            "#a5add8",
            "#63baa9",
            "#b6b6b6",
        ]

    data = []
    for player in players:
        player_df = df[df['player'] == player]
        for metric in metrics:
            line_trace = go.Scatter(
                x=player_df[x],
                y=player_df[metric],
                mode='lines+markers',
                name=f"{player} - {metric}",
                connectgaps=False
                # ... other line_trace settings
            )
            data.append(line_trace)

    layout = go.Layout(
        title=dict(
            text=title,
            font=dict(size=33, color="rgba(62, 62, 62, 0.25)"),
            x=0.05,
            y=0.44,
        ),
        xaxis=dict(
            tickmode='array',
            tickvals=df[x].unique(),
            tickangle=-45,
            showgrid=show_vertical_grid,
            gridcolor=vertical_grid_color,
            title=x_label,
        ),
        yaxis=dict(
            title=y_label,
            showgrid=show_horizontal_grid,
            gridcolor=horizontal_grid_color,
        ),
        plot_bgcolor="rgba(0,0,0,0)",  # Fully transparent
        paper_bgcolor="rgba(0,0,0,0)",  # Fully transparent
        font=dict(color="#3e3e3e"),
        margin=dict(l=margin_l, r=margin_r, t=margin_t, b=margin_b),
        height=height,
        width=width,
        showlegend=True
    )

    fig = go.Figure(data=data, layout=layout)
    return dcc.Graph(figure=fig, config={'displayModeBar': False, 'showLink': False, 'displaylogo': False})


def generate_sunburst_chart(
        df,
        values,
        labels,
        parents,
        title,
        display_legend=True,
        height=500,
        width=None,
        legend_x=0.8,
        legend_y=0.1,
        font_size=13,
        color_palette=None
):
    """
    Generate a sunburst chart using Plotly.

    Parameters:
    - df: A DataFrame containing the data to plot.
    - values (str): Column name in df for the values of each sector in the sunburst chart.
    - labels (str): Column name in df for the labels of each sector in the sunburst chart.
    - parents (str): Column name in df for the parent node of each label. This is used to structure the hierarchy of the chart.
    - title (str): The title of the chart.
    - display_legend (bool, optional): If True, display the chart legend. Default is True.
    - height (int, optional): The height of the chart in pixels. Default is 500.
    - width (int, optional): The width of the chart in pixels. If None, the width is automatically adjusted. Default is None.
    - legend_x (float, optional): The x position of the legend. Default is 0.8.
    - legend_y (float, optional): The y position of the legend. Default is 0.1.
    - font_size (int, optional): The font size for the chart text. Default is 13.
    - color_palette (list of str, optional): The color palette to use for the chart. If None, a default palette is used. Default is None.

    Returns:
    - A dcc.Graph object containing the generated chart.

    Usage example:
    ```
    df = pd.DataFrame({
        'labels': ['Region 1', 'Country 1', 'Country 2', 'Region 2', 'Country 3'],
        'parents': ['', 'Region 1', 'Region 1', '', 'Region 2'],
        'values': [10, 5, 5, 10, 10],
    })
    sunburst_chart = generate_sunburst_chart(df, 'values', 'labels', 'parents', 'My Sunburst Chart')
    ```
    """
    hovertext = ["{}: {}".format(label, val) for label, val in zip(df[labels], df[values])]

    # Default color palette
    if color_palette is None:
        color_palette = [
            "#ea592e",
            "#f28f7f",
            "#6561a9",
            "#0f5153",
            "#3e3e3e",
            "#f8ac33",
            "#f9c5af",
            "#a5add8",
            "#63baa9",
            "#b6b6b6",
        ]

    fig = go.Figure(
        go.Sunburst(
            labels=df[labels],
            parents=df[parents],
            values=df[values],
            hoverinfo="label+value+percent parent",
            hovertext=hovertext,
            marker=dict(
                colors=color_palette,
                line=dict(color="#FFFFFF", width=1),
            ),
            textfont=dict(size=font_size),
            insidetextorientation="radial",
        )
    )

    fig.update_layout(
        title=dict(
            text=title, font=dict(size=18, color="#3e3e3e"), x=0.5, y=0.99
        ),
        legend=dict(
            font=dict(size=14),
            bgcolor="rgba(0,0,0,0)",
            bordercolor="rgba(0,0,0,0)",
            borderwidth=1,
            x=legend_x,
            y=legend_y,
        ),
        showlegend=display_legend,
        plot_bgcolor="rgba(0,0,0,0)",  # Fully transparent
        paper_bgcolor="rgba(0,0,0,0)",  # Fully transparent
        font=dict(color="#3e3e3e"),
        margin=dict(l=30, r=10, t=80, b=10),
        height=height,
        width=width
    )

    return dcc.Graph(figure=fig, config={'displayModeBar': False, 'showLink': False, 'watermark': False})

