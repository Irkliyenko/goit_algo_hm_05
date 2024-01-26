def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    num_of_iterations = 0

    while low <= high:

        mid = (high + low) // 2
        num_of_iterations += 1

        # If x is greater than the value in the middle, ignore the left half
        if arr[mid] < x:
            low = mid + 1

        # If x is less than the value in the middle, ignore the right half
        elif arr[mid] > x:
            high = mid - 1

        # If x is found at the middle, return its index, number of iterations, and update the upper bound
        else:
            upper_bound = arr[mid + 1]
            return (mid, num_of_iterations, upper_bound)

    # If the element is not found
    return -1


if __name__ == '__main__':

    arr = [2.5, 3.1, 4.2, 7.3, 8.0, 9.5, 12.7, 15.3, 17.0, 20.2]
    x = 8.0
    result = binary_search(arr, x)
    print(result)
