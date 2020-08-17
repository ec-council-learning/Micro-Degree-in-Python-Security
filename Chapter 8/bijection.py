from collections_extended import bijection

bij = bijection({"a": 1, "b": 2, "c": 3})


if __name__ == "__main__":
    print(bij.inverse[2])
    bij["a"] = 2
    print(bij == bijection({"a": 2, "c": 3}))
    bij.inverse[1] = "a"
    print(bij == bijection({"a": 1, "c": 3}))
    print(bij.inverse.inverse is bij)
