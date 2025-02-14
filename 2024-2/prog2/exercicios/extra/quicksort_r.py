'''
def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        less = [x for x in l[1:] if x <= pivot]
        greater = [x for x in l[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
'''

def quick_sort(l):
    if len(l) <= 1:
        return l

    pivot = l[0]

    less = []
    equal = []
    greater = []

    for element in l:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)

    return quick_sort(less) + equal + quick_sort(greater)
