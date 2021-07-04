#range minimum query using sparse table
import math
a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
n = len(a)
MAX = 10
lookup = [[0 for i in range(MAX)]
                 for j in range(MAX)]

                

def rmq(arr,n):
    for i in range(n):
        lookup[i][0]=arr[i]
    j=1
    while (1<<j)<=n:
        i=0
        while (i+(1<<j)-1)<n:
            if (lookup[i][j - 1] <= lookup[i + (1 << (j - 1))][j - 1]):
                lookup[i][j] = lookup[i][j - 1]
            else:
                lookup[i][j] = lookup[i + (1 << (j - 1))][j - 1]
            i+=1
        j+=1
def query(L, R):
    j = int(math.log2(R - L + 1))
    if lookup[L][j] <= lookup[R - (1 << j) + 1][j]:
        return lookup[L][j]
    else:
        return lookup[R - (1 << j) + 1][j]

#rmq(a, n)
#print(query(0, 4))
#print(query(4, 7))
#print(query(7, 8))
#print(lookup)

#range gcd using sparse table
def gcd(arr,n):
    for i in range(n):
        lookup[i][0]=arr[i]
    j=1
    while (1<<j)<=n:
        i=0
        while (i+(1<<j)-1)<n:
            lookup[i][j]=math.gcd(lookup[i][j-1],lookup[i+(1<<j-1)][j-1])
            i+=1
        j+=1

def query(L, R):
    j=int(math.log2(R-L+1))
    return math.gcd(lookup[L][j],lookup[R-(1<<j)+1][j])
gcd(a, n)
print(query(0, 2))
print(query(1, 3))
print(query(4, 5))

