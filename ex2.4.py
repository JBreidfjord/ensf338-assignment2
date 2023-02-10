import json
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(20000)
def quick_sort(arr, low, high):
    while low < high:
        pivot = choose_pivot(arr, low, high)
        pivot = partition(arr, low, high, pivot)
        quick_sort(arr, low, pivot - 1)
        low = pivot + 1

def choose_pivot(arr, low, high):
    mid = (low + high) // 2
    pivot = high
    if arr[low] < arr[mid]:
        if arr[mid] < arr[high]:
            pivot = mid
    elif arr[low] < arr[high]:
        pivot = low
    return pivot

def partition(array, start, end, pivot):
    pivot_value = array[pivot]
    array[end], array[pivot] = array[pivot], array[end]
    store_index = start
    for i in range(start, end):
        if array[i] < pivot_value:
            array[store_index], array[i] = array[i], array[store_index]
            store_index += 1
    array[end], array[store_index] = array[store_index], array[end]
    return store_index


def main():
    with open('ex2.json') as f:
        data = json.load(f)
    for i in data:
        start = time.time()
        quick_sort(i, 0, len(i)-1)
        end = time.time()
        print(end - start)
        plt.plot(len(i), end - start, 'ro')
        plt.xlabel('Input Size')
        plt.ylabel('Time Taken (in seconds)')
    plt.show()
    
     
    

if __name__ == '__main__':
    main()