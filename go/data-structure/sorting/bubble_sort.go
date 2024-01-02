package sorting

// perform bubble sort on the slice
func BubbleSort[T []int](arrPtr *T) *T {
	array := *arrPtr
	sorted := true // determine if sort has performed

	for idx := 1; idx < len(array); idx++ {
		if array[idx-1] > array[idx] {
			sorted = false

			tmp := array[idx-1]
			array[idx-1] = array[idx]
			array[idx] = tmp
		}
	}

	if sorted == true {
		return &array
	}

	// recursion on BubbleSort again
	return BubbleSort(&array)
}
