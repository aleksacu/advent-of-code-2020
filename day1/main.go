package main

import (
	"errors"
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

func partOne(entries []int) (int, error) {
	for i, v := range entries {
		for _, e := range entries[i+1:] {
			if v + e == 2020 {
				return v * e, nil
			}
		}
	}
	return 0, errors.New("No entries sum up to 2020")
}

func partTwo(entries []int) (int, error) {
	for i, v := range entries {
		for j, e := range entries[i+1:] {
			for _, n := range entries[j+1:] {
				if v + e + n == 2020 {
					return v * e * n, nil
				}
			}
		}
	}
	return 0, errors.New("No triplet sums up to 2020")
}

func main() {
	data := readInput("./input.txt")

	inputs := strings.Split(data, "\n")
	inputs = inputs[:len(inputs) - 1]
	entries := make([]int, len(inputs))

	for i, v := range inputs {
		entry, err := strconv.Atoi(v)
		check(err)
		entries[i] = entry
	}

	solution, err := partOne(entries)
	check(err)
	fmt.Println("Part one:", solution)

	solution, err = partTwo(entries)
	fmt.Println("Part two:", solution)
}
