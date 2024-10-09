from random import randint


class Treasure:
    def __init__(self, benefit):
        self.benefit={
            'Poción de ataque':randint(1,25),
            'Poción de defensa':randint(1, 25),
            'Poción de salud':randint(1, 25)
        }
    def find_trasure(self, hero):
        print("El héroe ha encontrado un tesoro: "+self.benefit[randint(1,3)])

