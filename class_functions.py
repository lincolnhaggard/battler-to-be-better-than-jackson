import math
import random


def dmg(self,value,other):
    self.damage=value

def heal(self,value,other):
    self.heal=value

def strgl(self,value,other):
    self.damage=value
    self.recoil=math.floor(value/2)

def invis(self,value,other):
    self.dodge=math.floor(80-(80*(0.916^math.floor(value))))
    self.d_timer=2

def block(self,value,other):
    self.dmg_reduce=value

def true_strike(self,value,other):
    self.dmg=value
    self.unblockable=True

def stun_strike(self,value,other):
    self.dmg=value
    other.stuned=True

def meditate(self,value,other):
    self.bonus=value

def leaf_storm(self,value,other):
    self.dmg=value
    self.multi_hit=random.randint(3,10)

def body_slam(self,value,other):
    self.dmg=math.floor(self.health/3)

def regenerate(self,value,other):
    self.regen=value

def arrow_roll(self,value,other):
    self.dmg=value
    self.dmg_reduce=math.floor(value/2)

def evasion(self,value,other):
    self.dodge=math.floor(80-(80*(0.916^math.floor(value+self.dodge))))
    if self.d_timer==0:
        self.d_timer=2
    else:
        self.d_timer+=1