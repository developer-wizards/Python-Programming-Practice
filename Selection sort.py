'''
Given a Array of N items and L=0, Selection sort will:
1. find the position X of the smallest element in Array[L...N-1]
2. Swap Xth element with Lth item
3. Increase the value of L by 1 and repeat the step 1 for L=N-2

Without loss of generality, we can also implement Selection Sort in reverse:
Find the position of the largest item Y and swap it with the last item.

Complexity Analyis:-

void selectionSort(int A[], int N){
    for(L=0;L<=N-2;L++){ //O(n)
        int K = min_element(A[L..N]); //O(n)
        swap(A[K], A[L]);
    }
}

therefore, T.C is O(n^2)

Algo:-

repeat(numOfElements -1) times
    set 1st unsorted element as a minimum
    for each of the unsorted elements
        if element < minimum:
            set element as a new minimum
    swap minimum with first unsorted position

'''

#Code :-

def selectionSort(nums):
    for i in range(0,len(nums)-1):
        #minimum = nums[i]
        min_index = i
        for j in range(i+1, len(nums)):
            if(nums[j] < nums[i]):
                #minimum = nums[j]
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i] #Swapping
        print(i,end=' ');print(nums); #Printing the output of each pass - if you 
    return nums

#driver code
#nums = [9,8,7,6,5,4,32,1]
nums = [9,8,7,6,5,4,3,2,1]
print(-1, end=' ');print(nums) #print original array
result = selectionSort(nums);
print(result)
        
