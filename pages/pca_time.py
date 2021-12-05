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
    html.H1('Time Series Plot', style={"textAlign": "center", "marginBottom": "50px"}),
    dbc.Row([
            dbc.Col(
                [
                    html.H2("Findings: (The following sentences are fake...)"),
                    html.P("If you're visiting this page, you're likely here because you're searching for a random sentence. Sometimes a random word just isn't enough, and that is where the random sentence generator comes into play. By inputting the desired number, you can make a list of as many random sentences as you want or need. Producing random sentences can be helpful in a number of different ways.")
                ],
                width=12,
                lg=4,
                style={"paddingLeft": "50px"}
            ),
            dbc.Col([
                dbc.Row(
                    [
                        dbc.Col(html.H4("Please select component: "), width=6),
                        dbc.Col(
                            dcc.Dropdown(
                            id='pca_time_dropdown', value='PC1', clearable=False,
                            persistence=True, persistence_type='session',
                            options=[{"label" : item, "value": item} for item in ['PC1','PC2','PC3','PC4','PC5','PC6']],
                            style={"color": "black"}

                        ), 
                        width=6)
                    ],
                    justify="center",
                    style={"marginBottom": "50px"}
                ),
                dbc.Row(
                    dbc.Col(
                        dcc.Graph(id='pca_time', figure={})),
                    justify="center",
                )
            ], width=12 , lg=8 ,style={"paddingLeft":"100px", "paddingRight":"100px"})
    ])   
])


@app.callback(
    Output(component_id='pca_time', component_property='figure'),
    [Input("pca_time_dropdown", "value")]
)
def display_value(value):
    dfg_pcd_time = dfg
    time_fig = px.scatter(dfg_pcd_time, x="Year", y=value, color="Event_Type",
                 color_discrete_map={'Floods': 'red','Hurricane':'blue', 'Tornado':'seagreen','Wildfire':'orange'})
    time_fig.update_traces(marker=dict(size=10,
                              line=dict(width=1,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
    return time_fig