#Import packages
from enum import unique
import pandas as pd
import numpy as np
import os
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import json
import requests
from IPython.display import JSON
import visdcc
import itertools as it
import re
import collections
from dash import dash_table as dt


#Download the astronaut database from SuperCluster
astronaut_db_url = 'https://supercluster-iadb.s3.us-east-2.amazonaws.com/adb.json'
astronauts_db = requests.get(astronaut_db_url).json()


#Make dataframes
df1 = pd.json_normalize(astronauts_db['astronauts'])
df2 = pd.json_normalize(astronauts_db['missions'])

#Grab columns
df_astro = df1[['_id','astroNumber','awards','name','gender','inSpace','overallNumber','spacewalkCount','species','speciesGroup',
                'totalMinutesInSpace','totalSecondsSpacewalking','lastLaunchDate.utc']]

df_miss = df2[['_id','astronauts','keywords','name',
               'seriesName','shortDescription','vagueLaunchDate',
               'landDate.utc','launchDate.utc']]


#Change column names
df_astro = df_astro.rename(columns={'_id': 'astronaut_id'})

#Get row per award
df_awards = df_astro[['astronaut_id', 'awards']].copy()
df_awards['awards'] = df_awards['awards'].apply(lambda awards: [award['title'] for award in awards])

#Join awards column back on astronaut df
df_astro = pd.merge(df_astro,df_awards,how='left',on=['astronaut_id'])

#Clean up astronaut df
del df_astro['awards_x']
df_astro = df_astro.rename(columns={'awards_y': 'awards'})


#Change column names
df_miss = df_miss.rename(columns={'_id': 'mission_id'})

#Expand df to have multiple rows (many astronauts per mission)
df_test = df_miss.explode(['astronauts']).reset_index(drop=True)


#Pull out list of astronauts from JSON format
astronauts = pd.json_normalize(df_test['astronauts'])


#Add list of astronauts back into mission df
df_miss = pd.concat([df_test, astronauts], axis=1)

#Change column names
df_miss = df_miss.rename(columns={'_id': 'astronaut_id'})
del df_miss['astronauts']

#Cleaning time/day variables
df_miss['launch_time'] = pd.to_datetime(df_miss['launchDate.utc']).dt.time
df_miss['land_time'] = pd.to_datetime(df_miss['landDate.utc']).dt.time
df_miss['launch_date'] = df_miss['vagueLaunchDate']
df_miss['land_date'] = pd.to_datetime(df_miss['landDate.utc']).dt.date

del df_miss['vagueLaunchDate'],df_miss['landDate.utc'], df_miss['launchDate.utc']

#Join astronaut database with mission database
df_full = pd.merge(df_miss,df_astro,how='left',on=['astronaut_id'])

# Number of Awards per Astronaut
df_full['num_awards'] = df_full['awards'].str.len()
del df_full['lastLaunchDate.utc']


df_full = df_full.rename(columns={'name_x': 'mission_name'})
df_full = df_full.rename(columns={'name_y': 'astronaut_name'})


#Get the countries
from bs4 import BeautifulSoup
#!pip install selenium
from selenium import webdriver
#!pip install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options


data = []

url = 'https://www.supercluster.com/astronauts?ascending=false&limit=5000&list=true&sort=launch%20order'

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.maximize_window()
driver.get(url)
time.sleep(10)

soup = BeautifulSoup(driver.page_source, 'lxml')
driver.close()
tags = soup.select('.astronaut_cell.x')

for item in tags:
    name = item.select_one('.bau.astronaut_cell__title.bold.mr05').get_text()
    #print(name.text)
    country = item.select_one('.mouseover__contents.rel.py05.px075.bau.caps.small.ac')
    if country:
        country=country.get_text()
    #print(country)
    
    data.append([name, country])



cols=['name','country']
df = pd.DataFrame(data,columns=cols)

df['names'] = df['name'].str.split(", ")

df['last_names'] = df['names'].str[0]
df['first_names'] = df['names'].str[1]
df['full_names'] = df['first_names'] + ' ' + df['last_names']
del df['names'], df['first_names'], df['name'], df['last_names']

