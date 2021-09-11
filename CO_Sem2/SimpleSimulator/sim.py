import numpy as np
import matplotlib.pyplot as plt

Dict = {"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
RegDict = {"000":"R0","001":"R1","010":"R2","011":"R3","100":"R4","101":"R5","110":"R6","111":"FLAGS"}
Dict2 = {"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0 , "FLAGS" : 0}
listinst = ["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
TypeA = ["add","sub","mul","xor","or","and"]
TypeAOP = ["00000", "00001" , "00110" , "01010" , "01011" , "01100"]
TypeB = ["rs","ls"]
TypeBOP = ["00010" , "01000" , "01001"]
TypeC = ["div","not","cmp"]
TypeCOP = ["00011" , "00111" ,"01101" , "01110"]
TypeD = ["ld","st"]
TypeDOP = ["00100","00101"]
TypeE = ["jmp","jlt","jgt","je"]
TypeEOP = ["01111","10000","10001","10010"]
TypeF = ["hlt"]
TypeFOP = ["10011"]
MemDict = {}
Dict3 = {"111":"0"*16}

cycle =0 
PC = "0"*8
machinecode = ""
cyclst=[0]
memlist=[0]
V ="0"
L ="0"
G ="0"
E ="0"

def decimalToBinary(n):
    b = bin(int(n)).replace("0b", "")
    return "0"*(8-len(b))+b

def decimalToBinary1(n):
    b = bin(int(n)).replace("0b", "")
    return "0"*(16-len(b))+b

for i in range(256):
    MemDict[decimalToBinary(i)] = "0"*16

from sys import stdin
string1 = ""
for s in stdin:
    if s=="":
        break
    string1 = string1 +s
# string1 = ""
# file = open("a.txt","r")
# for line in file:
#     string1 += line 

machinecode = string1.splitlines()
# print(machinecode)
j=0
for line in machinecode:
    # print(line)
    MemDict[decimalToBinary(j)] = line
    # print(j)
    # print(MemDict[decimalToBinary(j)])
    j+=1
    
# check once 
def binaryToDecimal(n):
    return int(str(n),2)

def identify(string):
    global cycle 
    global PC
    global Dict3,V,L,G,E
    
    # print(Dict2)
    # print(PC)
    # print(len(machinecode))
    PC = decimalToBinary(binaryToDecimal(PC)+1)

    if int(PC,2)<len(machinecode):
        if string[:5] in TypeAOP:
            # Dict3 = {"111":"0"*12+V+L+G+E}
            V,L,G,E = "0","0","0","0"
            Dict2["FLAGS"] = 0
            if string[:5] == TypeAOP[0]:
                if (Dict2[RegDict[string[10:13]]] + Dict2[RegDict[string[13:16]]])>65535:
                    V="1"
                    Dict2[RegDict[string[7:10]]] = (Dict2[RegDict[string[10:13]]] + Dict2[RegDict[string[13:16]]])%65535
                else:
                    Dict2[RegDict[string[7:10]]] = (Dict2[RegDict[string[10:13]]] + Dict2[RegDict[string[13:16]]])
            elif string[:5] == TypeAOP[1]:
                if((Dict2[RegDict[string[10:13]]] < Dict2[RegDict[string[13:16]]])):
                    V="1"
                    Dict2[RegDict[string[7:10]]]=0
                else:
                    Dict2[RegDict[string[7:10]]] = (Dict2[RegDict[string[10:13]]] - Dict2[RegDict[string[13:16]]])

            elif string[:5] == TypeAOP[2]:
                if((Dict2[RegDict[string[10:13]]]* Dict2[RegDict[string[13:16]]]))>65535:
                    V = "1"
                    Dict2[RegDict[string[7:10]]] = (Dict2[RegDict[string[10:13]]]* Dict2[RegDict[string[13:16]]])%65535
                else:
                    Dict2[RegDict[string[7:10]]] = (Dict2[RegDict[string[10:13]]]* Dict2[RegDict[string[13:16]]])

            elif string[:5] == TypeAOP[3]:
                str12 = ""
                for i in range(16):
                    if decimalToBinary1(Dict2[RegDict[string[10:13]]])[i] == decimalToBinary1(Dict2[RegDict[string[13:16]]])[i]:
                        str12+="0"
                    else:
                        str12+="1"
                Dict2[RegDict[string[7:10]]] = int(str12,2)

            elif string[:5] == TypeAOP[4]:
                Dict2[RegDict[string[7:10]]] = (Dict2[RegDict[string[10:13]]] | Dict2[RegDict[string[13:16]]])
            elif string[:5] == TypeAOP[5]:
                Dict2[RegDict[string[7:10]]] = (Dict2[RegDict[string[10:13]]] & Dict2[RegDict[string[13:16]]])

        # if in typebOP....
        elif string[:5] in TypeBOP:
            # Dict3 = {"111":"0"*16}
            V,L,G,E = "0","0","0","0"
            Dict2["FLAGS"] = 0
            if string[:5] == TypeBOP[0]:
                Dict2[RegDict[string[5:8]]] = int(string[8:16],2)
                # Dict2[RegDict[string[5:8]]] = decimalToBinary(binaryToDecimal(string[8:16]))
            elif string[:5] == TypeBOP[1]:
                Dict2[RegDict[string[5:8]]] = decimalToBinary(binaryToDecimal(int(Dict2[RegDict[string[5:8]]])) >> binaryToDecimal(string[8:16]))
            elif string[:5] == TypeBOP[2]:
                Dict2[RegDict[string[5:8]]] = decimalToBinary(binaryToDecimal(int(Dict2[RegDict[string[5:8]]])) << binaryToDecimal(string[8:16]))

        elif string[:5] in TypeCOP:
            
            if string[:5] == TypeCOP[0]:
                if "111" == string[13:16]:
                    Dict2[RegDict[string[10:13]]] = binaryToDecimal("0"*12+V+L+G+E)
                else:
                    Dict2[RegDict[string[10:13]]] = (Dict2[RegDict[string[13:16]]])
                # print(Dict2[RegDict[string[13:16]]])
            V,L,G,E = "0","0","0" , "0"
            if string[:5] == TypeCOP[1]:
                Dict2["R0"] = decimalToBinary(binaryToDecimal((Dict2[RegDict[string[10:13]]])) // binaryToDecimal(Dict2[RegDict[string[13:16]]]))
                Dict2["R1"] = decimalToBinary(binaryToDecimal((Dict2[RegDict[string[10:13]]])) % binaryToDecimal(Dict2[RegDict[string[13:16]]]))
            elif string[:5] == TypeCOP[2]:
                Dict2[RegDict[string[10:13]]] = decimalToBinary(~(binaryToDecimal(Dict2[RegDict[string[13:16]]])))
            elif string[:5] == TypeCOP[3]:
                # Dict3 = {"111":"0"*16}
                # L,G,E = "0","0","0"
                Dict2["FLAGS"] = 0
                if Dict2[RegDict[string[10:13]]]<Dict2[RegDict[string[13:16]]]:
                    # Dict3["111"] = "0*13"+"1"+"0"*2
                    # Dict3["111"] = "0*13"+"1"+"0"*2
                    L="1"
                if Dict2[RegDict[string[10:13]]]>Dict2[RegDict[string[13:16]]]:
                    # Dict3["111"] = "0*14"+"1"+"0"*1
                    G = "1"
                if Dict2[RegDict[string[10:13]]] == Dict2[RegDict[string[13:16]]]:
                    # Dict3["111"] = "0*15"+"1"
                    E="1"
                    # Dict2["FLAGS"] = 1
                Dict2["FLAGS"] = int("0"*12+V+L+G+E,2)
                # print(Dict2["FLAGS"])
            
            if RegDict[string[13:16]] == "FLAGS":
                    # Dict3 = {"111":"0"*16}
                    V,L,G,E = "0","0","0","0"
                    Dict2["FLAGS"] = 0
            # elif string[:5] == TypeCOP[3]:
            #     Dict2[RegDict[string[7:10]]] = (binaryToDecimal((Dict2[string[10:13]])) + binaryToDecimal(Dict2[string[13:16]]))
            # Compare function -- flags set krne h..ye dekh lena
        elif string[:5] in TypeDOP:
            # Dict3 = {"111":"0"*16}
            V,L,G,E = "0","0","0","0"
            Dict2["FLAGS"] = 0
            if(string[:5]==TypeDOP[0]):
                Dict2[RegDict[string[5:8]]] = MemDict[string[8:16]]

            elif string[:5] == TypeDOP[1]:
                MemDict[string[8:16]] = "0"*8+decimalToBinary(Dict2[RegDict[string[5:8]]])

        elif string[:5] in TypeEOP:
            if string[:5]==TypeEOP[0]:
                PC = string[8:]
            elif string[:5] == TypeEOP[1]:
                if L=="1":
                # if Dict3["111"] == "0*13"+"1"+"0"*2:
                    PC = string[8:]
            elif string[:5] == TypeEOP[2]:
                # if Dict3["111"] == "0*14"+"1"+"0"*1:
                if G=="1":
                    PC = string[8:]
            elif string[:5] == TypeEOP[3]:
                # if Dict3["111"] == "0*15"+"1":
                if E=="1":
                    PC = string[8:]
            V,L,G,E = "0","0","0","0"
            Dict2["FLAGS"] = 0
            

        elif string[:5] in TypeFOP:
            V,L,G,E = "0","0","0","0"
            if string[:5] == TypeFOP[0]:
                return PC
        cycle+=1 
        cyclst.append(cycle)
        print(decimalToBinary(binaryToDecimal(PC)-1)+ " " + decimalToBinary1(Dict2["R0"]) + " " + decimalToBinary1(Dict2["R1"]) + " " + decimalToBinary1(Dict2["R2"]) + " " + decimalToBinary1(Dict2["R3"]) + " " + decimalToBinary1(Dict2["R4"]) + " " + decimalToBinary1(Dict2["R5"]) + " " + decimalToBinary1(Dict2["R6"]) + " " + ("0"*12+V+L+G+E))
        memlist.append(binaryToDecimal(PC))
        identify(MemDict[PC])


identify(MemDict["0"*8])
print(decimalToBinary(binaryToDecimal(PC)-1)+ " " + decimalToBinary1(Dict2["R0"]) + " " + decimalToBinary1(Dict2["R1"]) + " " + decimalToBinary1(Dict2["R2"]) + " " + decimalToBinary1(Dict2["R3"]) + " " + decimalToBinary1(Dict2["R4"]) + " " + decimalToBinary1(Dict2["R5"]) + " " + decimalToBinary1(Dict2["R6"]) + " " + ("0"*12+V+L+G+E))
for i in range(256):
    print(MemDict[decimalToBinary(i)])


def plot ():
    global cyclst
    global memlist
    x=np.array(cyclst)
    y=np.array(memlist)
    x1=np.max(cyclst)
    y1=np.max(memlist)  
    # if(abs(x1)>abs(x2)):
    #     x_dim=abs(x1)
    # else:
    #     x_dim=abs(x2)
    # if(abs(y1)>abs(y2)):
    #     y_dim=abs(y1)
    # else:
    #     y_dim=abs(y2)
    x_dim, y_dim = 1.2*x1, 1.2*y1
    plt.plot((-x_dim, x_dim),[0,0],'k-')
    plt.plot([0,0],(-y_dim, y_dim),'k-')
    plt.xlim(0,x_dim)
    plt.ylim(0,y_dim)
    plt.grid()
    
    plt.plot(x,y, marker = 'o')
    plt.show()

plot()

# 0001000100000100
# 0001001000000100
# 0111000000001010
# 0001100000011111
# 0001010000000001
# 0111000000011100
# 1000100000000111
# 1001100000000000