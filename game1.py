from random import randint as rd

def atak1(player1, player2, power):
    hit = rd(player1[1], player1[1] * 2) * power
    print(f" нанесли {hit} урона ")
    player2[0] -= hit
    print(f"у врага  {player2[0]} здоровья ")


player = False
enemy = [150, 9]


while not player :
    x = int(input("Выбери персонажа дурачок/отличник "))
    if x == 1:
        player = [200, 6]
    elif x == 2:
        player = [100, 12]
    else:
        print('False////')



while player[0] > 0 and enemy[0] > 0:


    power = int(input("Выбери удар \n1) простой урона \n2) рискованый  \n --- "))



    print("вы ------------------------------------")
    if power == 1:
        atak1(player, enemy, power)
    elif power == 2:
        if rd(1, 2) % 2 == 0:
            atak1(player, enemy, power)
        else:
            print("промахнулся")


    print("враг ------------------------------------")
    if rd(1,2)%2 == 0:
        atak1(enemy, player, 2)
    else:
        print("промахнулся")