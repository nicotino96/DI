def sum(x, y):#método para que devuelve los dos argumentos sumados
    return x + y
def rest(x, y):#método para que devuelve los dos argumentos restads
    return x - y
def multiply(x, y):#método para que devuelve los dos argumentos multiplicados
    return x * y
def divide (x, y):#método para que devuelve los dos argumentos divididos (controla la división entre 0)
    try:
        return x / y
    except ZeroDivisionError as e:
        print("no se puede dividir entre 0")

