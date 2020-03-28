import matplotlib.pyplot as plt

#Datos
a = [1,8,3,7,15,21]
b = [11,22,33,44,55,66]
bins = [0,10,20,30,40,50,60,70,80,90]
divisiones = [8,5,5,2]
colores = ['red','blue','orange','green']
labels = ['ZonaA' ,'ZonaB' ,'ZonaC', 'ZonaD']

#Diagrama de Lineas
#plt.plot(a, b, color='blue', linewidth=3, label='linea')

#Diagrama de barras
#plt.bar(a,b, label = 'Datos', width = 0.5, color = 'orange')

#Histograma
#plt.hist(a,bins, histtype= 'bar', rwidth= 0.8, color= 'lightgreen')

#Grafico de Dispersion
#plt.scatter(a,b, label= 'Datos Dispersos', color = 'red')

#Explode: es para sacar una seccion hacia fuera para destacarla
#Autopct: es para mostrar los numeros o simbolos dentro de cada seccion

#Grafico Circular
plt.pie(divisiones, explode=(0.1,0.2,0,0), labels=labels, colors=colores,startangle=90,
shadow=True, autopct='%1.1f%%')

#Definir Titulo y nombre de los ejes
plt.title('Grafico')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

plt.legend()
plt.show()
