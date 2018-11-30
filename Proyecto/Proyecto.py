import time
start_time = time.time()
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("---Bubble---")
print(arr)
def bubble(arr, n):
    if n<len(arr):
        n+=1
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                aux = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = aux
        bubble(arr, n)
        
bubble(arr, 0)
print(arr)
print("---%s segundos ---"%(time.time()-start_time))

start_time = time.time()
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("---Quicksort---")
print(arr)
def quick(arr, izq, der):
    i = izq
    d = der
    piv = (arr[i]+arr[d])/2

    while i < d:
        while arr[i]<piv:
            i+=1
        while arr[d]>piv:
            d-=1
        if i<=d:
            aux=arr[d]
            arr[d]=arr[i]
            arr[i]=aux
            i+=1
            d-=1
    if izq<d:
        arr=quick(arr, izq, d)
    if der>i:
        arr=quick(arr, i, der)
    return arr
quick(arr, 0, len(arr)-1)
print(arr)
print("---%s segundos ---"%(time.time()-start_time))

start_time = time.time()
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("---Shellsort---")
print(arr)
def shell(arr): 
    dist=len(arr)//2
    while (dist>0): 
        for i in range(dist,len(arr)):
            j=i 
            aux=arr[i] 
            while ((j>=dist) and (arr[j-dist]>aux)):  
                arr[j]=arr[j-dist]
                j=j-dist
            arr[j]=aux
        if (dist==2):
            dist=1 
        else:
            dist=int(dist/2.2)
    return arr
shell(arr)
print(arr)
print("---%s segundos ---"%(time.time()-start_time))

start_time = time.time()
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("---Mergesort---")
print(arr
      )
def merge(arr):
    if len(arr)>1:
        mitad = len(arr)//2
        mitadIzq = arr[:mitad]
        mitadDer = arr[mitad:]

        merge(mitadIzq)
        merge(mitadDer)

        i=0
        j=0
        k=0
        while i < len(mitadIzq) and j < len(mitadDer):
            if mitadIzq[i] < mitadDer[j]:
                arr[k]=mitadIzq[i]
                i=i+1
            else:
                arr[k]=mitadDer[j]
                j=j+1
            k=k+1
        while i < len(mitadIzq):
            arr[k]=mitadIzq[i]
            i=i+1
            k=k+1
        while j < len(mitadDer):
            arr[k]=mitadDer[j]
            j=j+1
            k=k+1
            
merge(arr)
print(arr)
print("---%s segundos ---"%(time.time()-start_time))
