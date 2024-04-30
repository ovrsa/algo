from log_config import logger

"""Buuble Sort"""
def bubble_sort(arr):
    # リストの長さを取得
    len_numbers = len(arr)
    # リミットを設定
    for i in range(len_numbers):
        # リストの最後からi番目まで繰り返す
        # len_numbers - 1は次行で隣接する要素を比較するため
        for j in range(len_numbers - 1 - i):
            # arr[j]とarr[j-1]を比較して、arr[j]の方が小さければ入れ替える
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

"""Selection Sort"""
def selection_sort(arr):
    # listの長さを取得
    len_numbers = len(arr)
    # リミットの設定
    for i in range(len_numbers):
        # 最小値のindexを設定
        min_idx = i
        # i+1からリストの最後まで繰り返す
        for j in range(i + 1, len_numbers):
            # arr[min_idx]がarr[j]より大きい場合、min_idxをjに更新
            if arr[min_idx] > arr[j]:
                min_idx = j
        # 最初に設定したiとmin_idxを入れ替える
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


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


"""Quick Sort"""
def partition(arr: list[int], low: int, high: int) -> int:
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: list[int]) -> list[int]:
    def _quick_sort(arr: list[int], low: int, high: int) -> list[int]:
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)
    return arr


"""Merge Sort"""
def merge_sort(arr:list[int]) -> list[int]:
    # 再帰の終了条件
    if len(arr) <= 1:
        return arr
    
    center = len(arr) // 2
    left = arr[:center]
    right = arr[center:]

    merge_sort(left)
    merge_sort(right)

    # i,j,kを0に設定
    i = j = k = 0
    # leftとrightの要素を比較して、小さい方をarrに格納する
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # 残りの要素を格納する
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # 残りの要素を格納する
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr