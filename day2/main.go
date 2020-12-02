package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func readInput(filePath string) string {
	data, err := ioutil.ReadFile(filePath)
	check(err)
	return string(data)
}

func count(passwords string) (int, int) {
	var partOneCount int
	var partTwoCount int

	pattern := regexp.MustCompile(
		"(?P<min>[1-9][0-9]*)\\-(?P<max>[1-9][0-9]*) (?P<letter>[a-z]): (?P<password>[a-z]+)\n",
	)
	matches := pattern.FindAllStringSubmatch(passwords, -1)

	for _, match := range matches {
		min, err := strconv.Atoi(match[1])
		check(err)
		max, err := strconv.Atoi(match[2])
		check(err)
		letter := match[3][0]
		letterRune := rune(letter)
		password := match[4]

		numOccurences := 0
		for _, l := range password {
			if l == letterRune {
				numOccurences++
			}
		}
		if numOccurences >= min && numOccurences <= max {
			partOneCount++
		}

		if (password[min-1] == letter) != (password[max-1] == letter) {
			partTwoCount++
		}
	}

	return partOneCount, partTwoCount
}

func main() {
	data := readInput("./input.txt")
	partOne, partTwo := count(data)
	fmt.Println("Part one:", partOne)
	fmt.Println("Part two:", partTwo)
}
