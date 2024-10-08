def suma(x, y):
    return x + y
def resta(x , y):
    return x - y
def multiplicacion(x, y):
    return x * y
def division (x , y):
    try:
        return x / y
    except ZeroDivisionError as e:
        print("no se puede dividir entre 0")

