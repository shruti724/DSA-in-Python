def reverse_string(s):
    left = 0
    right = len(s) - 1
    chars = list(s)  # Convert string to a list of characters

    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    reversed_string = "".join(chars)  # Convert the list back to a string
    return reversed_string


input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print(reversed_str)