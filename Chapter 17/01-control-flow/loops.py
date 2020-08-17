#%% While loops check for the conditions at each step.
x = 1
while x < 10:
    print(x)
    x += 1
print('Loop finished.')

#%% For loops are used to iterate through a sequence of elements.
a = [1, 2, 3]
for item in a:
    print(item)
print()

#%% range(n) returns an iterator from 0 to (n - 1).
for index in range(len(a)):
    print(index, a[index])

#%% One can loop through the keys in a dictionary in a for loop.
dict = {'a': 1, 'b': 2, 'c': 3}
for key in dict:
    print(key, dict[key])
print()

#%% enumerate() returns the individual elements and their corresponding index
#   in pairs in a list.
for index, value in enumerate(a):
    print(index, value)
print()

#%% zip() returns the individual elements of two given lists in pairs.
b = [2, 3, 4]
print(a)
print(b)
print()

for a_i, b_i in zip(a, b):
    print(a_i, b_i)
