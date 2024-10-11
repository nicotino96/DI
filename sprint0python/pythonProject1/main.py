from pythonProject1.dungeon import Dungeon
from pythonProject1.hero import Hero
from pythonProject1.treasure import Treasure


def main():
    heroName= input("Introduce nombre del héroe: ")

    hero = Hero(heroName)
    print("Vida de ",heroName,": ",hero.hp)
    dungeon = Dungeon(hero)
    dungeon.play()

if __name__ == "__main__":
    main()