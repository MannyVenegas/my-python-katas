#The goal of this exercise is to convert a string to a new string where each character in the new string is
# "(" if that character appears only once in the original string, or ")"
#if that character appears more than once in the original string.
#Ignore capitalization when determining if a character is a duplicate.
def duplicate_encode(word):
    #your code here
    list = []
    low = word.lower() #to ignore case sensitive
    for i in low:
        if low.count(i) == 1:
            list.append("(")
        elif low.count(i) > 1:
            list.append(")")
    print(list)
    result = print("".join(list))
    return result

duplicate_encode("rEcede")
