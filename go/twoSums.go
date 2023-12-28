package main

import (
	"flag"
	"log"
	"fmt"
	"strconv"
)

func twoSum(nums []int, target int) []int {
	for i, num1 := range nums {
		for j, num2 := range nums {
			if i==j {
				continue
			}
			current_sum := num1 + num2
			if current_sum == target {
				return []int{i, j}
			}
		}
	}
	return []int{0, 0}
}

func twoSum2(nums []int, target int) []int {
	sNums := make(map[int]bool)
	for _, num := range nums {
		sNums[num] = true
	}

	for i, num1 := range nums {
		target := target - num1
		if sNums[target] {
			for j, num2 := range(nums) {
				if i!=j && num2 == target {
					return []int{i, j}
				}
			}
		}
	}
	return []int{0, 0}
}

func main() {
	target := flag.Int("target", 0, "Defines the target number")
	flag.Parse()
	strNums := flag.Args()
	var nums []int 
	for _,v := range strNums {
		n, err := strconv.Atoi(v)
		if err != nil {
			log.Fatalf("Bad param: %s\n", err)
		}
		nums = append(nums, n)
	}
	result := twoSum2(nums, *target)
	fmt.Printf("Result is: %v\n", result)
}
