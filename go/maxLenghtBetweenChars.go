package main

import (
	"flag"
	"fmt"
	"strings"
)

func maxLenghtBetweenEqualCharacters(s string) int {
	maxLenght := -1
	reversedString := reverseString(s)
	for _, char := range s {
		posLeft := strings.Index(s, string(char))
		posRight := (len(s) - 1) - strings.Index(reversedString, string(char))
		distance := posRight - posLeft - 1
		fmt.Printf("Distance for %s: %d\n", string(char), distance)
		if distance > maxLenght {
			maxLenght = distance
		}
	}
	return maxLenght
}


func reverseString(s string) string {
	runes := []rune(s)
	fmt.Println(runes)
	for i, j := 0, len(s) - 1; i < j; i, j = i + 1, j - 1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}


func main() {
	input := flag.String("input", "", "String to be analyzed")
	flag.Parse()
	verdict := maxLenghtBetweenEqualCharacters(*input)
	fmt.Printf("verdict: %d\n", verdict)
}
