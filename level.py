import random
import math

class level:
    def __init__(self):
        self.stage=[]
        self.playerpos=[None,None]
        self.generate()

    def generate(self):
        colums=10
        rows=4
        maxrooms=3
        minrooms=1
        maxpaths=2
        minpaths=1
        self.colums=colums
        self.rows=rows
        for x in range(colums):
            if x==0:
                toapp=[None]*rows
                paths={}
                options=list(range(self.rows))
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
                options=[]
                for x,i in enumerate(toapp):
                        if i!=None:
                            options.append(x)
                options3=options.copy()
                if len(prepaths)*maxpaths<len(options):
                    for i in list(prepaths.keys()):
                        options2=options.copy()
                        prepaths[i]=[]
                        for _ in range(len(options)):
                            if len(options2)>1:
                                prepaths[i].append(options2.pop(random.randint(0,len(options2)-1)))
                            else:
                                prepaths[i].append(options2.pop(0))
                                
                        del options2
                else:
                    while len(options3)>0:
                        options3=options.copy()
                        for i in list(prepaths.keys()):
                            options2=options.copy()
                            prepaths[i]=[]
                            for _ in range(random.randint(minpaths,maxpaths)):
                                if len(options2)>1:
                                    prepaths[i].append(options2.pop(random.randint(0,len(options2)-1)))
                                    if prepaths[i][-1] in options3:
                                        options3.remove(prepaths[i][-1])
                                else:
                                    prepaths[i].append(options2.pop(0))
                                    if prepaths[i][-1] in options3:
                                        options3.remove(prepaths[i][-1])
                                    break
                                    
                            del options2
                        
                self.stage.append(toapp)
                self.stage.append(paths)
    def __str__(self):
        height=self.rows
        width=self.colums*10
        screen=[]
        for i in range(width):
            screen.append([])
            for x in range(height):
                screen[-1].append(" ")
        for x,i in enumerate(self.stage):
            if isinstance(i,list):
                for y,k in enumerate(i):
                    if k!=None:
                        screen[x*5][y]=str(k)[0]
            
            else:
                for k in range(self.rows):
                    try:
                        path=i[k]
                        #between -4 and 4, 9 units of space
                        screen[x*5-4][k]="-"
                        for j in path:
                            height2=0
                            increase=j-k
                            increase/=7
                            screen[x*5+4][j]="-"
                            
                            for u in range(7):
                                height2+=increase
                                if increase<0:
                                    #nightmare if statement block
                                    if int(math.ceil(height2+increase))<int(math.ceil(height2)):
                                        if screen[x*5-3+u][k+int(math.ceil(height2))]=="-":
                                            screen[x*5-3+u][k+int(math.ceil(height2))]="+"
                                            if screen[x*5-3+u][k+int(math.ceil(height2))-1]==" ":
                                                screen[x*5-3+u][k+int(math.ceil(height2))-1]="-"
                                        elif screen[x*5-3+u][k+int(math.ceil(height2))]=="\\":
                                            screen[x*5-3+u][k+int(math.ceil(height2))]="x"
                                        elif screen[x*5-3+u][k+int(math.ceil(height2))]=="x" or screen[x*5-3+u][k+int(math.ceil(height2))]=="+":
                                            screen[x*5-3+u][k+int(math.ceil(height2))]="#"
                                        elif screen[x*5-3+u][k+int(math.ceil(height2))]==" ":
                                            screen[x*5-3+u][k+int(math.ceil(height2))]="/"
                                    else:
                                        if screen[x*5-3+u][k+int(math.ceil(height2))]=="/" or screen[x*5-3+u][k+int(math.ceil(height2))]=="\\":
                                            screen[x*5-3+u][k+int(math.ceil(height2))]="+"
                                        elif screen[x*5-3+u][k+int(math.ceil(height2))]=="x":
                                            screen[x*5-3+u][k+int(math.ceil(height2))]="#"
                                        elif screen[x*5-3+u][k+int(math.ceil(height2))]==" ":
                                            screen[x*5-3+u][k+int(math.ceil(height2))]="-"
                                else:
                                    if int(math.floor(height2+increase))>int(math.floor(height2)):
                                        if screen[x*5-3+u][k+int(math.floor(height2))]=="-":
                                            screen[x*5-3+u][k+int(math.floor(height2))]="+"
                                            if screen[x*5-3+u][k+int(math.floor(height2))+1]==" ":
                                                screen[x*5-3+u][k+int(math.floor(height2))+1]="-"
                                        elif screen[x*5-3+u][k+int(math.floor(height2))]=="/":
                                            screen[x*5-3+u][k+int(math.floor(height2))]="x"
                                        elif screen[x*5-3+u][k+int(math.floor(height2))]=="x" or screen[x*5-3+u][k+int(math.floor(height2))]=="+":
                                            screen[x*5-3+u][k+int(math.floor(height2))]="#"
                                        elif screen[x*5-3+u][k+int(math.floor(height2))]==" ":
                                            screen[x*5-3+u][k+int(math.floor(height2))]="\\"
                                    else:
                                        if screen[x*5-3+u][k+int(math.floor(height2))]=="/" or screen[x*5-3+u][k+int(math.floor(height2))]=="\\":
                                            screen[x*5-3+u][k+int(math.floor(height2))]="+"
                                        elif screen[x*5-3+u][k+int(math.floor(height2))]=="x":
                                            screen[x*5-3+u][k+int(math.floor(height2))]="#"
                                        elif screen[x*5-3+u][k+int(math.floor(height2))]==" ":
                                            screen[x*5-3+u][k+int(math.floor(height2))]="-"
                    except:
                        pass
        screen2=[]
        for i in range(height):
            screen2.append([])
            for x in range(width):
                screen2[-1].append(" ")
        for k,i in enumerate(screen):
            for y,x in enumerate(i):
                screen2[y][k]=x
                
        toret=""
        for i in screen2:
            for x in i:
                toret+=x
            toret+="\n"
        return toret
    def choose_path(self):
        pass
        
            



    
class room:
    def __init__(self):
        chance=random.randint(1,100)
        if chance<=10:
            self.type="Sshop"
        elif chance<=20:
            self.type="Lelite"
        elif chance<=30:
            self.type="Rrest"
        elif chance<=40:
            self.type="Cchest"
        elif chance<=60:
            self.type="Vevent"
        else:
            self.type="Eenemy"
    def __str__(self):
        return self.type
