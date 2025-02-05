'''
insertion sort (O(n^2)) pseudocode

procedure INSERTION-SORT(A)
    for j = 2 to length[A] do
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key do
            A[i + 1] = A[i]
            i = i - 1
        end while
        A[i + 1] = key
    end for
end procedure

Explanation of the Pseudocode:
	Initialization: The algorithm starts with the second element (index 2), as a single-element array (the first element) is inherently sorted.
	Outer Loop: The outer loop iterates through each element of the array from the second to the last.
	Key Element: The current element (key) is stored, and a pointer i is initialized to the index of the last sorted element.
	Inner Loop: The inner loop shifts elements in the sorted portion of the array to the right until it finds the correct position for the key.
	Insertion: Finally, the key is placed in its correct position.
'''

