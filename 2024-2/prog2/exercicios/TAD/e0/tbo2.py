'''
selection sort (O(n^2)) pseudocode

procedure SELECTION-SORT(A)
    n = length(A)
    for i = 0 to n - 1 do
        minIndex = i
        for j = i + 1 to n - 1 do
            if A[j] < A[minIndex] then
                minIndex = j
            end if
        end for
        swap(A[i], A[minIndex])
    end for
end procedure

Explanation of the Pseudocode:
    Initialization: The algorithm begins by determining the length of the array A.
    Outer Loop: The outer loop iterates over each element of the array, treating the current index i as the starting point of the unsorted section.
    Finding Minimum: The inner loop searches through the unsorted section (from i+1 to the end of the array) to find the index of the minimum element.
    Swapping: After identifying the minimum element's index, it swaps that element with the one at index i, effectively expanding the sorted portion of the array.
'''

def selecao(lista):
    menor = 0
    i = 0
    j = 0

    for i in range(len(lista) - 1):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j

        aux = lista[menor]
        lista[menor] = lista[j]
        lista[j] = aux

    return lista