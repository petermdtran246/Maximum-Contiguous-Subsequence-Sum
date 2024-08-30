# Maximum Contiguous Subsequence Sum
This project involves creating a Python program that generates a random list of 1000 integers (both positive and negative) and finds the maximum contiguous subsequence sum along with its starting and ending indices. This solution implements Kadane’s Algorithm, which works efficiently in O(n) time.

## Project Overview
The program:
1. Generates a random vector of 1000 integers, ranging from -1000 to 1000.
2. Implements an algorithm to find the maximum sum of any contiguous subsequence within the vector.
3. Returns the maximum sum and the indices of the subsequence that produces this sum.

## Files Included
  -  main.py: The main Python script containing the implementation of the maximum contiguous subsequence sum algorithm.
  -  README.md: Documentation and details about the project.

## Algorithm Explanation
The code uses Kadane's Algorithm to find the maximum sum of a contiguous subsequence:

1. Initialization:
  -  max_current: Tracks the sum of the current subsequence.
  -  max_ending: Tracks the maximum sum found so far.
  -  start_index and end_index: Track the starting and ending indices of the subsequence with the maximum sum.
  -  temp_start_index: Temporarily stores the starting index while calculating the current sum.

2. Iteration:
  -  The program iterates through the array, adding each element to max_ending.
  -  If max_ending exceeds max_current, it updates max_current and the indices.
  -  If max_ending drops below zero, it resets max_ending and updates temp_start_index.

3. Output:
  -  The maximum subsequence sum is printed, along with the starting and ending indices.

## Output
The program outputs:
  -  The maximum contiguous subsequence sum.
  -  The starting index of the subsequence.
  -  The ending index of the subsequence.

