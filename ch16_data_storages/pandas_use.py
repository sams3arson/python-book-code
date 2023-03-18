import pandas

data = pandas.read_csv("villains.csv")
print(data)

dates = pandas.date_range("2019-01-01", periods=3, freq="MS")
print(dates)

