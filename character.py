import random
import math
from basics import *
from class_stats import CLASS_STATS
from class_functions import strgl

MOVE_VALUES={"name":0,'typ':1,"value":2,"cost":3,"multi":4,"func":5}

NAMES=readfile("names.txt")

ABRIVES={"atk":"attack","spd":"speed","mgc":"magic","dmg":"attack"}


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
        self.maxhealth=math.floor(100*self.level*self.stats["health"])
        self.maxmana=math.floor(8.5*self.level*self.stats["magic"])
        self.health=self.maxhealth
        self.mana=self.maxmana
        self.speed=math.floor(self.level+self.stats["speed"])#it is meant to be addition
        self.moves=[]
        for x,move in enumerate(self.stats["moves"]):
            if isinstance(move,int):
                if move<=self.level:
                    self.moves.append(self.stats["moves"][x+1])

        self.dodge=0#chance to dodge
        self.d_timer=0#time left before dodge becomes zero
        self.dmg_reduce=0#amount to reduce damage by
        self.damage=0#damage to deal to the enemy
        self.unblockable=False#if the damage to the enemy is unblockable
        self.stuned=False#if stunned and will skip turn
        self.bonus=0#adds x damage to next attack
        self.multi_hit=0#how many times the attack will hit, less than or equal to one will just disable it
        self.recoil=0#how much damage you take |||


    def attack(self,other,isbot):
        if not self.stuned:
            move=self.choose_move(other,isbot)
            #0 name
            #1 value
            #2 mana cost
            #3 multi
            #4 function
            #start of turn
            self.mana+=math.ceil(self.maxmana*0.16)
            if self.mana>self.maxmana:self.mana=self.maxmana
            self.dmg_reduce=0
            self.d_timer-=1
            if self.d_timer<=0:
                self.dodge=0
            self.unblockable=False
            self.damage=0
            

            if move[2]==None: 
                move[4](self,move[1]*self.stats[ABRIVES[move[3]]],other)
            elif move[2]<self.mana:
                self.mana-=move[2]
                move[4](self,move[1]*self.stats[ABRIVES[move[3]]],other)
            else:
                print("Not enough mana, you should not be able to see this mesage")
                input(">")
            self.damage=math.ceil(self.damage)
            print(self.damage,move)
            if self.damage>0:
                total_damage=0
                dodged_count=0
                hit_count=0
                if self.multi_hit<=1:
                    self.multi_hit=1
                for i in range(self.multi_hit):
                    if (self.unblockable or random.randint(1,100)>other.dodge):
                        if not self.unblockable:
                            self.damage-=other.dmg_reduce
                        self.damage+=self.bonus
                        hit_count+=1
                        if self.damage<=0:
                            self.damage=0
                        total_damage+=self.damage
                        other.health-=self.damage
                    else:
                        dodged_count+=1
                self.bonus=0
                if isbot:
                    if self.multi_hit>1:
                        if hit_count>1:
                            print(f"The enemy hit you {hit_count} times for a total of {total_damage} damge")
                            if dodged_count>0:
                                print(f"You dodged {dodged_count} of the enemies attacks")
                        elif hit_count==1:
                            print(f"The enemy hit you {hit_count} time for a total of {total_damage} damge")
                            if dodged_count>0:
                                print(f"You dodged {dodged_count} of the enemies attacks")
                        else:
                            print("You dodge all of the enemies attacks")
                    else:
                        if dodged_count==1:
                            print("You dodged")
                        else:
                            print(f"The enemy hit you for {total_damage} damage")
                    input(">")
                else:
                    if self.multi_hit>1:
                        if hit_count>1:
                            print(f"You hit the enemy {hit_count} times for a total of {total_damage} damge")
                            if dodged_count>0:
                                print(f"The enemy dodged {dodged_count} of your attacks")
                        elif hit_count==1:
                            print(f"You hit the enemy {hit_count} time for a total of {total_damage} damge")
                            if dodged_count>0:
                                print(f"The enemy dodged {dodged_count} of your attacks")
                        else:
                            print("The enemy dodged all of your attacks")
                    else:
                        if dodged_count==1:
                            print("The enemy dodged")
                        else:
                            print(f"You hit the enemy for {total_damage} damage")
                    input(">")
            else:
                if isbot:
                    print(f"The enemy {move[0]} for {move[1]*self.stats[ABRIVES[move[3]]]}")
                else:
                    print(f"You {move[0]} for {move[1]*self.stats[ABRIVES[move[3]]]}")
                input(">")
        else:
            self.mana+=math.ceil(self.maxmana*0.16)
            if self.mana>self.maxmana:self.mana=self.maxmana
            self.dmg_reduce=0
            self.d_timer-=1
            if self.d_timer<=0:
                self.dodge=0
            self.unblockable=False

            if isbot:
                print("The enemy was stunned")
                input(">")
            else:
                print("you were stunned")
                input(">")

    def print_battle_ui(self,other):
        clear()
        attacks=""
        struggle=True
        for x,move in enumerate(self.moves):
            if x%2==0 and x!=0:
                attacks+="\n"
            mana=""
            manalen=0
            if move[2]!=None:
                if move[2]>self.mana:
                    mana=clr(f"M:{move[2]}",50,25,25,)
                    manalen=len(f"M:{move[2]}")
                else:
                    mana=f"M:{move[2]}"
                    manalen=len(f"M:{move[2]}")
                    struggle=False
            else:
                struggle=False
            attacks+=f"{x+1}.{move[0]}{" "*(15-len(move[0])-manalen)} {mana}   "
        if struggle:
            x+=1
            if x%2==0 and x!=0:
                attacks+="\n"
            attacks+=f"{x+1}.struggle{" "*(15-len("struggle"))}    "

        print(
f"""---------------------------------------
|                {other.name}
|                {clr(f"{"#"*math.ceil(8*other.health/other.maxhealth)}{" "*(8-math.ceil(8*other.health/other.maxhealth))}({other.health}/{other.maxhealth})",hc(other.health/other.maxhealth)[0],hc(other.health/other.maxhealth)[1],hc(other.health/other.maxhealth)[2])}
|
|{self.name}
|{clr(f"{"#"*math.ceil(8*self.health/self.maxhealth)}{" "*(8-math.ceil(8*self.health/self.maxhealth))}({self.health}/{self.maxhealth})",hc(self.health/self.maxhealth)[0],hc(self.health/self.maxhealth)[1],hc(self.health/self.maxhealth)[2])}
---------------------------------------
{clr(f"{"#"*math.ceil(8*self.mana/self.maxmana)}{" "*(8-math.ceil(8*self.mana/self.maxmana))}({self.mana}/{self.maxmana})",0,0,255)}
{attacks}""")

    def choose_move(self,other,isbot):
        if isbot:
            choices=[]
            for i in self.moves:
                if i[2]==None or i[2]<self.mana:
                    choices.append(i)
            if len(choices)<=0:
                return ("struggle",5,None,"atk",strgl)
            return random.choice(list(choices))
        else:
            
            while True:
                struggle=True
                for x,move in enumerate(self.moves):
                    if move[2]!=None:
                        if move[2]<=self.mana:
                            
                            struggle=False
                    else:
                        struggle=False

                user=input(">")
                try:
                    user=int(user)
                except:
                    print("Not a valid input")
                    input(">")
                    self.health-=1
                    continue
                try:
                    if struggle:
                        if user-1==x:
                            return ("struggle",5,None,"atk",strgl)
                        else:
                            n=0/0
                    if self.moves[user-1][2]!=None and self.mana<self.moves[user-1][2]:
                        n=0/0
                    return self.moves[user-1]
                except:
                    print("Unavailable move")
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

def hc(num):
    return (int(math.floor(215*(1-num)))+40, int(math.floor(215*(num)))+40, 21)
    

