import pandas as pd
def load_and_process(path_to_csv_file):
    dataframe = pd.read_csv(path_to_csv_file)
    
    dataframe = (dataframe.drop(['id','overall_pick','team','player','position','to_year','amateur_team',
                 'points','plus_minus','penalties_minutes','goalie_games_played','goalie_wins',
                 'goalie_games_played','goalie_wins','goalie_losses','goalie_ties_overtime',
                 'save_percentage','goals_against_average','point_shares', 'games_played',
                 'goals','assists'], axis=1).reset_index(drop=True).rename(columns={"year":"Draft Year"})
                 .rename(columns={"nationality":"Nationality"}).assign(Nation_Name = lambda x: x.Nationality))
    
    dataframe['Nation_Name'] = dataframe['Nation_Name'].replace('CA', 'Canada')
    dataframe['Nation_Name'] = dataframe['Nation_Name'].replace('US', 'USA')
    dataframe['Nation_Name'] = dataframe['Nation_Name'].replace('SE', 'Sweden')

    return dataframe