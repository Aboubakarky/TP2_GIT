
import pandas

lire = pandas.read_csv("data.csv", encoding='latin1')

print(lire)

print(lire.info())

print(lire.describe())