df = df.rename(columns={'full_names': 'astronaut_name'})
#df_full.iloc[0:5, 10:20]

#Join country onto full astro df
astro_db = pd.merge(df_full,df,how='left',on=['astronaut_name'])
astro_db['country'].unique()

#astro_db.to_csv('/Users/jonzimmerman/Desktop/Data Projects/Astronaut Database/astro_db.csv', index=False)

#Call on the data cleaning script
exec(open("/Users/jonzimmerman/Desktop/Data Projects/Astronaut Database/data_cleaning_for_astrodb.py").read())

astro_db['country'].value_counts()

astro_db['launch_year'] = astro_db['launch_date'].str[0:4].astype(int)
#astro_db.to_csv('/Users/jonzimmerman/Desktop/Data Projects/Astronaut Database/astro_db.csv', index=False)



#choice - test out dropdown
astro_db['ones'] = 1
country_condensed = astro_db[['country','ones']]
country_condensed = country_condensed.groupby(['country']).sum().reset_index()
country_condensed = country_condensed[country_condensed['ones']>1]

country_choices = country_condensed['country'].astype('str').unique()

country_choices = sorted(country_choices)
year_choices = astro_db['launch_year'].unique()
mission_choices = sorted(astro_db['mission_name'].unique().tolist())

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'color':'white',
    'backgroundColor': '#222222'

}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#626ffb',
    'color': 'white',
    'padding': '6px'
}



