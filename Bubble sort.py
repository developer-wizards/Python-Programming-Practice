'''
Given an array of N element, Bubble sort will:
1. Compare a pair of adjacent elements (a,b)
2. Swap them if they are not in order (if a> b)
3. repeat step 1 and 2 untill we reach at the end of the array
 (the last pair is the (N-2)-th and (N-1)-th items as we use 0-based indexing)
4. By now the largest element will be at last position, we now reduce N by 1 and repeat step 1 untill we have N=1

Why called as bubble sort?
-- In each pass last element will always be at it correct position,
the element of array is act as a bubble, the biggest bubble will come first out and this process repeats

Comparison and swap require time that is bounded by a constant, let's call it c.
There are two nested loops in (the standard) Bubble Sort.

The outer loop runs for exactly N iterations.
But the inner loop runs get shorter and shorter:

When i=0, (N−1) iterations (of comparisons and possibly swaps),
When i=1, (N−2) iterations,
...,
When i=(N−2), 1 iteration,
When i=(N−1), 0 iteration.
Thus, the total number of iterations = (N−1)+(N−2)+...+1+0 = N*(N−1)/2, Total time = c*N*(N−1)/2 = O(N^2).

Tech Algorithm:-
do
  swapped = False
  for i = 0 to N-1
      if leftElement > RightElement:
          swap(leftElement, RightElement)
          swapped = True
  N -= 1
While swapped

Efficiency?
Bubble Sort is actually inefficient with its O(N^2) time complexity. Imagine that we have N = 105 numbers.
Even if our computer is super fast and can compute 108 operations in 1 second, Bubble Sort will need about 100 seconds to complete.
However, it can be terminated early, e.g. try bubble sort on the small sorted ascending example shown above [3, 6, 11, 25, 39] where it terminates in O(N) time.
The improvement idea is simple: If we go through the inner loop with no swapping at all, it means that the array is already sorted and we can stop Bubble Sort
at that point.

'''

def bubbleSort(x):

    for i in range(len(x)):

        for j in range(len(x) - i -1):

            if(x[j]>x[j+1]):
                x[j], x[j+1] = x[j+1], x[j]


    return x

#driver code
arr = [4,1,9,0,5,7,2,8]
result = bubbleSort(arr)
print(result)
    

