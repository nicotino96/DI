from pythonProject1.hero import Hero
from pythonProject1.monster import Monster
from pythonProject1.treasure import Treasure


class Dungeon:
    hero: Hero

    def __init__(self):
        self.hero = Hero()
        self.monsters = [Monster(),Monster(),Monster(),Monster(),Monster()]
        self.treasure = Treasure()
    def play(self):
        print("Héroe entra en la mazmorra")
        for i in range(0,len(self.monsters,1)):
            monster=self.monsters[i]
            print("Te has encontrado con un ", self.monsters[1].name)

    def face_enemy(self, monster):
        while True:
            print("¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            opcion=int(input())
            if opcion == 1:
                self.hero.attack(monster)
                break
            elif opcion == 2:
                self.hero.defend()
                break
            elif opcion == 3:
                self.hero.heal()
                break
            else:
                print("Opción no válida")
    def search_treasure(self):
        print("Buscando tesoro...")
        self.treasure.find_treasure(self.hero)
