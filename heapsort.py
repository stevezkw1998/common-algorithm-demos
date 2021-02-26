arr = [2,5,7,2,7,4,8,9,3,9,54,2,3,45,2,15,16,18]

# ------------------堆排序, 时间复杂度O(nlogn)-----------------------
# ------------------方法A-------------------------------------------
def solution(arr):
    n = len(arr)
    build_heap(arr, n)
    print(arr)

def build_heap(arr, n):
    last_node = n - 1
    parent = (last_node-1) // 2
    for i in range(parent, -1, -1):
        heapify(arr, n, i)
        
def heapify(arr, n, i):
    # 对第i个节点进行heapify, 大顶堆
    if i >= n:
        return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    maxvalue = i
    if c1 < n and arr[c1] > arr[maxvalue]:
        maxvalue = c1
    if c2 < n and arr[c2] > arr[maxvalue]:
        maxvalue = c2
    if maxvalue != i:
        arr[maxvalue], arr[i] = arr[i], arr[maxvalue]
        heapify(arr, n, maxvalue)

def heapify_2(arr, n, i):
    # 对第i个节点进行heapify, 小顶堆
    if i >= n:
        return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    minvalue = i
    if c1 < n and arr[c1] < arr[minvalue]:
        minvalue = c1
    if c2 < n and arr[c2] < arr[minvalue]:
        minvalue = c2
    if minvalue != i:
        arr[minvalue], arr[i] = arr[i], arr[minvalue]
        heapify_2(arr, n, minvalue)

# ------------------方法B-------------------------------------------
def solution2(arr):
    heapsort(arr, len(arr))
    print(arr)

def heapsort(arr, n):
    # 从孩子节点开始和父母比大小, 大顶堆
    for index in range(1, n):
        while arr[(index-1) // 2] < arr[index] and index > 0:
            arr[(index-1) // 2], arr[index] = arr[index], arr[(index-1) // 2]
            index = (index-1) // 2
        return arr

def heapsort_2(arr, n):
    # 从孩子节点开始和父母比大小, 大顶堆
    for index in range(1, n):
        while arr[(index-1) // 2] > arr[index] and index > 0:
            arr[(index-1) // 2], arr[index] = arr[index], arr[(index-1) // 2]
            index = (index-1) // 2
        return arr

solution(arr)
solution2(arr)