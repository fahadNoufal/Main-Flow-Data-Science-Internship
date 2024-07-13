import pandas as pd

df=pd.read_csv('01.Data Cleaning and Preprocessing.csv')
#reading csv file

df.head(10)
#displaying first 10 rows of the data

df[df['BlowFlow']<df.BlowFlow.mean()]
#displays rows containing blowFlow values less than the mean value

df.ffill()
#forward fill

df.bfill()
#backward fill

df.interpolate( inplace=True)

df.dropna( inplace=True)
#dropping the rows with NaN values


df.describe()
#gives the summary statistics