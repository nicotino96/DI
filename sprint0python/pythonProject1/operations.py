def sum(x, y):
    return x + y
def rest(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide (x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        print("no se puede dividir entre 0")

