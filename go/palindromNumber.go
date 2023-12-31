package main

import (
	"flag"
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	stringX := strconv.Itoa(x)
	slots := len(stringX)
	revSlice := make([]string, slots)
	for i := range stringX {
		revSlice[slots - 1] = string(stringX[i])
		slots -= 1
	}
	var revStringX string
	for _, char := range revSlice {
		revStringX += char
	}
	fmt.Printf("comparing: %s -- %s\n", stringX, revStringX)
	return stringX == revStringX
}

func isPalindrome2(x int) bool {
	stringX := strconv.Itoa(x)
	runes := []rune(stringX)
	for i, j := 0, len(runes) - 1; i < j; i, j = i+1, j-1 {
		fmt.Printf("%d -- %d\n", i, j)
		runes[i], runes[j] = runes[j], runes[i]
	}
	fmt.Printf("comparing: %s -- %s\n", stringX, string(runes))
	return stringX == string(runes)
}

func main() {
	target := flag.Int("target", 0, "Defines the target number")
	flag.Parse()
	verdict := isPalindrome2(*target)
	fmt.Printf("verdict: %t\n", verdict)
}
