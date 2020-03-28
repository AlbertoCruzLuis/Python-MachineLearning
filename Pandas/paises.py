import pandas as pd

#Guardamos la ruta del archivo csv
paises_path = "Paises_Capitales.csv"

#Leemos los datos y los guardamos en la varible data
data = pd.read_csv(paises_path)

#Guardar la lista de paises
paises = data.Country

#Mostrar la capital de Alemania
print(data.loc[data.Country.isin(['Alemania'])])

#Mostramos los datos
#print(paises)

