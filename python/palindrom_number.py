import argparse


class Solution:
    def is_palindrome(self, x: int) -> bool:
        return str(x) == "".join(reversed(str(x)))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', type=int)
    args = parser.parse_args()
    return args.number


def main():
    x = parse_args()
    s = Solution()
    flag = s.is_palindrome(x)
    print(f"Verdict: {flag}")


if __name__ == "__main__":
    main()