app = dash.Dash(__name__,assets_folder=os.path.join(os.curdir,"assets"))
server = app.server
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Welcome',value='tab-1',style=tab_style, selected_style=tab_selected_style,
               children=[
                   html.Div([
                       html.H1(dcc.Markdown('''**My Astronaut Database Dashboard**''')),
                       html.Br()
                   ]),
                   
                   html.Div([
                        html.P(dcc.Markdown('''**What is the purpose of this dashboard?**''')),
                   ],style={'text-decoration': 'underline'}),
                   html.Div([
                       html.P("blah blah blah."),
                       html.Br()
                   ]),
                   html.Div([
                       html.P(dcc.Markdown('''**What data is being used for this analysis?**''')),
                   ],style={'text-decoration': 'underline'}),
                   
                   html.Div([
                       html.P(["Blah blah"]),
                       html.Br()
                   ]),
                   html.Div([
                       html.P(dcc.Markdown('''**What are the limitations of this data?**''')),
                   ],style={'text-decoration': 'underline'}),
                   html.Div([
                       html.P("BLah blah blah")
                   ])


               ]),
        dcc.Tab(label='Countries',value='tab-2',style=tab_style, selected_style=tab_selected_style,
        children=[
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                        id='dropdown0',
                        style={'color':'black'},
                        options=[{'label': i, 'value': i} for i in country_choices],
                        value=country_choices[-1]
                    )
                ])
            ]),
            dbc.Row([
                #Row of cards
                dbc.Col([
                    dbc.Card(id='card1')
                ],width=4),
                dbc.Col([
                    dbc.Card(id='card2')
                ],width=4),
                 dbc.Col([
                    dbc.Card(id='card3')
                ],width=4)
            ]),
            dbc.Row([
                #Graph row - Timeline chart and bar chart of awards
                dbc.Col([
                    dcc.Graph(id='timeline_graph')
                ],width=6),
                dbc.Col([
                    dcc.Graph(id='award_bar_chart')
                ],width=6)
            ]),
            dbc.Row([
                dbc.Button("Click Here for Award Descriptions",id='open0',block=True,size='lg'),
            
                #Button for Award Description
                html.Div([
                    dbc.Modal(
                        children=[
                            dbc.ModalHeader("Award Descriptions"),
                            dbc.ModalBody(
                                children=[
                                    html.P(dcc.Markdown('''**1.) Crossed 80KM Line**''')),
                                    html.P('Crossed the NASA Space Line (80KM), which is the minimum altitude at which NASA considers a person to have flown in outer space.'),
                                    html.P(dcc.Markdown('''**2.) Crossed Kármán Line**''')),
                                    html.P('Crossed the Kármán Line (100 km), the internationally accepted boundary of space.'),
                                    html.P(dcc.Markdown('''**3.) ISS Visitor**''')),
                                    html.P('Visited the International Space Station.'),
                                    html.P(dcc.Markdown('''**4.) Elite Spacewalker**''')),
                                    html.P('Top 5% for total spacewalking time.'),
                                    html.P(dcc.Markdown('''**5.) Space Resident**''')),
                                    html.P('Spent over a month in space.'),
                                    html.P(dcc.Markdown('''**6.): Frequent Walker**''')),
                                    html.P('Top 5% for number of space walks.'),
                                    html.P(dcc.Markdown('''**7.) Frequent Flyer**''')),
                                    html.P('Top 5% for number of missions.'),
                                    html.P(dcc.Markdown('''**8.) Elite Spaceflyer**''')),
                                    html.P('Top 5% for total time in space.'),
                                    html.P(dcc.Markdown('''**9.) Moonwalker**''')),
                                    html.P('Walked on the moon.'),
                                    html.P(dcc.Markdown('''**10.) Memorial**''')),
                                    html.P('Gave their life in the pursuit of space exploration.')
                            
                                ]
                            ),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="close0")#,color='Secondary',className='me-1')
                            ),
                        ],id="modal0", size="xl",scrollable=True

                    )
                ])
            ])
        ]),

        dcc.Tab(label='Astronauts',value='tab-3',style=tab_style, selected_style=tab_selected_style,
               children=[
                   dbc.Row([
                       dbc.Col([
            
                       ])
                   ])
               ]),
        dcc.Tab(label='Missions',value='tab-4',style=tab_style, selected_style=tab_selected_style,
               children=[
                   dbc.Row([
                        dbc.Col([
                            dcc.Dropdown(
                                id='dropdown1a',
                                style={'color':'black'},
                                options=[{'label': i, 'value': i} for i in mission_choices],
                                value=mission_choices[0]
                            )
                       ],width=4),
                       dbc.Col([
                            dcc.Dropdown(
                                id='dropdown1',
                                style={'color':'black'},
                                options=[{'label': i, 'value': i} for i in country_choices],
                                value=country_choices[-1]
                            )
                       ],width=4),
                       dbc.Col([
                            dcc.RangeSlider(
                                    id='range_slider',
                                    min=year_choices.min(),
                                    max=year_choices.max(),
                                    step=1,
                                    value=[2010, year_choices.max()],
                                    allowCross=False,
                                    pushable=2,
                                    tooltip={"placement": "bottom", "always_visible": True},
                                    marks={
                                        1950: '1950',
                                        1960: '1960',
                                        1970: '1970',
                                        1980: '1980',
                                        1990: '1990',
                                        2000: '2000',
                                        2010: '2010',
                                        2020: '2020'
                                    }
                                ),

                       ],width=4)
                   ]),
                   dbc.Row([
                       dbc.Col([
                            html.P(id='mission_table')
                       ],width=6),
                       dbc.Col([
                            visdcc.Network(
                                id='ng',
                                options = dict(
                                    height='600px', 
                                    width='100%',
                                    physics={'barnesHut': {'avoidOverlap': 0.5}},
                                    maxVelocity=0,
                                    stabilization={
                                        'enabled': 'true',
                                        'iterations': 15,
                                        'updateInterval': 50,
                                        'onlyDynamicEdges': 'false',
                                        'fit': 'true'
                                    },
                                    scaling='value'
                                )
                            )
                       ],width=6)
                   ])
               ]
        )

    ])
])


#Configure Reactivity for Tab Colors
@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])

    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])

    elif tab == 'tab-4':
        return html.Div([
            html.H3('Tab content 4')
        ])


#Configure callback for mission table
@app.callback(
    Output('mission_table','children'),
    Input('dropdown1a','value'),
    Input('range_slider','value')
)
def filter_table(dd1a,range_slider1):
    filtered = astro_db[['mission_name','shortDescription','launch_year']]
    filtered = filtered[(filtered['launch_year']>=range_slider1[0]) & (filtered['launch_year']<=range_slider1[1])]

    filtered = filtered[filtered['mission_name']==dd1a]
    del filtered['launch_year'], filtered['mission_name']
    #Only keep first row - make sure still pandas df


    mission_table = dt.DataTable(
        columns=[{"name": i, "id": i} for i in filtered.columns],
        data=filtered.to_dict('records'),
        style_data={
            'whiteSpace': 'normal',
            'height': '150px',
            'color':'black',
            'backgroundColor': 'white'
        },
        style_cell={'textAlign': 'left'}
    )

    return mission_table


