from class_functions import *

#stats add to 10
#cleric and ranger
CLASS_STATS={   "Mage":{"health":2,"attack":1,"magic":4,"speed":3,
                             #format unlocklvl:(name,type,value,magic cost,multi)
                             #if move is spc lvl:(name,'spc',value,magic cost,multi,function)
                        "moves":[0,("fire bolt",'dmg',10,5,"mgc"),
                              0,('heal','hl',5,15,"mgc"),
                              3,("fire ball","dmg",25,60,"mgc"),
                              5,('invisibilty',"spc",5,40,"mgc",invis)]},

                "Fighter":{"health":3.5,"attack":3.5,"magic":0.5,"speed":2.5,
                           'moves':[0,('slash',"dmg",5,None,"atk"),
                                    0,("block","spc",5,None,"spd",block),
                                    3,('true strike','spc',10,8,"dmg",true_strike),
                                    5,("stun strike","spc",15,10,"dmg",stun_strike)]},
                                    
                  "Druid":{"health":3.5,"attack":1,"magic":3,"speed":2.5,
                           "moves":[0,("leaf","dmg",5,5,"mgc"),
                                    0,("heal","hl",15,15,"mgc"),
                                    3,("meditate","spc",10,5,"mgc",meditate),
                                    5,("leaf storm","spc",5,30,"mgc",leaf_storm)]},
            }