import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



# Step 1: Launch the Application
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Step 2: Import the Data
df = pd.read_csv('TeamPoints_Current.csv')


available_indicators = df['team_id'].unique()



# Step 3: Create Dash Layout
app.layout = html.Div([
    html.Div([

        html.Div([
            #Team ID
            dcc.Dropdown(
                id='Team',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='1'
            )
            ],

        style={'width': '48%', 'display': 'inline-block'}),

    ]),



    dcc.Graph(id='indicator-graphic'),

])





# Step 4: Add Callback Function
@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('Team', 'value')])

def update_graph(Team):
    dff = df[df['team_id']]
    trace1 = go.Bar(x=dff['Player Salary'], y=dff[Team], name=Team.title(), )

    return {
        'data': [trace1],
        'layout': go.Layout(title=f'State vs Export: {selected_product1.title()}',
                            colorway=["#EF963B", "#EF533B"], hovermode="closest",
                            xaxis={'title': "State", 'titlefont': {'color': 'black', 'size': 14},
                                   'tickfont': {'size': 9, 'color': 'black'}},
                            yaxis={'title': "Export price (million USD)", 'titlefont': {'color': 'black', 'size': 14, },
                                   'tickfont': {'color': 'black'}})}




# Step 5: Add the Server Clause
if __name__ == '__main__':
    app.run_server(debug=True)
