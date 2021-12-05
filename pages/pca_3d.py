import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent


# dfg = pd.read_csv(DATA_PATH.joinpath("opsales.csv"))

layout = html.Div([
    html.H1('PCA', style={"textAlign": "center"}),

])


# @app.callback(
#     Output(component_id='my-map', component_property='figure'),
#     [Input(component_id='pymnt-dropdown', component_property='value'),
#      Input(component_id='country-dropdown', component_property='value')]
# )
# def display_value(pymnt_chosen, country_chosen):
#     dfg_fltrd = dfg[(dfg['Order Country'] == country_chosen) &
#                     (dfg["Type"] == pymnt_chosen)]
#     dfg_fltrd = dfg_fltrd.groupby(["Customer State"])[['Sales']].sum()
#     dfg_fltrd.reset_index(inplace=True)
#     fig = px.choropleth(dfg_fltrd, locations="Customer State",
#                         locationmode="USA-states", color="Sales",
#                         scope="usa")
#     return fig