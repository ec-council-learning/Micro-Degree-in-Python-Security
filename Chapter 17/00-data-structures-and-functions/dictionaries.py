#%% A dictionary is initialized with curly braces.
a = {
    'Alice': 2,
    'Bob': 5,
    'Carol': 10
}

print(a['Alice'])
print(a['Carol'])
print(a['Dan'])

#%% Adding a new key is done in the same way as changing the value of a key.
a['Bob'] = 7
a['Dan'] = 6
print(a)

#%% Not everything can be a dictionary key.
a[1] = 2
a[(1, 2)] = 0
print(a)
a[[1, 2]] = 0
print(a)
