def stock_list(list_of_art, list_of_cat):
    new_list = []
    new_dict = {"A": [], "B": [], "C": [], "D": []}
    for string in list_of_art:
        new_list.append(string.split(' '))
    print(new_list)

    itemDict = {item[0]: item[1:] for item in new_list}
    print(itemDict)

    for string in list_of_cat:
        for k,v in itemDict:
            if string[0] == k[0]:



print(stock_list(["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"],["A", "B", "C", "D"]))

def stock_list(l, m):
    if len(l) == 0 or len(m) == 0:
        return ''

    result = {}

    for category in m:
        result[category] = 0

    for pair in l:
        if pair[0] in result:
            result[pair[0]] += int(pair.split()[1])

    return ' - '.join([f'({key} : {value})' for (key, value) in result.items()])
