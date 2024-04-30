def greet(name="Unknown"):
    print("Hello " + name + "!")


user_input = input("Please type in a name:")
if user_input:
    greet(user_input)
else:
    greet()


