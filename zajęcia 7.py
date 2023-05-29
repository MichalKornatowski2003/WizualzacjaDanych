import numpy as np
import pandas as pd

# zad 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

# zad 2a
x = df[df['Liczba'] > 1000]
#print(x)

# zad 2b
imie = df[df['Imie'] == "MICHAŁ"]
#print(imie)

# zad 2c
suma = df['Liczba'].sum()
#print(suma)

# zad 2d
suma2 = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]['Liczba'].sum()
#print(suma2)

# zad 2e
chłopcy = df[df['Plec'] == "M"]['Liczba'].sum()
#print(chłopcy)
dziewczyny = df[df['Plec'] == "K"]['Liczba'].sum()
#print(dziewczyny)

# zad 2f
for rok in df['Rok'].unique():
    rok_df = df[df['Rok'] == rok]
    popularneD = rok_df[rok_df['Plec'] == 'K']['Imie'].iloc[-1]
    #print(rok, popularneD)
    popularneM = rok_df[rok_df['Plec'] == 'M']['Imie'].iloc[-1]
    #print(rok, popularneM)
# zad 2g
kobiety = df[df['Plec'] == 'K']
meszczyzni = df[df['Plec'] == 'M']
imionaM = kobiety.groupby('Imie')['Liczba'].sum().reset_index().rename(columns={'Liczba': 'Suma', 'Imie': 'Imiona'})
imionaK = meszczyzni.groupby('Imie')['Liczba'].sum().reset_index().rename(columns={'Liczba': 'Suma', 'Imie': 'Imiona'})
max_idxM = imionaM['Suma'].idxmax()
max_idxK = imionaK['Suma'].idxmax()
najwM = imionaM.loc[max_idxM]
najwK = imionaM.loc[max_idxK]
print(najwM)
print(najwK)


