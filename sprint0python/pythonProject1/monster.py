from pythonProject1.character import Character


class Monster(Character):
    def __init__(self):
        super().__init__("goblin", 5, 7, 100)

    def attack(self, hero):
        print("El monstruo ",self.name," ataca a ",hero.name)
        damage = (self.ad - hero.dp)
        if damage > 0:
            hero.hp -= damage
            print("El héroe ",hero.name," ha recibido ",damage," puntos de daño.")
            print("Vida de ",hero.name,": ",hero.hp)
        else:
            print(f"El héroe ha bloqueado el ataque.")