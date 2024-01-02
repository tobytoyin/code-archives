package array

import (
	"errors"
	"sort"
)

// create a new ordered array based on an array
func NewOrderedArray(data []int) *orderedArray {
	sort.Ints(data)
	return &orderedArray{data}
}

// private ds
type orderedArray struct {
	data []int
}

func (array *orderedArray) search(target int) (int, error) {
	// iterate the array from the sorted left to right
	// orderedArray perform 2 types of comparison in search:
	// 1. equality of the search target
	// 2. gt of the search target to halt future search

	// if element is found, return the idx
	// if element isn't found, return the idx at search halt

	for idx, num := range array.data {
		if num == target {
			return idx, nil
		}

		if num > target {
			return idx, errors.New("value not found in array")
		}
	}
	return len(array.data), errors.New("value not found in array")
}
