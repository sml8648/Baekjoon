package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func primeList(n int) []int {
	// 에라토스테네스의 체 초기화: n개 요소에 true 설정(소수로 간주)
	sieve := make([]bool, n)
	for i := range sieve {
		sieve[i] = true
	}

	// n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
	m := int(math.Sqrt(float64(n)))
	for i := 2; i <= m; i++ {
		if sieve[i] { // i가 소수인 경우
			for j := i * i; j < n; j += i { // i 이후 i의 배수들을 false 판정
				sieve[j] = false
			}
		}
	}

	// 소수 목록 산출
	primes := make([]int, 0)
	for i := 2; i < n; i++ {
		if sieve[i] {
			primes = append(primes, i)
		}
	}
	return primes
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	n := 1000000

	result := primeList(n)

	var s, e int
	fmt.Fscan(reader, &s, &e)

	for _, each := range result {
		if each >= s && each <= e {
			fmt.Println(each)
		} else if each > e {
			break
		}
	}
}