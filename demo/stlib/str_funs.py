def hasUpper(s):
    for c in s:
        if c.isupper():
            return True

    return False


def countUpper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count
