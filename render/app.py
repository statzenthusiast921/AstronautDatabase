#Import packages

from enum import unique
import pandas as pd
import numpy as np
import os
import plotly.express as px
import dash
from dash import dcc, html
#import urllib.request
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
#import json
import requests
#from IPython.display import JSON
import visdcc
#import itertools as it
import re
import collections
from dash import dash_table as dt
### Read image from URL
from PIL import Image
import requests
from io import BytesIO
#import plotly.graph_objects as go
import ast

#Read in processed data from github
astro_db = pd.read_csv('https://raw.githubusercontent.com/statzenthusiast921/AstronautDatabase/main/data/astro_db.csv', encoding = "ISO-8859-1")

# #Download the astronaut database from SuperCluster
# astronaut_db_url = 'https://supercluster-iadb.s3.us-east-2.amazonaws.com/adb.json'
# astronauts_db = requests.get(astronaut_db_url).json()

# #Load bio data
# bio_data = pd.read_csv('https://raw.githubusercontent.com/statzenthusiast921/AstronautDatabase/main/name_bio.csv',encoding='latin-1')


# #Clean up bio data
# bio_data['names'] = bio_data['name'].str.split(", ")

# bio_data['last_names'] = bio_data['names'].str[0]
# bio_data['first_names'] = bio_data['names'].str[1]
# bio_data['full_names'] = bio_data['first_names'] + ' ' + bio_data['last_names']
# del bio_data['names'], bio_data['first_names'], bio_data['name'], bio_data['last_names'], bio_data['bio'], bio_data['Remove End'], bio_data['Remove Front'], bio_data['Check'], bio_data['Last_Name'],bio_data['Name_in_Bio']

# #Fix discrepancies between names (usually middle initial)
# code1 = 'https://raw.githubusercontent.com/statzenthusiast921/AstronautDatabase/main/data_cleaning_for_bio_name.py'
# response1 = urllib.request.urlopen(code1)
# data1 = response1.read()
# exec(data1)
from natsort import natsorted, ns


astro_db['bio_cleaned'] = astro_db['bio_cleaned'].str.replace('KÃ¡rmÃ¡n','Kármán')
astro_db['bio_cleaned'] = astro_db['bio_cleaned'].str.replace('Ê',' ')
astro_db['bio_cleaned'] = astro_db['bio_cleaned'].str.replace('Krmn','Kármán')
astro_db['bio_cleaned'] = astro_db['bio_cleaned'].str.replace('©','')
astro_db['bio_cleaned'] = astro_db['bio_cleaned'].str.replace('Ã','')

astro_db['awards'] = astro_db['awards'].str.replace('KÃ¡rmÃ¡n','Kármán')
astro_db['shortDescription'] = astro_db['shortDescription'].str.replace('â','')
astro_db['shortDescription'] = astro_db['shortDescription'].str.replace('â ',' ')
astro_db['shortDescription'] = astro_db['shortDescription'].str.replace("âs","'s")



#Cut data off after December 31, 2021 and before January 1
astro_db = astro_db[(astro_db['launch_year']<2022) & (astro_db['launch_year']>1960)]

# #Make astronaut and mission dataframes
# df1 = pd.json_normalize(astronauts_db['astronauts'])
# df2 = pd.json_normalize(astronauts_db['missions'])

# #Grab columns
# df_astro = df1[['_id','astroNumber','awards','name','gender','inSpace','overallNumber','spacewalkCount','species','speciesGroup',
#                 'totalMinutesInSpace','totalSecondsSpacewalking','lastLaunchDate.utc','image.asset.url']]

# df_miss = df2[['_id','astronauts','keywords','name',
#                'seriesName','shortDescription','vagueLaunchDate',
#                'landDate.utc','launchDate.utc']]


# #Change column names
# df_astro = df_astro.rename(columns={'_id': 'astronaut_id'})

# #Get row per award
# df_awards = df_astro[['astronaut_id', 'awards']].copy()
# df_awards['awards'] = df_awards['awards'].apply(lambda awards: [award['title'] for award in awards])

# #Join awards column back on astronaut df
# df_astro = pd.merge(df_astro,df_awards,how='left',on=['astronaut_id'])

# #Clean up astronaut df
# del df_astro['awards_x']
# df_astro = df_astro.rename(columns={'awards_y': 'awards'})


# #Change column names
# df_miss = df_miss.rename(columns={'_id': 'mission_id'})

# #Expand df to have multiple rows (many astronauts per mission)
# df_test = df_miss.explode(['astronauts']).reset_index(drop=True)


