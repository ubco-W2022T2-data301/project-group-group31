import pandas as pd
def load_and_process(path_to_csv_file):
    dataframe = pd.read_csv(path_to_csv_file)
    
    dataframe = (dataframe.drop(['id','overall_pick','team','player','position','age','to_year','amateur_team',
                 'points','plus_minus','penalties_minutes','goalie_games_played','goalie_wins',
                 'goalie_games_played','goalie_wins','goalie_losses','goalie_ties_overtime',
                 'save_percentage','goals_against_average','point_shares', 'games_played',
                 'goals','assists'], axis=1).reset_index(drop=True))

    return dataframe