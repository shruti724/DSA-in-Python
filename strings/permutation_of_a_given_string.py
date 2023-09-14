# def permutation(word):
#     if len(word)==1:
#         return [word]
#
#     perms = permutation(word[1:])
#     char = word[0]
#     result = []
#
#     for perm in perms:
#         for i in range(len(perm)+1):
#             result.append(perm[:1] + char + perms[1:])
#
#     return result
#
#
# word = "ABC"
# print(permutation(word))


# lis = [1, 2, 4, 5]
# print(*lis)

# ------------------------------------------------------------------------------------------------------------------------

def permutation(word):
    if len(word) == 0:
        return ['']

    result = []

    for i in range(len(word)):
        char = word[i]
        perms = permutation(word[:i] + word[i + 1:])
        for perm in perms:
            result.append(char + perm)

    return result


word = "ABCE"
print(permutation(word))
