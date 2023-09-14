def find_duplicates(s):
    duplicates = set()
    length = len(s)

    for i in range(length - 1):
        for j in range(i + 1, length):
            if s[i] == s[j]:
                duplicates.add(s[i])

    duplicates_str = ''.join(duplicates)
    return duplicates_str


# Example usage
input_str = "Hello, World!"
duplicates = find_duplicates(input_str)
print(duplicates)  
