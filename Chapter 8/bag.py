from collections_extended import bag

b = bag("bananarama")
s = set("bananarama")

if __name__ == "__main__":
    print(b.count("a"))
    b.remove("a")
    print(b.count("a"))
    print("a" in b)
    print(b.count("r"))
    b.remove("r")
    print(b.count("r"))
    print("r" in b)
    print("")
    # print(s.count("a"))
    s.remove("a")
    # print(s.count("a"))
    print("a" in s)
    # print(s.count("r"))
    s.remove("r")
    # print(s.count("r"))
    print("r" in s)
