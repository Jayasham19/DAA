def horspool(text, pattern):
    m = len(pattern)
    n = len(text)

    if m > n:
        return -1

    # Step 1: Create the shift table with 256 ASCII characters
    shift = [m] *150
    for i in range(m - 1):
        shift[ord(pattern[i])] = m - 1 - i

    # Step 2: Search phase
    pos = 0
    while pos <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[pos + j]:
            j -= 1
        if j < 0:
            return pos  # Match found
        else:
            pos += max(1, shift[ord(text[pos + m - 1])])

    return -1  # No match found
text = "ababcababcac"
pattern = "abcac"
index = horspool(text, pattern)

if index != -1:
    print(f"Pattern found at index {index}")
else:
    print("Pattern not found")