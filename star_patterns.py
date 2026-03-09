# 1st pattern
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()

print()

# 2nd pattern
rows = 5
for i in range(rows):
    for j in range(rows - i):
        print('*', end=' ')
    print()

print()

# 3rd pattern
rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(' ', end = ' ')
    for k in range(i + 1):
            print('*', end = ' ')
    print() 

print()
# 4th pattern
rows = 5
for i in range(rows):
    for j in range(rows):
        print('*', end=' ')
    print()

print()
# 5th pattern
n = 5
for i in range(n, 0 , -1):
    for j in range(i):
        print('*', end=' ')
    print()

print()
# 6th pattern
rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(' ', end=' ')
    for j in range(2*i + 1):
        print('*', end=' ')
    print()