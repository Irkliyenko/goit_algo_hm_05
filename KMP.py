def compute_lps(pattern):
    """Compute the Longest Prefix Suffix (LPS) array for the Knuth-Morris-Pratt (KMP) algorithm."""
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
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


def kmp_search(main_string, pattern):
    """Search for a pattern in the main string using the Knuth-Morris-Pratt (KMP) algorithm."""
    M = len(pattern)
    N = len(main_string)
    # Compute the Longest Prefix Suffix (LPS) array for the pattern
    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        # If the entire pattern is found, return its position in the main string
        if j == M:
            return i - j

    return -1  # If the pattern is not found, return -1


if __name__ == "__main__":
    main_string = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    print(kmp_search(main_string, pattern))
