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
    def insert_greatest_common_divisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while True:
            val_current = current.val
            if current.next is not None:
                next_adjacent = current.next
                divisor = self.find_greatest_common_divisors(val_current, next_adjacent.val)
                node_to_add = ListNode(divisor)
                current.next = node_to_add
                node_to_add.next = next_adjacent
                current = next_adjacent
            else:
                break
        return head

    @staticmethod
    def find_greatest_common_divisors(n1: int, n2: int) -> int:
        divisor = min(n1, n2)
        while divisor > 1:
            if n1 % divisor == 0 and n2 % divisor == 0:
                break
            divisor -= 1
        return divisor

    @staticmethod
    def create_list_node(data: list) -> ListNode:
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


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--l', nargs="+", type=int, default=[])
    args = parser.parse_args()
    return args.l


if __name__ == "__main__":
    linked_list = parse_args()
    s = Solution()
    node = s.create_list_node(linked_list)
    result = s.insert_greatest_common_divisors(node)
    print(result)
