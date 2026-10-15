# this function sorts an array using the insertion sort algorithm
def insertionSort(arr):
    # this loop iterates through the array
    for i in range(0, len(arr)):
        # this loop iterates through the earlier elements in the array to the current value at index i
        for j in range(0, i):
            # checks if the value at i is greater than earlier elements
            if arr[i] < arr[j]:
                # swaps the two items if they are in the wrong order
                arr[i], arr[j] = arr[j], arr[i]

    return arr

print(insertionSort([5,3,6,1,4,2]))