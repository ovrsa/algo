from time import time

from memory_profiler import memory_usage

from algo.sort import *


def measure_performance(func, test_cases):
    """Measure function execution time, memory usage, and correctness for multiple test cases."""
    for data, expected in test_cases:
        start_time = time()
        mem_usage_start = memory_usage()[0]
        result = func(data)
        mem_usage_end = memory_usage()[0]
        end_time = time()
        
        # 実行時間とメモリ使用量を表示
        print(f"{func.__name__}: 実行時間 {end_time - start_time} 秒, メモリ使用量 {mem_usage_end - mem_usage_start} MiB")
        
        # 結果の正確性を検証
        assert result == expected, f"{func.__name__} failed: {result} != {expected}"
        print(f"{func.__name__} passed the test.")

if __name__ == '__main__':
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([], []),  # 空のリストのケース
        ([10, -1, 2, 11, 5], [-1, 2, 5, 10, 11])  # 負の数を含むケース
    ]
    # 実行したい関数を指定
    measure_performance(merge_sort, test_cases)