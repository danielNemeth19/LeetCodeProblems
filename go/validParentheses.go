package main

import (
	"flag"
	"fmt"
	"strings"
)

func isValid(s string) bool {
	for true {
		if strings.Contains(s, "()") {
			fmt.Printf("Found ()")
		}
	}
	return false
}

func main() {
	input := flag.String("input", "", "String to be checked if valid parentheses")
	flag.Parse()
	sum := isValid(*input)
	fmt.Printf("verdict: %t\n", sum)
}
