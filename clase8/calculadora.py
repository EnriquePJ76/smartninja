
# bienvenida
print ("\nBienvenido a mi primera calculadora de python.")
print("Ahora introduce los datos")
print()

# En esta parte recoguemos los datos
op = input("Que quieres hacer (+-*/): ")
num1 = float(input("Introduce el primer número : "))
num2 = float(input("Introduce el segundo número: "))
resultado = None

# Aqui procesamos los datos

if op == "+":
    resultado = num1 + num2
elif op == "-":
    resultado = num1 - num2
elif op == "*":
    resultado = num1 * num2
elif op == "/":
    resultado = num1 / num2
else:
    print ("No has metido una operacion correcta!!!")
    exit()


# En esta parte imprimimos los resultaods
print ("\nEl resultado de la operación es:")
print (str(num1) + " " + op + " " + str(num2) + " = " + str(resultado))