#Import packages
import pandas as pd
import numpy as np
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import json
import requests
from IPython.display import JSON
import visdcc
import itertools as it


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

del df_miss['vagueLaunchDate']
del df_miss['landDate.utc']
del df_miss['launchDate.utc']

#Join astronaut database with mission database
df_full = pd.merge(df_miss,df_astro,how='left',on=['astronaut_id'])

# Number of Awards per Astronaut
df_full['num_awards'] = df_full['awards'].str.len()
del df_full['lastLaunchDate.utc']
astro_db = df_full




#choice - test out dropdown

name_choices = astro_db['name_y'].unique()



tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}



app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
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
        dcc.Tab(label='Network Graph',value='tab-2',style=tab_style, selected_style=tab_selected_style,
               children=[
                   dbc.Row([
                       dbc.Col([
                            dcc.Dropdown(
                                id='dropdown1',
                                style={'color':'black'},
                                options=[{'label': i, 'value': i} for i in name_choices],
                                value=name_choices[0]
                            ),
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
                       ])
                   ])
               ]
        )

    ])
])


#Configure Reactibity for Tab Colors
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


@app.callback(
    Output('ng','data'),
    Input('dropdown1','value')
)

def network(dd1):
    
    filtered = astro_db[['mission_id','name_y']]
    #filtered = filtered[filtered['name_y']==dd1]


    def assets_pairs(astronauts):
        unique_astronauts = set(astronauts)
        if len(unique_astronauts) == 1:
            x = astronauts.iat[0]  # get the only unique asset
            pairs = [[x, x]]
        else:
            pairs = it.permutations(unique_astronauts, r=2)  # get all the unique pairs without repeated elements
        return pd.DataFrame(pairs, columns=['Source', 'Target']) 
   
    df_pairs = (
        filtered.groupby(['mission_id'])['name_y']
        .apply(assets_pairs)   # create asset pairs per group 
        .groupby(['Source', 'Target'], as_index=False)  # compute the weights  by 
        .agg(Weights = ('Source', 'size'))              # counting the unique ('Source', 'Target') pairs
    )

    new_df = df_pairs[df_pairs['Source']==dd1]

    node_list = list(
        set(new_df['Source'].unique().tolist()+new_df['Target'].unique().tolist())
    )

    nodes = [{
        'id': node_name, 
        'label': node_name,
        'shape':'dot',
        'size':15
        }
        for i, node_name in enumerate(node_list)]

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






#app.run_server(host='0.0.0.0',port='8055')
if __name__=='__main__':
	app.run_server()
