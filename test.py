from heap import heapSort
from merge import mergeSort
from tim import timSort

arr = [1,3,4,2]
heapSort(arr)
assert arr == [1,2,3,4]

arr = [1,3,4,2]
mergeSort(arr)
assert arr == [1,2,3,4]

arr = [1,3,4,2]
timSort(arr)
assert arr == [1,2,3,4]
