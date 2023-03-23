import pandas as pd

def load_and_process(path_to_csv_file):
    #Load dataframe from given path
    df = pd.read_csv(path_to_csv_file)
    
    #Method chain 3, keeps only rows from 1982 - present, drops all unneccessary columns, and adds score column
    df = (df.loc[227:9928]
          .drop(['id', 'age', 'plus_minus', 'penalties_minutes', 'goalie_losses', 'to_year',
                      'goalie_ties_overtime', 'save_percentage', 'goals_against_average',
                      'point_shares','team','player','year','overall_pick','goals','assists'], axis=1)
         .assign(score=lambda x: x.games_played + x.points))
    
    return df

