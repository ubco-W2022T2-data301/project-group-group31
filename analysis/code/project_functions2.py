import pandas as pd
def load_and_process(path_to_csv_file):
    dataframe = pd.read_csv(path_to_csv_file)
    
    dataframe = (dataframe.drop(['id','overall_pick','team','player','position','to_year','amateur_team',
                 'points','plus_minus','penalties_minutes','goalie_games_played','goalie_wins',
                 'goalie_games_played','goalie_wins','goalie_losses','goalie_ties_overtime',
                 'save_percentage','goals_against_average','point_shares', 'games_played',
                 'goals','assists'], axis=1).reset_index(drop=True).rename(columns={"year":"Draft Year"})
                 .rename(columns={"nationality":"Country"}).assign(Nationality = lambda x: x.Country))
    
    dataframe2 = dataframe
    dataframe2 = (dataframe2.drop(['Country'],axis=1).reset_index(drop=True))

    
    dataframe['Nationality'] = dataframe['Nationality'].replace('CA', 'Canada')
    dataframe['Nationality'] = dataframe['Nationality'].replace('US', 'USA')
    dataframe['Nationality'] = dataframe['Nationality'].replace('SE', 'Sweden')
    dataframe['Nationality'] = dataframe['Nationality'].replace('RU', 'Russia')
    dataframe['Nationality'] = dataframe['Nationality'].replace('FI', 'Finland')
    dataframe['Nationality'] = dataframe['Nationality'].replace('CZ', 'Czechia')
    dataframe['Nationality'] = dataframe['Nationality'].replace('SK', 'Slovakia')
    dataframe['Nationality'] = dataframe['Nationality'].replace('DE', 'Germany')
    dataframe['Nationality'] = dataframe['Nationality'].replace('CH', 'Switzerland')
    dataframe['Nationality'] = dataframe['Nationality'].replace('LV', 'Latvia')
    dataframe['Nationality'] = dataframe['Nationality'].replace('UA', 'Ukraine')
    dataframe['Nationality'] = dataframe['Nationality'].replace('BY', 'Belarus')
    dataframe['Nationality'] = dataframe['Nationality'].replace('DK', 'Denmark')
    dataframe['Nationality'] = dataframe['Nationality'].replace('KZ', 'Kazakhstan')
    dataframe['Nationality'] = dataframe['Nationality'].replace('NO', 'Norway')
    dataframe['Nationality'] = dataframe['Nationality'].replace('GB', 'Great Britain')
    dataframe['Nationality'] = dataframe['Nationality'].replace('AT', 'Austria')
    dataframe['Nationality'] = dataframe['Nationality'].replace('FR', 'France')
    dataframe['Nationality'] = dataframe['Nationality'].replace('SI', 'Slovenia')
    dataframe['Nationality'] = dataframe['Nationality'].replace('PL', 'Poland')
    dataframe['Nationality'] = dataframe['Nationality'].replace('LT', 'Lithuania')
    dataframe['Nationality'] = dataframe['Nationality'].replace('YU', 'Yugoslavia')
    dataframe['Nationality'] = dataframe['Nationality'].replace('HU', 'Hungary')
    dataframe['Nationality'] = dataframe['Nationality'].replace('UZ', 'Uzbekistan')
    dataframe['Nationality'] = dataframe['Nationality'].replace('JP', 'Japan')
    dataframe['Nationality'] = dataframe['Nationality'].replace('IT', 'Italy')
    dataframe['Nationality'] = dataframe['Nationality'].replace('BR', 'Brazil')
    dataframe['Nationality'] = dataframe['Nationality'].replace('BE', 'Belgium')
    dataframe['Nationality'] = dataframe['Nationality'].replace('BS', 'Bahamas')
    dataframe['Nationality'] = dataframe['Nationality'].replace('KR', 'South Korea')
    dataframe['Nationality'] = dataframe['Nationality'].replace('EE', 'Estonia')
    dataframe['Nationality'] = dataframe['Nationality'].replace('NG', 'Nigeria')
    dataframe['Nationality'] = dataframe['Nationality'].replace('SU', 'Soviet Union')
    dataframe['Nationality'] = dataframe['Nationality'].replace('JM', 'Jamacia')
    dataframe['Nationality'] = dataframe['Nationality'].replace('TH', 'Thailand')
    dataframe['Nationality'] = dataframe['Nationality'].replace('NL', 'Netherlands')
    dataframe['Nationality'] = dataframe['Nationality'].replace('CN', 'China')
    dataframe['Nationality'] = dataframe['Nationality'].replace('TZ', 'Tanzania')
    dataframe['Nationality'] = dataframe['Nationality'].replace('BN', 'Brunei')
    dataframe['Nationality'] = dataframe['Nationality'].replace('AU', 'Australia')
    dataframe['Nationality'] = dataframe['Nationality'].replace('ZA', 'South Africa')
    dataframe['Nationality'] = dataframe['Nationality'].replace('ME', 'Serbia')
    dataframe['Nationality'] = dataframe['Nationality'].replace('HT', 'Haiti')
    dataframe['Nationality'] = dataframe['Nationality'].replace('TW', 'Taiwan')
    dataframe['Nationality'] = dataframe['Nationality'].replace('PY', 'Paraguay')
    dataframe['Nationality'] = dataframe['Nationality'].replace('VE', 'Venezuela')

    return dataframe