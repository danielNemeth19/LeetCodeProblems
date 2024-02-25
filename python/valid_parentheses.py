import argparse


class Solution:
    def __init__(self):
        self.types = {"(": ")", "[": "]", "{": "}"}

    def valid_parentheses(self, s: str) -> bool:
        print(f"validate remaining: {s}")
        if len(s) == 1:
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
        if not cleaned_str:
            return True
        if len(s) == len(cleaned_str):
            return False
        return self.valid_parentheses(cleaned_str)

    def valid_next_match(self, s: str, i: int, p: str):
        if i == len(s) - 1:
            return False
        match = self.types.get(p)
        if match and (match == s[i+1]):
            return True
        return False

    def valid_parentheses2(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return True if not s else False



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str)
    args = parser.parse_args()
    return args.input


def main():
    s = parse_args()
    result = Solution().valid_parentheses2(s)
    print(result)


if __name__ == "__main__":
    main()
