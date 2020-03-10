### Guía Python by dM ###

#########################
##### Zen of Python #####
#########################

>>> import this
The Zen of Python, by Tim Peters

"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

####################################
##### Estándares de Desarrollo #####
####################################

Los estándares de desarrollo constituyen las normas o patrones de referencia que se deben implementar en el desarrollo de
aplicaciones de software. Entre los estándares de desarrollo más comunes se encuentran: normas de codificación, normas y
esquemas de seguridad, estándares de interfaz u/s, entre otros.

##### Normas de Codificación #####

Para el desarrollo de un sistema se pueden implementar algunos estándares básicos para su codificación, los cuales contemplan lo
establecido en la PEP-8 --> https://www.python.org/dev/peps/pep-0008/

Algunos puntos importantes que encontramos en el PEP8 son los siguientes:

-Use sangría de 4 espacios, sin tabulaciones.

-Las líneas no deberían sobrepasar los 79 caracteres.

-Use líneas en blanco para separar funciones y clases, también para grandes bloques de código dentro de funciones.

-Cuando sea posible, coloque los comentarios aparte del código de tal manera que en esa línea sólo haya comentarios.

-Use cadenas de documentación (docstrings)

-Use espacios a los lados de los operadores y después de comas, pero no directamente dentro de constructos
con paréntesis. Ej: a = f(1, 2) + g(3, 4)

-Nombre sus clases y funciones de forma consistente, como convención se utiliza CamelCase para las clases y
minúsculas_con_guion_bajo para funciones y métodos. Siempre utilice self como el nombre para el primer argumento de un método.

-No use codificaciones de caracteres lujosas si su código pretende ser utilizado en el ámbito internacional.
Se prefiere que utilicen UTF-8. Tomar en cuenta el PEP-0263 colocando la directiva para codificación
UTF-8 (# -*- coding: utf-8 -*-) a los archivos .py

##### Estándares para la documentación del código fuente #####

-La utilización de docstrings permite generar automáticamente documentación, como alternativas a utilizar para generar la
documentación del proyecto tenemos doxygen o Sphinx.

Cabecera para los scripts de Python, indica al compilador o editor que se trata de un fichero python
La segunda linea da codificación UTF-8 al programa:

#!/usr/bin/env python
# -*- coding: utf-8 -*-

A veces solo es necesario usar la segunda línea:

# -*- coding: utf-8 -*-

---

# Comentarios de línea en Python

""" Comentarios de 
Múltiple Línea """

''' Comentarios de 
Múltiple Línea '''

# CTRL + L //Limpiar Pantalla
# CTRL + SHIFT + L //Limpiar Pantalla

# exit() //Para salir de la consola de Python

# import os // Librería del clear, se coloca al principio del .py
# os.system('clear') //Nos permite limpiar la consola en Python

#Para ejecutar un archivo.py hay que situarse en la carpeta donde esta ubicado el archivo y ejecutar en Terminal: python nombredelarchivo.py

#Python distingue mayúsculas de minúsculas, Hola es un identificador y hola es otro identificador

#Se usa el punto decimal (.) en lugar de coma (,) para representar valores no enteros, es la notación que utiliza Python

##### Palabras Reservadas en Python #####

and        del       from     not      while
as         elif      global   or       with
assert     else      if       pass     yield
break      except    import   print
class      exec      in       raise
continue   finally   is       return
def        for       lambda   try


##### Expresiones booleanas de comparación en Python #####

Expresión  ---  Significado

a == b          a es igual a b

a != b          a es distinto de b

a < b           a es menor que b

a <= b          a es menor o igual que b

a > b           a es mayor que b

a >= b          a es mayor o igual que b

Ejemplos:

6==6
True

6!=6
False

6>6
False

6>=6
True

6>4
True

6<4
False

6<=4
False

4<6
True

##############################
##### OPERADORES LÓGICOS #####
##############################

Expresión --- Significado

a and b   --- El resultado es True solamente si a es True y b es True de lo contrario el resultado es False
a or b    --- El resultado es True si a es True o b es True de lo contrario el resultado es False
not a     --- El resultado es True si a es False de lo contrario el resultado es False

Ejemplos:
>>> 5>2 and 5>3
True
>>> 5>2 and 5>6
False

>>> 5>2 or 5>3
True
>>> 5>2 or 5>6
True
>>> 5>8 or 5>6
False

>>> 5>8
False
>>> not (5>8)
True
>>> 5>2
True
>>> not (5>2)
False

##################################
##### OPERCIONES MATEMÁTICAS #####
##################################

# Python permite utilizar las operaciones  +  -  *  /  (división entera) y ** (potenciación)

5*7
35

2+3*7
23

(2+3)*7
35

10/5
2

5**2
25

a = 26
b = 11.3
c = 5
d = 3.5

# SUMA
print a + b
37.3

# RESTA
print c - a
-21

# MULTIPLICACION
print d * c
17.5

# EXPONENTE
print c ** 2
25

# DIVISION
#El resultado sera un entero
#Asi los datos tengan decimales y el resultado real tenga decimales Ejemplo: 0.1923
#Toma unicamente la parte izquerda del punto decimal 
print c / a
0

# DIVISION
#Convierte lo que esta en parentesis a flotante o real
print float(c) / a
0.192307692308

# DIVISION ENTERA 
print 7 / 2
3

# MODULO
print 7%3

# += Suma un valor al valor de la variable y asigna el nuevo valor producto de la suma a la variable
x = 3
x += 2
print x
5

# -= Resta un valor al valor de la variable y asigna el nuevo valor producto de la resta a la variable
x = 10
x -= 2
print x
8

# *= Multiplica un valor por el valor de la variable y asigna el nuevo valor producto de la multiplicación a la variable
x = 10
print x
x *= 2
print x

# /= Divide un valor entre el valor de la variable y asigna el nuevo valor producto de la multiplicación a la variable
x = 10
print x
x /= 2
print x

######################
##### VARIABLES ######
######################

a = 2 # Declaramos (a) y le asignamos un valor (INT) entero

a = 2L # La (L) al final significa que sera variable de tipo LONG, numeros muy grandes que ocupan mas memoria del sistema

a = "casa" # Declaramos (a) y le asignamos una cadena de caracteres

print a # Imprime el valor de (a)
a #Imprime el valor de (a) directamente, si esta cargada 

#################
##### print #####
#################

#Imprimer por pantalla el contenido entre las comillas simples o dobles: ('') o ("")

print 'Troya es madre de todos, peleen por ella' # Comillas Simples
Troya es madre de todos, peleen por ella

print 'La ciencia exacta no es una ciencia exacta' # Comillas Simples
La ciencia exacta no es una ciencia exacta

print "Anote su metodo Mr Borden, describalo por completo" # Comillas Dobles
Anote su metodo Mr Borden, describalo por completo

print "Hola como estan" # Comillas Dobles
Hola como estan

print "Hola \ncomo estan" # \n Permite hacer un salto de linea dentro de la cadena
Hola
como estan

print "Hola \t como estan" # \t Permite hacer una tabulacion
Hola      como estan

print "Hola \n\tcomo estan" # \n\t Salto de Linea y tabulacion al mismo tiempo
Hola 
    como estan

print""" 
Linea 1
Linea 2
Linea 3
Linea 4
"""
#Imprime el texto entre las triples comillas respetando saltos de linea y tabulaciones 

Linea 1
Linea 2
Linea 3
Linea 4

###################
##### Función #####
###################

def funcion(): #Declaramos el nombre de la Función
    print "Esto es una funcion" #Contenido de la Función
    print "Rictusempra y Sectusempra" #Contenido de la Función

funcion() #Invocación de la Función

##################################
##### Función con parámetros #####
##################################

#---Función con un parámetro:
def funcion(alguien): #Podemos pasar un parametro a la función
    print "Hola",alguien,"!" 
funcion("Argenis") #Llamamos la función y le pasamos una cadena como parámetro 

#---Función con mas de un parámetro:
def funcion(nombre,apellido):
    print "Hola",nombre,apellido,"!" 
funcion("Argenis","Osorio")

# Simulando que recibe el id y username
def funcion(id,username):
    print "id:",id,"username:",username
funcion(1,"admin")

#---Función de suma con declaración de variables:
def prueba(): 
    num = 1
    num2 = 2 
    suma = num+num2
    print"La suma es",suma
prueba()

#---otro Ejemplo:
def prueba(): 
    num = 10
    print num * 3 #El resultado es 30
prueba()

#---otro Ejemplo:
def prueba(): 
    x = [1, 2, 3, 4]
    print x #Imprime: [1, 2, 3, 4]
prueba()

# Imprimiento un elemento de la lista
def prueba(): 
    x = [1, 2, 3, 4]
    #print x #Imprime: [1, 2, 3, 4]
    print x[2]
prueba()
    
#---Ejemplo de Función Matemática:
def cuadrado(num): #Calcula el cuadrado de un número dado
    print num*num

cuadrado(5) #Para invocarala y darle el valor a calcular (5 por ejemplo)

#---Otro ejemplo de Función Matemática:
def cuadrado2(): #Creamos una nueva función
    n = input("Ingrese un número: ") #Pedira al usuario que introduzca un número
    cuadrado(n) #Pasara el valor introducido a la funcion matematica declarada anteriormente (Cuadrado de un número)

cuadrado2() #Ejecutara la función, nos pedira un numero, realizara los calculos y mostrara el resultado

#Usando las dos funciones
def cuadrado(num): #Calcula el cuadrado de un número dado
    print num*num

def cuadrado2(): #Creamos una nueva función
    n = input("Ingrese un número: ") #Pedira al usuario que introduzca un número
    cuadrado(n) #Pasara el valor introducido a la funcion matematica declarada anteriormente (Cuadrado de un número)

cuadrado2()

-----

#---EJEMPLO de Función y Cálculo

# input : Devuelve el valor ingresado por teclado tal como se lo digita (en particular sirve para ingresar valores numéricos)

# raw_input : Devuelve lo ingresado por teclado como si fuera un texto.

#Este programa convierte millas, pies , pulgadas y kilometros a metros
def main():
    print "Este programa convierte millas, pies, pulgadas y kilometros a metros"
    millas = input("Cuantas millas?: ")
    pies = input("Cuantos pies?: ")
    pulgadas = input("Cuantas pulgadas?: ")
    km = input("Cuantas kilometros?: ")
        metros = 1609.344 * millas
    metros2 = 0.3048 * pies
    metros3 = 0.0254 * pulgadas 
    metros4 = 1000 * km    
    print millas, "millas son:",metros,"metros"
    print pies, "pies son:",metros2,"metros"
    print pulgadas, "pulgadas son:",metros3,"metros"
    print km, "kilometros son:",metros4,"metros"
main()

-----

#Llevar horas a minutos y segundos
def funcion ():
    print "Llevar horas a minutos y segundos"
    horas = input("Cantidad de horas: ")
    minutos = 60 * horas 
    segundos = 3600 * horas 
    print horas, "horas " "son", minutos, "minutos"
    print horas, "horas " "son", segundos, "Segundos"
funcion()

-----

# -*- coding: utf-8 -*-
"""
Función random para generar un número
aleatorio dentro de un rango.
"""
import random
for x in range(1):
    print random.randint(1,4)

#########################
##### CONCATENACIÓN #####
#########################

print "Un divertido "+"programa "+"de "+ "radio"
Un divertido programa de radio

#Multiplicando cadenas
print 3 * "programas "
programas programas programas 

#Ejemplo
def prueba():
    nombre="Christopher"
    print nombre+" Robinson" #Imprime: Christopher Robinson
    print nombre * 3 #Imprime: #Imprime: ChristopherChristopherChristopher
prueba()

#Otro Ejemplo
def prueba(): 
    nom = raw_input ("Ingrese un Nombre: ") #Nos pedirá un Nombre
    ape = raw_input ("Ingrese un apellido: ") #Nos pedirá un Apellido

    print "El nombre completo es",nom,ape,"!" #Imprime: El nombre completo es Argenis Osorio !
    print "El nombre completo es",nom+ape,"!" #Imprime: El nombre completo es ArgenisOsorio !
prueba()

###############
##### FOR #####
###############

# -*- coding: utf-8 -*-
def prueba(): 
    n1 = 0
    n2 = 10
    for x in range(n1, n2):
        print x #Imprime números del 0 hasta el 1 usando el cilco repetitivo
        #print x+x
prueba()

----

#---Secuencia a mano
def prueba(): 
    for x in [1, 3, 9, 27]:
        print x #Imprimirá los los números 1, 3, 9 y 27
prueba()

----

"""
Imprimir un numero x cantidad de veces
"""
# -*- coding: utf-8 -*-
def prueba():
    for i in range(5):
        print("1")
prueba()

----

"""
Imprimir un numero x cantidad de veces
"""
# -*- coding: utf-8 -*-
def prueba(): 
    n1 = 0
    n2 = 9000
    for x in range(n1, n2):
        print x #Imprime números del 0 hasta el 900 usando el cilco repetitivo
        #print x+x
prueba()

##############
##### IF #####
##############

#Introducir la nota, el programa calcula si APROBO o SUSPENDIO XD
nota = input ("Escriba la nota: ")

if nota == 1:
    print "*****Cambiese de carrera*****"
if nota < 10:
    print "*****SUPENDIO! bruto*****"
if nota == 10:
    print "*****APROBO! DE LECHE*****"
if nota > 10:
    print "*****APROBO! parece que chuleteandose*****"
if nota == 20:
    print "*****NO INVENTE! que usted nunca ha sacado 20*****"

###################
##### IF ELSE #####
###################

usuario = raw_input ("USUARIO: ")
if usuario == "canaima":
    print "*****ACCESO CONCEDIDO*****"
else:
    print "*****ACCESO DENEGADO*****"

#---Con números
password = input ("CONTRASENA: ")

if password == 123:
    print "*****ACCESO CONCEDIDO*****"
else:
    print "*****USUARIO DENEGADO*****"

#---Con (not) negacion
x = input("Ingrese un numero: ")
if x > 0:
    print "Numero positivo"
if not (x > 0):
    print "Numero no positivo"

################
##### ELIF #####
################

x = input("Ingrese un numero: ")
if x > 0:
    print "Numero positivo"
elif x == 0:
    print "Igual a 0"
else:
    print "Numero negativo"

#---Con (for) 
i = input("Cuantos numeros quiere procesar?: ")
for j in range(0,i):
    x = input("Ingrese un numero: ")
    if x > 0:
             print "Numero positivo"
    elif x == 0:
             print "Igual a 0"
    else:
        print "Numero negativo"

#################
##### WHILE #####
#################

numero = input("Escriba un numero negativo: ")
while numero > 0:
    print "Ha escrito un numero positivo! Intentelo de nuevo"
    numero = input("Escriba un numero negativo: ")
print "Gracias por su colaboracion"

#---Otro Ejemplo
Datos = "Si"
while Datos == "Si":
    x = input("Ingrese un numero: ")
    if x > 0:
        print "Numero positivo"
    elif x == 0:
        print "Igual a 0"
    else:
        print "Numero negativo"
    Datos = input("Quiere seguir? S o N: ")

#---Ciclo con Centinela
#Uso de un valor distinguido Ejemplo (*) si se lee, le indica al programa que el usuario desea salir del ciclo
x = input ("Ingrese un numero ("*" para terminar): ")
while x <> "*":
        if x > 0:
            print "Numero positivo"
        elif x == 0:
            print "Igual a 0"
        else:
            print "Numero negativo"    
    x = input ("Ingrese un numero ("*" para terminar): ")

#---Usando break para salir del ciclo
while True:
    x = input("Ingrese un numero '*' para terminar: ")
        if x == '*':
            break
        elif x > 0:
            print "Numero positivo"
        elif x == 0:
            print "Igual a 0"
        else:
        print "Numero negativo"

##################
##### Listas #####
##################

'''
La lista es un tipo de datos versátil disponible en Python, que puede escribirse
como una lista de valores separados por comas (cosas) entre corchetes.
Lo importante de una lista es que los elementos de una lista
no tienen por qué ser del mismo tipo.
'''

lista = [2,"tres",True,["uno",10]] #Cada elemento de la lista contiene un indice, desde el 0,1,2...
print lista

----

#Imprimiendo los elementos de la lista
lista = ["Proyecto1","Proyecto2","Proyecto3",["David","Usain"]]
print lista[0]
print lista[1]
print lista[2]
print lista[3][0]#Accedemos al elemento de la posición tres e imprimimos el subelemento de la posicion 0
print lista[3][1]#Accedemos al elemento de la posición tres e imprimimos el subelemento de la posicion 1

----

lista = ["Proyecto1","Proyecto2","Proyecto3",["David","Usain"]]
lista [1] = 4 #cambiar el valor del elemento en la posicion 1 por un entero
lista [1] = "casa" #cambiar el valor del elemento en la posicion 1 por una cadena
print lista

----

lista = ["casa","carro","perro","gato","ventana","puerta"] #Nueva lista
lista2 = lista[0:3] #Imprmir elementos desde la lista desde el 0 hasta la posicion 3
print lista2

----

lista = ["casa","carro","perro","gato","ventana","puerta"]
lista[0:1] = 5,6 #Sustituir valores en las posiciones
print lista

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
lista = [1,"Dos",3]
buscar = 1
print buscar in lista #Se traduciría como: ¿Buscar esta en la lista?
#Nos devolvería un True porque si está ese valor en la lista

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Obtener el índice de un elemento de la lista
lista = [1,"Dos",3]
buscar = 1
print lista.index(buscar) #Obtener el índice de un elemento de la lista

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Buscando elementos en una lista
lista = [1,"Dos",3]
buscar = "Dos"
if buscar in lista: #Buscar el eleménto en la lista
    print lista.index(buscar) #Mostrar el índice del elemento
else:
    print "No esta el elemento" #Notificar si el elemento no existe

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Agregando un nuevo elemento a la lista
lista = [1,"Dos",3]
print lista
lista.append("Nuevo elemento") #Agregamos un nuevo elemento a la lista
print lista

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Contar el numero de elementos presentes en una lista
lista = [1,"Dos",3,4,"Cinco",3]
print lista.count(3) #Buscar y contar cuantas veces está un elemento en la lista.

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Insertando un nuevo elemento en la lista
lista = [1,"Dos",3,4,"Cinco",3]
print lista
lista.insert(2,"Nuevo") #Insertamos un nuevo elemento en la lista, en este caso insertamos la cadena "Nuevo" en la posición 2, pero no sustituye, solo se inserta, el resto de valores se corren ascendentemente.
print lista

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Juntar dos listas
lista = [1,2,3]
print lista
lista2 = [5,6,7]
lista.extend(lista2) #Método extend, juntar dos listas, podemos agregar una nueva lista al final de primera lista
print lista

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Extraer y eliminar un elemento de la lista
lista = [1,2,3]
print lista
lista.pop() #Elimina el último elemento de la lista si no especificamos un indice que borrar
print lista

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Extraer y eliminar un elemento de la lista, indicando la posición
lista = [1,2,3]
print lista
lista.pop(1) #Eliminamos el elemento que está en la posición 1 de la lista
print lista

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Método reverse, que invierte los elementos de la lista
lista = [1,2,3]
print lista
lista.reverse()
print lista

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Agregar elementos al final de una lista.
"""
alist = [123, 'xyz', 'zara', 'abc'];
print alist
alist.append( 2009 );
print alist

###########################
##### VARIABLE GLOBAL #####
###########################

a = 5

def function():
    global a
    a = 42
    print a

def function2():
    print myglobal


print a
function()
#function2()

##################
##### Tuplas #####
##################

Una tupla es una secuencia de objetos de Python.
Las tuplas son secuencias, al igual que las listas.
Las diferencias entre tuplas y las listas son, las tuplas
no se pueden actualizar a diferencia de las listas y las
tuplas utilizan paréntesis, mientras que las listas utilizan corchetes.

# Imprimiendo el contenido de una tupla
tupla = (1,True,"hola")
print tupla

# Imprimiendo el contenido de una tupla, posición a posición.
tupla = (1,True,"hola")
print tupla[0]
print tupla[1]
print tupla[2]

########################
##### Diccionarios #####
########################

Los diccionarios en Python son un tipo de estructuras de datos que permite guardar un conjunto
no ordenado de pares clave-valor, siendo las claves únicas dentro de un mismo diccionario
(es decir que no pueden existir dos elementos con una misma clave).
Los diccionarios son estructuras de datos muy extendidos en otros lenguajes de programación.

# -*- coding: utf-8 -*-
#Imprimiendo el contenido del diccionario
diccionario = {
    'Clave1':[
        1,2,3
    ],
    'Clave2':True
}
print diccionario

----

# -*- coding: utf-8 -*-
#Imprimiendo el contenido del diccionario, accedemos a los valores a través de la clave
diccionario = {
    'Clave1':[
        1,2,3
    ],
    'Clave2':True
}
print diccionario['Clave1']
print diccionario['Clave2']

----

# -*- coding: utf-8 -*-
#Imprimiendo el contenido del diccionario, accedemos a los valores a través de la clave
diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript']}
print diccionario['nombre']
print diccionario['edad']
print diccionario['cursos']

----

# -*- coding: utf-8 -*-
#Imprimiendo el contenido del diccionario, accedemos a los valores a través de la clave que puede
#cualquier tipo de dato, una cadena, un entero, etc, pero no listas ni diccionarios
diccionario = {
    'Clave1':[
        1,2,3
    ],
    'Clave2':True,
    4:"numero"
}
print diccionario['Clave1']
print diccionario['Clave2']
print diccionario[4]

----

# -*- coding: utf-8 -*-
# Imprimir datos de un diccionario por posición
data = {
    "usuarios": [
        {
            "username":"admin",
            "password":123456
        },
        {
            "username":"admin1",
            "password":12345678
        },
    ]
}
print data["usuarios"]
print data["usuarios"][0]["username"]
print data["usuarios"][0]["password"]
print data["usuarios"][1]["username"]
print data["usuarios"][1]["password"]

----

# -*- coding: utf-8 -*-
#Imprimiendo el contenido del diccionario, accedemos a los valores a través de la clave y de los índices:
diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript']}
print diccionario['cursos'][0]
print diccionario['cursos'][1]
print diccionario['cursos'][2]

----

# -*- coding: utf-8 -*-
# Imprimir datos de un diccionario por posición
data = {
  "Fruteria":[
    {
      "Fruta":[
        {
          "Nombre":"Manzana","Cantidad":10
          },
          {
            "Nombre":"Pera","Cantidad":20
          },
          {
            "Nombre":"Naranja","Cantidad":30
          }
      ]
    },
    {
      "Verdura":[
        {
          "Nombre":"Lechuga","Cantidad":80
        },
        {
          "Nombre":"Tomate","Cantidad":15
        },
        {
          "Nombre":"Pepino","Cantidad":50
        }
      ]
    }
  ]
}
print data["Fruteria"][0]["Fruta"][0]["Cantidad"]
print data["Fruteria"][0]["Fruta"][1]["Cantidad"]
print data["Fruteria"][0]["Fruta"][2]["Cantidad"]
print "---"
print data["Fruteria"][0]["Fruta"][0]["Nombre"]
print data["Fruteria"][0]["Fruta"][1]["Nombre"]
print data["Fruteria"][0]["Fruta"][2]["Nombre"]
print "---"
print data["Fruteria"][1]["Verdura"][0]["Cantidad"]
print data["Fruteria"][1]["Verdura"][1]["Cantidad"]
print data["Fruteria"][1]["Verdura"][2]["Cantidad"]

----

# -*- coding: utf-8 -*-
# Recorrer el Diccionario, haciendo uso de la estructura for
diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript']}
for key in diccionario:
  print key, ":", diccionario[key]

----

# -*- coding: utf-8 -*-
"""
Insertando datos en un diccionario.
"""
persona = {}
print persona
print "----"
persona['Nombre'] = 'José'
print persona
persona['Apellido'] = 'Carlos'
print "----"
print persona

----

# -*- coding: utf-8 -*-
"""
Insertando datos en un diccionario y borrando elementos mediante la clave.
"""
persona = {}
print persona
print "----"
persona['Nombre'] = 'José'
print persona
persona['Apellido'] = 'Carlos'
print "----"
print persona
print "----"
del persona['Apellido']
print persona

-----

# -*- coding: utf-8 -*-
"""
Actualizar el valor de uno de los elementos del diccionario,
accedemos y actualizamos mediante la clave.
"""
inventario = {"manzanas":10,"bananas":15,"naranjas":20}
print inventario
inventario["naranjas"]=25
print inventario

-----

# -*- coding: utf-8 -*-
"""
Removiendo un valor usando el metodo remove de las listas
"""
dic = {"hola":"mundo", 3:"tres","nombre":["luis","arturo","carlos"]}
print dic
dic["nombre"].remove("carlos")
print dic

##### Métodos de los Diccionarios #####

# -*- coding: utf-8 -*-
# dict() Recibe como parámetro una representación de un diccionario y si es factible, devuelve un diccionario de datos.
dic =  dict(nombre='nestor', apellido='Plasencia', edad=22)
print dic

----

# -*- coding: utf-8 -*-
"""
zip() Recibe como parámetro dos elementos iterables, ya sea una cadena, una lista o una tupla.
Ambos parámetros deben tener el mismo número de elementos. Se devolverá un diccionario
relacionando el elemento i-esimo de cada uno de los iterables.
"""
dic = dict(zip('abcd',[1,2,3,4]))
print dic

----

# -*- coding: utf-8 -*-
"""
items() Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero
será la clave y el segundo, su valor.
"""
dic =  {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
items = dic.items()
print items

----

# -*- coding: utf-8 -*-
# keys() Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.
dic =  {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
keys = dic.keys()
print keys

----

# -*- coding: utf-8 -*-
# values() Retorna una lista de elementos, que serán los valores de nuestro diccionario.
dic =  {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
values = dic.values()
print values

----

# -*- coding: utf-8 -*-
# clear() Elimina todos los ítems del diccionario dejándolo vacío.
dic =  {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
print dic
dic.clear()
print dic

----

# -*- coding: utf-8 -*-
# copy() Retorna una copia del diccionario original.
dic = {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
dic1 = dic.copy()
print dic1

----

# -*- coding: utf-8 -*-
"""
fromkeys() Recibe como parámetros un iterable y un valor, devolviendo un diccionario
que contiene como claves los elementos del iterable con el mismo valor ingresado.
Si el valor no es ingresado, devolverá none para todas las claves.
"""
dic = dict.fromkeys(['a','b','c','d'],1)
print dic

----

# -*- coding: utf-8 -*-
"""
get() Recibe como parámetro una clave, devuelve el valor de la clave.
Si no lo encuentra, devuelve un objeto none.
"""
dic = {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
valor = dic.get('b')
print valor
valor = dic.get('h')
print valor

----

# -*- coding: utf-8 -*-
"""
pop() Recibe como parámetro una clave, devuelve su valor y elimina esta clave y valor.
Si no lo encuentra, devuelve error.
"""
dic = {'a':1,'b':2,'c':3}
print dic
valor = dic.pop('b')
print valor
print dic

----

# -*- coding: utf-8 -*-
"""
setdefault() Funciona de dos formas. En la primera como get
"""
dic = {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
valor = dic.setdefault('a')
print valor
"""
Y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.
"""
dic2 = {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
print dic2
valor = dic2.setdefault('e',5)
print dic2

----

# -*- coding: utf-8 -*-
"""
update() Recibe como parámetro otro diccionario. Si se tienen claves iguales,
actualiza el valor de la clave repetida; si no hay claves iguales, este par clave-valor
es agregado al diccionario.
"""
dic1 = {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
print dic1
dic2 = {'c' : 6, 'b' : 5, 'e' : 9 , 'f' : 10}
dic1.update(dic2)
print dic1

##########################
##### Manejando json #####
##########################

JSON es una notación de objetos, utiliza una sintaxis que nos permite crear objetos de
manera rapida y simple, estos objetos pueden ser utilizados de la manera que queramos y la notación se
utiliza muy comúnmente para crear servicios REST, objetos, e incluso fue adoptada por algunas bases de
datos como lo es MongoDB.

Básicamente es un diccionario de python que guarda objetos.

Para escribir JSON debemos tener en cuenta lo siguiente:
La creación de los objetos JSON implica escribir datos, para ello:

-Los objetos JSON estan rodeados por llaves “{}”
-Los datos estan separados por comas.
-Los datos se escriban en pares, siendo primero el nombre o atributo del mismo y luego el valor del dato.
-Llaves cuadradas [] guardan arreglos, incluyendo otros objetos JSON

El formato JSON tiene la siguiente notación:

{key : value, key2 : value2, key3 : value3,...}

Y también puede ser serializado y multidimensional, por ejemplo:

[{key : value, key2 : value2, key3 : value3, key : { key : value, key2 : value2, key3 : value3} },{key : value, key2 : value2, key3 : value3,...}]

Ejemplo de un objeto JSON que guarda un usuario y password:

# -*- coding: utf-8 -*-
# Imprimir datos de un diccionario
data = {"usuarios":[{"username":"admin","password":123456}]}
print data["usuarios"]
print data

----

# -*- coding: utf-8 -*-
# Imprimir datos de un diccionario
import json
data = {"Fruteria":[{"Fruta":[{"Nombre":"Manzana","Cantidad":10},{"Nombre":"Pera","Cantidad":20}]}]}
print data
print "-----"
#Nos devuelve el string con el JSON
data_string = json.dumps(data)
print data_string

---

# -*- coding: utf-8 -*-
# Decodificar JSON
# Para decodificar un JSON a vamos a hacer uso de la función json_loads(String)
import json
data = {"Fruteria":[{"Fruta":[{"Nombre":"Manzana","Cantidad":10},{"Nombre":"Pera","Cantidad":20}]}]}
data_string = json.dumps(data)
print 'ENCODED:', data_string
decoded = json.loads(data_string)
print 'DECODED:', decoded

---

# -*- coding: utf-8 -*-
# Decodificar JSON
# Imprimir valores del json, por posíción
import json
data = {
  "Fruteria":[
    {
      "Fruta":[
        {
          "Nombre":"Manzana","Cantidad":10
          },
          {
            "Nombre":"Pera","Cantidad":20
          },
          {
            "Nombre":"Naranja","Cantidad":30
          }
      ]
    },
    {
      "Verdura":[
        {
          "Nombre":"Lechuga","Cantidad":80
        },
        {
          "Nombre":"Tomate","Cantidad":15
        },
        {
          "Nombre":"Pepino","Cantidad":50
        }
      ]
    }
  ]
}
#encoded
data_string = json.dumps(data)
#Decoded
decoded = json.loads(data_string)
print "Tenemos "+str(decoded["Fruteria"][0]["Fruta"][0]["Cantidad"])+" Manzanas"
print "Tenemos "+str(decoded["Fruteria"][0]["Fruta"][1]["Cantidad"])+" Peras"
print "Tenemos "+str(decoded["Fruteria"][0]["Fruta"][2]["Cantidad"])+" Naranjas"
print "Tenemos "+str(decoded["Fruteria"][1]["Verdura"][0]["Cantidad"])+" Lechugas"
print "Tenemos "+str(decoded["Fruteria"][1]["Verdura"][1]["Cantidad"])+" Tomates"
print "Tenemos "+str(decoded["Fruteria"][1]["Verdura"][2]["Cantidad"])+" Pepino"

---

# -*- coding: utf-8 -*-
# Decodificar JSON
# Imprimir valores del json, por posíción
import json
data = {
  "Fruteria":[
    {
      "Fruta":[
        {
          "Nombre":"Manzana","Cantidad":10
          },
          {
            "Nombre":"Pera","Cantidad":20
          },
          {
            "Nombre":"Naranja","Cantidad":30
          }
      ]
    },
    {
      "Verdura":[
        {
          "Nombre":"Lechuga","Cantidad":80
        },
        {
          "Nombre":"Tomate","Cantidad":15
        },
        {
          "Nombre":"Pepino","Cantidad":50
        }
      ]
    }
  ]
}
# Mostrando la data completa
print "*****Data total*****"
print data

# Mostrando la data del primer hijo
print "*****Data Frutas*****"
print data['Fruteria'][0]

# Mostrando la data del segundo hijo
print "*****Data Verduras*****"
print data['Fruteria'][1]

---

# -*- coding: utf-8 -*-
# Decodificar JSON
# Imprimir valores del json, por posíción, accediendo al último nivel
import json
data = {
  "Fruteria":[
    {
      "Fruta":[
        {
          "Nombre":"Manzana","Cantidad":10
          },
          {
            "Nombre":"Pera","Cantidad":20
          },
          {
            "Nombre":"Naranja","Cantidad":30
          }
      ]
    },
    {
      "Verdura":[
        {
          "Nombre":"Lechuga","Cantidad":80
        },
        {
          "Nombre":"Tomate","Cantidad":15
        },
        {
          "Nombre":"Pepino","Cantidad":50
        }
      ]
    }
  ]
}
# Mostrando la data completa
print "*****Data total*****"
print data

# Mostrando la data del primer hijo
print "*****Data Frutas*****"
print data['Fruteria'][0]

# Mostrando la data del segundo hijo
print "*****Data Verduras*****"
print data['Fruteria'][1]

# Mostrando la data de los elementos de Frutas
print "*****Data de elementos de Frutas *****"
print data['Fruteria'][0]["Fruta"][0]["Nombre"]
print data['Fruteria'][0]["Fruta"][0]["Cantidad"]
print data['Fruteria'][0]["Fruta"][1]["Nombre"]
print data['Fruteria'][0]["Fruta"][1]["Cantidad"]
print data['Fruteria'][0]["Fruta"][2]["Nombre"]
print data['Fruteria'][0]["Fruta"][2]["Cantidad"]

# Mostrando la data de los elementos de Verduras
print "*****Data de elementos de Verduras *****"
print data['Fruteria'][1]["Verdura"][0]["Nombre"]
print data['Fruteria'][1]["Verdura"][0]["Cantidad"]
print data['Fruteria'][1]["Verdura"][1]["Nombre"]
print data['Fruteria'][1]["Verdura"][1]["Cantidad"]
print data['Fruteria'][1]["Verdura"][2]["Nombre"]
print data['Fruteria'][1]["Verdura"][2]["Cantidad"]

##################
##### Clases #####
##################

En la vida cotidiana, conocemos los objetos, como una carro, una botella, una perdona, etc.
Esos objetos poseen ciertas caracteristicas, esas características, en programación orientada a objetos
las llamámos atributos del objeto, y a las acciones que puede realizar el objeto se conocen como métodos.
Podriamos crear un objeto llamado Humano, y sus atributos serian, la edad, estatura, nombre, cedula, nacionalidad
Y sus métodos serían, caminar, correr, levantarse, etc.
Una clase es una plantilla del cual proviene nuestro objeto, en ella establecemos los atributos y métodos que tendra un objeto.

¿Que es self?
Self es simplemente el nombre convencional para el primer argumento de un método en Python.
Por ejemplo, un método definido de la forma meth(self, a, b, c) debe ser llamado
con x.meth(a, b, c), por alguna instancia de la clase x, en la cual ocurre la definición;
de esta forma el método llamado pensara que es llamado como meth(x, a, b, c)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Definimos una clase, por convención se usa la primera letra en mayúscula
class Humano:
    def __init__(self): #Definimos un método, es una función pero cuando está dentro de una clase es un método, éste método init python lo reconoce, cuando se cree un nuevo objeto, automáticamente se va a ejecutar este método. En la variable self se va a guardar la referencia al objeto que estemos creando
        print "Soy un nuevo objeto"

pedro = Humano() #Creamos un objeto que tiene como plantilla la clase Humano

#********************
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Definimos una clase, por convención se usa la primera letra en mayúscula
class Humano:
    def __init__(self): #Definimos un método, es una función pero cuando está dentro de una clase es un método, éste método init python lo reconoce, cuando se cree un nuevo objeto, automáticamente se va a ejecutar este método. En la variable self se va a guardar la referencia al objeto que estemos creando
        print "Soy un nuevo objeto"

    def hablar(self,mensaje):
        print mensaje

pedro = Humano() #Creamos el objeto
raul = Humano() #Creamos el objeto
pedro.hablar('Hola') #Le pasamos valores por parametro que recibirá el método
raul.hablar('Hola, Pedro') #Le pasamos valores por parametro que recibirá el método

#********************
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Humano:
    def __init__(self):
        self.edad = 25 #Agregamos un atributo, cada objeto que cree a partir de esta clase, tendra ese atributo
        print "Soy un nuevo objeto"

    def hablar(self,mensaje):
        print mensaje

pedro = Humano() #Creamos el objeto
print "Soy Pedro y tengo", pedro.edad

#********************
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Humano:
    def __init__(self,edad):#Agregamos la variable edad
        self.edad = edad #Tenemos el atributo edad y le asignamos la variable edad que recibiremos como argumento del método

    def hablar(self,mensaje):
        print mensaje

pedro = Humano(26) #Enviamos por parámetro el valor que será recibido por el método, ya que está declarado el argumento edad junto a self
raul = Humano(21) #Enviamos por parámetro el valor que será recibido por el método, ya que está declarado el argumento edad junto a self
print "Soy Pedro y tengo", pedro.edad
print "Soy Raul y tengo", raul.edad

####################
##### Herencia #####
####################

#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Humano:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print self.edad
        print mensaje

class IngSistemas(Humano): #Subclase que hereda de la Superclase, la subclase heredara todos los atributos y métodos de la Superclase
    def programar(self,lenguaje):
        print 'Voy a programar en ', lenguaje

class LicDerecho(Humano):
    def estudiarCaso(self,de):
        print 'Debo estudiar el caso de ', de

pedro = IngSistemas(26) #Objeto creado con la clase IngSistemas pero usa el método de la Superclase Humano
raul = LicDerecho(27) #Objeto creado con la clase IngSistemas pero usa el método de la Superclase Humano
print "Soy Pedro y tengo", pedro.edad
print "Soy Raul y tengo", raul.edad
pedro.hablar('Hola')
raul.hablar('Hola, Pedro')

#Usando el método programar y enviando valores al argumento que necesita
#Usando el método estudiarCaso y enviando valores al argumento que necesita
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Humano:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print mensaje

class IngSistemas(Humano):
    def programar(self,lenguaje):
        print 'Voy a programar en ', lenguaje

class LicDerecho(Humano):
    def estudiarCaso(self,de):
        print 'Debo estudiar el caso de ', de

pedro = IngSistemas(26)
raul = LicDerecho(27)
pedro.hablar('Hola')
raul.hablar('Hola, Pedro')
pedro.programar('Python') #Usando el método programar y enviando valores al argumento que necesita
raul.estudiarCaso('Pedro')

#Definimos el método init que sobrescribira al método heredado de Humano, cuando el objeto use el metodo init usará el suyo y no el heredado.
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Humano:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print mensaje

class IngSistemas(Humano):
    def __init__(self): #Definimos el método init que sobrescribira al método heredado de Humano, cuando el objeto use el metodo init usará el suyo y no el heredado
        print 'Hola'

    def programar(self,lenguaje):
        print 'Voy a programar en ', lenguaje

class LicDerecho(Humano):
    def estudiarCaso(self,de):
        print 'Debo estudiar el caso de ', de

pedro = IngSistemas()
raul = LicDerecho(27)
pedro.hablar('Hola')
raul.hablar('Hola, Pedro')
pedro.programar('Python')
raul.estudiarCaso('Pedro')

#############################
##### Herencia multiple #####
#############################

#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Humano:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print mensaje

class IngSistemas(Humano):
    def __init__(self):
        print 'Hola'

    def programar(self,lenguaje):
        print 'Voy a programar en ', lenguaje

class LicDerecho(Humano):
    def estudiarCaso(self,de):
        print 'Debo estudiar el caso de ', de

class Estudioso(IngSistemas,LicDerecho): #Hereda de dos clases
    pass #Palabra reservada, interpretada como vete! no hay nada que ver aquí. Cuando creamos una clase, forzosamente debe de existir un método y si no existe, usamos pass, en este ejemplo ya está heredando los métodos de otras clases

pepe = Estudioso() #Creamos el objeto
pepe.hablar('Hola, soy de herencia multiple') #Usando el método heredado de Humano, ya que la clase Estudioso hereda de IngSistemas y de LicDerecho, que a su vez heredan de Humano
pepe.programar('C++') #Usando el método programar heredado
pepe.estudiarCaso('Juan') #Usando el estudiarCaso heredado

###################
##### Métodos #####
###################

##### len() #####

# -*- coding: utf-8 -*-
#El método len() devuelve el número de elementos de la lista, una variable, etc.
a = "casa"
print len(a)

# -*- coding: utf-8 -*-
#El método len() devuelve el número de elementos de la lista, una variable, etc.
lista = ["Proyecto1","Proyecto2","Proyecto3"]
print lista
print len(lista)

# -*- coding: utf-8 -*-
#Otro Ejemplo
list1, list2 = [123, 'xyz', 'zara'], [456, 'abc']
print "First list length : ", len(list1)
print "Second list length : ", len(list2)

########################################################
##### Usando APIs con el Modulo Requests de Python #####
########################################################

#Requests es una librería para HTTP

Para este ejemplo aclaremos:

Github y Stackoverflow proporcionan su API para extraer diversos tipos de datos.

La documentación de la API de Github y StackOverflow se puede encontrar aquí.
Github: https://developer.github.com/v3/
StackOverflow: http://api.stackexchange.com/docs 

Pero ¿qué es lo que usamos para comunicarse con estas API?
Trabajar con HTTP es una tarea dolorosa. Python incluye un módulo llamado urllib2 pero trabajar con él puede llegar a ser engorroso.

### Solicitudes HTTP ###

Instalamos el paquete python-requests para hacer solicitudes HTTP

# apt-get install python-requests

Creamos y guardamos el fichero postrequest.py con el siguiente contenido:

#----- begin
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
r = requests.get('https://api.github.com', auth=('username', '123456'))
print r.status_code
print r.headers['content-type']
#----- end

Contiene la llamada a la librería instalada "import requests", creamos una variable "r"
y le asignames una solicitud GET a la api de logeo de github, donde le pasaremos el nombre de usuario y la contraseña, al ejecutarlo
nos dara una respuesta gracias a los print que declaramos, hora de probarlo:

$ python postrequest.py

#Si el usuario o la contraseña no coinciden, o no consigue nungun recurso buscado, acceso, etc, nos dará el siguiente error:

401
application/json; charset=utf-8

#De lo contrario si el usuario y la contraseña coinciden, si encontro el recurso o acceso, nos mostrara un OK:

200
application/json; charset=utf-8

-----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ejemplo pidiendo los datos al usuario.
import requests
username = raw_input("Username: ")
password = raw_input("Password: ")
r = requests.get('https://api.github.com', auth=(username, password))
print r.status_code
print r.headers['content-type']

################################################
##### Imprimir datetime de python y django #####
################################################

$ python
>>> import datetime
>>> now = datetime.datetime.now()
>>> print now
2017-01-05 04:08:15.932157

##############################################################
##### Cambiar la forma en que se muestra la fecha y hora #####
##############################################################

# -*- coding: utf-8 -*-
from datetime import datetime
"""
Cambiando la forma en que se muestra la fecha y hora de python
"""
fecha_hora = datetime.now()
fecha_hora_otro_formato = fecha_hora.strftime("%d-%m-%Y %H:%M")
print str(datetime.now())
print str(fecha_hora_otro_formato)

##################
##### Base64 #####
##################

'''
-- ¿Qué es la codificación Base64?

El Base64 es la manera en que los datos binarios de 8 bits se codifican a un formato que pueda ser representado en 7 bits.
Esto se hace utilizando sólo los caracteres A-Z, a-z, 0-9, +, y / con el fin de representar los datos.
El término base 64 viene del estándar Multipurpose Internet Mail Extensions (MIME), que es ampliamente utilizado para HTTP y XML, y
fue desarrollado originalmente para la codificación de adjuntos de los correos electrónicos y su correcta transmisión. 

-- ¿Por qué utilizamos Base64?

Base64 es muy importante para la representación de datos binarios, tanto que permite que los datos binarios puedan ser
representados de manera que parezcan y actúen como texto sin formato. Esto hace que sea más seguro almacenarlos en bases
de datos, enviarlos a través de correo electrónico o utilizarlos en formatos basados en texto como XML. Base64 se utiliza
básicamente para representar datos en formato ASCII.

-- La codificación Base64

La codificación Base64 es el proceso de convertir los datos binarios, en un juego de caracteres limitado a 64 caracteres.
Como hemos dicho en la primera sección, esos caracteres son A-Z, a-z, 0-9, +, y / (¿Los has contado?, ¿te has dado cuenta
de que se suman 64?). Este conjunto de caracteres se considera el conjunto de caracteres más común, y se conoce como el Base64
de MIME. Utiliza A-Z, a-z, 0-9, +, y / para los primeros 62 valores, y +, y / para los dos últimos valores.

Los datos codificados en Base64 terminan siendo más grandes que los datos originales, de manera que, como hemos dicho antes, por cada 3
bytes de datos binarios, hay al menos 4 bytes de datos codificados en Base64. Esto es debido al hecho de que estás apretando los datos en
un conjunto más pequeño de caracteres. 
'''

# -*- coding: utf-8 -*-
# Codificar con base64 una imágen
with open("path/of/file.*", "rb") as f:
    data = f.read()
    print data.encode("base64")

---

# -*- coding: utf-8 -*-
#Decodificar una cadena en base64 y convertirla en imágen
import base64
image = """
Aqui iría la cadena superlarga
generada con la codificación en base64
"""
imgdata = base64.b64decode(image)
filename = 'fff.png'  #Nombre con el que se va a crear la imágen 
with open(filename, 'wb') as f:
    f.write(imgdata)

----

# -*- coding: utf-8 -*-
# Decodificar y Codificar en un solo script usando base64 en python
import base64
with open("firefox-icon.png", "rb") as f:
    data = f.read()
    data1 = data.encode("base64")
    imgdata = base64.b64decode(data1)
    filename = 'fff.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)

----

# -*- coding: utf-8 -*-
# Codificar con base64 una imágen y guardar la cadena codificada en un fichero.
with open("my_image.png", "rb") as f:
    data = f.read()
    print data.encode("base64")
    archivo = open("my_file.txt", "w")
    archivo.write(data.encode("base64"))
    archivo.close()

###################################
#### Validar email con python #####
###################################

# -*- coding: utf-8 -*-
"""
Validar email con python.
"""
import re
correo='nombre@dominio.com'
if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
    print "Correo correcto"
else:
    print "Correo incorrecto"

##############################################################
##### Importar un fichero, script, directorio en python #####
##############################################################

import sys
sys.path.append(pathToFolderContainingScripts)
from scriptName import functionName #scriptName without .py extension

################################################################
##### Enlace simbólico a las version de python por defecto #####
################################################################

/usr/bin/python

Si queremos cambiar de version por defecto de python, entonces borramos /usr/bin/python creamos un enlace simbólico /usr/bin/python que apunte a python 3.x

####################################################################################
##### Descarga de archivos desde una url http y almacenarlo en disco en Python #####
####################################################################################

# -*- coding: utf-8 -*-
import urllib
urllib.urlretrieve ("http://192.168.12.82/x.zip", "x.zip")

################################################
########## Ambiente virtual en Python ##########
################################################

Cuando se desarrollando software con Python, quizas se presente el problema de tener
utilizar diferentes versiones de una mismo paquete en diferentes proyectos, ya sea el
mismo Python o diferentes versiones de un Framework como Django por ejemplo, el
problema a solucionar radica en como poder instalar las dos o mas versiones de la
misma librería con el fin de poder desarrollar varios proyectos de forma simultánea.

La solución consiste en crear virtualenvs o entornos virtuales. Un entorno virtual de
Python es un espacio completamente independiente de otros entornos virtuales y de los
paquetes instalados globalmente en el sistema. Esto significa que es posible instalar la versión
2.7 de Python en un entorno virtual y la versión 3.0 en otro diferente o de forma
global sin problema alguno.

El porder tener diferentes entornos donde podemos instalar diferentes versiones de paquetes
nos da la oportunidad de hacer un desarrollo simultaneo así como poder hacer pruebas si
afectar a los paquetes del sistema global.

##### Instalación: #####

Para crear un ambiente virtual instalamos lo siguiente:

# aptitude install python-setuptools python-dev python-pip

# aptitude install python-virtualenv virtualenvwrapper

$ mkvirtualenv nombre_ambiente_virtual //  Con un usuario (diferente a root) cree un ambiente virtual para su proyecto.

$ workon nombre_ambiente_virtual // Para acceder al nombre del ambiente virtual creado

ejemplo: 
user@debian:/home$ workon proyecto // Accedemos al entorno virtual creado
(proyecto)user@debian:/home$ // Ya estamos en el entorno virtual creado, denotado por el nombre del entorno al inicio del prompt

$ deactivate nombre_ambiente_virtual // Para salir del entorno virtaul, o simplemente deactivate

$ lsvirtualenv // Para listar los entornos virtuales creados o disponibles.

$ rmvirtualenv nombre_virtualenv // Remover o borrar un entorno virtual.

// Los entornos virtuales se crean en el directorio /home/user/.virtualenvs

##### Tips #####

En Debian GNU/Linux 8 (Jessie) a veces el comando mkvirtualenv no funciona por lo que hacemos lo siguiente:

# apt-get install virtualenvwrapper

$ vim .bashrc // Como usuario normal (NO ROOT), hay que agregar las variables con la ruta para virtualenv en el .bashrc, Agregar el siguiente contenido:

# to virtualenvwrapper
export WORKON_HOME=$HOME/django
source /etc/bash_completion.d/virtualenvwrapper

luego:

$ source .bachrc

#############################
##### Usando virtualenv #####
#############################

Installation: 

# aptitude install python-virtualenv python-pip

-Crear un virtualenv:

$ virtualenv mi_env

-Activar el virtualenv:

$ source mi_env/bin/activate

-Instalar un paquete (p.ej. Django) en el virtualenv:

(mi_env)$ pip install django

-Trabajar en el proyecto.

-Salir del virtualenv:

(mi_env)$ deactivate

##### Usando Python 3 en virtualenvwrapper #####

# apt-get install python3.4 python3-pip python3.4-dev python3-setuptools

# apt-get install python3-virtualenv virtualenvwrapper

$ mkvirtualenv --python=/usr/bin/python3 my_env

$ workon my_env

(my_env)$

##### Usando Python 3 en virtualenv #####

$ virtualenv -p python3 my_env

##### Borrar entorno virtual #####

No hay comando para borrar un entorno virtual desde virtualenv, basta con cancelar o detener los procesos (servidores y servicios) usados por
ese entorno y luego borrar el directorio.

$ rm -rf myenv

########################
##### Paquetes pip #####
########################

// Para desarrollar software con rapidez y calidad, es imprescindible utilizar paquetes externos que ayuden
con parte de la funcionalidad que se desea implementar. En el ambiente Python esto no es la excepción.

// Para solventar ésta necesidad, la comunidad Python ha puesto convenientemente a disposición de los desarrolladores
un repositorio de paquetes de fácil acceso llamado PyPi. Solo es necesario ejecutar un comando en la terminal
para poder instalar el paquete Python que necesitemos. Incluso es posible instalar paquetes que no se encuentren
en el mencionado repositorio.

// Para descargar paquetes del repositorio PyPi se pueden utilizar varias herramientas, pero en este caso se
va a usar pip. Es necesario instalar esta herramienta en el sistema en caso de no estar disponible, antes
de poder instalar un paquete Python.

// El comando pip equivale al apt-get de Debian pero para paquetes Python.

# aptitude install python-pip python-dev python-setuptools python3-pip // Instalamos pip y otros necesarios, com python3 para pip, necesario en algunos proyectos.

// Una vez instalado ya podremos instalar paquetes de Python a traves de pip ejemplo:

$ pip install django // Nos instalara la ultima version de Django disponible en los paquetes pi

$ pip install django==1.7 // Instalar una versión específica de algun paquete.

// Tambien es posible crear ficheros que contengan rutinas para automatizar la instalacion
de varios paquetes ejemplo:

Creamos un requirements.txt y dentro escribimos como ejemplo:
django==1.5.12
pillow==2.4.0
Geraldo==0.4.17

// Luego podemos ejecutar un pip install sobre el fichero e instalará lo que contenga:

$ pip install -r requirements.txt

$ pip install -r requirements.txt --timeout 120 // Con este parametro le daremos mayor tiempo de respuesta al servidor, para conexiones lentas.

// Dentro de los .virtualenvs, dentro de nuestro entorno virtual en
lib/python2.7/site-packages podemos ver que se instalaron los paquetes de requirements.txt
de no ser así hay que revisar el fichero o el nombre de los paquetes a instalar, etc.

$ pip search nombre_paquete // Buscar un paquete.

$ pip uninstall package // Desinstalar un paquete.

$ pip show package // Para ver si un paquete está instalado, si es así, mostrará la version, y la ruta donde está instalado.

$ pip install Package --upgrade // Para actualizar un paquete a su última versión.

$ pip install --upgrade Package package==1.x.x // Actualizar un paquete a una versión específica.

$ pip freeze // Listar los paquetes instalado y sus versiones exactas.

##### Error: ImportError: No module named packaging.version #####

Puede que alguna vez a pip le pique el trasero y no deje realizar acciones
de búsqueda, actualización etc.. entonces moveremos unos ficheros:

$ cd /usr/local/lib/python2.7/dist-packages

$ mv pkg_resources/ pkg_resources_bak/

Funcionó cuando se instalo en el sistema base, si está en un entorno virtual la
ruta será diferente.

###########################################
##### Usando un espejo de pip cercano #####
###########################################

Para usar los repositorios py.pi internos de Cenditel
vamos al directorio /home/usuario/.pip/
y creamos dentro el fichero pip.conf
Agregamos el siguiente contenido al fichero creado y guardamos:

[global]
index-url = http://pypi.cenditel/simple/

Luego actualizamos el pip y listo, si estamos usando un entorno virtual de python
entonces ejecutaremos los comandos dentro del entorno virtual.

$ pip install --upgrade pip
$ pip install package_name --trusted-host pypi.cenditel
$ pip install -r requirements.txt --trusted-host pypi.cenditel // Para instalar recursivamente un fichero de requerimientos.
$ pip install package_name --trusted-host pypi.python.org // Usando el espejo oficial de python.

##### Nota #####

Hay paquetes que requieren permisos de superusuario, entonces al usar sudo, o estar como
superusuarios ya no hará efecto el pip.conf que está en /home/usuario/.pip/
entonces, para que sirva con el root tambien crearemos el pip.conf pero en el home del root
que está en /root/.pip/

# touch /root/.pip/pip.conf

# nano /root/.pip/pip.conf // Y hacemos lo mismo que arriba, copiamos el contenido, guardamos y listo.

A veces no se crea el directorio .pip del usuario entonces lo creamos manualmente

/home/user$ mkdir .pip

root@debian# mkdir .pip // en /root

####################
##### Archivos #####
####################

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Abrir, escribir y cerrar un archivo.
"""
archivo = open("hello.txt", "w")
archivo.write("Hola")
archivo.close()

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Abrir, leer y cerrar un archivo.
"""
archivo = open("hello.txt", "r")
archivo.read()
archivo.close()

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usabndo readlines() para leer línea por línea
e imprimirlas en pantalla.
"""
archivo = open("hello.txt", "r")
for linea in archivo.readlines():
    print linea
archivo.close()

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Crear un archivo .csv a partir de los datos de una lista.
"""
import csv
mylist = ['a','b','c']
with open('data.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(mylist)

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Crear un archivo .csv a partir de los datos de una lista.
"""
import csv
mylist = ['a','b','c']
mylist2 = ['1','2','3']
with open('data.csv', 'wb') as myfile:
    #wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr = csv.writer(myfile) # Omitiendo las comillas al escribir el la data en el .csv
    wr.writerow(mylist)
    wr.writerow(mylist2)

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Crear un archivo .csv a partir de los datos de un diccionario.
"""
import csv
dic = {"John": "john@example.com", "Mary": "mary@example.com"}
nombre_archivo = "data.csv" # Nombre que tendrá el archivo .csv
csv = open(nombre_archivo, "w") 
columnTitleRow = "name, email\n"
csv.write(columnTitleRow)

for key in dic.keys():
    name = key
    email = dic[key]
    row = name + "," + email + "\n"
    csv.write(row)

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Leer datos de un .csv y mostrando la data por pantalla.
"""
import csv
with open('data.csv', 'r') as listado:
    datos = csv.reader(listado, delimiter=',') # Separar la data por coma.
    for row in datos:
        if row[0].startswith('#'): # Permite comentar líneas en el archivo csv.
            continue
        nombre = row[0] # Columna 1 que corresponde a Nombre y Apellido.
        email = row[1] # Columna 2 que corresponde al Email.
        print nombre
        print email
listado.close()

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Leer datos de un .csv y almacenarlos en una lista.
"""
"""
El .csv debe contener:
1,Mar?a Morales,15940181,Curso TDA,15940181-ctda-.pdf,0
2,Argenis Osorio,19592165,Curso TDA,19562165-ctda-.pdf,0
3,Lionel Messi,15796551,Curso TDA,15796551-ctda-.pdf,0
4,Carlos Ramirez,18456789,Curso TDA,18456789-ctda-.pdf,0
5,Perla Becerra,17789321,Curso TDA,17789321-ctda-.pdf,0
"""

import csv
with open('data.csv', 'r') as listado:
    datos = csv.reader(listado, delimiter=',') # Separar la data por coma.
    alist = [];
    for row in datos:
        if row[0].startswith('#'): # Permite comentar líneas en el archivo csv.
            continue
        id_id = row[0]
        alist.append(id_id);
        nombre = row[1]
        alist.append(nombre);
        cedula = row[2]
        alist.append(cedula);
        evento = row[3]
        alist.append(evento);
        nombre_archivo = row[4]
        alist.append(nombre_archivo);
        date = row[5]
        alist.append(date);
listado.close()
print alist

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Leyendo datos de un .csv y escribiendolos en otro

data.csv:
Name,Profession
Derek,Software Developer
Steve,Software Developer
Paul,Manager
"""
import csv
# create list holders for our data.
names = []
jobs = [] 
# open file
with open('data.csv', 'rb') as f:
    reader = csv.reader(f)
 
    # read file row by row
    rowNr = 0
    for row in reader:
        # Skip the header row.
        if rowNr >= 1:
            names.append(row[0])
            jobs.append(row[1])
 
        # Increase the row number
        rowNr = rowNr + 1
# Print data 
#print names
#print jobs
with open('data_final.csv', 'wb') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(names)
    wr.writerow(jobs)

----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Leyendo datos de un .csv y escribiendolos en otro .csv
"""

"""
data.csv
Name,Profession
Derek,Software Developer
Steve,Software Developer
Paul,Manager
"""

import csv
with open('data.csv', 'r') as listado:
    datos = csv.reader(listado, delimiter=',') # Separar la data por coma.
    alist = [];
    for row in datos:
        if row[0].startswith('#'): # Permite comentar líneas en el archivo csv.
            continue
        nombre = row[0]
        alist.append(nombre);
        profesion = row[1]
        alist.append(profesion);
listado.close()
with open('data_final.csv', 'wb') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(alist)

###################################################
##### Escribir comandos de Linux desde python #####
###################################################

# -*- coding: utf-8 -*-
import os

"""
Script para copiar un fichero a un servidor.
"""
#os.system("scp FILE USER@SERVER:PATH")
os.system("scp ff.jpg user@192.168.x.x:/home/user/tmp")

-----

# -*- coding: utf-8 -*-
import os

"""
Crear una carpeta.
"""
os.system("mkdir new_folder")

-----

# -*- coding: utf-8 -*-
import os

"""
Uso de comandos de unix desde python.
"""
p = os.popen('ls -la')
print(p.read())

-----

# -*- coding: utf-8 -*-
"""
Imprimir el directorio actual.
"""
import os

print os.getcwd()

----

# -*- coding: utf-8 -*-
import os

"""
Crear carpeta con python.
"""
print os.getcwd() # Imprimir el directorio actual
if not os.path.exists("x"):
  os.makedirs("x")

----

# -*- coding: utf-8 -*-
"""
Cambiarse a un directorio.
"""
import os

os.chdir("/home/user")

----

# -*- coding: utf-8 -*-
"""
Copiando y moviendo ficheros con python.
"""
import os
a = os.getcwd() # Almaceno en "a" el directorio actual.
os.system("mkdir fff") # Creo la carpeta fff.
os.chdir(a+'/fff') # Navego hasta la carpeta fff del directorio actual.
os.system("touch xxx.txt") # Creo el archivo xxx.txt dentro de la carpeta fff.
os.system("cp xxx.txt ../") # Copio a xxx.txt un directorio atrás.

######################################
##### Cifrado de datos en python #####
######################################

##### Pycrypto #####

Kit de herramientas de criptografía Python (pycrypto)

Esta es una colección de funciones de hash seguras (como SHA256 y RIPEMD160)
y varios algoritmos de cifrado (AES, DES, RSA, ElGamal, etc.). El paquete está
estructurado para facilitar la incorporación de nuevos módulos.

-----

# -*- coding: utf-8 -*-
"""
Cifrar datos usando DES del paquete Crypto
"""
# Importar el módulo DES
from Crypto.Cipher import DES

# Como usamos DES, el número de caracteres a cifrar es 8.
text="abcdefgh"

# Creamos un cifrador, el parámetro '12345678' es la clave de cifrado.
cipher=DES.new('12345678')

# Para cifrar usamos la función encrypt.
c_text=cipher.encrypt(text)

# Imprimimos el texto cifrado.
print "Texto cifrado: " +c_text

# Para descifrar usamos la función decrypt.
d_text=cipher.decrypt(c_text)

# Imprimimos el texto descifrado.
print "Texto descifrado: " +d_text

-----

# -*- coding: utf-8 -*-
"""
Ejemplo usando el modulo SHA256 para generar un hash a partir de datos.
"""
from Crypto.Hash import SHA256
hash = SHA256.new()
hash.update('my message')
hash.digest()
print hash.digest()

-----

# -*- coding: utf-8 -*-
"""
Ejemplo usando el modulo MD5 para generar un hash a partir de datos.
"""
from Crypto.Hash import MD5
m=MD5.new()
m.update('Hola mundo')
print m.digest()

-----

# -*- coding: utf-8 -*-
"""
Ejemplo usando el algoritmo de encriación AES cifrar y descifrar un texto.
"""
from Crypto.Cipher import AES
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message="The answer is no"
print message
ciphertext=obj.encrypt(message)
print ciphertext
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
deciphertext=obj2.decrypt(ciphertext)
print deciphertext

-----

# -*- coding: utf-8 -*-
"""
Usando el módulo random de Crypto.
"""
from Crypto.Random import random
x=random.choice(['dogs', 'cats', 'bears'])
print x

###################################################################
##### Saltar InsecureRequestWarning: Unverified HTTPS request #####
###################################################################

import urllib3
...
urllib3.disable_warnings()

#################################
##### Expresiones regulares #####
#################################

Las expresiones regulares, son patrones que definen un conjunto de cadenas que puede
ser finito o infinito. Por ejemplo, el conjunto de cadenas que formaría la expresión
regular (bar|ar|mar)co, es barco, arco y marco. Es un conjunto finito. En cambio la
expresión regular ab+c crea un conjunto infinito formado
por: abc, abbc, abbbc, abbbbbc, .... Así infinitamente.

Otro concepto...

Cuando manejamos texto en Python, una de las operaciones más comunes es la
búsqueda de una subcadena; ya sea para obtener su posición en el texto o
simplemente para comprobar si está presente. Si la cadena que buscamos es
fija, los métodos como find(), index() o similares nos ayudarán. Pero si
buscamos una subcadena con cierta forma, este proceso se vuelve más complejo.

Al buscar direcciones de correo electrónico, números de teléfono, validar campos
de entrada, o una letra mayúscula seguida de dos minúsculas y de 5 dígitos entre
1 y 3; es necesario recurrir a las Expresiones Regulares, también
conocidas como Patrones.

--- Componentes de las Expresiones Regulares ---

Las expresiones regulares son un mini lenguaje en sí mismo, por lo que para
poder utilizarlas eficientemente primero debemos entender los componentes de
su sintaxis; ellos son:

-Literales: Cualquier caracter se encuentra a sí mismo, a menos que se trate
de un metacaracter con significado especial. Una serie de caracteres encuentra
esa misma serie en el texto de entrada, por lo tanto la plantilla "raul"
encontrará todas las apariciones de "raul" en el texto que procesamos.

-Secuencias de escape: La sintaxis de las expresiones regulares nos permite
utilizar las secuencias de escape que ya conocemos de otros lenguajes de
programación para esos casos especiales como ser finales de línea, tabs, barras
diagonales, etc. Las principales secuencias de escape que podemos encontrar, son:

Secuencia de escape  -  Significado
\n  Nueva línea (new line). El cursor pasa a la primera posición de la línea siguiente
\t  Tabulador. El cursor pasa a la siguiente posición de tabulación
\\  Barra diagonal inversa
\v  Tabulación vertical
\ooo    Carácter ASCII en notación octal
\xhh    Carácter ASCII en notación hexadecimal
\xhhhh  Carácter Unicode en notación hexadecimal

-Clases de caracteres: Se pueden especificar clases de caracteres encerrando
una lista de caracteres entre corchetes [], la que que encontrará uno cualquiera
de los caracteres de la lista. Si el primer símbolo después del "[" es "^", la
clase encuentra cualquier caracter que no está en la lista.

-Metacaracteres: Los metacaracteres son caracteres especiales que son la esencia
de las expresiones regulares.

--- Patrones ---

Las expresiones regulares son un potente lenguaje de descripción de texto.
Y no existe un lenguaje moderno que no permita usarlas. Las reglas con las que se
forman son bastante simples. Pero aprender a combinarlas correctamente requiere
de práctica.

Utilizándolas podemos buscar una subcadena al principio o al final del texto.
Incluso si queremos que se repita cierta cantidad de veces, si queremos que algo
NO aparezca, o si debe aparecer una subcadena entre varias posibilidades. Permite
además, capturar aquellos trozos del texto que coincidan con la expresión para
guardarlos en una variable o reemplazarlos por una cadena predeterminada; o incluso
una cadena formada por los mismos trozos capturados. Estos son algunos aspectos
básicos de las expresiones regulares:

Metacaracteres - delimitadores

Esta clase de metacaracteres nos permite delimitar dónde queremos
buscar los patrones de búsqueda.

Ellos son:

Metacaracter  -  Descripción
^   inicio de línea.
$   fin de línea.
\A  inicio de texto.
\Z  fin de texto.
.   cualquier caracter en la línea.
\b  encuentra límite de palabra.
\B  encuentra distinto a límite de palabra.

--- Metacaracteres  -  clases predefinidas ---

Estas son clases predefinidas que nos facilitan la utilización de
las expresiones regulares. Ellos son:

Metacaracter  -  Descripción
\w  un caracter alfanumérico (incluye "_").
\W  un caracter no alfanumérico.
\d  un caracter numérico.
\D  un caracter no numérico.
\s  cualquier espacio (lo mismo que [ \t\n\r\f]).
\S  un no espacio.

--- Metacaracteres - iteradores ---

Cualquier elemento de una expresion regular puede ser seguido
por otro tipo de metacaracteres, los iteradores. Usando estos
metacaracteres se puede especificar el número de ocurrencias
del caracter previo, de un metacaracter o de una subexpresión.

Ellos son:

Metacaracter  -  Descripción
*   cero o más, similar a {0,}.
+   una o más, similar a {1,}.
?   cero o una, similar a {0,1}.
{n}     exactamente n veces.
{n,}    por lo menos n veces.
{n,m}   por lo menos n pero no más de m veces.
*?  cero o más, similar a {0,}?.
+?  una o más, similar a {1,}?.
??  cero o una, similar a {0,1}?.
{n}?    exactamente n veces.
{n,}?   por lo menos n veces.
{n,m}?  por lo menos n pero no más de m veces.

En estos metacaracteres, los dígitos entre llaves de la forma {n,m}, especifican
el mínimo número de ocurrencias en n y el máximo en m.

--- Metacaracteres - alternativas ---

Se puede especificar una serie de alternativas para una
plantilla usando "|" para separarlas, entonces do|re|mi
encontrará cualquier "do", "re", o "mi" en el texto de
entrada. Las alternativas son evaluadas de izquierda a
derecha, por lo tanto la primera alternativa que coincide
plenamente con la expresión analizada es la que se selecciona.

Por ejemplo: si se buscan foo|foot en "barefoot'', sólo la parte " foo
" da resultado positivo, porque es la primera alternativa probada, y
porque tiene éxito en la búsqueda de la cadena analizada.

Ejemplo:

foo(bar|foo) --> encuentra las cadenas 'foobar' o 'foofoo'.

--- Metacaracteres - subexpresiones ---

La construcción ( ... ) también puede ser empleada para definir
subexpresiones de expresiones regulares.

Ejemplos:

(foobar){10} --> encuentra cadenas que contienen 8, 9 o 10 instancias de 'foobar'

foob([0-9]|a+)r --> encuentra 'foob0r', 'foob1r' , 'foobar', 'foobaar', 'foobaar' etc.
Metacaracteres - memorias (backreferences)

Los metacaracteres \1 a \9 son interpretados como memorias. \ encuentra la subexpresión previamente encontrada #.

Ejemplos:

(.)\1+ --> encuentra 'aaaa' y 'cc'.

(.+)\1+ --> también encuentra 'abab' y '123123'

(['"]?)(\d+)\1 --> encuentra '"13" (entre comillas dobles), o '4' (entre comillas simples) o 77 (sin comillas) etc.

--- Metacaracteres ---

Se conoce como metacaracteres a aquellos que, dependiendo del contexto, tienen un
significado especial para las expresiones regulares. Por lo tanto, los debemos
escapar colocándoles una contrabarra() delante para buscarlos explícitamente.
A continuación listaré los más importantes:

-Anclas: Indican que lo que queremos encontrar se encuentra al principio o al
final de la cadena. Combinándolas, podemos buscar algo que represente a la cadena entera:

patron: coincide con cualquier cadena que comience con patron.

patron$: coincide con cualquier cadena que termine con patron.

patron$: coincide con la cadena exacta patron.

-Clases de caracteres: Se utilizan cuando se quiere buscar un caracter dentro
de varias posibles opciones. Una clase se delimita entre corchetes y lista
posibles opciones para el caracter que representa:

[abc]: coincide con a, b, o c

[387ab]: coincide con 3, 8, a o b

niñ[oa]s: coincide con niños o niñas.

Para evitar errores, en caso de que queramos crear una clase de caracteres
que contenga un corchete, debemos escribir una barra \
delante, para que el motor de expresiones regulares lo considere un
caracter normal: la clase [ab\[] coincide con a, b y [.

--- Rangos ---

Si queremos encontrar un número, podemos usar una clase como [0123456789]
o podemos utilizar un rango. Un rango es una clase de caracteres abreviada
que se crea escribiendo el primer caracter del rango, un guión y el último
caracter del rango. Múltiples rangos pueden definirse en la misma
clase de caracteres.

[a-c]: equivale a [abc]

[0-9]: equivale a [0123456789]

[a-d5-8]: equivale a [abcd5678]

Es importante notar que si se quiere buscar un guión debe colocarse al
principio o al final de la clase. Es decir, inmediatamente después
del corchete izquierdo o inmediatamente antes del corchete derecho; o
en su defecto, escaparse. Si no se hace de esta forma, el motor de
expresiones regulares intentará crear un rango y la expresión no
funcionará como debe (o dará un error). Si queremos, por ejemplo
crear una clase que coincida con los caracteres a, 4 y -, debemos
escribirla así:

[a4-]

[-a4]

[a\-4]

--- Rango negado ---

Así como podemos listar los caracteres posibles en cierta posición de la cadena,
también podemos listar caracteres que no deben aparecer. Para lograrlo, debemos
negar la clase, colocando un circunflejo inmediatamente después del
corchete izquierdo:

[^abc]: coincide con cualquier caracter distinto a a, b y c

--- Cuantificadores ---

Son caracteres que multiplican el patrón que les precede. Mientras que con las
clases de caracteres podemos buscar un dígito, o una letra; con los
cuantificadores podemos buscar cero o más letras, al menos 7 dígitos, o entre
tres y cinco letras mayúsculas. Los cuantificadores son:

**?**: coincide con cero o una ocurrencia del patrón. Dicho de otra forma, hace que el patrón sea opcional

**+**: coincide con una o más ocurrencias del patrón

*****: coincide con cero o más ocurrencias del patrón.

**{x}**: coincide con exactamente x ocurrencias del patrón

**{x, y}**: coincide con al menos x y no más de y ocurrencias. Si se omite x, el mínimo es cero, y si se omite y, no hay máximo. Esto permite especificar a los otros como casos particulares: ? es {0,1}, + es {1,} y * es {,} o {0,}.

Ejemplos:

.* : cualquier cadena, de cualquier largo (incluyendo una cadena vacía)

[a-z]{3,6}: entre 3 y 6 letras minúsculas

\d{4,}: al menos 4 dígitos

.*hola!?: una cadena cualquiera, seguida de hola, y terminando (o no) con un !

--- Otros metacaracteres --

Existen otros metacaracteres en el lenguaje de las expresiones regulares:

**?**: Además de servir como cuantificador, puede modificar el comportamiento de otro.

De forma predeterminada, un cuantificador coincide con la mayor cadena posible.
Cuando se le coloca un ?, se indica que se debe coincidir con la menor
cadena posible. Esto es: dada la cadena bbbbb, b+ coincide con la cadena entera
mientras que b+? coincide solamente con b. Es decir, la menor cadena que cumple el patrón.

**()**: agrupan patrones. Sirven para que aquel pedazo de la cadena que coincida con
el patrón sea capturado; o para delimitar el alcance de un cuantificador. Ejemplo: ab+
coincide con ab, abb, abbbbb, …, mientras que (ab)+ coincide con ab, abab, abab…

**|** : permite definir opciones para el patrón: perro|gato coincide con perro y con gato.

--- Módulo re ---

Para utilizar Expresiones Regulares, Python provee el módulo re. Importando este módulo
podemos declarar la expresión regular. Python nos ofrece 2 formas distintas de hacerlo:

---

import re
# 1º forma
regex = r'(bar|ar|mar)co'
# 2º forma
regex = re.compile(r'(bar|ar|mar)co')

---

La 1º forma es más eficaz y ocupa menos espacio en memoria, porque solo es una simple
cadena con el prefijo r, pero cada vez que se utiliza, esta crea las estructuras
internas necesarias para su ejecución y una vez finalizada su tarea, destruye esas
mismas estructuras.

La 2º forma en cambio crea las estructuras desde el principio
y no las destruye hasta que la propia variable que contiene la expresión regular
es destruida. Ocupa más espacio en memoria y necesita del paquete re de Python.
¿Cuál elegir? Pues depende del uso. Si solo vas utilizar una o 2 veces la misma
expresión regular, la 1º forma es la mejor, porque ocupa menos espacio en memoria.
Si la expresión regular se va a utilizar de manera repetida y en múltiples sitios.

La 2º forma es la mejor, porque crea las estructuras al principio y no las borra
cuando se utiliza la expresión regular.

--- Empezando con lo básico ---

Una vez visto lo básico, vamos a ver como utilizar las funciones para
expresiones regulares de Python y que usos les podemos dar.

---

# -*- coding: utf-8 -*-
import re

regex_format1 = re.compile(r'ab+c')
regex_format2 = r'ab+c'
text1 = 'abc'

print "\nLlamando la primera función"
if regex_format1.search(text1):
    print "La cadena está dentro del conjunto de la expresión regular"
else:
    print "La cadena no está dentro del conjunto de la expresión regular"
# output La cadena está dentro del conjunto de la expresión regular.

print "\nLlamando la segunda función"
text2 = 'test'
if re.search(regex_format2, text2):
    print "La cadena está dentro del conjunto de la expresión regular"
else:
    print "La cadena no está dentro del conjunto de la expresión regular"
# output La cadena no está dentro del conjunto de la expresión regular.

---

La función search() comprueba si una parte de un texto está dentro del
conjunto de la expresión regular. Si es así devuelve un objeto llamado
Match Object. Sino coincide devuelve None.

---

# -*- coding: utf-8 -*-
"""
Devuelve la parte de la cadena que coincide con la expresión regular.
"""
import re
regex = re.compile(r'[a-z]+')
text = '0122 test test1'
a = re.search(regex, text)
print(a.group(0)) # group(0) devuelve la parte de la cadena que coincide con la expresión regular.
# output: test

--- match() vs search() ---

Existe cierta confusión con ambas funciones. Las 2 sirven para lo mismo, comprobar que
una cadena coincide con una expresión regular. Pero hay una diferencia fundamental entra ambas.
match() comprueba que la cadena completa coincida con la expresión regular. search() comprueba
si una parte de la cadena coincide con la expresión regular.

---

# -*- coding: utf-8 -*-
import re
cadena1 = 'casa'
cadena2 = 'casas'
cadena3 = 'pasa'

if re.match(cadena1, cadena2):
    print "cadena1 y cadena2 son coincidentes"
else:
    print "cadena1 y cadena2 no son coincidentes"
 
if re.match(cadena1, cadena3):
    print "cadena1 y cadena3 son coincidentes"
else:
    print "cadena1 y cadena3 no son coincidentes"

---

La función findall() devuelve una lista con las subcadenas que cumplen
el patrón en una cadena.

---

# -*- coding: utf-8 -*-
"""
Usando un rango de números para buscar en el texto.
"""
import re
regex = re.compile('[1-3]+') # Rango de números del 1 al 3.
text = '5 4 1 3 2'
a = regex.findall(text)
print a

---

# -*- coding: utf-8 -*-
import re

# Expresión regular que comprueba que la cadena es un número.
regex = re.compile(r'[0-9]+')

text1 = '01234'
if regex.search(text1):
    print('Entra porque text1 coincide con la expresión regular.')

if regex.match(text1):
    print('Entra porque text1 coincide con la expresión regular.')

text2 = 'test 01234'
if regex.search(text2):
    print('Entra porque parte de text2 coincide con la expresión regular.')

if regex.match(text2):
    pass  # No entrará
else:
    print('No entra porque text2 no coincide con la expresión regular.')

--- Substituir con expresiones regulares ---

Sin duda esta es la función más útil de las expresiones regulares. La de sustituir
la parte de la cadena de texto que coincide con la expresión regular. Para ello utilizamos
la función sub() del paquete re de Python.

---

# -*- coding: utf-8 -*-
import re
"""
Sustituir los espacios en blanco por -
"""
regex = re.compile(r'\s+') # Expresión regular que busca todos los caracteres espacios.
text = "      test1 test2     test3\ntest4   \ntest5   "
#Reemplazar todo los espacios por el caracter -.
result = regex.sub('-', text)
print result
# output: -test1-test2-test3-test4-test5-

---

# -*- coding: utf-8 -*-
import re
regex = re.compile('a[3-5]+') # coincide con una letra, seguida de al menos 1 dígito entre 3 y 5
text = 'a3'
text2 = 'a2'

if regex.search(text):
    print "Sí"
else:
    print "No"

if regex.search(text2):
    print "Sí"
else:
    print "No"

---

# -*- coding: utf-8 -*-
import re
regex = re.compile('a[3-5]+') # coincide con una letra, seguida de al menos 1 dígito entre 3 y 5
text = 'a1 a2 a3 a4 a5'
a = regex.findall(text)
print a
# output: ['a3', 'a4', 'a5']

---

# -*- coding: utf-8 -*-
import re
text = """Podrá nublarse el sol eternamente; 
Podrá secarse en un instante el mar; 
Podrá romperse el eje de la tierra 
como un débil cristal. 
¡todo sucederá! Podrá la muerte 
cubrirme con su fúnebre crespón; 
Pero jamás en mí podrá apagarse 
la llama de tu amor."""
regex = re.compile(r'\W+') # patron para dividir donde no encuentre un caracter alfanumerico.
a = regex.split(text)
print a

---

# -*- coding: utf-8 -*-
"""
Validando una URL
"""
import re
text = "https://www.youtube.com/"
regex = re.compile(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")
if regex.search(text):
    print "Es una url"
else:
    print "No es una url"

---

# -*- coding: utf-8 -*-
"""
Validando una direccion IP.
"""
import re
text = "192.168.12.255"
regex = re.compile('^(?:(?:25[0-5]|2[0-4][0-9]|''[01]?[0-9][0-9]?)\.){3}''(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
if regex.search(text):
    print "Es una ip"
else:
    print "No es una ip"

---

# -*- coding: utf-8 -*-
"""
Validando una fecha.
"""
import re
text = "30/01/1982"
regex = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$')
if regex.search(text):
    print "Es una fecha"
else:
    print "No es una fecha"

---

La barra vertical “|” expresa distintas alternativas que podrán darse para que se cumpla la expresión.

---

# -*- coding: utf-8 -*-
"""
Validando coincidencias, por ejemplo
extenciones de ficheros.
"""
import re
extensiones = ['jpg','png','gif','mp3','doc']
for tipoarchivo in extensiones:
    if re.match('jpg|png|gif|bmp', tipoarchivo):
        print "La extension ",tipoarchivo," corresponde con una imagen"
    else:
        print "La extension ",tipoarchivo," no corresponde con una imagen"

---

# -*- coding: utf-8 -*-
"""
Imprimiendo los terminos que coincidan con la expresión regular.
"""
import re
palabras = ['careta', 'carpeta', 'colita', 'cateta', 'cocreta', 'caleta', 'caseta']
for termino in palabras:
    if re.match('ca(..|...)ta', termino):
        print termino # careta , carpeta, cateta, caleta, caseta 

maspalabras = ['masa', 'mata', 'mar', 'mana','cama', 'marea']
for termino in maspalabras:
    if re.match('ma(s|m|n)a', termino):
        print termino  # masa, mana

---

# -*- coding: utf-8 -*-
import re
codigos = ['se1','se9','ma2','se:','se.','se2','hu2','se3','sea','sec']

for elemento in codigos:
    if re.match('se[0-5]', elemento):  # el 3er carácter puede ser nº de 0-5
        print elemento

for elemento in codigos:
    if re.match('se[0-5a-z]', elemento):  # nº de 0 a 5 y letra de a a z
        print elemento

for elemento in codigos:
    if re.match('se[.:]', elemento):  # el tercer carácter puede ser . ó :
        print  elemento

for elemento in codigos:
    if re.match('se[^0-2]', elemento):  # debe comenzar por nº de 0 a 2 
        print elemento

---

# -*- coding: utf-8 -*-
"""
\d  Cualquier carácter que sea dígito
\D  Cualquier carácter que no sea dígito
\w  Cualquier carácter alfanumérico
\W  Cualquier carácter no alfanumérico
\s  Espacio en blanco
\S  Cualquier carácter que no sea espacio
"""
import re
codigos = ['se1','se9','ma2','se:','se.','se2','hu2','se3','sea','sec']

for elemento in codigos:
    if re.match('se\d', elemento):  # el 3er carácter debe ser número
        print elemento

---

# -*- coding: utf-8 -*-
"""
+  El carácter de la izquierda aparecerá una o varias veces
*  El carácter de la izquierda aparecerá cero o más veces
?  El carácter de la izquierda aparecerá cero o una vez
{}  Indica el número de veces que debe aparecer el carácter de la izquierda:
{3} 3 veces; {1,4} de 1 a 4; {,3} de 0 a 3; {2,} dos o más veces
"""
import re
codigos = ['aaa111', 'aab11', 'aaa1111', 'aaz1', 'aaa'] 

for elemento in codigos:
    if re.match('aa[a-z]1{2,}', elemento):
        print elemento # aaa111 , aab11, aaa1111

for elemento in codigos:
    if re.match('a+1+', elemento):
        print elemento # aaa111 , aaa1111 

##########################
##### Function str() #####
##########################

The str() function converts the specified value into a string.
