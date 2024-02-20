package main

import (
	"fmt"
	"flag"
)

func longestCommonPrefix(strs []string) string {
	fmt.Println(strs)
	return ""
}


func main() {
	fmt.Println("hello")
	strs := flag.Args()
	var st []string
	for _, v := range(strs) {
		st = append(st, v)
	}
	longestCommonPrefix(st)
}

// func main() {
	// target := flag.Int("target", 0, "Defines the target number")
	// flag.Parse()
	// strNums := flag.Args()
	// var nums []int 
	// for _,v := range strNums {
		// n, err := strconv.Atoi(v)
		// if err != nil {
			// log.Fatalf("Bad param: %s\n", err)
		// }
		// nums = append(nums, n)
	// }
	// result := twoSum2(nums, *target)
	// fmt.Printf("Result is: %v\n", result)
// }
