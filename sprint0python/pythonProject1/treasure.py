from random import randint
from traceback import print_tb


class Treasure:
    def __init__(self):
        #lista de posibles tesoros
        self.benefit=[
            'Poción de ataque',
            'Poción de defensa',
            'Poción de salud'
        ]
    def find_treasure(self, hero):
        aleatorio=randint(1,3)#para escoger un tesoro al azar
        print("El héroe ha encontrado un tesoro: "+self.benefit[aleatorio-1])#se resta 1 para que no se vaya de rango en la lista
        if aleatorio == 1:#correspondería a la posición 0 en el array etc..
            hero.ad += randint(1,25)#la cantidad de recompensa también es aleatoria
            print("Poder de ataque aumentado: ",hero.ad)#se iforma de la nueve estadística del héroe
        if aleatorio == 2:
            hero.dp += randint(1, 25)
            print("Poder de defensa aumentado: ",hero.dp)
        if aleatorio == 3:
            hero.hp += randint(1, 25)
            if hero.hp > hero.max_hp:
                hero.hp=hero.max_hp
            print("Te has curado: ",hero.hp)


