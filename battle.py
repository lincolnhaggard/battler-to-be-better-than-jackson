import random


def start_battle(cont1,cont2,bot2):
    cont1.start_battle()
    cont2.start_battle()

    while cont1.health>0 and cont2.health>0:
        battle_turn(cont1,cont2,bot2)
    if cont2.health>0:
        print(f"{cont2.name} was victorious")
    elif cont1.heath>0:
        print(f"{cont1.name} was victorious")
    else:
        print("it was a tie")
    input(">")

def battle_turn(cont1,cont2,bot2):
    if cont2.speed>cont1.speed:
        fcont=cont2
        scont=cont1
        bot1=bot2
        bot2=False
    elif cont1.speed>cont2.speed:
        fcont=cont1
        scont=cont2
        bot1=False
    else:
        if random.randint(1,2)==1:
            fcont=cont2
            scont=cont1
            bot1=bot2
            bot2=False
        else:
            fcont=cont1
            scont=cont2
            bot1=False
    

    fcont.attack(scont,bot1)
    if scont.health>0:
        scont.attack(fcont,bot2)