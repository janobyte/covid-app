import pandas as pd
import pandas_datareader.data as web
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly

url_c = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
url_d = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
data_c = pd.read_csv(url_c)
data_d = pd.read_csv(url_d)

def clean_data(dataset, columnName):
    clean_data = dataset.drop(['Lat', 'Long'], axis=1) \
        .melt(id_vars=['Province/State', 'Country/Region'], var_name='date', value_name=columnName) \
        .astype({'date':'datetime64[ns]', columnName:'Int64'}, errors='ignore')
    clean_data['Province/State'].fillna('<all>', inplace=True)
    clean_data[columnName].fillna(0, inplace=True)
    return clean_data

dataset = clean_data(data_c, 'confirmed').merge(clean_data(data_d, 'deaths'))


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Covid-19 infoHub'),



    html.Div(children='''
        still wip
        data acquired from: https://github.com/CSSEGISandData/COVID-19
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1,2,3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Covid-19 Cases in 10 most affected countries'
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
