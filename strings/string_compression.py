def compress_string(s):
    compressed = ""
    count = 1
    length = len(s)

    # Iterate through the characters of the string
    for i in range(1, length):
        if s[i] == s[i - 1]:
            # If the current character is the same as the previous one, increment the count
            count += 1
        else:
            # If the current character is different, append the previous
            # character and its count to the compressed string
            compressed += s[i - 1] + str(count)
            count = 1

    # Append the last character and its count
    compressed += s[length - 1] + str(count)

    # Check if the compressed string is shorter than the original string
    if len(compressed) >= length:
        return s
    else:
        return compressed

# Example usage
input_str = "aaabbbcc"
compressed_str = compress_string(input_str)
print(compressed_str)  # Output: "a3b3c2"
