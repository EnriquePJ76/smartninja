
# bienvenida
print ("\nBienvenido a mi primera calculadora de python.")


print("Ahora introduce los datos")
print()

op = ""
while op != "q":
    # En esta parte recoguemos los datos
    print ("Escribe q para salir.")
    op = input("Que quieres hacer (+-*/q): ")
    if op != "q":
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
    elif op == "q":
        break
    else:
        print ("No has metido una operacion correcta!!!")


    # En esta parte imprimimos los resultaods
    print ("\nEl resultado de la operación es:")
    print (str(num1) + " " + op + " " + str(num2) + " = " + str(resultado))
    print ("%s %s %s = %s" % (num1, op, num2, resultado))
    print ("{0} {1} {2} = {3} -----> {3}".format(num1,op,num2,resultado))

print ("Bye bye!!!")