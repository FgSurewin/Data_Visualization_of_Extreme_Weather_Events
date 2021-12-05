from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from app import app

ratio = [0.403634  , 0.21803177, 0.15440164, 0.12259775, 0.06709435, 0.03424049]
EXP_var=pd.DataFrame(ratio, columns=["Explained Variance"])
EXP_var["Pricipal Components"]=['PC1','PC2','PC3','PC4','PC5','PC6']

fig_ratio = px.bar(EXP_var, 
             x='Pricipal Components', y='Explained Variance',
             text='Explained Variance',
)
fig_ratio.update_traces(texttemplate='%{text:.3f}', textposition='outside')
fig_ratio.update_layout(template='ggplot2') 

layout = html.Div([
    html.H1('Variance Ratio - Scree plot', style={"textAlign": "center", "marginBottom": "50px"}),
    dbc.Row([
            dbc.Col([
                dbc.Row(
                    dbc.Col(
                        dcc.Graph(id='pca_scree_plot', figure=fig_ratio)),
                    justify="center",
                )
            ], width=12 , lg=8 ,style={"paddingLeft":"100px", "paddingRight":"100px"}),
            dbc.Col(
                [
                    html.H2("Findings: (The following sentences are fake...)"),
                    html.P("If you're visiting this page, you're likely here because you're searching for a random sentence. Sometimes a random word just isn't enough, and that is where the random sentence generator comes into play. By inputting the desired number, you can make a list of as many random sentences as you want or need. Producing random sentences can be helpful in a number of different ways.")
                ],
                width=12,
                lg=4,
                style={"paddingRight": "50px"}
            )
    ])   
])

