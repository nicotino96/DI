

from pythonProject1.hero import Hero
from pythonProject1.monster import Monster
from pythonProject1.treasure import Treasure


class Dungeon:
    hero: Hero

    def __init__(self, hero):
        # Asigna el héroe pasado como parámetro a la mazmorra
        self.hero = hero
        # Crea una lista de 5 instancias de la clase Monster
        self.monsters = [Monster(),Monster(),Monster(),Monster(),Monster()]
        # Crea una instancia de la clase Treasure
        self.treasure = Treasure()

    def play(self):
        print("Héroe entra en la mazmorra.")

        for i in range(0,len(self.monsters),1):# Recorre la lista de monstruos
            monster=self.monsters[i]# Selecciona el monstruo actual
            print("Te has encontrado con un ", monster.name, "(" ,monster.hp," hps)")
            dp_aum=False
            while monster.hp>0 and self.hero.hp>0:# Mientras ambos, el héroe y el monstruo, tengan salud positiva, sigue el combate
                if dp_aum:
                    self.hero.reset_defense()#reseteo de la defensa en caso de haber sido aumentada en el turno anterior
                dp_aum=self.face_enemy(monster)# El héroe toma una acción contra el monstruo
                monster.attack(self.hero)# En este juego el monstruo siempre ataca haga lo que haga el héroe
            if self.hero.hp<=0:# Si muere el héroe termina el juego
                print("Héroe ha sido derrotado.")
                break
            self.search_treasure()#Después de la muerte del monstruo y antes de la aparición del siguiente el héroe encuentra un tesoro
        print("¡Héroe ",self.hero.name, "ha ganado la partida!")#Se acaba el juego cuando la lista de monstruos termina
    def face_enemy(self, monster):
        while True:
            try:
                print("¿Qué deseas hacer?")
                print("1. Atacar.")
                print("2. Defender.")
                print("3. Curarse.")
                opcion=int(input())
                if opcion == 1:
                    self.hero.attack(monster)
                    return False
                elif opcion == 2:
                    self.hero.defend()
                    return True #el método True cuando se escoge defensa para que se controle se he aumentado y así poder resetearla en el siguiente turno
                elif opcion == 3:
                    self.hero.heal()
                    return False
                else:
                    print("Número del 1 al 3")#Repite los mensajes en caso de que el valor numérico no esté dentro del rango
            except ValueError:
                print("Se requier un valor numérico")#Repite en caso de que no se introduzca un valor numérico
    def search_treasure(self):
        print("Buscando tesoro...")
        self.treasure.find_treasure(self.hero) # método en clase Treasure para encontrar un tesoro
