import dash

# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
# (1) Style:
# Bootstrap Theme: https://bootswatch.com/
# Download the one you want and put it inside the assets folder. (Or replace the old css file)

# (2) Title:
app.title = "Data Analysis of Extreme Weather Events"

server = app.server