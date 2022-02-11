names = ["Carlos", "Cyrus", "Fabian", "Alex"]
print(names)
def crowd_test(names):
    if len(names) > 3:
        print("Error: Too Many Names")
    else:
        print("Room is not very crowded")
    while len(names) > 3:
        names.pop()
    print(names)
crowd_test(names)

