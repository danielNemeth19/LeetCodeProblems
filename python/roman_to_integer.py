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

    def roman_to_integer2(self, s: str) -> int:
        result = 0
        skip_next = False
        for i, c in enumerate(s):
            if skip_next:
                skip_next = False
                continue
            current_value = self.map[c]
            next_value = 0 if i == (len(s) - 1) else self.map[s[i+1]]
            if current_value == 1 and next_value in (5, 10):
                skip_next = True
                result += next_value - current_value
            elif current_value == 10 and next_value in (50, 100):
                skip_next = True
                result += next_value - current_value
            elif current_value == 100 and next_value in (500, 1000):
                skip_next = True
                result += next_value - current_value
            else:
                result += current_value
        return result


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str)
    args = parser.parse_args()
    return args.input


def main():
    s = parse_args()
    result = Solution().roman_to_integer2(s)
    print(result)


if __name__ == "__main__":
    main()
