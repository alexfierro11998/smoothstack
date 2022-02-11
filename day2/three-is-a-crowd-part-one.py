names = ["Carlos", "Cyrus", "Fabian", "Alex"]
print(names)
def crowd_test(names):
    if len(names) > 3:
        print("Room is crowded")
    while len(names) > 3:
        names.pop()
    print(names)
crowd_test(names)

