import random

#add to 10
CLASS_STATS={"Mage":{"health":0.5,"attack":0.5,"magic":6,"speed":3},}

class Character:
    def __init__(self, iclass=random.choice(("Mage","Fighter","Druid","Cleric","Ranger")),xp=0):
        self.iclass=iclass
        self.xp=xp

        self.health=0

    

