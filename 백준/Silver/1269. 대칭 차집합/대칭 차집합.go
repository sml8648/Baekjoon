package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// 표준 입력에서 입력을 읽기 위한 bufio.Reader 생성
	reader := bufio.NewReader(os.Stdin)

	// 첫 번째 줄을 읽어들여 A와 B의 원소 개수를 가져옴
	countsInput, _ := reader.ReadString('\n')
	countsInput = strings.TrimSpace(countsInput)
	// counts := strings.Split(countsInput, " ")
	// countA, _ := strconv.Atoi(counts[0])
	// countB, _ := strconv.Atoi(counts[1])

	// 두 번째 줄과 세 번째 줄을 읽어들여 A와 B의 원소를 가져옴
	setAInput, _ := reader.ReadString('\n')
	setAInput = strings.TrimSpace(setAInput)
	setA := make(map[int]bool)
	setAElements := strings.Split(setAInput, " ")
	for _, element := range setAElements {
		num, _ := strconv.Atoi(element)
		setA[num] = true
	}

	setBInput, _ := reader.ReadString('\n')
	setBInput = strings.TrimSpace(setBInput)
	setB := make(map[int]bool)
	setBElements := strings.Split(setBInput, " ")
	for _, element := range setBElements {
		num, _ := strconv.Atoi(element)
		setB[num] = true
	}

	// A-B, B-A의 원소 수를 계산하고 더함
	diffAB := difference(setA, setB)
	diffBA := difference(setB, setA)
	symmetricDifferenceCount := len(diffAB) + len(diffBA)

	// 결과 출력
	fmt.Println(symmetricDifferenceCount)
}

// 집합 A에서 집합 B의 원소를 제외한 결과를 반환
func difference(setA, setB map[int]bool) []int {
	result := []int{}
	for element := range setA {
		if !setB[element] {
			result = append(result, element)
		}
	}
	return result
}