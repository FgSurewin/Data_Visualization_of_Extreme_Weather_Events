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
                    html.H2("Findings:"),
                    html.P("The following visualization is a time series plot that presents the variation of the first principal component (the one with highest explained variance) over time."),
                    html.P("Here, it is evident that hurricanes are the most prominent disastrous event, however when plotting it against the years, another piece of information is revealed. There is an increase in the PC score for Hurricanes as the years increase from 1996 to 2015. The increase in PC scores means an increase in the impact of Hurricane in terms of property damage, crops damage, fatality and injuries. The increased impact over years could be due to the increased severity/frequency of the event. climate change and the overwhelming increase of greenhouse gases in the atmosphere. Lastly, color has been implemented as a visual encoding to help the end user understand and differentiate between the different types of extreme weather events."),
                    html.P("The next visualization is the time series plot of the second principal component. The plot shows a peak value in principal component scores in 2005, which contributes to the hurricane Katrina, the most destructive for United States landfalling storms. Here also we used color encoding to differentiate between different types of extreme weather events."),
                ],
                width=12,
                lg=4,
                style={"padding": "0 50px", "fontSize":"20px"}
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