# #Pull out list of astronauts from JSON format
# astronauts = pd.json_normalize(df_test['astronauts'])


# #Add list of astronauts back into mission df
# df_miss = pd.concat([df_test, astronauts], axis=1)

# #Change column names
# df_miss = df_miss.rename(columns={'_id': 'astronaut_id'})
# del df_miss['astronauts']

# #Cleaning time/day variables
# df_miss['launch_time'] = pd.to_datetime(df_miss['launchDate.utc']).dt.time
# df_miss['land_time'] = pd.to_datetime(df_miss['landDate.utc']).dt.time
# df_miss['launch_date'] = df_miss['vagueLaunchDate']
# df_miss['land_date'] = pd.to_datetime(df_miss['landDate.utc']).dt.date

# del df_miss['vagueLaunchDate'],df_miss['landDate.utc'], df_miss['launchDate.utc']

# #Join astronaut database with mission database
# df_full = pd.merge(df_miss,df_astro,how='left',on=['astronaut_id'])

# # Number of Awards per Astronaut
# df_full['num_awards'] = df_full['awards'].str.len()
# del df_full['lastLaunchDate.utc']

# #Rename columns
# df_full = df_full.rename(columns={'name_x': 'mission_name'})
# df_full = df_full.rename(columns={'name_y': 'astronaut_name'})


# #----------Scrape countries from Supercluster site----------#
# from bs4 import BeautifulSoup
# #!pip install selenium
# from selenium import webdriver
# #!pip install webdriver_manager
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# from selenium.webdriver.chrome.options import Options


# data = []

# url = 'https://www.supercluster.com/astronauts?ascending=false&limit=5000&list=true&sort=launch%20order'

# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
# driver.maximize_window()
# driver.get(url)
# time.sleep(10)

# soup = BeautifulSoup(driver.page_source, 'lxml')
# driver.close()
# tags = soup.select('.astronaut_cell.x')

# for item in tags:
#     name = item.select_one('.bau.astronaut_cell__title.bold.mr05').get_text()
#     #print(name.text)
#     country = item.select_one('.mouseover__contents.rel.py05.px075.bau.caps.small.ac')
#     if country:
#         country=country.get_text()
#     #print(country)
    
#     data.append([name, country])



# cols=['name','country']
# df = pd.DataFrame(data,columns=cols)


# #Clean up names
# df['names'] = df['name'].str.split(", ")
# df['last_names'] = df['names'].str[0]
# df['first_names'] = df['names'].str[1]
# df['full_names'] = df['first_names'] + ' ' + df['last_names']
# del df['names'], df['first_names'], df['name'], df['last_names']

# df = df.rename(columns={'full_names': 'astronaut_name'})
# #df_full.iloc[0:5, 10:20]

# #Join country onto full astro df
# astro_db = pd.merge(df_full,df,how='left',on=['astronaut_name'])
# astro_db['country'].unique()


# #Call on the data cleaning script
# code2 = 'https://raw.githubusercontent.com/statzenthusiast921/AstronautDatabase/main/data_cleaning_for_astrodb.py'
# response2 = urllib.request.urlopen(code2)
# data2 = response2.read()
# exec(data2)

# #Create launch year variable
# astro_db['launch_year'] = astro_db['launch_date'].str[0:4].astype(int)


# #Join bio data on astro_db
# del bio_data['Duplicate']
# astro_db = pd.merge(astro_db,bio_data,how='left',left_on = "astronaut_name",right_on='full_names')

#astro_db.to_csv('filename.csv',index=False)

#----------Create lists and dictionaries for use in dashboard----------#

#1.) List of countries
astro_db['ones'] = 1
country_condensed = astro_db[['country','ones']]
country_condensed = country_condensed.groupby(['country']).sum().reset_index()
country_condensed = country_condensed[country_condensed['ones']>1]
country_choices = country_condensed['country'].astype('str').unique()
country_choices = sorted(country_choices)

#2.) List of launch years
year_choices = astro_db['launch_year'].unique()

#3.) List of astronauts
astro_db['astronaut_name'] = astro_db['astronaut_name'].astype('str')
astro_db.drop(astro_db[astro_db['astronaut_name'] =='nan'].index, inplace=True)
astronaut_choices = sorted(astro_db['astronaut_name'].unique().tolist())

#4.) Country --> Astronaut Dictionary
df_for_dict = astro_db[['country','astronaut_name']]
df_for_dict = df_for_dict.drop_duplicates(subset='astronaut_name',keep='first')
country_astro_dict = df_for_dict.groupby('country')['astronaut_name'].apply(list).to_dict()
country_astro_dict_sorted = {l: sorted(m) for l, m in country_astro_dict.items()} #sort value by list

