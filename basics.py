import keyboard

def readfile(file_name,line=None):
    try:
        f=open(file_name,'r')
    except:
        print(f"File not found '{file_name}'")
        return None
    try:
        lines=f.readlines()
        f.close()
    except:
        print(f"Unable to read file '{file_name}'")
        f.close()
        return None
    try:
        if line==None:
            biglist=[]
            smllist=[]
            smlvar=""
            for line in lines:
                for char in line:
                    if char!=",":
                        smlvar+=char
                    else:
                        smllist.append(smlvar)
                        smlvar=""
                biglist.append(smllist)
                smllist=[]
                smlvar=""
            return biglist
        else:
            smllist=[]
            smlvar=""
            for char in lines[line]:
                if char!=",":
                    smlvar+=char
                else:
                    smllist.append(smlvar)
                    smlvar=""
            if len(smllist)==1:
                smllist=smllist[0]
            return smllist
    except:
        print(f"File '{file_name}' is in an invalid format")
        return None

def writefile(file_name,varlist):
    try:
        f=open(file_name,'w')
    except:
        print(f"File not found '{file_name}'")
        return None
    try:
        towrite=""
        for bigvar in varlist:
            if isinstance(bigvar,list):
                for smlvar in bigvar:
                    towrite+=str(smlvar)
                    towrite+=","
            else:
                towrite+=str(bigvar)
                towrite+=","
            towrite+="\n"
    except:
        print(f"Invalid variable format while trying to write to file '{file_name}'")
    try:
        f.write(towrite)
        f.close()
    except:
        print(f"Unable to write to file '{file_name}'")
        f.close()
        return None
    
def editfile(file_name,varlist,line):
    var=readfile(file_name)
    var[line]=varlist
    writefile(file_name,var)

def clear():
    print("\033[H\033[2J",end="")

def makechoice(choices,num=False):
    while True:
        for num,text in enumerate(choices):
            print(f"{num+1}.{text}")
        user=input(">")
        try:
            user=int(user)
        except:
            print("Not a valid input")
            input(">")
            continue
        try:
            if num:
                print("num")
                return user-1
            else:
                
                return choices[user-1]
        except:
            print("Out of range")
            input(">")
            continue
    
def clr(text,r,g,b,end="\x1b[0m"):
    return f"\x1b[38;2;{r};{g};{b}m{text}{end}"
