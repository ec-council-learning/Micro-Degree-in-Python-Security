#%% Conditionals are made up of if's and else's.
x = 2
if x % 2 == 0:
    print('x is even.')
else:
    print('x is odd.')

#%% "elif" (else if) is used to go through multiple conditions.
if x % 3 == 0:
    print('x is divisible by 3.')
elif x % 3 == 1:
    print('x is congruent to 1 mod 3.')
else:
    print('x is congruent to 2 mod 3.')

#%% "and" and "or" are used to check for the truth value of combined conditions.
if x > 0 and x % 2 == 0:
    print('x is a positive even integer.')

if x % 2 == 0 or x % 3 == 0:
    print('x is divisible by either 2 or 3.')

#%% Conditionals can be nesting inside each other.
if x % 2 == 0:
    if x % 3 == 0:
        print('x is divisible by 6.')
    else:
        print('x is divisible by 2 but not by 3.')
