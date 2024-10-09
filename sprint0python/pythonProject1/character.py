class Character():
    def __init__(self, name, ap, dp, hp):
        self.name=name
        self.ad=25
        self.dp=30
        self.hp=40

    def is_alive(self):
        return self.hp > 0