def alt_ele_sum(li):
    sum = 0
    for i in range(0, len(li)):
        if i % 2 == 0:
            sum += li[i]
            # print(i, end=" ")
        else:
            continue
    return sum


li = [1, 3, 5, 7, 4]
print(alt_ele_sum(li))
