import pandas as pd

def load_and_process(path_to_csv_file):
    #Load dataframe from given path
    df = pd.read_csv(path_to_csv_file)
    

    df = (df.loc[:9927]
      .drop(['id', 'age', 'plus_minus', 'penalties_minutes', 'goalie_losses', 'to_year',
             'goalie_ties_overtime', 'save_percentage', 'goals_against_average',
             'point_shares', 'goals', 'assists','year','team','overall_pick','nationality'], axis=1)
      .assign(score=lambda x: x.games_played + x.points)
      .assign(Goalie_score=lambda x: x.goalie_games_played+x.goalie_wins)
      .dropna(subset=['goalie_games_played', 'games_played'], how='all')
     )

    # Move the 'score' column to the 6th position
    cols = df.columns.tolist()
    cols.insert(5, cols.pop(cols.index('score')))
    df = df.reindex(columns=cols)

    return df


