class Character():
    def __init__(self, name,ad, dp, hp):
        self.name=name
        self.ad=ad
        self.dp=dp
        self.hp=hp

    def is_alive(self):
        return self.hp > 0