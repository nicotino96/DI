from traceback import print_tb

from pythonProject1.operations import sum, rest, multiply, divide


otro = True

while otro:
    n1 = int(input("Introduzca un número: "))
    n2 = int(input("Introduzca otro número: "))
    resp = input("Operación a realizar: (sumar/restar/multiplicar/dividir) ")

    if resp == "sumar":
        outcome = sum(n1, n2)
        print(outcome)
    elif resp == "restar":
        outcome = rest(n1, n2)
        print(outcome)
    elif resp == "multiplicar":
        outcome = multiply(n1, n2)
        print(outcome)
    elif resp == "dividir":
        outcome = divide(n1, n2)
        print(outcome)
    else:
        print("Respuesta no válida")

    goOn = input("¿Desea realizar otra operación? (s/n) ")

    if goOn != "n" and goOn != "s":
        print("Respuesta no válida")
    if goOn == "n":
        otro = False