formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "hello, it's",
    "me",
    "can you",
    "hear me?",
    "can this line be printed?"# this line will be ommited.
    ))
