package sorting

import (
	"fmt"
	"reflect"
	"testing"
)

func TestBubbleSort(t *testing.T) {
	unsorted := []int{4, 2, 7, 1, 3}
	expected := []int{1, 2, 3, 4, 7}

	sorted := *BubbleSort(&unsorted)
	fmt.Println(sorted)

	if !reflect.DeepEqual(sorted, expected) {
		t.Errorf("sorted incorrectly")
	}
}
