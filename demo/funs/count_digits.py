def count_digits(s):
    count = 0
    for c in s:
        if c.isdigit():
            count += 1

    return count


print(count_digits("Abc123"))
