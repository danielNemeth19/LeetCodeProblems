package main

import (
	"flag"
	"fmt"
)

func countBits(n int) []int {
    var ans []int
    for i := 0; i <= n; i++ {
        bits := fmt.Sprintf("%b", i)
        ones := 0
        for _, c := range bits {
            if string(c) == "1" {
                ones++
            }
        }
        fmt.Printf("Result for %d (%b) >> %d\n", i, i, ones)
        ans = append(ans, ones)
    }
    return ans
}

func countBitsBetter(n int) []int {
    ans := make([]int, n+1)
    for i:=0; i<=n ; i++ {
        k := i
        for k != 0 {
            ans[i]++
            k &= k -1
        }
    }
    return ans
}

func main() {
	num := flag.Int("num", 0, "Defines the intput value")
	flag.Parse()
    fmt.Println(countBitsBetter(*num))
}
