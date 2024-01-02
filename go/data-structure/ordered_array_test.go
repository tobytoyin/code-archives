package array

import (
	"fmt"
	"testing"
)

func TestOrderedArray(t *testing.T) {
	array1 := NewOrderedArray([]int{202, 17, 3, 80})
	fmt.Println(array1)

}

func TestSearch(t *testing.T) {
	array1 := NewOrderedArray([]int{202, 17, 3, 80})

	idx, _ := array1.search(3)
	fmt.Printf("search found at index %d\n", idx)

	idx, err := array1.search(81)
	fmt.Println(err)
	fmt.Printf("search stops at index %d\n", idx)
}
