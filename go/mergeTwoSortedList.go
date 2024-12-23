package main

import (
	"fmt"
	"sort"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	h := getHeads(list1)
	h2 := getHeads(list2)
    h = append(h, h2...)
    sort.Slice(h, func(i int, j int) bool { return h[i] < h[j]}) 
    result := createListNode(h)
    fmt.Printf("Combined heads: %v\n", h)
	return result
}

func getHeads(node *ListNode) []int {
    if node == nil {
        return []int{}
    }
	heads := []int{}
	currentNode := node
	for true {
		val := currentNode.Val
		heads = append(heads, val)
		if currentNode.Next != nil {
			currentNode = currentNode.Next
		} else {
			break
		}
	}
	return heads
}

func createListNode(data []int) *ListNode {
	var node *ListNode
	var currentNode *ListNode
    
    if len(data) == 0 {
        return node
    }
	for i, v := range data {
        if i == 0 {
            node = &ListNode{Val: v}
            currentNode = node
        }
		if i < len(data)-1 {
			nextNode := &ListNode{Val: data[i+1]}
			currentNode.Next = nextNode
            currentNode = nextNode
		}
	}
	return node
}

func main() {
    node1 := createListNode([]int{3, 4, 56})
    node2 := createListNode([]int{1, 2, 34})
	mergeTwoLists(node1, node2)
}
