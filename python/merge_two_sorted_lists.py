import argparse
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # not required and used in solution
    # but the linked list can be made iterable like this
    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        previous = self.current
        self.current = self.current.next
        return previous

    def __str__(self):
        # ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: None}}}
        return f"ListNode{{val: {self.val}, next:{self.next}}}"


class Solution:
    def merge_two_lists_solution(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = self.get_head_values_without_iter(list1)
        h2 = self.get_head_values_without_iter(list2)
        return self.create_list_node(sorted(h1 + h2))

    @staticmethod
    def create_list_node(data: list):
        if not data:
            return []
        node, current_node = None, None
        for i, val in enumerate(data):
            if node is None:
                node = ListNode(val)
                current_node = node
            if i < len(data) - 1:
                next_node = ListNode(data[i+1])
                current_node.next = next_node
                current_node = next_node
        return node

    def get_head_values_without_iter(self, l_list: Optional[ListNode]) -> list:
        if not l_list:
            return []
        heads = []
        current = l_list
        while True:
            v = current.val
            heads.append(v)
            if current.next is not None:
                current = current.next
            else:
                break
        return heads


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--l1', nargs="+", type=int, default=[])
    parser.add_argument('--l2', nargs="+", type=int, default=[])
    args = parser.parse_args()
    return args.l1, args.l2


def main():
    s = Solution()
    l1, l2 = parse_args()
    node1 = s.create_list_node(l1)
    node2 = s.create_list_node(l2)

    sol = s.merge_two_lists_solution(node1, node2)
    print(sol)


if __name__ == "__main__":
    main()
