"""Linear Search"""
def linear_serach(arr: list[int], value: int) -> int:
    for i in range(len(arr)):
        if arr[i] == value:
            print(f'arr[{i}]: {arr[i]}, value: {value}')    
            return i
    return -1

"""Binary Search"""
def binary_search(arr: list[int], value: int) -> int:
    def _binary_search(arr: list[int], value: int, left: int, right: int) -> int:
        # 処理が終了した場合
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            return _binary_search(arr, value, mid + 1, right)
        else:
            return _binary_search(arr, value, left, mid - 1)
    # 再帰関数を呼び出す
    return _binary_search(arr, value, 0, len(arr) - 1)


if __name__ == '__main__':
    nums = [2, 3, 4, 10, 40]
    print(binary_search(nums, 10))