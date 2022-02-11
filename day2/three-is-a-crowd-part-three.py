names = ["Carlos", "Cyrus", "Fabian", "Alex", "Josiah", "Jordan", "Jonathan"]
print(names)
def crowd_test(names):
    if len(names) > 5:
        print("A mob is in this room")
    elif 3 <= len(names) <= 5:
        print("Room is crowded")
    elif len(names) == 1 or len(names) == 2:
        print("Room is not crowded")
    elif len(names) == 0:
        print("Room is empty")
    print(names)
crowd_test(names)

