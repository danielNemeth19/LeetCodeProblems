## Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### Example 1:
* Input: list1 = [1,2,4], list2 = [1,3,4]
* Output: [1,1,2,3,4,4]

### Example 2:
* Input: list1 = [], list2 = []
* Output: []

### Example 3:
* Input: list1 = [], list2 = [0]
* Output: [0]

### Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.


### Additional notes from python solution
* Manually creating a linked list for testing input
```
def manual_example(data: list):
    n = ListNode(data[0])
    n2 = ListNode(data[1])
    n3 = ListNode(data[2])
    n.next = n2
    n2.next = n3
    return n
```

* Primitive way to create a ListNode
```
def create_list_node_old(data: list):
    nodes = []
    for i in data:
        node = ListNode(i)
        nodes.append(node)
    for i, node in enumerate(nodes):
        if i < len(nodes) - 1:
            node.next = nodes[i+1]
    return nodes[0]
```
### Additional notes from Go
* Manually creating a linked list for testing input
```
node1 := ListNode{
    Val: 2,
    Next: &ListNode{
        Val: 3,
        Next: &ListNode{
            Val: 16,
            Next: &ListNode{
                Val:  34,
                Next: nil,
            },
        },
    },
}
```
