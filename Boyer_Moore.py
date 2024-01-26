def build_shift_table(pattern):
    """Build the shift table for the Boyer-Moore algorithm."""
    table = {}
    length = len(pattern)
    # For each character in the pattern, set the shift equal to the length of the pattern
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # If a character is not in the table, the shift is equal to the length of the pattern
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    """Search for a pattern in the text using the Boyer-Moore algorithm."""
    # Build the shift table for the pattern
    shift_table = build_shift_table(pattern)
    i = 0  # Initialize the starting index for the main text

    # Iterate through the main text, comparing with the pattern
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Start from the end of the pattern

        # Compare characters from the end of the pattern to the beginning
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Move towards the start of the pattern

        # If the entire pattern matches, return its position in the text
        if j < 0:
            return i  # Pattern found

        # Shift the index i based on the shift table
        # This allows skipping over non-matching parts of the text
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # If the pattern is not found, return -1
    return -1


if __name__ == "__main__":
    main_string = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    print(boyer_moore_search(main_string, pattern))
