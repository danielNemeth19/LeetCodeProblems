import argparse


class Solution:
    def max_score(self, s: str) -> int:
        best_score = 0
        for i, _ in enumerate(s):
            s1, s2 = s[:i], s[i:]
            if s1 and s2:
                lscore = s1.count("0")
                rscore = s2.count("1")
                current_score = lscore + rscore
                # this could be nicer (probably better too): best_score = max(best_score, current_score)
                best_score = best_score if best_score > current_score else current_score
        return best_score


def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inp", type=str, default="")
    arg = parser.parse_args()
    return arg.inp


if __name__ == "__main__":
    inp = parse_arg()
    result = Solution().max_score(inp)
    print(result)
