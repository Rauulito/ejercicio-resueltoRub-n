#Declaracion de Clases
class Figura:
    def dibujar(self):
        print ("Dibujar Figura")

    def pintar(self):
        print ("Pintando Figura")

class Cuadrado(Figura): #Heredando de la clase Figura
    def dibujar(self):   #Redefiniendo Metodo
        print ("Dibujar Cuadrado")

class Triangulo(Figura): #Heredando de la clase Figura
    def dibujar(self):   #Redefiniendo Metodo
        print ("Dibujar Triangulo")


#Programa Principal
c = Cuadrado();
c.dibujar()
c.pintar()
t = Triangulo()
t.dibujar()
t.pintar()