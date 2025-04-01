from basics import *

clear()
writefile("test.txt",[[1,2,3],2,3])

print(readfile("test.txt"))

editfile("test.txt",[2,3],1)

print(readfile("test.txt"))

print(makechoice(["choice_1","choice_2"]))