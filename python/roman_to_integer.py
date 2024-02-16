import argparse


class Solution:
    def __init__(self):
        self.map = self._create_map()

    def _create_map(self):
        return {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

    def roman_to_integer_slowest(self, s: str) -> int:
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

    def roman_to_integer_slower(self, s: str) -> int:
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

    def roman_to_integer(self, s: str) -> int:
        result = 0
        skip_next = False
        for i, c in enumerate(s):
            if skip_next:
                skip_next = False
                continue
            next_symbol = None if i == (len(s) - 1) else s[i+1]
            potential_symbol = f"{c}{next_symbol}"
            if potential_symbol in self.map:
                skip_next = True
                result += self.map[potential_symbol]
            else:
                result += self.map[c]
        return result


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
