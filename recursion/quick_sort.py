def partation(arr, si, ei):
    count_smaller_ele = 0
    i = si + 1
    while i <= ei:

        if arr[i] < arr[si]:
            count_smaller_ele += 1
            i += 1
        else:
            i += 1
    arr[si + count_smaller_ele], arr[si] = arr[si], arr[si + count_smaller_ele]

    x = arr[si + count_smaller_ele]
    s = 0
    e = len(arr) - 1
    while s <= e:
        if arr[s] < x:
            s += 1
        elif arr[e] > x:
            e -= 1
        else:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1

    return si + count_smaller_ele


def quick_sort(arr, si, ei):
    if si >= ei:
        return
    pivot_index = partation(arr, si, ei)
    quick_sort(arr, si, pivot_index-1)
    quick_sort(arr, pivot_index+1, ei)
    return arr


arr = [4, 8, 5, 2, 3, 1]
print(quick_sort(arr, 0, len(arr)-1))
