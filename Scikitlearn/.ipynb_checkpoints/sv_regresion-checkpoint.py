import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

######## IMPORTAR LOS DATOS #########

#Importar los datos de la libreria scikit-learn
boston = datasets.load_boston()
print(boston)

###### COMPRENDER LOS DATOS #######

print(boston.keys())
print(boston.DESCR)
print(boston.feature_names)

###### PREPARAR LOS DATOS ######

#Numero de habitaciones columana numero 6
X_svr = boston.data[:, np.newaxis, 5]

y_svr = boston.target

#Graficamos los datos
plt.scatter(X_svr, y_svr)
plt.show()

####### IMPLEMENTACION DE VECTORES DE SOPORTE REGRESION #######

from sklearn.model_selection import train_test_split

#Separar los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_svr, y_svr, test_size=0.2)

from sklearn.svm import SVR

#Definimos el algoritmo
#Probamos a cambiar los parametros y comparar el error obtenido
#svr = SVR(kernel='linear', C=1.0, epsilon=0.2)
svr = SVR(epsilon=0.1)


#Entreno el modelo
svr.fit(X_train, y_train)

#Realizo una prediccion
Y_pred = svr.predict(X_test)

#Graficamos los datos junto con el modelo
plt.scatter(X_test, y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=3)
plt.show()

#Datos del modelo
print('Datos del modelo de soporte regresion')

print('Presicion del Modelo')
print(svr.score(X_train, y_train))