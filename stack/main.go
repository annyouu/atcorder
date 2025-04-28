package main

import (
	"bufio"
	"fmt"
	"os"
)

func isValid(s string) bool {
	stack := []rune{}
	pairs := map[rune]rune{
		'(':')',
		'{':'}',
		'[':']',
	}

	for _, char := range s {
		if _, ok := pairs[char]; ok {
			stack = append(stack, char)
		} else if char == ')' || char == '}' || char == ']' {
			if len(stack) == 0 {
				return false
			}

			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if pairs[top] != char {
				return false
			}
		}
	}
	return len(stack) == 0
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		s := scanner.Text()
		result := isValid(s)
		fmt.Println(result)
	}
}