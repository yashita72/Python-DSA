def reverseArray(a):
   
    a1=[]
    i=0
    for i in range(len(a)-1,-1,-1):
        a1.append(a[i])
        
    return a1