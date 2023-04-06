import pandas as pd

# Mapping positions to forward (F) and defense (D)
positions_map = {
    'RW': 'Forward',
    'C': 'Forward',
    'LW': 'Forward',
    'C/LW': 'Forward',
    'LW/C': 'Forward',
    'C/RW': 'Forward',
    'W': 'Forward',
    'RW/D': 'Forward',
    'C RW': 'Forward',
    'C; LW': 'Forward',
    'LW/D': 'Forward',
    'RW/D': 'Forward',
    'D': 'Defence',
    'G': 'Goalie'
}

# Load dataframe and replace positions
def load_and_process(path_to_csv_file):
    #Load dataframe from given path
    df = pd.read_csv(path_to_csv_file)
    df = (df.loc[:9927]
       .drop(['id', 'age', 'plus_minus', 'penalties_minutes', 'goalie_losses','to_year',
             'goalie_ties_overtime', 'save_percentage', 'goals_against_average', 'player',
             'point_shares', 'goals', 'assists','team','overall_pick','nationality','goalie_games_played'], axis=1)
      .rename(columns={'year': 'Year','position': 'Position', 'amateur_team': 'Amateur Team', 
                       'games_played': 'Games', 'points': 'Points', 'goalie_wins': 'Goalie Wins'})
      .assign(Score=lambda x: x.Games + x.Points)
      .dropna(subset=['Games'], how='all')
     )


    #Fixing teams that changed their name 
    df['Amateur Team'] = df['Amateur Team'].replace('Portland Winter Hawks (WHL)', 'Portland Winterhawks (WHL)')
    df['Amateur Team'] = df['Amateur Team'].replace('USA U-18 Development Team (USDP/USHL)', 'USNDT (USA)')
    df['Amateur Team'] = df['Amateur Team'].replace('USA U-18 Development Team (USDP/NAHL)', 'USNDT (USA)')
    df['Amateur Team'] = df['Amateur Team'].replace('CSKA Moskva (Soviet)', 'CSKA Moskva (Russia)')
    df['Amateur Team'] = df['Amateur Team'].replace('Dynamo Moskva (Soviet)', 'Dynamo Moskva (Russia)')
    
    df['Amateur League'] = df['Amateur Team'].apply(lambda x: 'WHL' if '(WHL)' in x else
                                                ('BCHL' if '(BCHL)' in x else
                                                ('AJHL' if '(AJHL)' in x else
                                                ('OHL' if '(OHL)' in x else
                                                ('QMJHL' if '(QMJHL)' in x else
                                                ('USHL' if 'USHL' in x else
                                                ('USDP' if 'USDP' in x or '(USA)' in x else
                                                ('NAHL' if '(NAHL)' in x else
                                                ('High School' if 'High' in x else
                                                ('NCAA' if '(Big Ten)' in x or '(H-East)' in x or '(NCHC)' in x or '(CCHA)' in x else
                                                ('DEL' if '(Germany)' in x else
                                                ('KHL' if '(Russia)' in x else
                                                ('VHL' if '(Russia-2)' in x else
                                                ('MHL' if '(Russia Jr.)' in x else
                                                ('SHL' if '(Sweden)' in x else
                                                ('Allsvenskan' if '(Sweden-2)' in x else
                                                ('J20 Nationell' if '(Sweden Jr.)' in x else
                                                ('SM-liiga' if '(Finland' in x else
                                                ('SM-sarja' if '(Finland Jr.)' in x else
                                                ('Tipsport Extraliga' if '(Czech' in x else
                                                ('Tipos Extraliga' if '(Slovakia' in x else
                                                ('Fjordkraft-ligaen' if '(Norway' in x else
                                                ('NL' if '(Swiss' in x else '')))))))))))))))))))))))

    # Replace positions
    df['Position'] = df['Position'].replace(positions_map)
    
    return df





