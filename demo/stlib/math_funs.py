def iseven(n):
    """
    Check whether number is even
    :param n: Number to check
    :return: True on even, False otherwise
    """
    return n % 2 == 0


def ispositive(n):
    return n > 0


def isprime(n):
    """
    Check whether number is prime
    :param n: Number to check
    :return: True on prime, False otherwise
    """
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


# Testing
if __name__ == '__main__':  # Name of the module
    print(isprime(10), isprime(11))
