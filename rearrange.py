def rearrange(arr):
    for i in range(len(arr)):
        
        for j in range(len(arr)):
            if arr[j]==i:
                tmp=arr[i]
                arr[i]=arr[j]
                arr[j]=tmp
    for i in range(len(arr)):
         
        
        if (arr[i] != i):
            arr[i] = -1
    print(arr)
#rearrange([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1])

def reverse(arr):
    n=len(arr)
    start=0
    end=n-1
    while start<end:
     arr[start],arr[end]=arr[end],arr[start]
     start+=1
     end-=1
    print(arr)
#reverse([1,2,3,4,5])

def evenodd(arr):
    tmp=[]
    n=len(arr)
    for i in range(n):
        tmp.append(arr[i])
    tmp.sort(reverse=True)
    end=n-1
    for i in range(0,n-(n//2)):
        
        arr[end]=tmp[i]
        end=end-2
    if n%2==0:
        start=0
    else:
        start=1
    for i in range((n-n//2),n):
        arr[start]=tmp[i]
        start+=2
        
    print(arr)
evenodd([1, 2, 1, 4, 5, 6, 8, 8])   
