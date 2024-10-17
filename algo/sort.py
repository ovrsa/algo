from log_config import logger

def bubble_sort(arr):
    len_numbers = len(arr)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 -i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    len_numbers = len(arr)
    for i in range(len_numbers):
        min_idx = i
        for j in range(min_idx, len_numbers):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def gnome_sort(arr: list):
    n = len(arr)
    logger.debug(n)
    index = 0
    while index < n:
        if index == 0:
            index += 1

        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index- 1] = arr[index-1], arr[index]
            index -= 1
    return arr


def insertion_sort(arr: list[int]) -> list[int]:
    len_numbers = len(arr)
    for i in range(1, len_numbers):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


def partition(arr: list[int], low: int, high: int) -> int:
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr: list[int]) -> list[int]:
    def _quick_sort(arr: list[int], low: int, high: int):
        if low < high:
            partition_idx = partition(arr, low, high)
            _quick_sort(arr, low, partition_idx - 1)
            _quick_sort(arr, partition_idx + 1, high)
    
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def merge_sort(arr:list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    center = len(arr) // 2
    left = arr[:center]
    right = arr[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr