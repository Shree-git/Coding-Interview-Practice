from sys import setrecursionlimit

setrecursionlimit(10000)

def merge_sort(arr):
    if len(arr) > 1:

        m = len(arr) // 2
        L = arr[:m]
        R = arr[m:]

        merge_sort(L)
        merge_sort(R)

        i=j=k=0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k+=1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    
arr = [12,34,23,1,5,3,7,5,2]

merge_sort(arr)

print(arr)