#5.) List of Missions
mission_choices = astro_db['mission_name'].unique().tolist()


mission_choices = natsorted(mission_choices, key=lambda y: y.lower())


#6.) Launch Year --> Mission Dictionary
df2_for_dict = astro_db[['launch_year','mission_name']]
df2_for_dict = df2_for_dict.drop_duplicates(subset='mission_name',keep='first')
ly_miss_dict = df2_for_dict.groupby('launch_year')['mission_name'].apply(list).to_dict()
ly_miss_dict_sorted = {l: sorted(m) for l, m in ly_miss_dict.items()} #sort value by list


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


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])
server = app.server
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Welcome',value='tab-1',style=tab_style, selected_style=tab_selected_style,
               children=[
                   html.Div([
                       html.H1(dcc.Markdown('''**Welcome to my Astronaut Database Dashboard!**''')),
                       html.Br()
                   ]),
                   
                   html.Div([
                        html.P(dcc.Markdown('''**What is the purpose of this dashboard?**'''),style={'color':'white'}),
                   ],style={'text-decoration': 'underline'}),
                   html.Div([
                       html.P("This dashboard was created as a tool to: ",style={'color':'white'}),
                       html.P("1.) Understand the accomplishments and level of activity of countries over time in building space programs",style={'color':'white'}),
                       html.P("2.) Understand the accomplishemnts of individual astronauts",style={'color':'white'}),
                       html.P("3.) Visualize networks of astronauts connected by missions for which they participated",style={'color':'white'}),


                       html.Br()
                   ]),
                   html.Div([
                       html.P(dcc.Markdown('''**What data is being used for this analysis?**'''),style={'color':'white'}),
                   ],style={'text-decoration': 'underline'}),
                   
                   html.Div([
                       html.P(["The data utilized for this dashboard was scraped from the ",html.A('SuperCluster Astronaut Database.',href='https://www.supercluster.com/astronauts')],style={'color':'white'}),
                       html.Br()
                   ]),
                   html.Div([
                       html.P(dcc.Markdown('''**What are the limitations of this data?**'''),style={'color':'white'}),
                   ],style={'text-decoration': 'underline'}),
                   html.Div([
                       html.P("1.) When assigning a country as a feature of an astronaut, there is no clear distinction for Russian cosmonauts who participated in their nation's space program before vs. after the fall of the Soviet Union.  This is only an issue for cosmonauts who went into space around the late 1980s and early 1990s.  Further, it was difficult to determine how to categorize a cosmonaut who participated in a mission before the fall of the Soviet Union and then participated in another mission after the fall of the Soviet Union. The first country listed on their profile was utilized.",style={'color':'white'}),
                       html.P("2.) Initially, the entire scraping process was performed from scratch to construct a dataset each time the dashboard was loaded. Building the dashboard in this way slowed the processing speed down immensely. Thus, a static version of the dataset was downloaded after scraping and all records were cut off after December 31, 2021.",style={'color':'white'})
                   ])


               ]),
        
        
