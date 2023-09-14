def second_min_ele(li):
    li.remove(min(li))
    return min(li)


li = [3, 2, 5, 6, 8]
print(second_min_ele(li))