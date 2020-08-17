#%% A Python set can be declared with curly braces.
a = {1, 2, 3}

#%% Items that are already in a set won't be added again.
a.add(4)
print(a)

a.add(3)
print(a)

#%% Unions and intersections of sets can be computed.
b = {2, 4, 5}

print('A intersect B:')
print(a.intersection(b))

print('B union A:')
print(b.union(a))
