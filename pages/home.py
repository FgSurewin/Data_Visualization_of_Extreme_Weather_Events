import dash
from dash import dcc, callback_context
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from urllib.request import urlopen
import json
from app import app


URL = "https://raw.githubusercontent.com/FgSurewin/DSE_2700_DATA/main/DataVizs/clean%20dataset.csv"
df = pd.read_csv(URL, dtype={'FIPS': 'object'})


# pie chart
fig_pie = px.pie(df.loc[df["General Type"] != "Other", :], values='Adjusted Property Loss', names='General Type', 
             title='The contribution of four extreme events in property loss',
             color='General Type',
             color_discrete_map={'Floods':'blue',
                                 'Wildfire':'red',
                                 'Tornado':'green',
                                 'Hurricane':'purple'})
fig_pie.update_traces(textposition='inside', textinfo='percent+label')

# Scatter Plot
def scatter_all(event_name,title,linecol):
  impact=["General Type","Adjusted Property Loss","DEATHS_DIRECT","DEATHS_INDIRECT"]
  
  df0=pd.DataFrame(df[df["General Type"]==event_name].groupby("YEAR",as_index=False)[impact[0]].count())
  df1=pd.DataFrame(df[df["General Type"]==event_name].groupby("YEAR",as_index=False)[impact[1]].sum())
  df2=pd.DataFrame(df[df["General Type"]==event_name].groupby("YEAR",as_index=False)[impact[2]].sum())
  df3=pd.DataFrame(df[df["General Type"]==event_name].groupby("YEAR",as_index=False)[impact[3]].sum())

  fig=make_subplots(rows=2, cols=2,subplot_titles=('Total No. of Event','Total Property Loss',  'Direct Deaths', 'Indirect Deaths'))
  
  fig.add_trace(go.Scatter(x=df0["YEAR"], y=df0[impact[0]], mode='lines+markers',line_color=linecol), row=1,col=1)
  fig.add_trace(go.Scatter(x=df1["YEAR"], y=df1[impact[1]], mode='lines+markers',line_color=linecol), row=1,col=2)
  fig.add_trace(go.Scatter(x=df2["YEAR"], y=df2[impact[2]], mode='lines+markers',line_color=linecol), row=2,col=1)
  fig.add_trace(go.Scatter(x=df3["YEAR"], y=df3[impact[3]], mode='lines+markers',line_color=linecol), row=2,col=2)

  fig.update_layout(title=title, height=780, showlegend=False)
  fig.update_traces(marker_size=12,line_width=3)

  fig['layout']['yaxis']['title']="Counts"
  fig['layout']['yaxis2']['title']="Property Loss"
  fig['layout']['yaxis3']['title']="Direct Deaths"
  fig['layout']['yaxis4']['title']="Indirect Deaths"
  
  return fig



# Map
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
  counties = json.load(response)


County_Refs= pd.read_csv('https://raw.githubusercontent.com/kjhealy/us-county/master/data/census/fips-by-state.csv',encoding = 'unicode_escape')
County_Refs['County']=County_Refs['name']+', '+ County_Refs["state"]
County_Refs['fips']=County_Refs['fips'].apply(lambda x: str(x).zfill(5))
County_Refs.rename(columns={"fips":"FIPS"},inplace=True)




                          
def create_map_plot(event_type, attribute, agg_func, range_color=None):
  # Data Cleaning
  sub_df= df[df['General Type']==event_type].groupby(['FIPS'], as_index=False)[attribute].agg(agg_func)
  merged_sub=pd.merge(left=sub_df,right=County_Refs,how="outer", on="FIPS")
  merged_sub[attribute].fillna(0,inplace=True)
  County_Map=dict(zip(County_Refs["FIPS"],County_Refs['County']))
  merged_sub["County"] = merged_sub["FIPS"].map(County_Map)

  # Create Map
  color_dict = dict(Floods="blues" , Wildfire="reds", Tornado="greens", Hurricane="purp")
  count_number_dict = dict(Floods=100 , Wildfire=50, Tornado=50, Hurricane=10)
  property_number_dict = dict(Floods=5000000 , Wildfire=100000, Tornado=5000000, Hurricane=100000)
  final_color = color_dict[event_type]
  final_number = None
  title = None
  if attribute == 'Adjusted Property Loss': final_number = property_number_dict[event_type]
  else: final_number = count_number_dict[event_type]
  if range_color: final_number=range_color
  if event_type == "Floods": title = event_type[:-1]
  else: title = event_type
  fig = px.choropleth(merged_sub, geojson=counties, locations='FIPS', color=attribute,
                              color_continuous_scale= final_color,
                              range_color=(0, final_number),
                              hover_data = {'County':True, attribute: True, 'FIPS':False},
                              
                              scope="usa" )
  fig.update_layout(
    #   title="Total "+ title + "s Records during 1996-2020", 
      margin=dict(l=0, r=0, t=0, b=0),
      width=1000,
      height=680
      ) #,margin={"r":0,"t":0,"l":0,"b":0})
  return fig



