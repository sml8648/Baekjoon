package main

import (
    "fmt"
    "sort"
    "strconv"
)

func main() {
    var N int
    fmt.Scanln(&N)

    // Convert the integer N to a string to sort its digits
    digits := strconv.Itoa(N)

    // Convert the string back to an array of runes for sorting
    runes := []rune(digits)

    // Sort the array of runes in descending order
    sort.Slice(runes, func(i, j int) bool {
        return runes[i] > runes[j]
    })

    // Convert the sorted array of runes back to a string
    sortedDigits := string(runes)

    // Convert the sorted string of digits back to an integer
    sortedN, _ := strconv.Atoi(sortedDigits)

    fmt.Println(sortedN)
}