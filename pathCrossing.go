package main

import (
	"fmt"
	"log"
	"os"
)

func isPathCrossing(path string) bool {
	fmt.Printf("Processing path: %s\n", path)
	var x, y int
	x, y = 0, 0
	var cache [][]int
	cache = append(cache, []int{x, y})
	for _, char := range path {
		switch {
		case string(char) == "N":
			y += 1
		case string(char) == "E":
			x += 1
		case string(char) == "S":
			y -= 1
		case string(char) == "W":
			x -= 1
		default:
			log.Fatalf("Direction %s not recognized\n", string(char))
		}
		coordinates := []int{x, y}
		fmt.Printf("Current coordinates: (%d %d)\n", x, y)
		for _, cord := range cache {
			if cord[0] == coordinates[0] && cord[1] == coordinates[1] {
				return true
			}
		}
		cache = append(cache, coordinates)
	}
	return false
}

func main() {
	path := os.Args[1]
	result := isPathCrossing(path)
	fmt.Printf("Is path crossing: %v\n", result)
}
