import pandas as pd

def load_and_process(path_to_csv_file):
    #Load dataframe from given path
    df = pd.read_csv(path_to_csv_file)
    df = (df.loc[:9927]
      .drop(['id', 'age', 'plus_minus', 'penalties_minutes', 'goalie_losses', 'to_year',
             'goalie_ties_overtime', 'save_percentage', 'goals_against_average',
             'point_shares', 'goals', 'assists','team','overall_pick','nationality','goalie_games_played'], axis=1)
      .assign(score=lambda x: x.games_played + x.points+x.goalie_wins)
      .dropna(subset=['games_played'], how='all')
     )
    df['amateur_team'] = df['amateur_team'].replace('Portland Winter Hawks (WHL)', 'Portland Winterhawks (WHL)')
    df['amateur_team'] = df['amateur_team'].replace('USA U-18 Development Team (USDP/USHL)', 'USNDT (USA)')
    df['amateur_team'] = df['amateur_team'].replace('USA U-18 Development Team (USDP/NAHL)', 'USNDT (USA)')
    df['amateur_team'] = df['amateur_team'].replace('CSKA Moskva (Soviet)', 'CSKA Moskva (Russia)')
    df['amateur_team'] = df['amateur_team'].replace('Dynamo Moskva (Soviet)', 'Dynamo Moskva (Russia)')
    return df



