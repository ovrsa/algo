def linear_serach(arr: list[int], value: int) -> int:
    for i in range(len(arr)):
        if arr[i] == value:
            print(f'arr[{i}]: {arr[i]}, value: {value}')    
            return i
    return -1

if __name__ == '__main__':
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], 25, 2),
        ([5, 1, 4, 2, 8], 4, 2),
        ([], 5, -1),  # 空のリストのケース
        ([10, -1, 2, 11, 5], 11, 3)  # 負の数を含むケース
    ]
    for data, value, expected in test_cases:
        result = linear_serach(data, value)
        assert result == expected, f"linear_serach failed: {result} != {expected}"
        print("linear_serach passed the test.")