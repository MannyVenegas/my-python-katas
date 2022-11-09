#Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. 
# Spaces will be included only when more than one word is present.

def spin_words(phrase):
    list_of_words = phrase.split()
    empty_list = []
    for word in list_of_words:
        if len(word) > 5:
            empty_list.append(word[::-1])
        else:
            empty_list.append(word)
    return ' '.join(empty_list)
    print(spin_words("Hey fellow warriors"))
