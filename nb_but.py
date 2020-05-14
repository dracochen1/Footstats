import pandas as pd

dataframe = pd.read_csv("F1.csv")
print(dataframe)
dataframeHome = dataframe[["Date", "HomeTeam", "FTHG"]]
dataframeAway = dataframe[["Date", "AwayTeam", "FTAG"]]

dataframeHome = dataframeHome.rename(columns={"FTHG": "FTG", "HomeTeam" : "Team"})
dataframeAway = dataframeAway.rename(columns={"FTAG": "FTG", "AwayTeam" : "Team"})

result = pd.concat([dataframeHome, dataframeAway])
print(result)
somme = result.groupby(["Team"]).sum().reset_index()
print(somme)

