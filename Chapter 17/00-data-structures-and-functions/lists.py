#%% A Python list is an array of ordered elements.
a = [1, 2, 3]
print(a)
print(a[0])
print(a[2])
print(a[-2])

#%% Slicing a Python list results in a sublist.
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(b)
print(b[1:5])

#%% Skipping can be done with a second colon.
print(b[1::2])

#%% A list can be extended via appending or concatenation
c = [1, 2, 3]
print(c)

c.append(4)
print(c)

c += [5, 6, 7]
print(c)

#%% len() returns the length of a list.
print(len(c))
