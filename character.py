import random



class Character:
    def __init__(self, iclass=random.choice(("Mage","Fighter","Druid","Cleric","Ranger")),xp=0):
        self.iclass=iclass
        self.xp=xp

        self.health=0

    

