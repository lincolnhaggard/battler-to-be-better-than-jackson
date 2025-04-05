import random


def start_battle(cont1,cont2,bot2):
    cont1.start_battle()
    cont2.start_battle()

    while cont1.health>0 and cont2.health>0:
        battle_turn(cont1,cont2,bot2)

def battle_turn(cont1,cont2,bot2):
    if cont2.speed>cont1.speed:
        fcont=cont2
        scont=cont1
    elif cont1.speed>cont2.speed:
        fcont=cont1
        scont=cont2
    else:
        (fcont,scont)=random.shuffle((cont1,cont2))
    
    fcont.attack(scont,False)
    scont.attack(fcont,bot2)