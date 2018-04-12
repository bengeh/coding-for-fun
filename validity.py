#Scenario found online: Given a deck of cards with a value(positive integer) and a suit(lowercase letters)
#Find if the deck is perfect(all cards in deck are distinct and for any two cards (v1,s1) and (v2,s2), there exist (v1,s2) and (v2,s1)

def validity(n , value, suits):
    NumberOfValues = len(set(value)) #the use of set here eliminates duplicates, can use this to our advantage and get the not perfect deck
    print(NumberOfValues)
    print(set(value)) #returns 1 when value is {1,1,1}, returns 1,2 when value is {1,2,1}
    NumberOfSuits = len(set(suits))
    if NumberOfSuits * NumberOfValues != n:
        print("Not Perfect")
    else:
        print("Perfect Deck")


#Given a string where each letter appears exactly twice, remove one of the two copies of each letter.
#



def stringItr(word):
    d = {}
    seen = False
    seen_befre = ""
    for x in word:
        if x in d:
            seen = True
            break
        seen_befre = seen_befre + x
        d[x] = x
    print(d)


if __name__ == '__main__':
    validity(3, {1,2,1}, "hch")
    #stringItr("bbaa")