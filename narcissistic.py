def narcissistic( value ):
    new_list = []
    total = 0
    for i in map(int,str(value)):
        new_list.append(i)

    for n in new_list:
        total += n**(len(new_list))


    if total == value:
        return True
    else:
        return False

# TODO SE PUEDE RESUMIR A ESTO
#def narcissistic(value):
#    return value == sum(int(x) ** len(str(value)) for x in str(value))
#
