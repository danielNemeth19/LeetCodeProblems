## Counting bits
Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` `(0 <= i <= n)`, `ans[i]` is the number of 1's in the binary representation of i.

### Example 1:
* Input: n = 2
* Output: [0,1,1]
* Explanation:
```
0 --> 0
1 --> 1
2 --> 10
```

### Example 2:
* Input: n = 5
* Output: [0,1,1,2,1,2]
* Explanation:
```
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

### Constraints
* `0 <= n <= 10<sup>5</sup>`



### Go solution uses bitwise and operations
Let's consider two 4-bit binary numbers:
```
A = 1101
B = 1011
```

Performing the bitwise AND operation on A and B:
```
   1101
&  1011
------
   1001
```

### Explanation:

- The first bit of A is 1 and the first bit of B is 1. The result is 1.
- The second bit of A is 1 and the second bit of B is 0. The result is 0.
- The third bit of A is 0 and the third bit of B is 1. The result is 0.
- The fourth bit of A is 1 and the fourth bit of B is 1. The result is 1.

So, `1101 & 1011` results in `1001`.

### In the context of the go solution:

```go
k &= k-1
```

This operation is used to remove the lowest set bit (1) from the integer `k`. Here's how it works:

- `k-1` flips all the bits after the rightmost set bit (including the rightmost set bit itself).
- Performing `k & (k-1)` clears the rightmost set bit of `k`.

#### Example:

Let's say `k = 6` (binary `110`):
```
k     = 110
k-1   = 101
k & (k-1) = 100
```

The rightmost set bit in `110` is at position 1 (from the right). Subtracting 1 from `110` gives `101`, and performing the bitwise AND operation between `110` and `101` results in `100`, effectively removing the rightmost set bit.

This operation is repeated in the inner loop of the `countBits` function to count the number of 1-bits in the binary representation of `i`.
