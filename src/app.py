import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


global df
df = pd.read_csv('.../data/insurance.csv')
df_sort = df.sort_values(by='charges',)


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = dash.Dash(__name__)
app.layout = html.Div([html.H4(children='Lowest charge rate(highest is $63770)'),
                       generate_table(df_sort),

                       dcc.Graph(id='piechart',
                                 figure=go.Figure(go.Pie(labels=(df['region']),
                                                         values=(df['charges']),
                                                         title='Breakdown of fees by region',
                                                         insidetextorientation='horizontal',
                                                         textinfo='label+percent'))),

                       dcc.Graph(id='histogram',
                                 figure=px.histogram(df, x=df['age'],
                                                     y=df['charges'],
                                                     hover_data=['age', 'charges'],
                                                     height=650,
                                                     title='Insurance fee by age')),

                       dcc.Graph(id='stacked bargraph',
                                 figure=px.bar(df, x="sex", y="charges",
                                               height=650,
                                               title='Gender paying least fee')),

                       dcc.Graph(id='grouped bargraph',
                                 figure=px.bar(df, x="sex", y="charges",
                                               color='smoker',
                                               barmode='group',
                                               height=650,
                                               title='Rates by Smoker and non-Smoker')),

                       dcc.Interval(id='interval-component', interval=2000,
                                    n_intervals=0)])


if __name__ == '__main__':
    app.run_server(debug=True)
