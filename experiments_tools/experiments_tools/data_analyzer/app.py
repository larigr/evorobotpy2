import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.express as px
import os
import dash_table
import pandas as pd
experiments_path = '../exp_config_generator'
external_stylesheets = ['style.css', 'https://codepen.io/chriddyp/pen/bWLwgP.css' ]

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)

file_list = os.listdir(experiments_path)
folder_list = []
for f in file_list:
    if not '.' in f:
        if not '__pycache__' in f:
            folder_list.append(f)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])



index_page = html.Div([
    html.Div('Experiment Data Analyzer', style={'color': '#342e37', 'fontSize': 40}),
    html.P('What would you like to do?', className='my-class', id='my-p-element',  style={'color': '#342e37', 'fontSize': 20, 'margin-top':'30px'}),
    dcc.Link(html.Button('Analyze experiments in a serie', id='submit-val', n_clicks=0), href='/page-1'),
    dcc.Link(html.Button('Compare series of experiments', id='submit-val1', n_clicks=0), href='/page-2'),
], className='ini_div')

page_1_layout = html.Div([
    html.H3('Choose a folder to analyze:'),
    dcc.Dropdown(
        id='page-1-dropdown',
        options=[{'label': i, 'value': folder_list.index(i)} for i in folder_list]
    ),
    html.Br(),
    html.Div(id='page-1-content'),
    html.Br(),
    html.Div(id='graph-content'),
    dcc.Link('Go back to home', href='/'),
], className='analyze_serie')


@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    if value is not None:
        text = 'a'
        aux = ''
        exp_list = os.listdir(experiments_path+'/'+folder_list[int(value)])
        variations = os.listdir(experiments_path+'/'+folder_list[int(value)]+'/'+exp_list[0])
        for v in variations:
            if '.ini.txt' in v:
                params = open(experiments_path+'/'+folder_list[int(value)]+'/'+exp_list[0]+'/'+v)
                text = params.readlines()
                print(eval(text[1]))
                aux = aux + 'Changes in this series include:'
                for i in eval(text[1]).keys():
                    aux+=i+', '
                print(aux)
                
        return [html.P(aux), html.Br(),html.P('What experiment do you want to analyze?', className='my-class', id='my-p-element',  style={'color': '#342e37', 'fontSize': 20, 'margin-top':'30px'}),
    dcc.Dropdown(id='experiments_in_serie', 
                options=[{'label': i, 'value': folder_list[int(value)]+'/'+i} for i in exp_list] )]


@app.callback(dash.dependencies.Output('graph-content', 'children'),
              [dash.dependencies.Input('experiments_in_serie', 'value')])
def experiment_graphs(value):
    graph_list = os.listdir(experiments_path+'/'+value)
    graphs = []
    params_table = None
    statsumn = 0
    statavesum = 0
    np.random.seed(1)
    for f in graph_list:
        if "statS" in f:
            print(f)
            stat = np.load(experiments_path+'/'+value+'/'+f)
            size = np.shape(stat)
            newsize = (int(size[0] / 6), 6)
            stat = np.resize(stat, newsize)
            stat = np.transpose(stat)            
            col = np.random.uniform(low=0.0, high=1.0, size=3)
            df = pd.DataFrame({
                'generations' : stat[0],
                'fitness' : stat[2]
            })
            fig = px.line(df, x="generations", y="fitness", title=f) 
            graphs.append(dcc.Graph(figure=fig))
            statsumn = statsumn + 1
        elif ".ini" in f:
            print(f)
            params = open(experiments_path+'/'+value+'/'+f)
            first = []
            second = []
            for l in params.readlines():
                if "=" in l:
                    aux = l.split('=')
                    first.append(aux[0])
                    second.append(aux[1])
            
            params_table = html.Div([dash_table.DataTable(
                            id='data_table',
                            css=[{
                                'selector': '.dash-spreadsheet td div',
                                'rule': '''
                                    line-height: 15px;
                                    max-height: 30px; min-height: 30px; height: 30px;
                                    display: block;
                                    width:100px;
                                    overflow-y: hidden;
                                '''
                            }],
                            page_action="native",
                            page_current= 0,
                            page_size= 5,
                            columns=[{
                                'name': 'PARAMETER',
                                'id': 'column-0',
                            }, {
                                'name': 'VALUE',
                                'id': 'column-1',
                            }],
                            data=[
                            {'column-0': first[j], 'column-1':second[j]}
                            for j in range(0, len(first))
                            ]
                        )], className='table_param')
    if (statsumn == 0):
        return "\033[1mERROR: No stat*.npy file found\033[0m"
    else:   
        graphs.insert(0, params_table)
        graphs.insert(0, html.H4('parameters'))
        return graphs

page_2_layout = html.Div([
    html.H1('Page 2'),
    dcc.RadioItems(
        id='page-2-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])

@app.callback(dash.dependencies.Output('page-2-content', 'children'),
              [dash.dependencies.Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(debug=True)