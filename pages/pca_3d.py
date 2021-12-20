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
    html.H1('PCA Scores - 3D plot', style={"textAlign": "center", "marginBottom": "50px", "marginTop": "50px"}),
    dbc.Row([
            dbc.Col([
                dbc.Row(
                    [
                        dbc.Col(html.H4("Please select color encoding: "), width=6),
                        dbc.Col(
                            dcc.Dropdown(
                            id='pca_3d_dropdown', value='Event_Type', clearable=False,
                            persistence=True, persistence_type='session',
                            options=[{'label': "Event Type", 'value': "Event_Type"} , {'label': "Year", 'value': "Year"}],
                            style={"color": "black"}

                        ), 
                        width=6)
                    ],
                    justify="center",
                    style={"marginBottom": "50px"}
                ),
                dbc.Row(
                    dbc.Col(
                        dcc.Graph(id='pca_3d_plot', figure={})),
                    justify="center",
                )
            ], width=12 , lg=8 ,style={"paddingLeft":"100px", "paddingRight":"100px"}),
            dbc.Col(
                [
                    html.H2("Findings: "),
                    html.P("The following visualization is a 3-dimensional plot that describes the relationship between the first three principal components."),
                    html.P("As seen below, the most prominent events are Hurricanes since those are the events that deviate the most from the other occurrences. Floods, Tornadoes, and Wildfires seem to be in harmony with one another as they occupy the same area within this 3-dimensional space. There are no clear and evident clusters that differentiate one principal component from another. This is probably because the features selected don’t deviate as much as they should. Lastly, the main channel for this visualization is the color of each mark that maps to the specific event type from the data set."),
                ],
                width=12,
                lg=4,
                style={"padding": "0 50px", "fontSize": "20px"}
            ),
    ])   
])


@app.callback(
    Output(component_id='pca_3d_plot', component_property='figure'),
    [Input("pca_3d_dropdown", "value")]
)
def display_value(value):
    dfg_pcd_3d = dfg
    fig = px.scatter_3d(dfg_pcd_3d, x="PC1", y="PC2", z="PC3",
              color=value,
              color_discrete_map={'Floods': 'red','Hurricane':'blue','Tornado':'green','Wildfire':'orange'},
              opacity=0.6,
              height=800
              )
    # # tight layout
    # fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

    # # https://plotly.com/python/templates/
    # fig.update_layout(template='ggplot2')

    return fig