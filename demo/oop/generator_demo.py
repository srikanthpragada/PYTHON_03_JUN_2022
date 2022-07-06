def numbers(count):
    for n in range(count):
        yield n + 1


nums = numbers(5)
print(nums)
print(next(nums))
print(next(nums))

