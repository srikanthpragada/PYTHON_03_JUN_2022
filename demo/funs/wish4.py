def wish(message="Hi", user='Guest'):
    print(message, user)


wish()
wish("Hello")  # Positional args
wish("Hi", "Bill")
# Keyword args
wish(message="Hello")
wish(user="Larry")
