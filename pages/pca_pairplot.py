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
    html.H1('Pairplot', style={"textAlign": "center", "marginBottom": "50px"}),
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
                        dbc.Col(html.H4("Please select range: "), width=6),
                        dbc.Col(
                            dcc.Dropdown(
                            id='pca_range_dropdown', value=6, clearable=False,
                            persistence=True, persistence_type='session',
                            options=[{"label" : item, "value": item} for item in [2,3, 4,5,6]],
                            style={"color": "black"}

                        ), 
                        width=6)
                    ],
                    justify="center",
                    style={"marginBottom": "50px"}
                ),
                dbc.Row(
                    dbc.Col(
                        dcc.Graph(id='pca_pairplot', figure={})),
                    justify="center",
                )
            ], width=12 , lg=8 ,style={"paddingLeft":"100px", "paddingRight":"100px"})
    ])  
])


@app.callback(
    Output(component_id='pca_pairplot', component_property='figure'),
    [Input("pca_range_dropdown", "value")]
)
def display_value(value):
    components = dfg.iloc[:,:6].values
    ratio = [0.403634  , 0.21803177, 0.15440164, 0.12259775, 0.06709435, 0.03424049]
    labels = {
        str(i): f"PC {i+1} ({var:.1f}%)"
        for i, var in enumerate(ratio * 100)
    }

    fig_pairplot = px.scatter_matrix(
        components,
        labels=labels,
        dimensions=range(value),
        color=dfg['Event_Type'],
        color_discrete_map={'Floods': 'red','Hurricane':'blue', 'Tornado':'seagreen','Wildfire':'orange'}, 
        height=1000
    )
    fig_pairplot.update_traces(diagonal_visible=False)
    fig_pairplot.update_layout(template='ggplot2') 
    return fig_pairplot