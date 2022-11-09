import re
def decode(str):
    string = str
    numl = re.findall(r"\d",string)
    strs = re.findall(r"[a-zA-Z]",string)
    numlint = int("".join(numl))

    listofx = []
    listofints = []
    lisoffinals = []
    chrsfinal = []
    for i in strs:
        listofints.append(ord(i) - 97)

    for x in listofints:
        for y in range(0,26):
            if y * numlint % 26 == x:
                lisoffinals.append(y)

    for i in lisoffinals:
        chrsfinal.append(chr(i + 97))
    if strs != chrsfinal and len(chrsfinal) == len(strs):
        answer = "".join(chrsfinal)
    else:
        answer = "Impossible to decode"
return answer
#from re import findall as fa

#shorter solution
#def decode(s):
    #n, str = fa(r"\d+|\w+", s)
    #dec = ""
    #for c in str:
        #for i in range(26):
            #if i * int(n) % 26 == (ord(c) - 97):
                #dec += chr(i + 97)
    #return dec if len(dec) == len(str) else "Impossible to decode"
