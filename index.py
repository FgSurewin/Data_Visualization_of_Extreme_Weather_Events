
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


# --------------------------------- old code --------------------------------- #
# Connect to main app.py file
# from app import app
# from app import server

# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
# (1) Style:
# Bootstrap Theme: https://bootswatch.com/
# Download the one you want and put it inside the assets folder. (Or replace the old css file)

# (2) Title:
app.title = "Data Analysis of Extreme Weather Events"

server = app.server


# Connect to your app pages
from pages import pca_3d, pca_variance, home, pca_time, pca_pairplot, pca_heatmap


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            # dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
            dbc.DropdownMenu(
                children=[
                    # dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Scree Plot", href="/pca_scree"),
                    dbc.DropdownMenuItem("Pairplot", href="/pca_pairplot"),
                    dbc.DropdownMenuItem("3D Plot", href="/pca_3d"),
                    dbc.DropdownMenuItem("Time Series", href="/pca_time"),
                    dbc.DropdownMenuItem("Heatmap", href="/pca_heatmap"),
                ],
                nav=True,
                in_navbar=True,
                label="PCA",
            ),
        ],
        brand="Data Analysis of Extreme Weather Events",
        brand_href="/",
        color="primary",
        dark=True,
    ),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    if pathname == '/pca_3d':
        return pca_3d.layout
    if pathname == '/pca_scree':
        return pca_variance.layout
    if pathname == '/pca_time':
        return pca_time.layout
    if pathname == '/pca_pairplot':
        return pca_pairplot.layout
    if pathname == '/pca_heatmap':
        return pca_heatmap.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)