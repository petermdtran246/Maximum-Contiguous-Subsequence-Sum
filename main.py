import random

# Generate a list of 1000 random integers, both positive and negative
arr = [random.randint(-1000, 1000) for _ in range(1000)]

def  max_contiguous_subsequence_sum(arr):
    max_current = 0 # Stores the maximum sum found so far
    max_ending = 0 # Stores the current sum of the subsequence being considered
    start_index = 0 # Stores the starting index of the maximum subsequence
    end_index = 0 # Stores the ending index of the maximum subsequence
    temp_start_index = 0 # Stores the temporary starting index while calculating the current sum

    for i in range(len(arr)):
        # Add the current element to the current sum
        max_ending += arr[i]

        if max_ending > max_current:
            # Update the maximum sum and indices if the current sum is greater
            max_current = max_ending
            start_index = temp_start_index
            end_index = i

        if max_ending < 0:
            # Reset the current sum and update the temporary starting index
            max_ending = 0
            temp_start_index = i + 1

    return max_current, start_index, end_index

max_sum, start_index, end_index = max_contiguous_subsequence_sum(arr)

print('Maximum Contiguous Subsequence Sum: ', max_sum)
print('Starting Index of Subsequence: ', start_index)
print('Ending Index of Subsequence: ', end_index)