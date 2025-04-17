import random

class level:
    def __init__(self):
        self.stage=[]
        self.generate()

    def generate(self):
        colums=10
        rows=8
        maxrooms=5
        minrooms=3
        maxpaths=3
        minpaths=1
        self.colums=colums
        self.rows=rows
        for x in range(colums):
            if x==0:
                toapp=[None]*rows
                paths={}
                options=[0,1,2,3,4]
                random.shuffle(options)
                for i in range(3):
                    choice=options.pop(0)
                    toapp[choice]=room()
                    paths[choice]=None
                self.stage.append(toapp)
                self.stage.append(paths)
            else:
                prepaths=self.stage[-1]
                toapp=[None]*self.rows
                paths={}
                rooms=0
                y=0
                while rooms<minrooms:
                    for y in range(rows):
                        if random.randint(1,3)==1 and rooms<maxrooms:
                            toapp[y]=room()
                            paths[y]="ready"
                            rooms+=1
                choice=random.randint(0,4)
                toapp[choice]=room()
                paths[choice]=None
                options=[]
                for x,i in enumerate(toapp):
                        if i!=None:
                            options.append(x)
                for i in list(prepaths.keys()):
                    options2=options.copy()
                    prepaths[i]=[]
                    for _ in range(random.randint(minpaths,maxpaths)):
                        if len(options2)>1:
                            prepaths[i].append(options2.pop(random.randint(0,len(options2)-1)))
                        else:
                            prepaths[i].append(options2.pop(0))
                            break
                    del options2
                    
                self.stage.append(toapp)
                self.stage.append(paths)
    def __str__(self):
        height=self.rows
        width=self.colums*2
        screen=[]
        for i in range(width):
            screen.append([])
            for x in range(height):
                screen[-1].append("")
        for x,i in enumerate(self.stage):
            if isinstance(i,list):
                for y,k in enumerate(i):
                    if k!=None:
                        screen[x][y]=str(k)[0]
                    else:
                        screen[x][y]=" "
            else:
                for k in range(self.rows):
                    try:
                        screen[x][k]=f" {i[k]} {" "*(20-len(str(i[k])))}"
                    except:
                        screen[x][k]=f"  {" "*(20)}"
        screen2=[]
        for i in range(height):
            screen2.append([])
            for x in range(width):
                screen2[-1].append("")
        for k,i in enumerate(screen):
            for y,x in enumerate(i):
                screen2[y][k]=x
        toret=""
        for i in screen2:
            for x in i:
                toret+=x
            toret+="\n"
        return toret
        
            



    
class room:
    def __init__(self):
        chance=random.randint(1,100)
        if chance<=10:
            self.type="shop"
        elif chance<=20:
            self.type="elite"
        elif chance<=30:
            self.type="rest"
        elif chance<=40:
            self.type="chest"
        elif chance<=60:
            self.type="event"
        else:
            self.type="enemy"
    def __str__(self):
        return self.type
