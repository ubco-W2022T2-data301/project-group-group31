import pandas as pd

def load_and_process(path_to_csv_file):
    #Load dataframe from given path
    df = pd.read_csv(path_to_csv_file)
    
    #Method chain 1, keeps only rows from 1982 - present, drops all unneccessary columns, and adds score column
    df = (df.loc[:9927]
          .drop(['id', 'age', 'plus_minus', 'penalties_minutes', 'goalie_games_played', 'goalie_wins',
                    'goalie_losses', 'nationality', 'position', 'to_year', 'amateur_team', 'goalie_ties_overtime',
                     'save_percentage', 'goals_against_average', 'point_shares'], axis=1)
         .assign(score=lambda x: x.games_played + x.points))
    
    #Second method chain to rename all column names, and drop some teams that don't exist anymore
    df = (df.set_axis(['Year', 'Overall Pick', 'Team', 'Player', 'Games Played', 
                       'Goals', 'Assists', 'Points', 'Score'], axis=1)
          .query("Team != 'Hartford Whalers'").query("Team != 'Atlanta Thrashers'").query("Team !='Minnesota North Stars'"))
    
    return df