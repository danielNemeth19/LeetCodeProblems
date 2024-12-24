import argparse
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
        return f"ListNode {{{self.val}, next: {self.next}}}"


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = self.get_heads(l1)
        h2 = self.get_heads(l2)

        sum_of_nodes = self.sum_node(h1) + self.sum_node(h2)
        # res_heads = self.solve_for_num(sum_of_nodes)
        res_heads = self.decompose_number(sum_of_nodes)
        return self.create_list_node(res_heads)

    def create_list_node(self, data: list) -> ListNode:
        node, current_node = None, None
        for i, val in enumerate(data):
            if not node:
                node = ListNode(val)
                current_node = node
            if i < len(data) - 1:
                next_node = ListNode(data[i+1])
                current_node.next = next_node
                current_node = next_node
        return node

    @staticmethod
    def get_heads(node: ListNode) -> list:
        h = []
        current_node = node
        while True:
            val = current_node.val
            h.append(val)
            if current_node.next is not None:
                current_node = current_node.next
            else:
                break
        return h

    @staticmethod
    def sum_node(heads: list) -> int:
        target = 0
        multiplier = 1
        for i, x in enumerate(heads):
            multiplier = multiplier if i == 0 else multiplier * 10
            target += x * multiplier
        return target

    @staticmethod
    def solve_for_num(num: int) -> list:
        return [int(x) for x in reversed(str(num))]

    @staticmethod
    def decompose_number(num: int) -> list:
        if num == 0:
            return [0]
        num_list = []
        while num > 0:
            n = num % 10
            num_list.append(n)
            num //= 10
        return num_list


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--l1', nargs="+", type=int, default=[])
    parser.add_argument('--l2', nargs="+", type=int, default=[])
    args = parser.parse_args()
    return args.l1, args.l2


if __name__ == "__main__":
    list1, list2 = parse_args()
    s = Solution()
    node1 = s.create_list_node(list1)
    node2 = s.create_list_node(list2)
    res = s.add_two_numbers(node1, node2)
    print(res)