#Configure callback for network graph
@app.callback(
    Output('ng','data'),
    Input('dropdown1','value'),
    Input('dropdown1a','value'),
    Input('range_slider','value')

)

def network(dd1,dd1a,range_slider1):
    
    filtered = astro_db[['mission_name','astronaut_name','country','launch_year']]
    filtered['Weights'] = 1
    filtered = filtered[filtered['country']==dd1]
    filtered = filtered[(filtered['launch_year']>=range_slider1[0]) & (filtered['launch_year']<=range_slider1[1])]

    new_df = filtered
    new_df.rename(columns={new_df.columns[0]: "Source"}, inplace = True)
    new_df.rename(columns={new_df.columns[1]: "Target"}, inplace = True)

    node_list = list(
        set(new_df['Source'].unique().tolist()+new_df['Target'].unique().tolist())
    )

    nodes = [
        ({
        'id': node_name, 
        'label': node_name,
        'shape':'dot',
        'color':'#626ffb',
        'size':15
        })
        
        if node_name in new_df['Source'].unique()
        else
        ({
        'id': node_name, 
        'label': node_name,
        'shape':'dot',
        'color':'grey',
        'size':15
        })  
      
        for _, node_name in enumerate(node_list)]

    #Create edges from df
    edges=[]
    for row in new_df.to_dict(orient='records'):
        source, target = row['Source'], row['Target']
        edges.append({
            'id':source + "__" + target,
            'from': source,
            'to': target,
            'width': 2
        })

    data = {'nodes':nodes, 'edges': edges}

    return data

