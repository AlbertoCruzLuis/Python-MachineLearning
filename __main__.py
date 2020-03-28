from vehiculo import *
from curso import *

#Probar las clases creadas
lista = [
  Coche("azul", 4, 150, 1200),
  Camioneta("verde",4,120,1800,400),
  Bicicleta("roja", 2, "urbana"),
  Motocicleta("azul", 2, "deportiva", 180, 250)
]

for i in lista:
  print(i)

listaCursos = [
  Curso("Python"),
  Cplusplus(7)
]

for i in listaCursos:
  print(i)