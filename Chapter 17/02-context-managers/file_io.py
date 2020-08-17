#%% Verbose file I/O can be dangerous if one forgets to close a file.
f = open('02-context-managers/sample.txt', 'r')

lines = f.readlines()
print(lines)

f.close()

#%% Context managers automatically handle closing a file.
with open('02-context-managers/sample.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
