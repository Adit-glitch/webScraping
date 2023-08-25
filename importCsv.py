import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gdp.csv')

#print(df['GDP Real  (Inflation adj.)'])

df['GDP Real  (Inflation adj.)'] = df['GDP Real  (Inflation adj.)'].str.replace('$','').str.replace(',','').astype('int64')

plt.plot(df['Year'], df['GDP Real  (Inflation adj.)'])
plt.show()