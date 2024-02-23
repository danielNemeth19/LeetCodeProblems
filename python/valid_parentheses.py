import argparse


class Solution:
    def __init__(self):
        self.types = {"(": ")", "[": "]", "{": "}"}

    def valid_parentheses(self, s: str) -> bool:
        print(f"validate remaining: {s}")
        if len(s) == 1:
            return False
        if len(s) == 2 and not self.valid_next_match(s, 0, s[0]):
            return False
        cleaned_str = ""
        skip = False
        for i, p in enumerate(s):
            print(f"processing: {i} -- {p} skip: {skip}")
            if skip:
                skip = False
                continue
            if self.valid_next_match(s, i, p):
                skip = True
                continue
            cleaned_str += p
            skip = False
        if not cleaned_str:
            return True
        return self.valid_parentheses(cleaned_str)

    def valid_next_match(self, s: str, i: int, p: str):
        if i == len(s) - 1:
            return False
        match = self.types.get(p)
        if match and (match == s[i+1]):
            return True
        return False


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str)
    args = parser.parse_args()
    return args.input


def main():
    s = parse_args()
    result = Solution().valid_parentheses(s)
    print(result)


if __name__ == "__main__":
    main()
