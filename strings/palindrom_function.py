def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


input_str = "level"
is_pal = is_palindrome(input_str)
print(is_pal)  # Output: True

input_str = "hello"
is_pal = is_palindrome(input_str)
print(is_pal)