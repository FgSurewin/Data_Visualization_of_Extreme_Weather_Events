
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output



# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from pages import pca_3d


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            # dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
            dbc.DropdownMenu(
                children=[
                    # dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("3D Plot", href="/pca_3d"),
                    dbc.DropdownMenuItem("Scree Plot", href="/test2"),
                    dbc.DropdownMenuItem("Pairplot", href="/test3"),
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
    if pathname == '/pca_3d':
        return pca_3d.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)