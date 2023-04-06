#Import libraries
import pandas as pd
import numpy as np

#Read in data
astro_db = pd.read_csv('https://raw.githubusercontent.com/statzenthusiast921/AstronautDatabase/main/astro_db_full_data.csv', encoding = "ISO-8859-1")
astro_db = astro_db[(astro_db['launch_year']<2022) & (astro_db['launch_year']>1960)]

#Roll up data to have a list of astronauts per mission
neo4j_df = pd.DataFrame(
    astro_db.groupby(['mission_name','launch_year'])['astronaut_name'].apply(list)
)
#Get into easy to use column format
neo4j_df = neo4j_df.reset_index()

#Download
neo4j_df.to_csv('neo4j_df.csv', index=False)
