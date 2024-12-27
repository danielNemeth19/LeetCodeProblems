package main

import (
	"flag"
	"fmt"
	"slices"
	"strconv"
	// "strconv"
)

func decomposeNumber(n int) []uint8 {
	var res []uint8
	for n > 0 {
		remainder := n % 10
		res = append(res, uint8(remainder))
		n = n / 10
	}
	return res
}

func splitNum(num int) int {
	nums := decomposeNumber(num)
	var n1, n2 string
	slices.Sort(nums)
	for i, v := range nums {
		if i%2 == 0 {
			n1 += strconv.Itoa(int(v))
		} else {
			n2 += strconv.Itoa(int(v))
        }
	}
    n1_int,_ := strconv.Atoi(n1)
    n2_int,_ := strconv.Atoi(n2)
    return n1_int + n2_int
}

func main() {
	nums := flag.Int("num", 0, "Input number to work on")
	flag.Parse()
    r := splitNum(*nums)
    fmt.Println(r)
}
