from collections_extended import setlist

sl = setlist("bananarama")
s = set("bananarama")

if __name__ == "__main__":
    print(f"Full set: {sl}")
    print(f"Element at position 3: {sl[3]}")
    print(f"Element at final position: {sl[-1]}")
    print(f"'r' in setlist? {'r' in sl}")
    print(f"Position of 'r': {sl.index('r')}")
    sl.insert(1, "r")  # Inserting value already in set raises error
    print("")
    print(f"Full set: {s}")
    # print(f"Element at position 3: {s[3]}")
    # print(f"Element at final position: {s[-1]}")
    print(f"'r' in setlist? {'r' in s}")
    # print(f"Position of 'r': {s.index('r')}")
    # s.insert(1, "r")  # Inserting value already in set raises error
