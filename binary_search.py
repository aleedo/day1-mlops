"""binary search example"""
from typing import List


def search(nums: List[int], target: int) -> int:
    """get the index of the a target number"""
    low = 0
    high = len(nums) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if nums[mid] < target:
            low = mid + 1

        elif nums[mid] > target:
            high = mid - 1

        elif nums[mid] == target and mid != low:
            return mid

        else:
            return -1
