arr = [2,3,4,63,3,5,7,3,34,45,43,65]

def bubbleSort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(n):
        flag = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            break

bubbleSort(arr)
print(arr)