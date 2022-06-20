def wish(message, user):
    print(message, user)


wish("Hello", "Larry")  # Positional args
wish("Hi", "Bill")
# Keyword args
wish(user="Steve", message="Hello")
