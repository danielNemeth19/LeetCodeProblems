package main

import (
	"fmt"
	"log"
	"os"
)


type Point struct {
	x, y int
	visitedPaths [][]int
} 

func (p *Point) offSet(axis string, direction int) {
	if axis == "x" {
		p.x += direction
	} else {
		p.y += direction
	}
}

func (p *Point) checkIfVisited() bool {
	for _, coordinates := range p.visitedPaths {
		if coordinates[0] == p.x && coordinates[1] == p.y {
			return true
		}
	}
	return false
}

func (p *Point)storeCoordinates() {
	p.visitedPaths = append(p.visitedPaths, []int{p.x, p.y})
}

func (p *Point) isPathCrossing(path string) bool {
	for _, char := range path {
		switch {
		case string(char) == "N":
			p.offSet("y", 1)
		case string(char) == "E":
			p.offSet("x", 1)
		case string(char) == "S":
			p.offSet("y", -1)
		case string(char) == "W":
			p.offSet("x", -1)
		default:
			log.Fatalf("Direction %s not recognized\n", string(char))
		}
		fmt.Printf("Current coordinates: (%d %d)\n", p.x, p.y)
		if !p.checkIfVisited() {
			p.storeCoordinates()
		} else {
			return true
		}
	}
	return false
}


func main() {
	path := os.Args[1]
	point := Point{x: 0, y: 0}
	point.storeCoordinates()
	verdict := point.isPathCrossing(path)
	fmt.Printf("Verdit is: %v\n", verdict)

}
