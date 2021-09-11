Dict = {"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
Dict2 = {"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0}
listinst = ["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
TypeA = ["add","sub","mul","xor","or","and"]
TypeB = ["rs","ls"]
TypeC = ["div","not","cmp"]
TypeD = ["ld","st"]
TypeE = ["jmp","jlt","jgt","je"]
TypeF = ["hlt"]
check=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","0","1","2","3","4","5","6","7","8","9","_"]
checknum=["0","1","2","3","4","5","6","7","8","9"]
V=0
E=0
L=0
G=0
n = 0
v=0
count=0


def decimalToBinary(n):
    b = bin(n).replace("0b", "")
    return "0"*(8-len(b))+b

def typeA(line , count):
    # print("A")
    lst = list(line.split())
    a=""
    t=0
    if(lst[0][-1]==":"):
        t=1

    for i in range(t+1,len(lst)):  ### reg name wrong  ERROR ###
        if lst[i] not in Dict :
            print(" Wrong name of register in line {}".format(count))
            quit() 


    if(len(lst)<5):### less than required instruction in type A line  ERROR ###
    #~#
        if(t==1):
            print("ERROR NO INSTRUCTION PROVIDED AFTER LABEL line {}".format(count))
            quit()
        else:
            if(len(lst)<4):
                print("less than required instructions line ")
                quit()
    elif(len(lst)>4):
        if(t==1 and len(lst)>5):
            print("more than required instruction after LABEL line {}".format(count))
            quit()
        else:
            if(t==0 and len(lst)>4):
                print("more than required instructions line ")
                quit()

    if lst[t] == 'add':
        a="00000"+"00"+Dict[lst[t+1]]+Dict[lst[t+2]]+Dict[lst[t+3]]
        # print("h")
        # print(a)
        # if(Dict2[lst[t+2]]+Dict2[lst[t+3]])>255 or (Dict2[lst[t+2]]+Dict2[lst[t+3]]<0):
        #     V=1
    elif lst[t]=='sub':
        a="00001"+"00"+Dict[lst[t+1]]+Dict[lst[t+2]]+Dict[lst[t+3]]
        # if(Dict2[lst[t+3]>Dict2[lst[t+2]]]):
        #     Dict2[lst[t+1]]=0
        #     V=1
    elif lst[t]=='mul':
        a="00110"+"00"+Dict[lst[t+1]]+Dict[lst[t+2]]+Dict[lst[t+3]]
        # if((Dict2[lst[t+2]]*Dict2[lst[t+3]])>255 or (Dict2[lst[t+2]]*Dict2[lst[t+3]]<0)):
        #     V=1
    elif lst[t]=='xor':
        a="01010"+"00"+Dict[lst[t+1]]+Dict[lst[t+2]]+Dict[lst[t+3]]
    elif lst[t]=='or':
        a="01011"+"00"+Dict[lst[t+1]]+Dict[lst[t+2]]+Dict[lst[t+3]]
    elif lst[t]=='and':
        a="01100"+"00"+Dict[lst[t+1]]+Dict[lst[t+2]]+Dict[lst[t+3]]
    return a


def typeF(line):
    lst = list(line.split())
    a=""
    t=0

    if(lst[0][-1]==":"):
        t=1

    if(len(lst)>1):
        if(t==1 and len(lst)>2):
            print("more than required instruction after LABEL line ")
            quit()
        else:
            if(t==0 and len(lst)>1):
                print("more than required instructions line ")
                quit()
    

    if lst[t] == "hlt":
        a="1001100000000000"   

    return a


def typeE(line , count):
    lst = list(line.split())
    a=""
    t=0
    # print(Dict.items())
    if(lst[0][-1]==":"):
        t=1

    if(len(lst)<3):### less than required instruction in type A line  ERROR ###
    #~#
        if(t==1):
            print("ERROR NO INSTRUCTION PROVIDED AFTER LABEL line {}".format(count))
            quit()
        else:
            if(len(lst)<2):
                print("less than required instructions line ")
                quit()
    elif(len(lst)>2):
        if(t==1 and len(lst)>3):
            print("more than required instruction after LABEL line {}".format(count))
            quit()
        else:
            if(t==0 and len(lst)>2):
                print("more than required instructions line ")
                quit()

    if(lst[t+1] not in labelList):
        print("TYPO ")
        quit()

    if lst[t]=="jmp":
        a="01111"+"000"+Dict[lst[t+1]]
    elif lst[t] =="jlt":
        a="10000"+"000"+Dict[lst[t+1]]
    elif lst[t] =="jgt":
        a="10001"+"000"+Dict[lst[t+1]]
    elif lst[t] =="je":
        a="10010"+"000"+Dict[lst[t+1]]
    return a


def typeD(line , count):
    lst = list(line.split())
    a=""
    t=0
    if(lst[0][-1]==":"):
        t=1

    if(len(lst)<4):### less than required instruction in type A line  ERROR ###
    #~#
        if(t==1):
            print("ERROR NO INSTRUCTION PROVIDED AFTER LABEL line {}".format(count))
            quit()
        else:
            if(len(lst)<3):
                print("less than required instructions line {}".format(count))
                quit()
    elif(len(lst)>3):
        if(t==1 and len(lst)>4):
            print("more than reqd instruction after LABEL line {}".format(count))
            quit()
        else:
            if(t==0 and len(lst)>3):
                print("more than required instructions line {}".format(count))
                quit()

    if(lst[t+1] not in Dict2):
        print("TYPO ERROR of reg name in line {}".format(count))  ## ERROR not reg 
        quit()

    if(lst[t+2] not in varList):
        print("var not initiliased in line {}".format(count))  ## ERROR not init var
        quit()

    if(lst[t]=="ld"):
        a="00100"+Dict[lst[t+1]]+Dict[lst[t+2]]
    elif(lst[t]=="st"):
        a="00101"+Dict[lst[t+1]]+Dict[lst[t+2]]
    return a


def typeB(line,count):
    a=""
    lst=list(line.split())
    t=0
    if(lst[0][-1]==":"):
        t=1

    if(len(lst)<4):### less than required instruction in type A line  ERROR ###
    #~#
        if(t==1):
            print("ERROR NO INSTRUCTION PROVIDED AFTER LABEL line {}".format(count))
            quit()
        else:
            if(len(lst)<3):
                print("less than required instructions line ")
                quit()
    elif(len(lst)>3):
        if(t==1 and len(lst)>4):
            print("more than reqd instruction after LABEL line {}".format(count))
            quit()
        else:
            if(t==0 and len(lst)>3):
                print("more than required instructions line ")
                quit()
    
    if(lst[t+1] not in Dict2):
        print("TYPO ERROR of reg name in line {}".format(count))  ## ERROR not reg 
        quit()

    str=""
    str+=lst[t+2]
    if str[0]!= "$":
        print("not an correct imm value in line {}".format(count))  ## ERROR not imm
        quit()
    for i in str[1:]:
        if i not in checknum:
            print("not an imm value in line {}".format(count))  ## ERROR not imm
            quit()

    if lst[t]=="mov":
        # if lst[t+2] == "FLAGS":
        #     lst[t+2] = "p" + Dict["FLAGS"]
        a="00010"+Dict[lst[t+1]]+decimalToBinary(int(lst[t+2][1:]))
    if lst[t]=="rs":
        a="01000"+Dict[lst[t+1]]+decimalToBinary(int(lst[t+2][1:]))
    if lst[t]=="ls":
        a="01001"+Dict[lst[t+1]]+decimalToBinary(int(lst[t+2][1:]))
    return a

def typeC(line , count):
    a=""
    lst=list(line.split())
    t=0
    if(lst[0][-1]==":"):
        t=1

    if(len(lst)<4):### less than required instruction in type A line  ERROR ###
    #~#
        if(t==1):
            print("ERROR NO INSTRUCTION PROVIDED AFTER LABEL line {}".format(count))
            quit()
        else:
            if(len(lst)<3):
                print("less than required instructions line ")
                quit()
    elif(len(lst)>3):
        if(t==1 and len(lst)>4):
            print("more than reqd instruction after LABEL line {}".format(count))
            quit()
        else:
            if(t==0 and len(lst)>3):
                print("more than required instructions line ")
                quit()

    flg=0
    if(lst[t]=="mov" and lst[t+1] in Dict2 and lst[t+2]=="FLAGS"):
        flg=1

    if(flg==0 and (lst[t+1] not in Dict2 or lst[t+2] not in Dict)):
        print("TYPO ERROR of reg name ")  ## ERROR not reg 
        quit()

    if lst[t]=="mov":
        # if lst[t+2] == "FLAGS":
            # lst[t+2] = Dict["FLAGS"]
        a="0001100000"+Dict[lst[t+1]]+Dict[lst[t+2]]
    if lst[t]=="div":
        a="0011100000"+Dict[lst[t+1]]+Dict[lst[t+2]]
    if lst[t]=="not":
        a="0110100000"+Dict[lst[t+1]]+Dict[lst[t+2]]
    if lst[t]=="cmp":
        a="0111000000"+Dict[lst[t+1]]+Dict[lst[t+2]]
        # if(Dict2[lst[t+1]]<Dict2[lst[t+2]]):
        #     L=1
        # elif Dict2[lst[t+1]]>Dict2[lst[t+2]]:
        #     G=1
        # else:
        #     E=1
    return a

# fixed input stdin

from sys import stdin
string = ""
for s in stdin:
    if s=="":
        break
    string = string +s
# print(string)
# asscode = open("a1.txt","r")
# for s in asscode.readlines():
#     # asscode = asscode + s + "\n"
#     n=n+1
#     # print(s)
#     if (s==""):
#         break
    # string=string+s
    # while(string!=""):
    #     n = n+1
varList=[]

# lst = string.split("\n")
# print(lst)
# print(len(lst))
# quit()

# n = len(asscode.readlines())
n = len(string.splitlines())
if (n>256):
    print("Commands Exceed the valid Limit")
    quit()
# print(n)
labelList = []
# asscode.seek(0,0)
c=0
for s in string.splitlines(): # for s in asscode.readlines():
    # print("pallav1")
    lst=list(s.split())
    c+=1
    # print(lst)
    if len(lst)>0 and lst[0]=="var":
        if len(lst)!=2:
            # print(lst)
            print("Variable Syntax Error at line {}".format(c))
            quit()


        strs=""
        strs+=lst[1]
        for i in strs:   ## ERROR correct way of defining var name
            if (i not in check ):
                print("Incorrect way of defining var in line {} ".format(i))
                quit()


        varList.append(lst[1])
        v+=1
    else:
        continue

# print(varList)
a = set(varList)        ## ERROR var defined again
if len(varList) != len(a):
    print("Variable defined again")
    quit()


ncount = 0
# asscode.seek(0,0)

for s in string.splitlines(): # for s in asscode.readlines():
    lst = s.split()

    # print(lst)
    # print(len(lst))
    if(":" in lst):  ## space between label and : ERROR
        print("Incorrect way of defining label , no space between label name and colon ")
        quit()
    else:
        if len(lst)>0:
            if lst[0][-1] == ":":
                # print(lst)
                # print(varList)
                # print(labelList)
                labelList.extend(varList)
                # print(labelList)
                if lst[0][:-1] not in labelList:
                    str=""
                    str+=lst[0][:-1]
                    for i in str:
                        if(i not in check):
                            print("Incorrect way of defining label in line {}".format(ncount))    ### way of writing in label ERROR ###
                            quit()
                    # labelList.append(lst[0])

                else:
                    print("Label defined again line {}".format(ncount))  ### ERROR label define again
                    quit()
        # print(labelList)
            # print(lst[0])
                if lst[0][:-1] not in labelList:
                    labelList.append(lst[0][:-1])
                # print(lst[0][:-1])
                    Dict[lst[0][:-1]] = decimalToBinary(ncount-v)
                else:
                    print("Label defined Again")
                    quit()
                # print(Dict.items())
            # else:
            #     print("Label defined again line {}".format(ncount))
            #     quit()

    ncount+=1
    # print(ncount)

i=1
temp=[]
for s in string.splitlines():
    temp= s.split()
    if(i<n):
        for j in temp:
            if(j=="hlt"):
                print("hlt defined incorrectly at line {} ".format(i))
                quit()
    i=i+1

count = 0
# print("p")
for i in range(len(varList)):
    # print("pallav2")
    # print(varList[i])
    Dict[varList[i]] = decimalToBinary(n-v+i)
# print(Dict.items())

# asscode.seek(0,0)

for s in string.splitlines():# for s in asscode.readlines():
    # print("pallav3")
    if (count < v):
        count+=1
        # print(count)
        continue
    lst=list(s.split())
    # print(lst)
    # if lst[0]=="var":
        # print("error line{}".format(count))
        # break
    if len(lst)>0:
        if lst[0][-1] == ":":
        # print("pallav")
        # if lst[0][:-1:] not in labelList:
        #     labelList.append(lst[0][:-1:])
        #     # print(lst[0][:-1:])
        #     Dict[lst[0][:-1:]] = decimalToBinary(count)
        #     print(Dict.items())
        # else:
        #     print("Label defined again line {}".format(count))
        #     break
        # if lst[0][-2] == " ":
        #     print("error in line {}".format(count))
        #     break
        # else:
        #     Dict[lst[0][0:-2]] = decimalToBinary(count)
            if(lst[1] in TypeA):
                print(typeA(s,count))
            elif(lst[1] in TypeB):
                print(typeB(s,count))
            elif(lst[1] in TypeC):
                print(typeC(s,count))
            elif(lst[1] in TypeD):
                print(typeD(s , count))
            elif(lst[1] in TypeE):
                print(typeE(s,count))
            elif(lst[1] in TypeF):
                print(typeF(s))
                quit()
            elif(lst[1]=="mov" and lst[3][0]=="R" or lst[3]=="FLAGS"):
                print(typeC(s),count)
            elif(lst[1]=="mov" and (lst[3][0]=="$")):
                print(typeB(s),count)
            else:
                print("syntax error ")  # ERROR
                quit()
        
        else:
            if(lst[0] in TypeA):
                print(typeA(s,count))
            elif(lst[0] in TypeB):
                print(typeB(s,count))
            elif(lst[0] in TypeC):
                print(typeC(s,count))
            elif(lst[0] in TypeD):
                print(typeD(s , count))
            elif(lst[0] in TypeE):
                print(typeE(s,count))
            elif(lst[0] in TypeF):
                print(typeF(s))
                quit()
            elif(lst[0]=="mov" and lst[2][0]=="R" or lst[2]=="FLAGS"):
                print(typeC(s,count))
            elif(lst[0]=="mov" and (lst[2][0]=="$")):
                print(typeB(s,count))
            else:
                print("syntax error ")  # ERROR
                quit()
            
    count+=1