import re

def alphabet_position(text):
    dictt = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
    'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
    }
    new_text = text.lower()
    newlist = []
    for i in new_text:
        for k,v in dictt.items():
            if k == i:
                newlist.append(v)
    result = " ".join(newlist)
    return result



print(alphabet_position("The sunset sets at twelve o' clock."))
