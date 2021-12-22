from dash import dcc
from dash import html
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from app import app

corrs = [[ 0.87322866,  0.71124106,  0.45594481,  0.36783409,  0.5207684 ,
         0.73418292],
       [-0.05144104, -0.10986504, -0.47831011,  0.70955131, -0.55519895,
         0.50297578],
       [ 0.24794303, -0.46555809, -0.35275587,  0.33542313,  0.60232512,
        -0.22011091],
       [-0.18787384, -0.31441675,  0.65828829,  0.40410238, -0.02827643,
        -0.06316867],
       [ 0.20808651, -0.40798246,  0.06851589, -0.28966604, -0.08584071,
         0.3112024 ],
       [ 0.30782008, -0.00372992,  0.02931176,  0.03900239, -0.22268964,
        -0.24229067]]
feature_names = ['Adjusted Property Loss', 'Adjusted Crops Damage', 'INJURIES_DIRECT',
       'INJURIES_INDIRECT', 'DEATHS_DIRECT', 'DEATHS_INDIRECT']
pca_list = ['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6']


fig_heatmap = go.Figure(data=go.Heatmap(
                   z=corrs,
                   x=feature_names,
                   y=pca_list,
                   colorscale = 'matter',
                   hovertemplate='Feature Name: %{x}<br>PCs: %{y}<br>Score: %{z}<extra></extra>'))

# fig_ratio.update_traces(texttemplate='%{text:.3f}', textposition='outside')
fig_heatmap.update_layout(template='ggplot2') 

layout = html.Div([
    html.H1('PCs V.S. Feature Names - Heatmap', style={"textAlign": "center", "marginBottom": "50px", "marginTop": "50px"}),
    dbc.Row([
            dbc.Col([
                dbc.Row(
                    dbc.Col(
                        dcc.Graph(id='pca_heatmap', figure=fig_heatmap)),
                    justify="center",
                )
            ], width=12 , lg=8 ,style={"paddingLeft":"100px", "paddingRight":"100px"}),
            dbc.Col(
                [
                    html.H2("Findings: "),
                    html.P("We presented the Pearson correlation coefficients between principal component scores and observed data."),
                    html.P("Higher correlation coefficients are shown in dark purple (for negative correlations) and in light orange (for positive correlations). Each row corresponds to one of the PC scores and each column corresponds to one of the features in original data. We can conclude that the first principal component ( which explains the highest variability in data) is positively correlated with “Property Loss”, “Indirect Deaths” and “Crops Damage” and  the correlation coefficients are 0.87, 0.73 and 0.71, respectively. The second principal component is positively correlated  with “Indirect Injuries” (coefficient=0.71) and negatively correlated with “Direct Deaths” (coefficient = -0.56).")
                ],
                width=12,
                lg=4,
                style={"padding": "0 50px", "fontSize": "20px"}
            )
    ])   
])

