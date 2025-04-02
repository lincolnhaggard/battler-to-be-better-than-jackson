import math

def invis(self,value):
    self.dodge=math.floor(80-(80*(0.916^math.floor(value))))
    self.d_timer=2

def block(self,value):
    self.dmg_reduce=value