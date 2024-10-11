class Character():
    #clase padre de la que heredarán atributos héroe y monstruo
    def __init__(self, name,ad, dp, hp):#método constructor
        #atributos
        self.name=name
        self.ad=ad
        self.dp=dp
        self.hp=hp

    def is_alive(self):#para el juego es necesarios saber tanto si hereo como monstruo están vivos para continuar o terminar la partida
        return self.hp > 0