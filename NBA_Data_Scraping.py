import pandas as pd
import requests
import time
import numpy as np

# see all columns in a wide DataFrame
pd.set_option('display.max_column', None)

# collecting data from url
nba_stats = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2022-23&SeasonType=Regular%20Season&StatCategory=PTS'

r = requests.get(url=nba_stats).json()

# defining rows and headers and creating table
table_header = r['resultSet']['headers']
table_rows = r['resultSet']['rowSet']
pd.DataFrame(table_rows,columns=table_header)

df_cols = ['Year','Season_Type'] + table_header
df = pd.DataFrame(columns=df_cols)
season_type = ['Regular%20Season','Playoffs']
years = ['2022-23']#,'2011-12','2012-13','2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21','2021-22','2022-23']

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'stats.nba.com',
    'Origin': 'https://www.nba.com',
    'Referer': 'https://www.nba.com/',
    'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

begin_loop = time.time()

for y in years:
    for s in season_type:
        api_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season='+y+'&SeasonType='+s+'&StatCategory=PTS'
        r = requests.get(url=api_url, headers=headers).json()
        temp_df1 = pd.DataFrame(table_rows,columns=table_header)
        temp_df2 = pd.DataFrame({'Year':[y for i in range(len(temp_df1))],
                                'Season_Type':[s for i in range(len(temp_df1))]})
        temp_df3 = pd.concat([temp_df2,temp_df1],axis=1)
        df = pd.concat([df, temp_df3], axis=0)
        print(f'Finished scraping data for {y} {s}.')

print(f'Process Completed. Total run time: {round((time.time()-begin_loop)/60,2)}')
df.to_excel('2022-23_data.xlsx', index=False)

