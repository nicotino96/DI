from pythonProject1.dungeon import Dungeon
from pythonProject1.hero import Hero
from pythonProject1.treasure import Treasure


def main():
    hero_name= input("Introduce nombre del héroe: ")#comienza el juego pidiéndose el nombre del héroe
    hero = Hero(hero_name)#se instacia un héreo pasándole como argumento el nombre pedido
    print("Vida de ",hero.name,": ",hero.hp)#se informa de los atriubutos iniciales del héroe
    print("Poder de ataque : ",hero.ad)
    print("Poder de defensa : ",hero.dp)
    dungeon = Dungeon(hero)#se instancia una mazmorra (dungeon) que es donde ocurrirá el juego
    dungeon.play()#da comienzo al juego

if __name__ == "__main__":
    main()