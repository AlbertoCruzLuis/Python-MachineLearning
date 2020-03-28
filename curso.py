class Curso():
  __name = str()

  def __init__(self, name):
    self.__name = name

  def __str__(self):
    return "Curso de {}\n".format(self.__name)
  
class Cplusplus(Curso):
  __desc = "Curso para principiantes desde 0"
  __Ncap = int()
  __Cap = []

  def __init__(self, Ncap):
    self.__Ncap = Ncap
    super().__init__("C++")

  def crear_capitulo(self, cap = int()):
    self.__Cap.append(cap)

  def __str__(self):
    return super().__str__() + "Descripcion: {}".format(self.__desc)
  
