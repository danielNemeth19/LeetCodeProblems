import argparse


class Solution:
    def split_num(self, inp: int) -> int:
        nums = list(str(inp))
        x, y = '', ''
        for i, n_str in enumerate(sorted(nums)):
            if i % 2 == 0:
                x += n_str
            else:
                y += n_str
        print(f'x is {x} - y is {y}')
        return int(x) + int(y)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-num", required=True, type=int)
    args = parser.parse_args()
    return args.num


if __name__ == "__main__":
    num = parse_args()
    s = Solution()
    res = s.split_num(num)
    print(res)
