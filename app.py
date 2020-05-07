import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px


import pandas as pd

global df
df = pd.read_csv('insurance.csv')
df_sort = df.sort_values(by='charges',)


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns]),
            title='lowest charges(highest fee is 63770,43)'
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = dash.Dash(__name__)
app.layout = html.Div([generate_table(df_sort),

                       dcc.Graph(id='piechart',
                                 figure=px.pie(df,
                                               values='charges',
                                               names='region',
                                               color='region',
                                               title='Percentage Fees By Region')),

                       dcc.Graph(id='bargraph',
                                 figure=px.bar(df, x=df['age'],
                                               y=df['charges'],
                                               hover_data=['age', 'charges'],
                                               height=650,
                                               title='insurance fee by age')),

                       dcc.Graph(id='stacked bargraph',
                                 figure=px.bar(df, x="sex", y="charges",
                                               height=650,
                                               title='Gender paying least fee')),

                       dcc.Graph(id='grouped bargraph',
                                 figure=px.bar(df, x="sex", y="charges",
                                               color='smoker',
                                               barmode='group',
                                               height=650,
                                               title='Rates by gender(Smoker and non-Smoker)')),

                       dcc.Interval(id='interval-component', interval=2000,
                                    n_intervals=0)




                       ])


if __name__ == '__main__':
    app.run_server(debug=True)
