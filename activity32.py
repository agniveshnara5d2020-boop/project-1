rowsize = int(input("Enter the number of rows: "))

if rowsize % 2 == 0:
   halfdiamrow = rowsize // 2
else:
   halfdiamrow = rowsize // 2 + 1

# Top Half
space = halfdiamrow - 1
for i in range(1, halfdiamrow + 1):
  for j in range(space):
   print(" ", end="")

  num = 1
for j in range(2 * i - 1):
             print(num, end="")
             num += 1

print()
space -= 1

# Bottom Half
space = 1
for i in range(halfdiamrow - 1, 0, -1):
  for j in range(space):
   print(" ", end="")

  num = 1
for j in range(2 * i - 1):
   print(num, end="")
   num += 1

print()
space += 1
     