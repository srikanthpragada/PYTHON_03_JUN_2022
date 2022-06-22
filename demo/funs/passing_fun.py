def math_op(operation, a, b):
    return operation(a, b)


def add(n1, n2):
    return n1 + n2


print(math_op(add, 10, 20))
