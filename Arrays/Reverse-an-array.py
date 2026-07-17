def reverseArray(a):
   
    a1=[]
    i=0
    for i in range(len(a)-1,-1,-1):
        a1.append(a[i])
        
    return a1
def reverseArray(a):
    left = 0
    right = len(a) - 1

    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1

    return a