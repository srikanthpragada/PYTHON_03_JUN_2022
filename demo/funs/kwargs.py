def show(**details):
    print(details)


def display(*args, **kwargs):
    print(args)
    print(kwargs)


show(x=10, y=20, msg="Hello")
display(10, 20, 30, x=10, y=40)
