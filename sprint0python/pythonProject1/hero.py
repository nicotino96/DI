from pythonProject1.character import Character

class Hero(Character):
    def __init__(self):
        super().__init__(input(print("Introduzca nombre del héroe: ")), 20, 10, 100)
        self.max_hp=100
    def attack (self, monster):
        print("Héroe ataca a "+monster.name)
        if self.ad>monster.dp:
            print("El enemigo "+monster.name+" ha recibido"+(self.ad-monster.dp)+" puntos de daño")
        else:
            print("El enemigo ha bloquedo el ataque")
    def heal (self):
        if (self.hp + 20)>self.max_hp:
                self.hp=self.max_hp
        else:
            self.hp+=20
        print("Héroe se ha curado. Salud actual: ",self.hp)
    def defend (self):
        self.dp+=5
    def reset_defense(self):
        self.dp-=5
        print(("La de defense de "+self.name+" vuelve a la normalidad"))


