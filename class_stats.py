from class_functions import *

#stats add to 10
CLASS_STATS={   "Mage":{"health":0.5,"attack":0.5,"magic":4,"speed":3,'special':2,
                             #format unlocklvl:(name,type,value,magic cost)
                             #if move is spc lvl:(name,'spc',value,magic cost,function)
                        "moves":{0:("fire bolt",'dmg',14,5),
                              0:('heal','hl',5,15),
                              3:("fire ball","dmg",40,60),
                              5:('invisibilty',"spc",5,40,invis)}},

                "Fighter":{"heath":2.5,"attack":2.5,"magic":0.5,"speed":2.5,"special":2,
                           'moves':{0:('slash',"dmg",5,None),
                                    0:("block","spc",5,None,block),
                                    3:('swift strike','spc',10,8,)}}}