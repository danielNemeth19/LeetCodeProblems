import argparse
from typing import List


class Solution:
    """Given an array of integers (nums) and an integer (target)
    return indices of the two numbers such that they add up to 'target'"""

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                current_sum = num1 + num2
                if current_sum == target:
                    return [i, j]
        return []

    def two_sum2(self, nums: List[int], target: int) -> List[int]:
        d_nums = dict(enumerate(nums))
        for i, x in enumerate(nums):
            y = target - x
            if y in nums:
                for k, v in d_nums.items():
                    if v == y and i != k:
                        return [i, k]
        return []

    def two_sum3(self, nums: List[int], target: int) -> List[int]:
        d_nums = {num: i for i, num in enumerate(nums)}
        for i, x in enumerate(nums):
            y = target - x
            if y in d_nums:
                for j, v in enumerate(nums):
                    if v == y and i != j:
                        return [i, j]
        return []


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nums', nargs="+", type=int)
    parser.add_argument('--target', type=int)
    args = parser.parse_args()
    return args.nums, args.target


def main():
    nums, target = parse_args()
    s = Solution()
    result = s.two_sum3(nums=nums, target=target)
    print(result)


if __name__ == "__main__":
    main()
