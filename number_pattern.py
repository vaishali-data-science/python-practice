'''# 1st pattern
row = 5
for i in range(row):
    for j in range(i + 1):
        print(i + 1, end='')
    print()

print()
# 2nd pattern
row = 5
for i in range(row):
    for j in range(row - i):
        print(row - i, end='')
    print()

print()
# 3rd pattern
row = 5
for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for k in range(i + 1):
            print(i + 1, end='')
    print()

print()
# 4th pattern
row = 5
for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(2*i + 1):
        print(row - i, end='')
    print()

print()
# 5th pattern
row = 5
for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(2*i + 1):
        print(i + 1, end='')
    print()'''

print()
# 6th pattern
row = 5
for i in range(row):
    for j in range(i + 1):
        print(j + 1, end='')
    print()

print()
# 7th pattern
row = 5
for i in range(row):
    for j in range(row - i):
        print(row - j, end='')
    print()

print()
# 8th pattern
row = 5
for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for k in range(i + 1):
            print(k + 1, end='')
    print()

print()
# 9th pattern
row = 5
for i in range(row):
     for j in range(row - i - 1):
          print(' ', end='')
     for k in range(2*i + 1):
          print(k + 1, end='')
     print()