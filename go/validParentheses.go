package main

import (
	"flag"
	"fmt"
	"strings"
)

func isValid(s string) bool {
	for true {
		removal := 0
		if strings.Contains(s, "()") {
			removal ++
			s = strings.Replace(s, "()", "", -1)
		}
		if strings.Contains(s, "[]") {
			removal ++
			s = strings.Replace(s, "[]", "", -1)
		}
		if strings.Contains(s, "{}") {
			removal ++
			s = strings.Replace(s, "{}", "", -1)
		}
		if  s == "" {
			fmt.Printf("All cleared!\n")
			return true
		}
		if removal == 0 {
			fmt.Printf("Remained: %s\n", s)
			return false
		}
	}
	return true
}

func main() {
	input := flag.String("input", "", "String to be checked if valid parentheses")
	flag.Parse()
	sum := isValid(*input)
	fmt.Printf("verdict: %t\n", sum)
}
