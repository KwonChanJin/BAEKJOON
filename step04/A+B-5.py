sum = []
a = 100
b = 100
while True:
  a, b = input("").split()
  a, b = int(a), int(b)
  if a == 0 and b == 0:
    break
  else:
    num = a + b
    sum.append(num)

print(*sum, sep='\n')