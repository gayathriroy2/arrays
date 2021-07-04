def mo(arr,query):
    
    for i in range(len(query)):
        sum=0
        x=query[i][0]
        y=query[i][1]
        for j in range(x,y+1):
            sum+=arr[j]
        print("for",query[i],'the sum:',sum)
arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
Q = [[0, 4], [1, 3], [2, 4]]


def mo1(arr,query):
    query.sort(key= lambda x:x[1]) #sorted in ascnd order of x[1]
    currL,currR,currSum = 0,0,0
    for i in range(len(query)):
        L,R=query[i]
        while currL<L:
            currSum-=arr[currL]
            currL+=1
        while currL>L:
            currSum+=arr[currL-1]
            currL-=1
        while currR<=R:
            currSum+=arr[currR]
            currR+=1
        while currR>R+1:
            currSum-=arr[currR-1]
            currR-=1
        print("for",query[i],'the sum:',currSum)
arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
Q = [[0, 4], [1, 3], [2, 4]]
mo1(arr,Q)
