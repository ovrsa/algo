from log_config import logger

"""Buuble Sort"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


"""Quick Sort"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


"""Gnome Sort"""
def gnome_sort(arr: list):
    n = len(arr)
    logger.debug(n)
    index = 0
    while index < n:
        logger.debug('+++++')
        logger.debug(f'arr: {arr}')
        # 比較対象のラインが0の場合は1にする
        if index == 0:
            index += 1
        logger.debug(f'arr{index}: {arr[index]}, arr{index-1}: {arr[index-1]}')
        # 値を入れ替えてindexに1を足す
        logger.debug(f'index: {index}')
        if arr[index] >= arr[index - 1]:
            logger.debug('pass')
            index += 1
        # indexとindex-1の値を入れ替える
        else:
            arr[index], arr[index- 1] = arr[index-1], arr[index]
            logger.debug('check')
            logger.debug(f'arr{index}: {arr[index]}, arr{index-1}: {arr[index-1]}')
            # indexから1を引く
            index -= 1
        logger.debug('-----')
    return arr

"""Insertion Sort"""
def insertion_sort(arr: list[int]) -> list[int]:
    len_numbers = len(arr)
    # 0番目の要素は比較対象がないため1から始める
    for i in range(1, len_numbers):
        # 比較対象の値をtempに代入
        temp = arr[i]
        # 比較対象はi-1から始める
        j = i - 1
        # jが0以上かつ、arr[j]の値がtempより大きい場合
        while j >= 0 and arr[j] > temp:
            # jの値がtempより大きい場合、j+1にjの値を代入
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr