num = int(input(""))
list = []
for i in range(num):
  x = 0
  y = 0
  x, y = input("").split()
  x, y = int(x), int(y)
  z = x + y
  list.append(z)
for j in list:
  print(j)