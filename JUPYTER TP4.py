import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("/Users/Louis-Philip/PycharmProject/TP4/CrimeCitoyen.csv", delimiter=",", parse_dates=["DATE"])
df['CATEGORIE'] = df['CATEGORIE'].str.replace(u"�", "e")
df['CATEGORIE'] = df['CATEGORIE'].str.replace(u"vehicule e moteur", "vehicule a moteur")
df.head()

df['YEAR'] = pd.DatetimeIndex(df['DATE']).year
df['MONTH'] = pd.DatetimeIndex(df['DATE']).month
df.head()

Crime_par_année=df["YEAR"].value_counts()
print(Crime_par_année)
df.groupby(["YEAR"]).size().plot(kind='bar')
plt.show()

moyenne_par_annee=Crime_par_année.mean()
ecart_type_par_annee=Crime_par_année.mean()
moyenne_par_annee=moyenne_par_annee.round(2)
ecart_type_par_annee=ecart_type_par_annee.round(2)
print("La moyenne de crime par année est de " + str(moyenne_par_annee) + " par année")

print("L'écart-type de ce nombre est de " + str(ecart_type_par_annee) + " crimes")

df.groupby(['YEAR', 'CATEGORIE']).size()

df.groupby(['CATEGORIE','YEAR']).size().unstack().plot(kind='bar',stacked=True)
plt.show()

print(df.groupby(['CATEGORIE','QUART']).size())