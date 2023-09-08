--Dropping tables with column "PLAYER_ID", "TEAM_ID", "EFF"
ALTER TABLE stats_2010_to_2023
DROP COLUMN PLAYER_ID, TEAM_ID, EFF

--Updating multiple values in "Year" column
UPDATE stats_2010_to_2023
SET Year = 
	CASE 
		WHEN Year ='2010-11' THEN '2010'
		WHEN Year ='2011-12' THEN '2011'
		WHEN Year ='2012-13' THEN '2012'
		WHEN Year ='2013-14' THEN '2013'
		WHEN Year ='2014-15' THEN '2014'
		WHEN Year ='2015-16' THEN '2015'
		WHEN Year ='2016-17' THEN '2016'
		WHEN Year ='2017-18' THEN '2017'
		WHEN Year ='2018-19' THEN '2018'
		WHEN Year ='2019-20' THEN '2019'
		WHEN Year ='2020-21' THEN '2020'
		WHEN Year ='2021-22' THEN '2021'
		WHEN Year ='2022-23' THEN '2022'
	END

--Updating values in "Season_Type"
UPDATE stats_2010_to_2023
SET Season_Type = 'Regular Season'
WHERE Season_Type = 'Regular%20Season'

UPDATE stats_2010_to_2023
SET MIN = ROUND(MIN,1),
	FGM = ROUND(FGM,1),
	FGA = ROUND(FGA,1),
	FG_PCT = ROUND(FG_PCT,1),
	FG3M = ROUND(FG3M,1),
	FG3A = ROUND(FG3A,1),
	FG3_PCT = ROUND(FG3_PCT,1),
	FTM = ROUND(FTM,1),
	FTA = ROUND(FTA,1),
	FT_PCT = ROUND(FT_PCT,1),
	OREB = ROUND(OREB,1),
	DREB = ROUND(DREB,1),
	REB = ROUND(REB,1),
	AST = ROUND(AST,1),
	STL = ROUND(STL,1),
	BLK = ROUND(BLK,1),
	TOV = ROUND(TOV,1),
	PTS = ROUND(PTS,1)