from random import randint
from traceback import print_tb


class Treasure:
    def __init__(self):
        self.benefit=[
            'Poción de ataque',
            'Poción de defensa',
            'Poción de salud'
        ]
    def find_treasure(self, hero):
        aleatorio=randint(1,3)
        print("El héroe ha encontrado un tesoro: "+self.benefit[aleatorio])
        if aleatorio == 1:
            hero.ad += randint(1,25)
            print("Poder de ataque aumentado: ",hero.ad)
        if aleatorio == 2:
            hero.dp += randint(1, 25)
            print("Poder de defensa aumentado: ",hero.dp)
        if aleatorio == 3:
            hero.hp += randint(1, 25)
            print("Te has curado: ",hero.hp)


