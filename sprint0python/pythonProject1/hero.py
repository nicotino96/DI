from pythonProject1.character import Character

class Hero(Character):
    def __init__(self, nombre):
        super().__init__(nombre, 60, 10, 100)#se llama al constructor padre
        self.max_hp=100#se le añade este atributo propio de esta clase hijo
    def attack (self, monster):
        print("Héroe ataca a ",monster.name)
        damage=self.ad-monster.dp#resta del poder de ataque del atacante y el poder de defensa del oponente (que se manda como argumento al método)
        if damage>0:
            print("El enemigo ",monster.name," ha recibido",damage," puntos de daño")
            monster.hp-=damage
            print("Vida de goblin: ", monster.hp)#informa del nuevo estado del enemigo
        else:
            print("El enemigo ha bloquedo el ataque.")
    def heal (self):
        if (self.hp + 20)>self.max_hp: #no cura más allá de la salud máxima
                self.hp=self.max_hp
        else:
            self.hp+=20
        print("Héroe se ha curado. Salud actual: ",self.hp)#informa de la nueva vida del héroa
    def defend (self):
        self.dp+=5
        print("Héroe sube su defensa. Defensa actual: ",self.dp)
    def reset_defense(self):#metódo para resetear la defensa cuando ha sido aumentada
        self.dp-=5
        print("La de defense de ",self.name," vuelve a la normalidad: ",self.dp)


