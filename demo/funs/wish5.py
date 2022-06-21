def wish(*names, message='Hi'):
    print(type(names))
    for n in names:
        print(message, n)


wish("Bill", "Mark", "Larry", message="Hello")
wish("Jack", "Lee")
