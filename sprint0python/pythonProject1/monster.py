from pythonProject1.character import Character


class Monster(Character):
    def __init__(self):
        #se hace uso del constructor de la clase padre
        super().__init__("goblin", 5, 7, 100)#el nombre viene predeterminado,

    def attack(self, hero):#única acción del monstruo en este juego
        print("El monstruo ",self.name," ataca a ",hero.name)
        damage = (self.ad - hero.dp)
        if damage > 0:#solo inflije daño si su poder de ataque es superior de la defensa de su oponente
            hero.hp -= damage
            print("El héroe ",hero.name," ha recibido ",damage," puntos de daño.")
            print("Vida de ",hero.name,": ",hero.hp)
        else:
            print(f"El héroe ha bloqueado el ataque.")