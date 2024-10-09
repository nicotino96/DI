from pythonProject1.character import Character


class Monster(Character):
    def __init__(self):
        super().__init__(input(print("Introduzca nombre del héroe: ")), 35, 7, 100)

    def attack(self, hero):
        print(f"El monstruo {self.name} ataca a {hero.name}.")
        damage = (self.ad - hero.dp)
        if damage > 0:
            hero.hp -= damage
            print(f"El héroe {hero.name} ha recibido {damage} puntos de daño.")
        else:
            print(f"El héroe ha bloqueado el ataque.")