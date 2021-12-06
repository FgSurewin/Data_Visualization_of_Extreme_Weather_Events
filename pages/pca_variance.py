from dash import dcc
from dash import html
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from app import app

ratio = [0.403634  , 0.21803177, 0.15440164, 0.12259775, 0.06709435, 0.03424049]
EXP_var=pd.DataFrame(ratio, columns=["Explained Variance"])
EXP_var["PC"]=['PC1','PC2','PC3','PC4','PC5','PC6']
EXP_var["Cumulative Variance"]=EXP_var['Explained Variance'].cumsum()


fig_ratio = go.Figure()

fig_ratio.add_trace(
    go.Scatter(
        x=EXP_var['PC'],
        y=EXP_var['Cumulative Variance'],
        marker=dict(size=15, color="LightSeaGreen"),
        text=EXP_var['Cumulative Variance'],
        texttemplate='%{text:.3f}',
        textposition='middle right',
        name="Cumulative Variance"
    ))

fig_ratio.add_trace(
    go.Bar(
        x=EXP_var['PC'],
        y=EXP_var['Explained Variance'],
        marker=dict(color="RoyalBlue"),
        text=EXP_var['Explained Variance'],
        texttemplate='%{text:.3f}',
        textposition='outside',
        name="Explained Variance"
    ))

# fig_ratio.update_traces(texttemplate='%{text:.3f}', textposition='outside')
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
                    html.H2("Findings: "),
                    html.P("The following visualization is a bar chart that compares the relationship between the explained variance and the principal components."),
                    html.P("As seen below, the first principal component generated is the one that possesses the highest ratio as opposed to the other values computed. In other words, PC1 reveals the percentage of variance that is attributed by each of the selected components. In theory, it would be ideal to have an explained variance ratio below .80 to build accurate machine learning models without overfitting the data.")
                ],
                width=12,
                lg=4,
                style={"padding": "0 50px", "fontSize": "20px"}
            )
    ])   
])