dcc.Tab(label='Countries',value='tab-2',style=tab_style, selected_style=tab_selected_style,
        children=[
            dbc.Row([
                #Button #1 - 1/2 page width
                dbc.Col([
                    html.Div([
                        dbc.Button("Click Here for Detailed Instructions",id='open3',size='lg'),
                    ],className="d-grid gap-2"),
                    #Button for Instructions
                    html.Div([
                        dbc.Modal(
                            children=[
                                dbc.ModalHeader("Instructions"),
                                dbc.ModalBody(
                                    children=[
                                        html.P('Click on either of the dropdown boxes to update the graphs below.'),
                                        html.P('Using the slider will update the left graph and reveal the countries that participated in a mission in the selected year.  Using the dropdown box will update the right graph and reveal the awards won by a selected country.')
                                    ]
                                ),
                                dbc.ModalFooter(
                                    dbc.Button("Close", id="close3")#,color='Secondary',className='me-1')
                                ),
                            ],id="modal3", size="xl",scrollable=True
                        )
                    ])                
                ]),
                #Column for Button 2 - 1/2 page width
                dbc.Col([
                    html.Div([
                        dbc.Button("Click Here for Award Descriptions",id='open0',size='lg'),
                    ],className="d-grid gap-2"),
                    #Button for Award Description
                    html.Div([
                        dbc.Modal(
                            children=[
                                dbc.ModalHeader("Award Descriptions"),
                                dbc.ModalBody(
                                    children=[
                                        # html.P(dcc.Markdown('''**1.) Crossed 80KM Line**''')),
                                        # html.P('Crossed the NASA Space Line (80KM), which is the minimum altitude at which NASA considers a person to have flown in outer space.'),
                                        html.P(dcc.Markdown('''**1.) Crossed Kármán Line**''')),
                                        html.P('Crossed the Kármán Line (100 km), the internationally accepted boundary of space.'),
                                        html.P(dcc.Markdown('''**2.) ISS Visitor**''')),
                                        html.P('Visited the International Space Station.'),
                                        html.P(dcc.Markdown('''**3.) Elite Spacewalker**''')),
                                        html.P('Top 5% for total spacewalking time.'),
                                        html.P(dcc.Markdown('''**4.) Space Resident**''')),
                                        html.P('Spent over a month in space.'),
                                        html.P(dcc.Markdown('''**5.): Frequent Walker**''')),
                                        html.P('Top 5% for number of space walks.'),
                                        html.P(dcc.Markdown('''**6.) Frequent Flyer**''')),
                                        html.P('Top 5% for number of missions.'),
                                        html.P(dcc.Markdown('''**7.) Elite Spaceflyer**''')),
                                        html.P('Top 5% for total time in space.'),
                                        html.P(dcc.Markdown('''**8.) Moonwalker**''')),
                                        html.P('Walked on the moon.'),
                                        html.P(dcc.Markdown('''**9.) Memorial**''')),
                                        html.P('Gave their life in the pursuit of space exploration.')
                                
                                    ]
                                ),
                                dbc.ModalFooter(
                                    dbc.Button("Close", id="close0")#,color='Secondary',className='me-1')
                                ),
                            ],id="modal0", size="xl",scrollable=True

                        )
                    ])
                ]),
            ]),
            dbc.Row([
              
                dbc.Col([
                    html.Label(dcc.Markdown('''**Select a launch year: **'''),style={'color':'white'}),                        
                    dcc.Slider(
                        min=year_choices.min(),
                        max=year_choices.max(),
                        step=1, 
                        tooltip={"placement": "bottom", "always_visible": True},
                        value=year_choices.max(), 
                        id='slider0',
                        marks={
                            1961: '1961',
                            1970: '1970',
                            1980: '1980',
                            1990: '1990',
                            2000: '2000',
                            2010: '2010',
                            2020: '2020'
                        }
                    )
                ],width=6),
                dbc.Col([
                    html.Label(dcc.Markdown('''**Select a country: **'''),style={'color':'white'}),                        
                    dcc.Dropdown(
                        id='dropdown4',
                        style={'color':'black'},
                        options=[{'label': i, 'value': i} for i in country_choices],
                        value=country_choices[-1]
                    )
                ],width=6)
            
            ]),
            

            dbc.Row([
                #Graph row - Timeline chart and bar chart of awards
                dbc.Col([
                    dcc.Graph(id='num_astros_country')
                ],width=6),
                dbc.Col([
                    dcc.Graph(id='tree_map')
                ],width=6)
            ])
        ]),
        dcc.Tab(label='Astronauts',value='tab-3',style=tab_style, selected_style=tab_selected_style,
               children=[
                   dbc.Row([
                       dbc.Col([
                           html.Div([
                                dbc.Button("Click Here for Detailed Instructions",id='open4',size='lg'),
                           ],className="d-grid gap-2"),
                            #Button for Instructions
                                html.Div([
                                    dbc.Modal(
                                        children=[
                                            dbc.ModalHeader("Instructions"),
                                            dbc.ModalBody(
                                                children=[
                                                    html.P('Click on the dropdown boxes to select a country and then select a specific astronaut.'),
                                                    html.P('These choices will reveal:'),
                                                    html.P('1.) A biography for the astronaut'),
                                                    html.P('2.) The missions for which they participated'),
                                                    html.P('3.) The awards they have earned')
                                                ]
                                            ),
                                            dbc.ModalFooter(
                                                dbc.Button("Close", id="close4")#,color='Secondary',className='me-1')
                                            ),
                                        ],id="modal4", size="xl",scrollable=True
                                    )
                                ])
                       ],width=6),
                       dbc.Col([
                            html.Div([
                                dbc.Button("Click Here for Mission Descriptions",id='open1',size='lg'),
                            ],className="d-grid gap-2"),
                            #Button for Award Description
                        html.Div([
                            dbc.Modal(
                                children=[
                                    dbc.ModalHeader("Mission Descriptions"),
                                    dbc.ModalBody(
                                        children=[
                                            html.P(
                                                id='mission_table',
                                                style={'overflow':'auto','maxHeight':'400px'}
                                            ),
                                        ]
                                    ),
                                    dbc.ModalFooter(
                                        dbc.Button("Close", id="close1")#,color='Secondary',className='me-1')
                                    ),
                                ],id="modal1", size="xl",scrollable=True

                            )
                        ])
                       ],width=6),
                       dbc.Col([
                            html.Label(dcc.Markdown('''**Select a country: **'''),style={'color':'white'}),                        
                            dcc.Dropdown(
                                id='dropdown1',
                                style={'color':'black'},
                                options=[{'label': i, 'value': i} for i in country_choices],
                                value=country_choices[-1]
                            )
                       ],width=6),
                        dbc.Col([
                            html.Label(dcc.Markdown('''**Select an astronaut: **'''),style={'color':'white'}),                       
                            dcc.Dropdown(
                                id='dropdown2',
                                style={'color':'black'},
                                options=[{'label': i, 'value': i} for i in astronaut_choices],
                                value=astronaut_choices[0]
                            )
                       ],width=6)
                   ]),
                    dbc.Row([
        
                        dbc.Col([
                            dbc.Card(id='card5')
                        ],width=4),
                        dbc.Col([
                            dbc.Card(id='card6')
                        ],width=4),
                        dbc.Col([
                            dbc.Card(id='card7')
                        ],width=4),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.Img(id='bio_pic', style={'height':'300px', 'width':'200px'}),
                            #html.Br(),
                            
                        ],width=3),
                        dbc.Col([
                            html.Label(dcc.Markdown('''**Biography: **'''),style={'color':'white','text-decoration': 'underline'}),                        
                            html.P(id='bio_paragraph',style={'color':'white'})
                        ],width=6),
  
                     
                        dbc.Col([
                            html.Label(dcc.Markdown('''**List of Awards: **'''),style={'color':'white','text-decoration': 'underline'}),                        
                            html.P(id="award_list",style={'color':'white'}),
                            html.Label(dcc.Markdown('''**List of Missions: **'''),style={'color':'white','text-decoration': 'underline'}),                        
                            html.P(
                                id="mission_list",
                                style={'overflow':'auto','maxHeight':'400px','color':'white'}
                            )
                        ],width=3)
                    ])
                     
               ]),
        dcc.Tab(label='Missions',value='tab-4',style=tab_style, selected_style=tab_selected_style,
               children=[
                   dbc.Row([
                       dbc.Col([
                           #Item 1 of 3 --> The Instructions Button
                           html.Div([
                                dbc.Button("Click Here for Detailed Instructions",id='open2',size='lg'),
                           ],className="d-grid gap-2"),
                            html.Div([
                                dbc.Modal(
                                    children=[
                                        dbc.ModalHeader("Instructions"),
                                        dbc.ModalBody(
                                            children=[
                                                html.P('This page allows the user to visualize the connections between astronauts and the missions for which they participated.  The blue nodes in the graph represent a mission, while the grey nodes represent the astronauts who participated in the mission.'),
                                                html.P('The user can select a range of launch years to visualize more or fewer connections of missions.  For the best performance, try to select a range of launch years less than or equal to 10 years.  To view a specific mission, the user can search using the dropdown box.  To reveal detailed information about the mission including the astronauts who participated, the launch date, and a brief description, the user can click on the blue node.  Additionally, the user can zoom into the graph to view the mission and astronaut names.')
                                            ]
                                        ),
                                        dbc.ModalFooter(
                                            dbc.Button("Close", id="close2")#,color='Secondary',className='me-1')
                                        ),
                                    ],id="modal2", size="xl",scrollable=True

                                )
                            ])
                       ],width=6),
                       dbc.Col([
                            #Item 2 of 3 --> The Range Slider for Launch Years
                            html.Label(dcc.Markdown('''**Select a range of launch years: **'''),style={'color':'white'}),                        
                            dcc.RangeSlider(
                                    id='range_slider',
                                    min=year_choices.min(),
                                    max=year_choices.max(),
                                    step=1,
                                    value=[2016, year_choices.max()],
                                    allowCross=False,
                                    pushable=2,
                                    tooltip={"placement": "bottom", "always_visible": True},
                                    marks={
                                        1961: '1961',
                                        1970: '1970',
                                        1980: '1980',
                                        1990: '1990',
                                        2000: '2000',
                                        2010: '2010',
                                        2020: '2020'
                                    }
                                ),

                       ],width=6),
                       
                   ]),
                   dbc.Row([
                       dbc.Col([
                           dbc.Row([
                               dbc.Col([
                                   html.Label(dcc.Markdown('''**Click on a blue node below to reveal information about a mission and zoom in to see node labels.**'''),style={'color':'white'}),                        
                                   html.Li('Mission',style={'color':'#626ffb'}),        
                                   html.Li('Astronaut',style={'color':'grey'})                 
                

                               ],width=6),
                               dbc.Col([
                                    html.Label(dcc.Markdown('''**Highlight a specific mission: **'''),style={'color':'white'}),                        
                                    dcc.Dropdown(
                                        id='dropdown3',
                                        style={'color':'black'},
                                        options=[{'label': i, 'value': i} for i in mission_choices],
                                        value=mission_choices[0]
                                    )
                               ],width=6)
                           ]),
                            visdcc.Network(
                                id='ng',
                                selection = {
                                        'nodes':[], 
                                        'edges':[]
                                },
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
                       ],width=6),
                       html.Br(),
                       dbc.Col([
                            html.Br(),
                            html.Label(dcc.Markdown('''**Mission Details: **'''),style={'color':'white'}),                        
                            html.Div(id = 'nodes',style={'color':'white'}),
                            html.Div(id = 'edges',style={'color':'white'})
                       ],width=6),
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



#Tab #2: Country --> # Astronauts by Country Bar Graph
@app.callback(
    Output('num_astros_country','figure'),
    Input('slider0','value')
)
def countries_and_stuff(slider0):
    
    filtered = astro_db[astro_db['launch_year']==slider0]
    filtered = filtered.drop_duplicates(subset='astronaut_name', keep="first")

    #Lets make bar graph of # astronauts per country in the year
    filtered['ones'] = 1
    country_df = filtered[['country','ones']]
    country_df = country_df.groupby('country').sum().reset_index()
    country_df = country_df.sort_values(by=['ones'],ascending=True)

    fig = px.bar(
        country_df, 
        x="ones", y="country",
        #markers=True,
        orientation='h',
        template='plotly_dark',
        labels={'ones':'# Astronauts','country':'Country'},
        title=f'# Astronauts by Country in {slider0}',
        text_auto=True
    )

    
    return fig



#Tab #2: Country --> # Astronauts by Award Treemap Graph
@app.callback(
    Output('tree_map','figure'),
    Input('dropdown4','value')
)
def countries_and_stuff(dd4):
    
    filtered = astro_db[astro_db['country']==dd4]
    filtered = filtered.drop_duplicates(subset='astronaut_name', keep="first")

   
    #Pull out unique awards per country
    unique_awards = filtered[['astronaut_name','country','awards']]    
    
    unique_awards['ISS_Visitor'] = np.where(unique_awards['awards'].str.contains('ISS Visitor'),1,0)
    unique_awards['Crossed_Karman'] = np.where(unique_awards['awards'].str.contains('Crossed K'),1,0)
    unique_awards['Elite_Spacewalker'] = np.where(unique_awards['awards'].str.contains('Elite Spacewalker'),1,0)
    unique_awards['Space_Resident'] = np.where(unique_awards['awards'].str.contains('Space Resident'),1,0)
    unique_awards['Frequent_Walker'] = np.where(unique_awards['awards'].str.contains('Frequent Walker'),1,0)
    unique_awards['Frequent_Flyer'] = np.where(unique_awards['awards'].str.contains('Frequent Flyer'),1,0)
    unique_awards['Elite_Spaceflyer'] = np.where(unique_awards['awards'].str.contains('Elite Spaceflyer'),1,0)
    unique_awards['Moonwalker'] = np.where(unique_awards['awards'].str.contains('Moonwalker'),1,0)
    unique_awards['Memorial'] = np.where(unique_awards['awards'].str.contains('Memorial'),1,0)

    del unique_awards['awards'], unique_awards['country']


    num1 = len(unique_awards[unique_awards['Crossed_Karman']==1]['astronaut_name'].unique())
    num2 = len(unique_awards[unique_awards['ISS_Visitor']==1]['astronaut_name'].unique())
    num3 = len(unique_awards[unique_awards['Elite_Spacewalker']==1]['astronaut_name'].unique())
    num4 = len(unique_awards[unique_awards['Space_Resident']==1]['astronaut_name'].unique())
    num5 = len(unique_awards[unique_awards['Frequent_Walker']==1]['astronaut_name'].unique())
    num6 = len(unique_awards[unique_awards['Frequent_Flyer']==1]['astronaut_name'].unique())
    num7 = len(unique_awards[unique_awards['Elite_Spaceflyer']==1]['astronaut_name'].unique())
    num8 = len(unique_awards[unique_awards['Moonwalker']==1]['astronaut_name'].unique())
    num9 = len(unique_awards[unique_awards['Memorial']==1]['astronaut_name'].unique())


    bar_dict = {
        'Crossed Kármán Line': num1,
        'ISS Visitor': num2,
        'Elite Spacewalker': num3,
        'Space Resident': num4,
        'Frequent Walker': num5,
        'Frequent Flyer': num6,
        'Elite Spaceflyer': num7,
        'Moonwalker': num8,
        'Memorial': num9
    }
    


    od = collections.OrderedDict(sorted(bar_dict.items(),reverse=True))
    new_df = pd.DataFrame(od.items(), columns=['Awards','# Astronauts'])
    
    new_df = new_df[new_df['# Astronauts']>0]

    tree_fig = px.treemap(
        new_df, 
        path = ['Awards'],
        values = '# Astronauts',
        template='plotly_dark',
        title=f'Awards Earned by {dd4}',
        color = 'Awards',
        color_discrete_map={
            'Crossed Kármán Line':'#626ffb', 
            'Elite Spacewalker':'#b064fc', 
            'Space Resident': '#ef563b',
            'Frequent Walker': '#f45498',
            'Frequent Flyer': '#ff94fc',
            'Elite Spaceflyer': '#a8f064',
            'Moonwalker': '#24cce6',
            'Memorial': '#ffa45c',
            'ISS Visitor': '#00cc96'
        }   
    )

    tree_fig.update_traces(
        hovertemplate='# Astronauts=%{value}'
    )


    return tree_fig

#Tab #3: Astronauts --> Filter Astronaut Choices Based on Country Selection
@app.callback(
    Output('dropdown2', 'options'), #--> filter astronauts
    Output('dropdown2', 'value'),
    Input('dropdown1', 'value') #--> choose country
)
def set_astro_options(selected_astronaut):
    return [{'label': i, 'value': i} for i in country_astro_dict_sorted[selected_astronaut]], country_astro_dict_sorted[selected_astronaut][0],




#Tab #3: Astronauts --> All Astronaut Info Controlled by Dropdown Selection
@app.callback(
    Output('card5','children'),
    Output('card6','children'),
    Output('card7','children'),
    Output('mission_table','children'),
    Output('mission_list','children'),
    Output('award_list','children'),
    Output('bio_pic','src'),
    Output('bio_paragraph','children'),
    Input('dropdown2','value')
)

def astros_and_stuff(dd2):
    
    #Total # of astronauts card
    filtered = astro_db[astro_db['astronaut_name']==dd2]
    filtered_table = filtered[['mission_name','shortDescription']]
    filtered_table = filtered_table.rename(columns={'mission_name': 'Mission Name', 'shortDescription': 'Description'})

    #Metric #1 - Number of Missions
    #metric1 = len(filtered['mission_name'].unique())

    filtered_nodups = filtered.drop_duplicates(subset='astronaut_name', keep="first")
    
    #Metric #2 - Sum Min In Space
    total_min = int(filtered_nodups['totalMinutesInSpace'].sum())
    metric2 = "{:,}".format(total_min)

    #Metric #3 - # of SpaceWalks
    total_sw = int(filtered_nodups['spacewalkCount'].sum())
    metric3 = "{:,}".format(total_sw)

    #Metric #4 - Sum Min Spacewalking
    total_min_sw = round(filtered_nodups['totalSecondsSpacewalking'].sum()/60)
    metric4 = "{:,}".format(total_min_sw)

    award_row = filtered['awards'].iloc[0]
    award_row_fixed = ast.literal_eval(award_row)
    awards_list = [html.Div(i) for i in award_row_fixed]

    mission_col_list = filtered['mission_name'].tolist()
    mission_list = [html.Div(i) for i in mission_col_list]


    card5 = dbc.Card([
        dbc.CardBody([
            html.P('Total Min in Space'),
            html.H5(f"{metric2} minutes")
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

    card6 = dbc.Card([
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

    card7 = dbc.Card([
        dbc.CardBody([
            html.P('Total Min Spacewalking'),
            html.H5(f"{metric4} minutes"),
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



    mission_table = dt.DataTable(
        columns=[{"name": i, "id": i} for i in filtered_table.columns],
        data=filtered_table.to_dict('records'),
        style_data={
            'whiteSpace': 'normal',
            'height': '150px',
            'color':'black',
            'backgroundColor': 'white'
        },
        style_cell={'textAlign': 'left'}
    )

    #Output the picture
    pic = filtered['image.asset.url'].iloc[0]
    response = requests.get(pic)
    img = Image.open(BytesIO(response.content))

    #Output the bio paragraph
    bio = filtered['bio_cleaned'].iloc[0]


    return card5, card6, card7, mission_table, mission_list, awards_list, img, bio



#Tab #4: Missions --> Use Range Slider (Launch Years) To Filter Missions

@app.callback(
    Output('dropdown3', 'options'), #--> filter missions
    Output('dropdown3','value'),
    Input('range_slider', 'value') #--> choose launch years
)
def set_letter_options(selected_ly_range):
    values =  [
        ly_miss_dict_sorted[i] for i in 
        range(
            int(selected_ly_range[0]), 
            int(selected_ly_range[1])+1
        )
    ]


     
    new_values = []
    for val in values:
        if isinstance(val, list):
            for item in val:
                new_values.append(item)
        else:
            new_values.append(val)

    sorted_list = sorted(new_values)
   
    return [{'label':i,'value':i} for i in sorted_list], sorted_list[0]

#Tab #4: Missions --> Network Graph
@app.callback(
    Output('ng','data'),
    Input('range_slider','value'),
    Input('dropdown3','value')

)

def network(range_slider1,dd3):
    
    filtered = astro_db[['mission_name','astronaut_name','launch_year']]
    filtered['Weights'] = 1
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
        'color':'yellow',
        'size':15
        })
        if node_name == dd3
        else
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

        for _, node_name in enumerate(node_list)
        ]
        

    #Create edges from df
    edges=[]
    for row in new_df.to_dict(orient='records'):
        source, target = row['Source'], row['Target']
        edges.append({
            'id':str(source) + "__" + str(target),
            'from': source,
            'to': target,
            'width': 2
        })

    data = {'nodes':nodes, 'edges': edges}

    return data



#Tab #4: Missions --> Clicking on Nodes in Network Graph
@app.callback(
    Output('nodes', 'children'),
    Output('edges','children'),
    Input('ng', 'selection'),
)
def myfun(x): 
    s = "Mission Description: "
    c = ""
    line_break = html.Br()
    
    if len(x['nodes']) > 0 : 
        

        s += str(x['nodes'][0])
        #print(str(x['nodes'][0]))
        mission_name = s.split(": ",1)[1]
        header = s.split(": ",1)[0] + ": " 
        
        b = astro_db[astro_db['mission_name']==mission_name]
        c = [
            "Mission Name: ", mission_name, 
            line_break, 
            header, b['shortDescription'].values[0],
            line_break, 
            "Launch Date: ", b['launch_date'].values[0]
        ]
        d = [html.Div(i) for i in c]
    else:
        d=""


    s2 = ''
    header = ['Astronauts: ']
    if len(x['edges']) > 0 : 
        s2 = [html.Div(i) for i in x['edges']]
        test = list(map(str, s2))
        subs = [item.split('__') for item in test]
        b = [el[1] for el in subs]
        sub2 = [item.split("')") for item in b]
        b2 = [el2[0] for el2 in sub2]
        #print(len(b2))
        b3 = header+b2
        b4 = [line_break] + [html.Div(i) for i in b3]
    else:
        
        b4=""
    return d, b4

#Tab #4: Missions --> Clicking on Nodes Updates Dropdown Box Value
# @app.callback(
#     Output('dropdown3', 'value'),
#     Input('ng', 'selection'),
# )
# def node_updates_dd(x): 
#     if len(x['nodes']) > 0 : 
#         value = [str(x['nodes'][0])]
#     return value


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

@app.callback(
    Output("modal1", "is_open"),
    Input("open1", "n_clicks"), 
    Input("close1", "n_clicks"),
    State("modal1", "is_open")
)

def toggle_modal1(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal2", "is_open"),
    Input("open2", "n_clicks"), 
    Input("close2", "n_clicks"),
    State("modal2", "is_open")
)

def toggle_modal2(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal3", "is_open"),
    Input("open3", "n_clicks"), 
    Input("close3", "n_clicks"),
    State("modal3", "is_open")
)

def toggle_modal3(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal4", "is_open"),
    Input("open4", "n_clicks"), 
    Input("close4", "n_clicks"),
    State("modal4", "is_open")
)

def toggle_modal4(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open



if __name__=='__main__':
	app.run_server()
