"""binary search example"""
from typing import List

# Create simple function in a script, like sum_xy

# - Add a test case for the simple function

# - Add requirements.txt file

# - Create Makefile that supports install, lint, test functions.

# - Add github action to lint and test the simple function.

# - Creat fastapi app that has at least two endpoints, one support GET method and the other supports POST method.

# - Add test cases for fastapi app's endpoints

# - Add logging to the app


def search(nums: List[int], target: int) -> int:
    """get the index of the a target number"""
    low, high = 0, len(nums) - 1
    middle = (high + low) // 2
    while middle < high and middle > low:
        if nums[middle] == target:
            return middle

        if nums[middle] > target:
            high = middle
        else:
            low = middle
        middle = (high + low) // 2

    if nums[middle] == target:
        return middle

    if nums[high] == target:
        return high
    return -1
