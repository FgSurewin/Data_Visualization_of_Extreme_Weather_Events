from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from app import app

PCA_SCORES_URL = "https://raw.githubusercontent.com/FgSurewin/Data_Visualization_of_Extreme_Weather_Events/main/datasets/pca_scores.csv"
dfg = pd.read_csv(PCA_SCORES_URL)

layout = html.Div([
    html.H1('In Progress', style={"textAlign": "center", "marginBottom": "50px"}),
    # dbc.Row([
    #         dbc.Col(
    #             [
    #                 html.H2("Findings: (The following sentences are fake...)"),
    #                 html.P("If you're visiting this page, you're likely here because you're searching for a random sentence. Sometimes a random word just isn't enough, and that is where the random sentence generator comes into play. By inputting the desired number, you can make a list of as many random sentences as you want or need. Producing random sentences can be helpful in a number of different ways.")
    #             ],
    #             width=12,
    #             lg=4,
    #             style={"padding-left": "50px"}
    #         ),
    #         dbc.Col([
    #             dbc.Row(
    #                 [
    #                     dbc.Col(html.H4("Please select color encoding: "), width=6),
    #                     dbc.Col(
    #                         dcc.Dropdown(
    #                         id='pca_3d_dropdown', value='Event_Type', clearable=False,
    #                         persistence=True, persistence_type='session',
    #                         options=[{'label': "Event Type", 'value': "Event_Type"} , {'label': "Year", 'value': "Year"}],
    #                         style={"color": "black"}

    #                     ), 
    #                     width=6)
    #                 ],
    #                 justify="center",
    #                 style={"margin-bottom": "50px"}
    #             ),
    #             dbc.Row(
    #                 dbc.Col(
    #                     dcc.Graph(id='pca_3d_plot', figure={})),
    #                 justify="center",
    #             )
    #         ], width=12 , lg=8 ,style={"padding-left":"100px", "padding-right":"100px"})
    # ])   
])


# @app.callback(
#     Output(component_id='pca_3d_plot', component_property='figure'),
#     [Input("pca_3d_dropdown", "value")]
# )
# def display_value(value):
#     dfg_pcd_3d = dfg
#     fig = px.scatter_3d(dfg_pcd_3d, x="PC1", y="PC2", z="PC3",
#               color=value,
#               color_discrete_map={'Floods': 'red','Hurricane':'blue','Tornado':'green','Wildfire':'orange'},
#               opacity=0.6,
#               height=1000
#               )
#     # # tight layout
#     # fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

#     # # https://plotly.com/python/templates/
#     # fig.update_layout(template='ggplot2')

#     return fig