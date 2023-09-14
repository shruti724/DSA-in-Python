# Knuth-Morris-Pratt (KMP):

def compute_lps_table(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of the previous longest prefix suffix

    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps_table(pattern)

    i = j = 0  # Pointers for text and pattern

    occurrences = []  # List to store the indices of pattern occurrences

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:  # Pattern found
                occurrences.append(i - j)
                j = lps[j - 1]  # Move j to the previous longest prefix suffix
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences


# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matches = kmp_search(text, pattern)
print(matches)  # Output: [10]

