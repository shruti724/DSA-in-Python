def second_largest_element(li):

    li.remove(max(li))
    return max(li)


li = [1, 5, 4, 6, 34]
print(second_largest_element(li))
