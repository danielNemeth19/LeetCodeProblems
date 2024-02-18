import argparse
from typing import List


class Solution:
    def __init__(self):
        self.maxprefix = None

    def longest_common_prefix(self, strs: List[str]) -> str:
        self.maxprefix = strs[0]
        if not self.maxprefix:
            return ""
        if len(strs) == 1:
            return self.maxprefix
        cache = []
        for word in strs[1:]:
            current_length = 0
            iterate_to = min(len(word), len(self.maxprefix))
            for i in range(iterate_to):
                if self.maxprefix[i] == word[i]:
                    current_length += 1
                else:
                    cache.append(current_length)
                    break
            cache.append(current_length)
        length = min(cache) if cache else 0
        return self.maxprefix[:length]


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
