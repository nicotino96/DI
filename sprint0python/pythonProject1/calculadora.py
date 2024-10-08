from traceback import print_tb

from pythonProject1.operaciones import suma, resta, multiplicacion, division


otro = True

while otro:
    n1 = int(input("Introduzca un número: "))
    n2 = int(input("Introduzca otro número: "))
    resp = input("Operación a realizar: (sumar/restar/multiplicar/dividir) ")

    if resp == "sumar":
        resultado = suma(n1, n2)
        print(resultado)
    elif resp == "restar":
        resultado = resta(n1, n2)
        print(resultado)
    elif resp == "multiplicar":
        resultado = multiplicacion(n1, n2)
        print(resultado)
    elif resp == "dividir":
        resultado = division(n1, n2)
        print(resultado)
    else:
        print("Respuesta no válida")

    seguir = input("¿Desea realizar otra operación? (s/n) ")

    if seguir != "n" and seguir != "s":
        print("Respuesta no válida")
    if seguir == "n":
        otro = False