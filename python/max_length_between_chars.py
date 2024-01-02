import argparse


class Solution:
    def __init__(self):
        self.max_length = 0

    def max_length_between_equal_chars(self, s: str) -> int:
        if len(set(s)) == len(s):
            return -1
        counter_d = {}
        for c in s:
            counter_d[c] = counter_d.get(c, 0) + 1

        for k, v in counter_d.items():
            if v == 1:
                continue
            offset = 0
            positions = []
            for _ in range(v):
                pos = s.find(k, offset)
                positions.append(pos)
                offset = pos + 1

            current_max_lenght = positions[-1] - positions[0] - 1
            print(f"Positions for {k} (repeated {v} times): {positions} -- current_max_lenght: {current_max_lenght}")
            self.max_length = current_max_lenght if current_max_lenght > self.max_length else self.max_length
        return self.max_length

    def max_length_between_equal_chars2(self, s: str) -> int:
        max_length = -1
        for c in set(s):
            length = s.rfind(c) - s.find(c) - 1
            max_length = length if length > max_length else max_length
        return max_length

    # one-liner solution from comments
    def max_length_between_equal_chars_not3(self, s: str) -> int:
        return max(s.rfind(c) - s.find(c) - 1 for c in set(s))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str)
    args = parser.parse_args()
    return args.input


def main():
    input_s = parse_args()
    s = Solution()
    result = s.max_length_between_equal_chars2(input_s)
    print(f"Verdict: {result}")


if __name__ == "__main__":
    main()
