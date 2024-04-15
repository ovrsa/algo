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
    logger.debug(f'Starting insertion sort on array: {arr}')
    # 0番目の要素は比較対象がないため1から始める
    for i in range(1, len_numbers):
        logger.debug(f'Iteration {i}: Current array state: {arr}')
        # 比較対象の値をtempに代入
        temp = arr[i]
        logger.debug(f'Picking up value {temp} for insertion')
        # 比較対象はi-1から始める
        j = i - 1
        # jが0以上かつ、arr[j]の値がtempより大きい場合
        while j >= 0 and arr[j] > temp:
            logger.debug(f'Comparing {temp} with {arr[j]} at position {j}')
            # j+1にjの値を代入
            arr[j + 1] = arr[j]
            logger.debug(f'Moving {arr[j]} to position {j + 1}')
            # jを1減らすことで次の比較対象に移る
            j -= 1
        # 最後にtempの値をarr[j+1]に代入することで、挿入を完了する
        arr[j + 1] = temp
        logger.debug(f'Inserted {temp} at position {j + 1}, array state: {arr}')
    logger.debug(f'Finished insertion sort, final array state: {arr}')
    return arr


# partition: リストの中から基準値を選び、基準値より小さい値を左に、大きい値を右に分ける
def partition(arr: list[int], low: int, high: int) -> int:
    # i: リストの中で基準値より小さい値を探すためのインデックス
    i = low - 1
    # pivot: 基準値
    pivot = arr[high]
    # j: リストの中を移動するためのインデックス
    # lowからhighまでの範囲で繰り返す
    for j in range(low, high):
        # 基準値より小さい値を探す
        if arr[j] < pivot:
            # iを1増やし、arr[i]とarr[j]を入れ替える
            # これにより、基準値より小さい値を左に移動する
            # iを増やすことで、基準値より小さい値が見つかった場合に、その値を左に移動する
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # 基準値より小さい値を左に移動し終えたら、基準値とi+1の値を入れ替える
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

"""Quick Sort"""
def quick_sort(arr: list[int]) -> list[int]:
    # _quick_sort: クイックソートを行う再帰関数
    # low: リストの先頭のインデックス
    # high: リストの末尾のインデックス
    def _quick_sort(arr: list[int], low: int, high: int) -> None:
        if low < high:
            # partition_index: 基準値を選ぶためのインデックス
            partition_index = partition(arr, low, high)
            # 基準値より左側のリストを再帰的にソートする
            _quick_sort(arr, low, partition_index -1)
            # 基準値より右側のリストを再帰的にソートする
            _quick_sort(arr, partition_index + 1, high)
    _quick_sort(arr, 0, len(arr) - 1)
    return arr