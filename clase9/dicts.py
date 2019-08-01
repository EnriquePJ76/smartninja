
#Ejemplo entre lista vacía y diccinario vacío
list = []
dict = {}

"""
Hola esto es un comentario muy largo
Aq78 puedo escribir
hasta que me aburra


Adios
"""

#Diccionarios
pepe = {
    'edad': 30,
    'apellidos': 'Garcia Lopez',
    'nombre': 'Jose'
}

pepe['puntuacion'] = 2
pepe['veces_jugado'] = 23

print (pepe)
print ("{1}, {0}".format(pepe['nombre'], pepe['apellidos']))
print ("Edad: " + str(pepe.get('edad')) )


import datetime

print (datetime.datetime.now())