layout = html.Div([
    html.Div(style={"marginBottom": "20px"}),   
    dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.Div(id="map_title")
                    ]),
                    dbc.Row(
                        dbc.Col(
                            dcc.Graph(id='fig_map', figure={})),
                        justify="center",
                    )
                ])
                ],
                width=12, md=6,
                style={"paddingLeft":"50px" ,"fontSize": "20px"}
            ),
            dbc.Col([
                dbc.Row(
                    dbc.Col(
                        dcc.Graph(id='fig_scatter', figure={})),
                    justify="center",
                )
            ], width=12, md=6,style={"paddingLeft":"50px", "paddingRight":"50px"}), 
    ]),
    dbc.Row([
                dbc.Col([
                    dbc.ButtonGroup([
                        dbc.Button("Inspect the Damage Loss", style={"margin": "0 10px"},id='first_btn', n_clicks=0),
                        dbc.Button("Inspect the Number of Occurrences of Specific Event",id='second_btn', n_clicks=0),
                    ], class_name="d-flex justify-content-between")
                ], width=12, md=6), 
                dbc.Col([
                    html.Div([
                        html.H4(children="Event Types: "),
                        dcc.Dropdown(
                                id='event_type_dropdown', value="Tornado", clearable=False,
                                persistence=True, persistence_type='session',
                                options=[{'label': "Floods", 'value': "Floods"} , {'label': "Wildfire", 'value': "Wildfire"}, {'label': "Tornado", 'value': "Tornado"}, {'label': "Hurricane", 'value': "Hurricane"}],
                                style={"color": "black", "width": "400px"})
                        ], className="d-flex  justify-content-around", style={"paddingTop": "12px"})
                ], width=12, md=6)
            ]),
])

#Floods=blues , Wildfire=reds, Tornado=greens, Hurricane=purp

@app.callback(
    [Output(component_id='map_title', component_property='children'), Output(component_id='fig_map', component_property='figure'), Output(component_id='fig_scatter', component_property='figure'),],
    [Input("event_type_dropdown", "value"), Input("first_btn", "n_clicks"),Input("second_btn", "n_clicks"), ]
)
def display_value(value, first, second):
    if value == "Floods": title = value[:-1]
    else: title = value
    color_dict = dict(Floods="blue" , Wildfire="red", Tornado="green", Hurricane="purple")

    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'first_btn' in changed_id:
        fig_map = create_map_plot(event_type=value, attribute='Adjusted Property Loss', agg_func='sum')
        final_title = html.H5(children=["Record regarding Total Damage Caused By ", html.Span(title + "s", style={"color": color_dict[value], "fontWeight": "600"}), " During 1996-2020"])
        return [final_title], fig_map, dash.no_update
    elif 'second_btn' in changed_id:
        fig_map = create_map_plot(event_type=value, attribute='General Type', agg_func='count')
        final_title = html.H5(children=["Record regarding the number of ", html.Span(title, style={"color": color_dict[value], "fontWeight": "600"}), " occurrences during 1996-2020"])
        return [final_title], fig_map, dash.no_update
    else:
        fig_scatter = scatter_all(event_name=value,title="The Annual " + title  + " Records accross the US during 1996-2020",linecol=color_dict[value])
        fig_map = create_map_plot(event_type=value, attribute='Adjusted Property Loss', agg_func='sum')
        final_title = html.H5(children=["Record regarding Total Damage Caused By ", html.Span(title + "s", style={"color": color_dict[value], "fontWeight": "600"}), " During 1996-2020"])
        return [final_title], fig_map, fig_scatter

