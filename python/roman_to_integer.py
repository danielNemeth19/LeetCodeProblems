import argparse


class Solution:
    def __init__(self):
        self.map = self._create_map()

    def _create_map(self):
        return {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

    def roman_to_integer(self, s: str) -> int:
        result = []
        for i, c in enumerate(s):
            current_value = self.map[c]
            result.append(current_value)
            if i:
                previous_value = self.map[s[i-1]]
                if c in ("V", "X") and s[i-1] == "I":
                    value = current_value - previous_value
                    result.pop()
                    result[-1] = value
                elif c in ("L", "C") and s[i-1] == "X":
                    value = current_value - previous_value
                    result.pop()
                    result[-1] = value
                elif c in ("D", "M") and s[i-1] == "C":
                    value = current_value - previous_value
                    result.pop()
                    result[-1] = value
        return sum(result)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str)
    args = parser.parse_args()
    return args.input


def main():
    s = parse_args()
    result = Solution().roman_to_integer(s)
    print(result)


if __name__ == "__main__":
    main()
