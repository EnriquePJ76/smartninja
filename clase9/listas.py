import mimodulo

mimodulo.hola.

list = []
list_dos = [[1,2,3,4],"hola",True, None]
list_dos.append("adios")

for i in list_dos:
    print (i)

print (list_dos)

capitales = ['madrid', 'lisboa', 'paris', 'roma', 'berlin']

for cap in capitales:
    print("He estado en {0}".format(cap))

some_list = [1, 34, 12, 17, 87]
some_list.sort()
print(some_list)