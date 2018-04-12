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


#Found from topcoder:
#Hero has a string of lowercase English letters. Each letter that appears in the string appears exactly twice. Hero now wants to remove one half of his string. More precisely, he wants to remove one of the two copies of each letter in his string. The order of the letters he does not remove will remain unchanged. If there are multiple ways to remove the letters, Hero prefers the ones where the resulting string begins with a smaller letter (i.e., a letter that is earlier in the alphabet). You are given the String s containing Hero's string. Find the smallest letter that can appear at the beginning of the string after Hero removes half of the letters. Return a String with a single character: that letter.



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

    
    
#problem from SPOJ
# given a set of inputs, stop processing after reading number 42
def listtt():
    var = int(input())
    flag = True
    if var == 42:
        flag = False
    while flag:
        if var == 42:
            flag = False
        else:
            print(var)
            var = int(input())
    return var

#user can specify how many test case he/she wants
#finding prime no. given user input of min and max using Sieve of Eratosthenes
def primeNo():
    testCase = int(input())
    notPrime = set()
    prime = []
    tmp = []
    for a in range(0,testCase):
        min, max = list(map(int, input().split()))
        tmp.append(min)
        tmp.append(max)

    for a in range(0, len(tmp)-1):
        min = tmp[a]
        max = tmp[a+1] + 1
        for i in range(2,max):
            if i in notPrime:
                continue
            for j in range(i*i, max, i):
                notPrime.add(j)
            if i >= min:
                prime.append(i)
        prime.append('')
    for i in prime:
        print(i)

    return prime

        

    

if __name__ == '__main__':
    #primeNo()
    #validity(3, {1,2,1}, "hch")
    #stringItr("bbaa")
    #listtt()
    