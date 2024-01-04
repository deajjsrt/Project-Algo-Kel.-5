import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from time_measurement import time_function, CodeTimer
@time_function

def sentinel_linear_search(arr, target):
    
    last_value = arr[-1]
    
    arr[-1] = target

    i = 0
    while arr[i] != target:
        i += 1

    
    arr[-1] = last_value

    if i < len(arr) - 1 or arr[-1] == target:
        return i
    else:
        return -1


array_example = [4, 2, 7, 1, 9, 5, 3, 8, 6]
target_element = 7

result = sentinel_linear_search(array_example, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the array")