#=====================================
#  PROGRAMACION ORIENTADA A OBJETOS
#=====================================

#================================
# Una clase para un objeto vacio
# No esta vacio, necesita
# la palabra pass = pasar
#================================
class ObjetoVacio:
    pass

#=========================
#  nada es un ObjetoVacio
#=========================
nada = ObjetoVacio()
print(type(nada))

#==================
#  La clase llanta
#==================
class Llanta:
    #======================================
    #  Variable cuenta es de toda la clase
    #======================================
    cuenta = 0
    #=====================================
    #  Funcion constructora de identidad
    #  __init__ es una funcion reservada
    #  comienza con uno mismo: self
    #  pero puede ser otro nombre (mi)
    #  parametros de entrada = default
    #=====================================
    def __init__(mi,radio=50,ancho=30,presion=1.5):
        # variable de la estructura completa Llanta
        Llanta.cuenta += 1
        # variables exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion

#=========================
#  Objetos (instanciados)
#=========================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presion=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#====================================
#  Objeto que contiene otros objetos
#====================================
class Coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1,llanta2,llanta3,llanta4) 

print("Total de llantas: ",Llanta.cuenta) #Variable global de la clase
print("Presion de la llanta 4 = ",llanta4.presion) # Presion de la llanta 4
print("Radio de la llanta 4 = ",llanta4.radio)
print("Radio de la llanta 3 = ",llanta3.radio)
print("Presion de la llanta 1 de mi coche = ", micoche.llanta1.presion)

#===================
#  Encapsulamiento
#===================

#======================================================================
#  Uso de la funcion de python property para poner y obtener atributos
#======================================================================
class Estudiante:
    def __init__(mi):
        mi.__nombre = ' '
    def ponerme_nombre(mi,nombre):
        print('se llamo a ponerme_nombre')
        mi.__nombre = nombre
    def obtener_nombre(mi):
        print('se llamo a obtener_nombre')
        return mi.__nombre
    nombre=property(obtener_nombre,ponerme_nombre)

#======================================
#  Crear objeto estudiante sin nombre
#======================================
estudiante = Estudiante()

#========================================================================
#  Ponerle nombre usando la propiedad nombre y el metodo ponerme_nombre
#  (sin tener que llamar explicitamente la funcion)
#========================================================================
estudiante.nombre = "Diego"

#=====================================================================
#  Obtener el nombre con el metodo obtener_nombre
#  __nombre es una variable encapsulada (no visible fuera)
#  (sin tener que llamar explicitamente a la funcion obtener_nombre)
#=====================================================================
print(estudiante.nombre)

#  Esto no funciona
#  print(estudiante.__nombre)

