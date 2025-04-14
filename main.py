from basics import *
from character import Character
from battle import start_battle
from class_stats import CLASS_STATS
import os
import pickle
from level import level


lev=level()
print(lev)
input()



saves=os.listdir("saves")
savechoices=[]
savechoices.append("make new save file")
for save in saves:
    savechoices.append(save[:-4])

clear()
print("choose your save file")
save=makechoice(savechoices)
if save=="make new save file":
    while True:
        clear()
        name=input("Name your save file> ")
        if name in savechoices:
            print("That name is already taken")
            continue
        confirm=input(f"Confirm {name} (Y/N)> ").lower()
        if confirm=="y" or confirm=="yes":
            break
    save=name
    clear()
    print("Choose your class: ")
    player=Character(makechoice(list(CLASS_STATS.keys())))
    with open(f"saves/{save}.pkl","wb") as file:
        pickle.dump((player,level),file)

else:
    with open(f"saves/{save}.pkl","wb") as file:
        player,level=pickle.load(file)





