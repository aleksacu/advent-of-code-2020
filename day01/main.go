package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
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

func partOne(entries []int) int {
	for i, v := range entries {
		for _, e := range entries[i+1:] {
			if v+e == 2020 {
				return v * e
			}
		}
	}
	return -1
}

func partTwo(entries []int) int {
	for i, v := range entries {
		for j, e := range entries[i+1:] {
			for _, n := range entries[j+1:] {
				if v+e+n == 2020 {
					return v * e * n
				}
			}
		}
	}
	return -1
}

func main() {
	data := readInput("./input.txt")

	inputs := strings.Split(data, "\n")
	inputs = inputs[:len(inputs)-1]
	entries := make([]int, len(inputs))

	for i, v := range inputs {
		entry, err := strconv.Atoi(v)
		check(err)
		entries[i] = entry
	}

	solution := partOne(entries)
	if solution == -1 {
		fmt.Println("No two entries sum up to 2020")
	} else {
		fmt.Println("Part one:", solution)
	}

	solution = partTwo(entries)
	if solution == -1 {
		fmt.Println("No three entries sum up to 2020")
	} else {
		fmt.Println("Part two:", solution)
	}
}
