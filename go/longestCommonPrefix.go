package main

import (
	"flag"
	"fmt"
)

func setLength(lenght int, curr int) int {
	if lenght == -1 {
		return curr
	} else {
		return min(lenght, curr)
	}
}

func longestCommonPrefix(strs []string) string {
	base := strs[0]
	if base == "" {
		return ""
	}
	if len(strs) == 1 {
		return base
	}
	lenght := -1
	for _, word := range strs[1:] {
		currLenght := 0
		toIterate := min(len(base), len(word))
		for i := 0; i < toIterate; i++ {
			if string(word[i]) == string(base[i]) {
				currLenght++
			} else {
				lenght = setLength(lenght, currLenght)
				break
			}
		}
		lenght = setLength(lenght, currLenght)
	}
	return base[:lenght]
}



func main() {
	funcToRun := flag.String("problem", "", "Defines the problem to solve")
	flag.Parse()
	fmt.Println(*funcToRun)
	strs := flag.Args()
	result := longestCommonPrefix(strs)
	fmt.Printf("Result is: %s\n", result)
}
