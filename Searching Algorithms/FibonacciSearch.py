import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from time_measurement import time_function, CodeTimer
@time_function
def fibonacci_search(arr, target):
    n = len(arr)

    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib = fib_m_minus_2 + fib_m_minus_1

   
    while fib < n:
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib
        fib = fib_m_minus_2 + fib_m_minus_1

    offset = -1

    while fib > 1:
        i = min(offset + fib_m_minus_2, n - 1)

        if arr[i] < target:
            fib = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
            offset = i

        elif arr[i] > target:
            fib = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1

        else:
            return i 

    if fib_m_minus_1 and arr[offset + 1] == target:
        return offset + 1  

    return -1  


sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 6

result = fibonacci_search(sorted_array, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the array")