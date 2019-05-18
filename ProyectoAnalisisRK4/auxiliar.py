import math
# importar el módulo pyplot
from matplotlib import pyplot as plt
import matplotlib
import time
class RK4 :
    #valores que se inician al crear un objeto nuevo
    y=[]
    F=[]
    h=0
    #valores dinamicos, estos son auxiliares para encontrar a y
    t=0
    k1=[]
    k2=[]
    k3=[]
    k4=[]
    #listas para sacar la grafica del problema
    grafx=[]
    graft=[]
    #constructor del objeto para encontrar la solucion
    def __init__(self):
        #se agrega en el vector(lista) y los valores iniciales tomando en cuenta que
        #la primer posición es la variable x y la segunda es la variable y
        self.y=[1,1]
        #se define el vector F que es la función de cada una de las derivadas
        #de las variables arriba descritas, se ponen en vorma de cadena para
        #operarlas mediante el comando eval, haciendo dinamico este problema
        #podiendo agregar cualquier tipo de ecuacion
        self.F=['y','-1*math.sin(x)']
        #se define el paso, también puedde variar
        self.h=0.1
        #se agregan los valores iniciales en la lista de tiempos y de valores
        #en equis para su posteriror ploteo
        self.graft.append(self.t)
        self.grafx.append(self.y[0])
        
    #Esta funcion funge como auxiliar que calula el vector F de cada problema,
    #haciendolo funcion y generica lo podemos usar para cualquier k cambiando
    #unicamente los valores de entrada
    def Fcalcula(self,t,x,y):
        resultado=[]

        resultado.append(y)
        resultado.append(-(math.sin(x)))
    
        #se regresa una lista de resultados de evaluar F(t,Y)
        return resultado
    
    #Estas funciones solo cambian en los valores de x, y y t que se definen 
    #antes de pasar los parametros a la funcion Fcalcula descrita anteriormente.
    #Esta funcion guarda dentro de los atributos del objeto los valores para
    #k1,k2,k3 y k4 para su posterior operacion sin necesidad de andar pasando
    #parametros entre ellos, tomando en cuenta el paradigma funcional dentro
    #del paradigma orientado a objetos
    def kUno(self):
        k1=[]
        x=self.y[0]
        y=self.y[1]
        t=self.t
        Fevaluada=self.Fcalcula(t,x,y)
        for f in Fevaluada:
            k1.append(f*self.h)
        self.k1=k1
        
    def kDos(self):
        k2=[]
        x=self.y[0]+self.k1[0]/2
        y=self.y[1]+self.k1[1]/2
        t=self.t+self.h/2
        Fevaluada=self.Fcalcula(t,x,y)
        for f in Fevaluada:
            k2.append(f*self.h)
        self.k2=k2
        
    def kTres(self):
        k3=[]
        x=self.y[0]+self.k2[0]/2
        y=self.y[1]+self.k2[1]/2
        t=self.t+self.h/2
        Fevaluada=self.Fcalcula(t,x,y)
        for f in Fevaluada:
            k3.append(f*self.h)
        self.k3=k3
        
    def kCuatro(self):
        k4=[]
        x=self.y[0]+self.k3[0]
        y=self.y[1]+self.k3[1]
        t=self.t+self.h
        Fevaluada=self.Fcalcula(t,x,y)
        for f in Fevaluada:
            k4.append(f*self.h)
        self.k4=k4
    #se define la función NuevaY como la función que recalcula Y con los valores
    #de k1,k2,k3 y k4 objetnidos anteriormente
    def NuevaY(self):
        for i in range(len(self.y)):
            self.y[i]=self.y[i]+(1/6)*(self.k1[i]+2*self.k2[i]+2*self.k3[i]+self.k4[i])
            
    #se define la funcion itera para poder ocupar hacer uso de las funciones anteriores.
    #Las funciones anteriores no necesitan parametros mas que Fcalcula, esto es a lo que
    #pretendia llegar al usar el paradigma oriendato a objetos para no estar batallando
    #con saber que valores pasar a las funciones en una funcion global main como
    #la que se ve a continucacion.
    #Se define una nueva t, se generan las K's y posterior se genera la nueva y
    #al final estos valores se agregan a las listas para su ploteo
    def itera(self):
        self.t=round(self.t+self.h,1)
        self.kUno()
        self.kDos()
        self.kTres()
        self.kCuatro()
        self.NuevaY()
        print("X[",self.t,"] = ",self.y)
        self.graft.append(self.t)
        self.grafx.append(self.y[0])

problema=RK4()
for i in range(1000):
    problema.itera()
    plt.plot(problema.graft,problema.grafx,'+-')
    plt.show()
    time.sleep(0.0001)
