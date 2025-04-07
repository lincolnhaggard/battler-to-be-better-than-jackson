from class_functions import *

#stats add to 10
#cleric and ranger
CLASS_STATS={   "Mage":{"health":2,"attack":1,"magic":4,"speed":3,
                             #format unlocklvl:(name,value,magic cost,multi,function)

                        "moves":[0,("fire bolt",10,50,"mgc",dmg),
                              0,('heal',5,15,"mgc",heal),
                              3,("fire ball",25,60,"mgc",dmg),
                              5,('invisibilty',5,40,"mgc",invis)]},

                "Fighter":{"health":3.5,"attack":3.5,"magic":0.5,"speed":2.5,
                           'moves':[0,('slash',5,None,"atk",dmg),
                                    0,("block",5,None,"spd",block),
                                    3,('true strike',10,8,"dmg",true_strike),
                                    5,("stun strike",15,10,"dmg",stun_strike)]},
                                    
                  "Druid":{"health":3.5,"attack":1,"magic":3,"speed":2.5,
                           "moves":[0,("leaf",5,5,"mgc",dmg),
                                    0,("heal",15,15,"mgc",heal),
                                    3,("meditate",10,5,"mgc",meditate),
                                    5,("leaf storm",5,30,"mgc",leaf_storm)]},
            }