#Configure callback for astronaut totals
@app.callback(
    Output('card1','children'),
    Output('card2','children'),
    Output('card3','children'),

    Output('timeline_graph','figure'),
    Output('award_bar_chart','figure'),
    Input('dropdown0','value')
)
def countries_page(dd0):
    
    #Total # of astronauts card
    filtered = astro_db[astro_db['country']==dd0]
    metric1 = len(filtered['astronaut_name'].unique())
    filtered = filtered.drop_duplicates(subset='astronaut_name', keep="first")
    
    total_min = int(filtered['totalMinutesInSpace'].sum())
    metric2 = "{:,}".format(total_min)

    total_sw = int(filtered['spacewalkCount'].sum())
    metric3 = "{:,}".format(total_sw)


    card1 = dbc.Card([
        dbc.CardBody([
            html.P('# Astronauts in Space Program'),
            html.H5(f"{metric1}"),
        ])
    ],
    style={'display': 'inline-block',
           'width': '100%',
           'text-align': 'center',
           'background-color': '#70747c',
           'color':'white',
           'fontWeight': 'bold',
           'fontSize':16},
    outline=True)

    card2 = dbc.Card([
        dbc.CardBody([
            html.P('Total Min in Space - NEED TO FIX'),
            html.H5("@ astro level, want mission"),
        ])
    ],
    style={'display': 'inline-block',
           'width': '100%',
           'text-align': 'center',
           'background-color': '#70747c',
           'color':'white',
           'fontWeight': 'bold',
           'fontSize':16},
    outline=True)

    card3 = dbc.Card([
        dbc.CardBody([
            html.P('Total # of Spacewalks'),
            html.H5(f"{metric3}"),
        ])
    ],
    style={'display': 'inline-block',
           'width': '100%',
           'text-align': 'center',
           'background-color': '#70747c',
           'color':'white',
           'fontWeight': 'bold',
           'fontSize':16},
    outline=True)

    #Timeline of astronaut launches
    timeline_df = filtered[['launch_year','ones']]
    timeline_df = timeline_df.groupby('launch_year').sum().reset_index()


    fig = px.line(
        timeline_df, 
        x="launch_year", y="ones",
        markers=True,
        template='plotly_dark',
        labels={'ones':'# Astronauts','launch_year':'Year of Launch'}
    )
    fig.update_traces(marker=dict(color='white'))

    #Pull out unique awards per country
    unique_awards = filtered[['astronaut_name','country','awards']]
    unique_awards['awards_string'] = [','.join(map(str, l)) for l in unique_awards['awards']]
    
    
    unique_awards['ISS_Visitor'] = np.where(unique_awards['awards_string'].str.contains('ISS Visitor'),1,0)
    unique_awards['Crossed_Karman'] = np.where(unique_awards['awards_string'].str.contains('Crossed Kármán Line'),1,0)
    unique_awards['Elite_Spacewalker'] = np.where(unique_awards['awards_string'].str.contains('Elite Spacewalker'),1,0)
    unique_awards['Space_Resident'] = np.where(unique_awards['awards_string'].str.contains('Space Resident'),1,0)
    unique_awards['Frequent_Walker'] = np.where(unique_awards['awards_string'].str.contains('Frequent Walker'),1,0)
    unique_awards['Frequent_Flyer'] = np.where(unique_awards['awards_string'].str.contains('Frequent Flyer'),1,0)
    unique_awards['Elite_Spaceflyer'] = np.where(unique_awards['awards_string'].str.contains('Elite Spaceflyer'),1,0)
    unique_awards['Moonwalker'] = np.where(unique_awards['awards_string'].str.contains('Moonwalker'),1,0)
    unique_awards['Memorial'] = np.where(unique_awards['awards_string'].str.contains('Memorial'),1,0)
    unique_awards['Crossed_80KM'] = np.where(unique_awards['awards_string'].str.contains('Crossed 80km Line'),1,0)

    del unique_awards['awards'], unique_awards['awards_string'], unique_awards['country']


    num1 = len(unique_awards[unique_awards['Crossed_80KM']==1]['astronaut_name'].unique())
    num2 = len(unique_awards[unique_awards['Crossed_Karman']==1]['astronaut_name'].unique())
    num3 = len(unique_awards[unique_awards['ISS_Visitor']==1]['astronaut_name'].unique())
    num4 = len(unique_awards[unique_awards['Elite_Spacewalker']==1]['astronaut_name'].unique())
    num5 = len(unique_awards[unique_awards['Space_Resident']==1]['astronaut_name'].unique())
    num6 = len(unique_awards[unique_awards['Frequent_Walker']==1]['astronaut_name'].unique())
    num7 = len(unique_awards[unique_awards['Frequent_Flyer']==1]['astronaut_name'].unique())
    num8 = len(unique_awards[unique_awards['Elite_Spaceflyer']==1]['astronaut_name'].unique())
    num9 = len(unique_awards[unique_awards['Moonwalker']==1]['astronaut_name'].unique())
    num10 = len(unique_awards[unique_awards['Memorial']==1]['astronaut_name'].unique())


    bar_dict = {
        num1: 'Crossed 80KM Line',
        num2: 'Crossed Kármán Line',
        num3: 'ISS Visitor',
        num4: 'Elite Spacewalker',
        num5: 'Space Resident',
        num6: 'Frequent Walker',
        num7: 'Frequent Flyer',
        num8: 'Elite Spaceflyer',
        num9: 'Moonwalker',
        num10: 'Memorial'
    }
    


    od = collections.OrderedDict(sorted(bar_dict.items(),reverse=True))
    new_df = pd.DataFrame(od.items(), columns=['# Astronauts', 'Awards'])
    
    new_df = new_df[new_df['# Astronauts']>0]
    
    bar_fig = px.bar(new_df,
        x = 'Awards',
        y = '# Astronauts',
        template='plotly_dark'
    )
    bar_fig
    #bar_fig.update_xaxes(tickangle=35)


    return card1, card2, card3, fig, bar_fig

@app.callback(
    Output("modal0", "is_open"),
    Input("open0", "n_clicks"), 
    Input("close0", "n_clicks"),
    State("modal0", "is_open")
)

def toggle_modal0(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__=='__main__':
	app.run_server()
