


x = float( input("Mete el valor de x: ") )
y = float( input("Mete el valor de y: ") )
suma = x + y

texto = "En una variable - Resultado: "

print(texto)
print(suma)

t0="Pepe"
t1="es"
t2="Programador"

print (t0 + " " + t1 + " " + t2)

print (str(x) + " + " + str(y) + " = "+ str(suma))

print ( "%s + %s + %s = %s" % (x, y, y, suma))

print ( "{1} + {2} + {2} = {3}".format(x, y, suma))
