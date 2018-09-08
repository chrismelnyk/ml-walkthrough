#ML Class from @sentdex
import pandas as pd
import quandl
import quandl as Quandl

quandl.ApiConfig.api_key = "aYDDgqtMx1xtLoNteb6T"

df = Quandl.get("WIKI/GOOGL")

print(df.head())