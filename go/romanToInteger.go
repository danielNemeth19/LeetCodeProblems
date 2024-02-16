package main

import (
	"flag"
	"fmt"
)

var romanMap = map[string]int{
	"I": 1,
	"IV": 4,
	"V": 5,
	"IX": 9,
	"X": 10,
	"XL": 40,
	"L": 50,
	"XC": 90,
	"C": 100,
	"CD": 400,
	"D": 500,
	"CM": 900,
	"M": 1000,
}

func getNextSymbol(i int, s string) string {
	if i == len(s) - 1 {
		return ""
	}
	return string(s[i + 1])
}

func romanToInt(s string) int {
	var result int
	skipNext := false
	for i, c := range s {
		if skipNext {
			skipNext = false
			continue
		}
		nextSymbol := getNextSymbol(i, s)
		potentialSymbol := string(c)+nextSymbol
		v, found := romanMap[potentialSymbol]
		if found == true {
			skipNext = true
			result += v
		} else {
			result += romanMap[string(c)]
		}
	}
	return result 
}

func main() {
	input := flag.String("input", "", "Roman number to convert")
	flag.Parse()
	sum := romanToInt(*input)
	fmt.Printf("sum: %d\n", sum)
}
