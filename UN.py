import pandas as pd

un = pd.read_csv("https://raw.githubusercontent.com/markschaver/Data/master/UN/UN-coincidence-2018.csv", sep=",")

un[un['COINCIDENCE'] == un['COINCIDENCE'].max()]
un[un['COINCIDENCE'] == un['COINCIDENCE'].min()]
un['COINCIDENCE'].hist()
un['ABSENT'].hist()
un[un['ABSENT'] == un['ABSENT'].max()]
un[un['ABSENT'] == un['ABSENT'].min()]



