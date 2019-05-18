from tkinter import *
import matplotlib 
matplotlib.use('TkAgg')
import numpy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import time
import math

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
        for f in self.F:
            resultado.append(eval(f))
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
        #print("X[",self.t,"] = ",self.y)
        self.graft.append(self.t)
        self.grafx.append(self.y[0])

class Application(Frame):
    #inicializacion de la ventana
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.inicio()
    #le da aspecto a la ventana y llama las dos partes iniciales del la ventana
    #de inicio    
    def inicio(self):
        self.master.geometry("700x350")
        self.master.title("Proyecto 4° Parcial")
        self.master.config(bg="#EAFAFF")
        self.presentacion()
        self.createWidgets()
    #texto con la presentacion
    def presentacion(self):
        self.presentationFrame = Frame(self,bg="#EAFAFF")
        self.presentationFrame.pack({"side":"top"})
        arial30B=("arial","15","bold")
        times12=("times","12")
        self.label1= Label(self.presentationFrame, 
                           text="\nPROYECTO DEL CUARTO PARCIAL\n", 
                           justify=CENTER,bg="#EAFAFF", font=arial30B)
        self.label1.pack({"side":"top"})
        
        self.label2= Label(self.presentationFrame, 
                           text="A continuacion las instrucciones", 
                           justify=CENTER,bg="#EAFAFF",font=times12)
        self.label2.pack({"side":"top"})
        
        self.label3= Label(self.presentationFrame, 
                           text="Viene predeterminada la funcion a representar, por ello solo exiten los siguientes botones", 
                           justify=CENTER,bg="#EAFAFF",font=times12)
        self.label3.pack({"side":"top"})
        
        self.label4= Label(self.presentationFrame, 
                           text="Por pasos muestra como se va generando la grafica de la solucion a dicha ecuacion", 
                           justify=CENTER,bg="#EAFAFF",font=times12)
        self.label4.pack({"side":"top"})
        
        self.label5= Label(self.presentationFrame, 
                           text="Total muestra la lista de los 100 pasos con las soluciones de cada iteracion\n", 
                           justify=CENTER,bg="#EAFAFF",font=times12)
        self.label5.pack({"side":"top"})
    #botones para pasarnos a la siguiente ventana
    def createWidgets(self):
        self.botonesInicio = Frame(self,bg="#EAFAFF")
        self.botonesInicio.pack({"side":"bottom"})
        
        self.porPasos = Button(self.botonesInicio)
        self.porPasos["text"]="Por Pasos"
        self.porPasos["bg"]="light blue"
        self.porPasos["fg"]="black"
        self.porPasos["command"]=self.PasoPorPasoDesdeInicio
        self.porPasos.pack({"side":"left"})
        #comentado hasta poder hacer que se reinicie la grafica
        #self.total = Button(self.botonesInicio)
        #self.total["text"]="Total"
        #self.total["bg"]="light green"
        #self.total["fg"]="black"
        #self.total["command"]=self.TotalDesdeInicio
        #self.total.pack({"side":"left"})
        
        self.Salir = Button(self.botonesInicio)
        self.Salir["text"]="Salir"
        self.Salir["bg"]="white"
        self.Salir["fg"]="red"
        self.Salir["command"]=self.quit
        self.Salir.pack({"side":"left"})
    #comentado hasta poder hacer que se reinicie la grafica    
    #def PasoPorPasoDesdeTotal(self):
    #    self.botonesPantallaTres.destroy()
    #    self.textoFrame.destroy()
    #    #*********************************************************************
    #    self.botonesPantallaSecundaria()
    #    self.graficas()
    
    #llama la funcion ocultainicio y llama las funciones para agregar los 
    #componente s de la parte dos
    def PasoPorPasoDesdeInicio(self):
        self.ocultaInicio()
        self.botonesPantallaSecundaria()
        self.graficas()
    
    #forra los botones y los textos de la pantalla de inicio    
    def ocultaInicio(self):
       self.botonesInicio.destroy()       
       self.presentationFrame.destroy()
    
    #genera las graficas de una forma que parece video    
    def graficas(self):
        self.graficaFrame = Frame(self,bg="#EAFAFF")
        self.graficaFrame.pack({"side":"top"})
        
        fig = plt.figure(figsize=(8,4))
        plt.title("Grafica de la posición en X respecto al tiempo T")
        plt.xlabel("Tiempo T")
        plt.ylabel("Posicion en X")
        plt.grid()
        FIGURE=FigureCanvasTkAgg(fig,self.graficaFrame)
        FIGURE.get_tk_widget().grid(row=0,column=0)
        rk4=RK4()
        for i in range(100):
            rk4.itera()
            plt.plot(rk4.graft,rk4.grafx)
            fig.canvas.draw()
            time.sleep(0.1)   
        
    #genera los botones abajo de las graficas    
    def botonesPantallaSecundaria(self):
        self.botonesPantallaDos=Frame(self,bg="#EAFAFF")
        self.botonesPantallaDos.pack({"side":"bottom"})
        
        self.total = Button(self.botonesPantallaDos)
        self.total["text"]="Total"
        self.total["bg"]="light green"
        self.total["fg"]="black"
        self.total["command"]=self.TotalDesdePasoPorPaso
        self.total.pack({"side":"left"})
        
        self.Salir = Button(self.botonesPantallaDos)
        self.Salir["text"]="Salir"
        self.Salir["bg"]="white"
        self.Salir["fg"]="red"
        self.Salir["command"]=self.quit
        self.Salir.pack({"side":"left"})
        
    #def TotalDesdeInicio(self):
    #    self.ocultaInicio()
    #    self.botonesPantallaTerciaria()
    #    self.textoPantallaTerciaria()
    
    #se pasa de las graficas a las soluciones
    #se borran las graficas y los botones bajo esta, se generan los botones
    #de esta pantalla y presenta las soluciones    
    def TotalDesdePasoPorPaso(self):
        self.graficaFrame.destroy()
        self.botonesPantallaDos.destroy()
        self.botonesPantallaTerciaria()
        self.textoPantallaTerciaria()
    
    def botonesPantallaTerciaria(self):
        self.botonesPantallaTres=Frame(self,bg="#EAFAFF")
        self.botonesPantallaTres.pack({"side":"bottom"})
        
        #self.porPasos = Button(self.botonesPantallaTres)
        #self.porPasos["text"]="Por Pasos"
        #self.porPasos["bg"]="light blue"
        #self.porPasos["fg"]="black"
        #self.porPasos["command"]=self.PasoPorPasoDesdeTotal
        #self.porPasos.pack({"side":"left"})
        
        self.Salir = Button(self.botonesPantallaTres)
        self.Salir["text"]="Salir"
        self.Salir["bg"]="white"
        self.Salir["fg"]="red"
        self.Salir["command"]=self.quit
        self.Salir.pack({"side":"left"})
        
    def textoPantallaTerciaria(self):
        self.textoFrame = Frame(self,bg="#EAFAFF")
        self.textoFrame.pack({"side":"top"})
        
        self.impresion = Text(self.textoFrame)
        rk4=RK4()
        self.impresion.insert(INSERT,'X['+str(rk4.t)+'] = ['+str(rk4.y[0])+']\n')
        for i in range(100):
            rk4.itera()
            self.impresion.insert(INSERT,'X['+str(rk4.t)+'] = ['+str(rk4.y[0])+']\n')
        self.impresion.insert(END,'')
        self.impresion.pack({"side":"top"})
        
        
        
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()        
