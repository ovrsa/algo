from algo.sort import *

# テストケースと期待される結果をタプルのリストとして定義
test_cases = [
    ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([], []),  # 空のリストのケース
]

# 各ソート関数をテストするための関数を定義
def run_sort_tests(sort_func):
    for input_arr, expected in test_cases:
        assert sort_func(input_arr) == expected, f"{sort_func.__name__} failed"

if __name__ == '__main__':
    # 各ソート関数に対してテストを実行
    # run_sort_tests(bubble_sort)
    # run_sort_tests(quick_sort)
    run_sort_tests(gnome_sort)
    print('All tests passed!')