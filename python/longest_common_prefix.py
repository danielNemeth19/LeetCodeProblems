import argparse
from typing import List


class Solution:
    def __init__(self):
        self.maxprefix = None
        self.longest_prefix = None

    def longest_common_prefix(self, strs: List[str]) -> str:
        self.maxprefix = strs[0]
        if not self.maxprefix:
            return ""
        if len(strs) == 1:
            return self.maxprefix
        for word in strs[1:]:
            current_length = 0
            iterate_to = min(len(word), len(self.maxprefix))
            for i in range(iterate_to):
                if self.maxprefix[i] == word[i]:
                    current_length += 1
                else:
                    self.set_current_longest_prefix(current_length)
                    break
            self.set_current_longest_prefix(current_length)
        return self.maxprefix[:self.longest_prefix]

    def set_current_longest_prefix(self, current_length: int) -> None:
        if self.longest_prefix is None:
            self.longest_prefix = current_length
        else:
            self.longest_prefix = min(self.longest_prefix, current_length)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', nargs="+", type=str)
    args = parser.parse_args()
    return args.input


def main():
    strs = parse_args()
    result = Solution().longest_common_prefix(strs)
    print(result)


if __name__ == "__main__":
    main()
