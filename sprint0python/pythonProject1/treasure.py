from random import randint


class Treasure:
    def __init__(self):
        self.benefit=[
            'Poción de ataque',
            'Poción de defensa',
            'Poción de salud'
        ]
    def find_trasure(self, hero):
        aleatorio=randint(1,3)
        print("El héroe ha encontrado un tesoro: "+self.benefit[aleatorio])
        if aleatorio == 1:
            hero.ad += randint(1,25)
        if aleatorio == 2:
            hero.ad += randint(1, 25)
        if aleatorio == 3:
            hero.ad += randint(1, 25)


