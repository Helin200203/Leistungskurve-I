# Von https://www.geeksforgeeks.org/python-program-for-bubble-sort/ kopiert und verkürzt/aufgeräumt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr