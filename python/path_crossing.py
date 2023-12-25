import sys


class Solution:
    def __init__(self):
        self.x, self.y = 0, 0
        self.cache = [(self.x, self.y)]

    def is_path_crossing(self, path: str) -> bool:
        for d in path:
            cordinates = self.get_coordinates(d)
            if cordinates in self.cache:
                return True
            self.cache.append(cordinates)
        return False

    def get_coordinates(self, direction: str) -> tuple:
        if direction == "N":
            self.y += 1
        elif direction == "E":
            self.x += 1
        elif direction == "S":
            self.y -= 1
        else:
            self.x -= 1
        return (self.x, self.y)


def main():
    path = sys.argv[1]
    s = Solution()
    flag = s.is_path_crossing(path)
    print(f"Visited paths: {s.cache}")
    print(f"final coordinates: ({s.x}, {s.y})")
    print(f"Verdict: {flag}")


if __name__ == "__main__":
    main()
