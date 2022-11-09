def expanded_form(num):
    strNum = str(num)
    firstNum = (int(strNum[0])) * (10**(len(strNum) - 1))
    print(firstNum)
    remainder = num - firstNum
    list = [firstNum]
    while remainder > 0:
        newNum = (int(str(remainder)[0])) * (10**(len(str(remainder)) - 1))
        remainder = remainder - newNum
        list.append(newNum)
        print(newNum)
        continue
    print(list)
    strings = [str(x) for x in list]
    print(' + '.join(strings))



print(expanded_form(70304))
