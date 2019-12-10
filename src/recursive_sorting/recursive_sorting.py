# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    arrAIndex = 0
    arrBIndex = 0
    for i in range(len(merged_arr)):
        # If a has no more indexs, add b
        if arrAIndex >= len(arrA) and arrBIndex >= len(arrB):
            return merged_arr
        elif arrAIndex >= len(arrA):
            merged_arr[i] = arrB[arrBIndex]
            arrBIndex += 1  
        elif arrBIndex >= len(arrB):
            merged_arr[i] = arrA[arrAIndex]
            arrAIndex += 1
        elif arrA[arrAIndex] <= arrB[arrBIndex]:
            merged_arr[i] = arrA[arrAIndex]
            arrAIndex += 1
        # arrA[arrAIndex] >= arrB[arrBIndex]
        else:
            merged_arr[i] = arrB[arrBIndex]
            arrBIndex += 1
        print("Merged Array :", merged_arr)
    print("Merged Final :", merged_arr)
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):
    copyArr = list(arr)
    # TO-DO
    if len(arr) > 1:
        split = (len(arr)//2)
        leftSplit = arr[:split]
        rightSplit = arr[split:]
        leftSorted = merge_sort(leftSplit)
        rightSorted = merge_sort(rightSplit)
        # Set arr as merge()
        copyArr = merge(leftSorted, rightSorted)
    return copyArr

print("merge sort: ",merge_sort([2, 5, 3, 8, 9, 7, 1, 1, 9]))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
