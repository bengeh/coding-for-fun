def primeNo():
    testCase = int(input())
    notPrime = set()
    prime = []
    tmp = []
    for a in range(0,testCase):
        min, max = list(map(int, input().split()))
        tmp.append(min)
        tmp.append(max)
    noLst = list(range(min,max))
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
        
    for i in prime:
        print(i)
    del prime[:]
    return prime
    
    

if __name__ == '__main__':
    primeNo()