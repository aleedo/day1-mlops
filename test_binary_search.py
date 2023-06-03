import pytest
import binary_search

def test_target_for_general():
    nums, target, output = [-1,0,3,5,9,12], 9, 4
    message = f'Got {binary_search.search(nums, target)} instead of {output}'
    assert binary_search.search(nums, target) == output, message



nums, target, output = [-1,0,3,5,9,12], 9, 4
print(binary_search.search(nums, target))

if __name__ == '__main__':
    test_target_for_general()