#========================
#  Herencia de clases
#========================
class Cuadrilatero:
    def __init__(mi,a,b,c,d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d

    def perimetro(mi):
        p=mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
        print("perimetro=",p)
        return p

#=====================================
#  Su hijo rectangulo 
#  Rectangulo es hijo de Cuadrilatero
#  Rectangulo(Cuadrilatero)
#=====================================
class Rectangulo(Cuadrilatero):
    def __init__(self, a, b):
        #==========================
        #  Constructor de su madre
        #==========================
        super().__init__(a, b, a, b)

#======================
#  Su nieto Cuadrado
#  Hijo de Rectangulo
#======================
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area
    
    #def perimetro(self):
    #    p =4.0*self.lado1
    #    print("perimetro =",p)
    #    return p

#====================
#  Crear un cuadrado
#====================
cuadrado1 = Cuadrado(5)

#========================================================
#  Llamar al metodo perimetro de su abuelo Cuadrilatero
#========================================================
perimetro1 = cuadrado1.perimetro()

#======================================
#  Llamar a su propio metodo de area
#======================================
area1 = cuadrado1.area()

print("Perimetro = ", perimetro1)
print("Area = ", area1)

#==================================================================
#  Sobre-escribir un metodo de su madre o abuela o tatarabuela...
#  Es volver a definir una funcion ya existente
#==================================================================



#==============
#  ASOSIACION
#==============


#========================================
#  La clase A tiene tres numeros reales
#========================================
class A:
    __a:float=0.0
    __b:float=0.0
    __c:float=0.0

    def __init__(self,a:float,b:float,c:float):
        self.a = a
        self.b = b
        self.c = c

#========================================
#  La clase B tiene dos numeros reales
#========================================
class B:
    __d:float=0.0
    __e:float=0.0

    def __init__(self,d:float,e:float):
        self.d = d
        self.e = e

    #==========================================
    #  Metodo sumar todo (internos + externos)
    #==========================================
    def sumar_todo(self, aa:float, bb:float):
        x:float=self.d+self.e+aa+bb
        return x

#==============
#  ASOCIACION
#==============
#Usando objetos independientes
objetoA = A(1.0,2.0,3.0)
objetoB = B(4.0,5.0)
print(objetoB.sumar_todo(objetoA.a,objetoA.b))

#==============================================
#  El objeto C tiene dos reales y un objeto A
#  El objeto A se instancia dentro de C
#==============================================
class C:
    __d:float=0.0
    __e:float=0.0
    __Aa:A=None

    def __init__(self,d:float,e:float):
        self.d = d
        self.e = e
        # A esta instanciado adentro
        self.Aa = A(1.0,2.0,3.0)

    def sumar_todo(self):
        x:float=self.d+self.e+self.Aa.a+self.Aa.b
        return x

#================================
#  COMPOSICION
#  Contiene otro objeto dentro
#================================
objetoC = C(4.0,5.0)
print(objetoC.sumar_todo())

#===========================================
#  Objeto D tiene dos reales y un objeto A
#  definido por fuera
#===========================================
class D:
    __d:float=0.0
    __e:float=0.0
    __Aa:A=None

    def __init__(self,d:float,e:float,Aa:A):
        self.d = d
        self.e = e
        self.Aa = Aa

    def sumar_todo(self):
        x:float=self.d+self.e+self.Aa.a+self.Aa.b
        return x

#============================================
#  AGREGACION
#  Construye el objeto agregado por fuera
#============================================
objetoD = D(4.0,5.0,objetoA)
print(objetoD.sumar_todo())



#======================
#  Clase computadora
#======================
class Computadora:
    marca: str = None
    capacidad: int = 0
    ram: int = 0

    #==================
    #  Constructor
    #==================
    def __init__(self, marca:str, capacidad:int, ram:int):
        print(f"Accediendo al constructor de la pc: {marca}")
        self.marca = marca
        self.capacidad = capacidad
        self.ram = ram

    def imprimirInfoPC(self):
        print(f"Esta es la computadora marca: {self.marca} con almacenamiento de {self.capacidad}GB y memoria de {self.ram}GB")

    #=======================
    #  Destructor 
    #=======================
    def __del__(self):
        print(f"Se elimino la computadora: {self.marca}")

#=====================
#  Objeto persona
#=====================
class Persona:
    nombres: str = None
    apellidos: str = None
    edad: int = 0
    direccion: str = None
    computadora: Computadora = None

    #===========================
    #  Constructor de persona
    #===========================
    def __init__(self, nombres:str, apellidos:str, edad:int, direccion:str, marca:str, capacidad:int, ram:int):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.Computadora = Computadora(marca, capacidad, ram)
        print(f"--- Accedimos al constructor de la persona: {nombres} {apellidos}")

    def imprimirInfo(self) -> None:
        print(f"--- Mi nombre es {self.nombres} {self.apellidos}, tengo {self.edad} años de edad, vivo en {self.direccion}")

    #=====================
    #  Destructor
    #=====================
    def __del__(self):
        print(f"--- Eliminamos el objeto... {self.nombres} {self.apellidos}")

#============================
#  Funcion 1 es el programa
#============================
def funcion1():
    persona = Persona("Carlos","Perez",40,"Xochimilco","Lenovo",700,8)
    print("\n")
    persona.imprimirInfo()
    print("\n")
    persona2 = Persona("Magdalena","Carrillo",35,"Jalapa","IBM",200,4)
    print("\n")
    persona2.imprimirInfo()
    print("\n")

#=======================
#  Llamar a funcion1
#=======================
funcion1()
