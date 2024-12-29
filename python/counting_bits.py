import argparse
from typing import List


class Solution:
    def count_bits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            bits = f"{i:b}"
            ans.append(bits.count("1"))
        return ans


def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num", type=int)
    args = parser.parse_args()
    return args.num


if __name__ == "__main__":
    num = parse_arg()
    s = Solution()
    print(s.count_bits(num))
