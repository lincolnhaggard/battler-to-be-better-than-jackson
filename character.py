import random
import math
from basics import *
from class_stats import CLASS_STATS

MOVE_VALUES={"name":0,'typ':1,"value":2,"cost":3,"multi":4,"func":5}

NAMES=readfile("names.txt")



class Character:
    def __init__(self, iclass=None,xp=0):
        self.iclass=iclass
        if iclass==None:
            self.iclass=random.choice(list(CLASS_STATS.keys()))
        self.xp=xp
        self.level=1
        self.stats=CLASS_STATS[self.iclass]
        self.name=generate_name()
    
    def __str__(self):
        return f"LVL:{self.level} {self.iclass} {self.name}"
        
    
    def start_battle(self):
        #defines and resets all the attributes used in battle
        self.maxhealth=math.floor(25*self.level*self.stats["health"])
        self.maxmagic=math.floor(8.5*self.level*self.stats["magic"])
        self.health=self.maxhealth
        self.magic=self.maxmagic
        self.speed=math.floor(self.level+self.stats["speed"])#it is meant to be addition
        self.moves=[]
        for x,move in enumerate(self.stats["moves"]):
            if isinstance(move,int):
                if move<=self.level:
                    self.moves.append(self.stats["moves"][x+1])

        self.dodge=0#chance to dodge
        self.d_timer=0#time left before dodge becomes zero
        self.dmg_reduce=0#amount to reduce damage by
        self.dmg=0#damage to deal to the enemy
        self.unblockable=False#if the damage to the enemy is unblockable
        self.stuned=False#if stunned and will skip turn
        self.bonus=0#adds x damage to next attack
        self.multi_hit=0#how many times the attack will hit, less than or equal to one will just disable it


    def attack(self,other,isbot):
        self.choose_move(other,isbot)

    def choose_move(self,other,isbot):
        if isbot:
            return random.choice(list(self.moves))
        else:
            attacks=""
            for x,move in enumerate(self.moves):
                if x%2==0 and x!=0:
                    attacks+="\n"
                attacks+=f"{x+1}.{move[0]}{" "*(10-len(move[0]))}"
            while True:
                clear()
                print(
f"""---------------------------------------
|            {other.name}
|            {"#"*math.ceil(8*other.health/other.maxhealth)}{"#"*(8-math.ceil(8*other.health/other.maxhealth))}({other.health}/{other.maxhealth})
|
|{self.name}
|{"#"*math.ceil(8*self.health/self.maxhealth)}{"#"*(8-math.ceil(8*self.health/self.maxhealth))}({self.health}/{self.maxhealth})
---------------------------------------
{attacks}""")
                user=input(">")
                try:
                    user=int(user)
                except:
                    print("Not a valid input")
                    input(">")
                    continue
                try:
                    return self.moves[user-1]
                except:
                    print("Out of range")
                    input(">")
                    continue

def generate_name():
    if random.randint(1,2)==1:
        midname=random.choice(NAMES[0])
    else:
        midnames=random.choices(NAMES[1],k=random.randint(1,3))
        midname=""
        for name in midnames:
            midname+=name.lower()
        midname=midname.title()
    if random.randint(1,2)==1:
        prefix=random.choice(NAMES[2])+" "
    else:
        prefix=""
    if random.randint(1,2)==1:
        sufix=" The "+random.choice(NAMES[3])
    else:
        sufix=""
    return prefix+midname+sufix
    

