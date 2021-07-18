l = []
l2 = []
sum = 1
count = {}
for i in range(10):
  a = int(input(""))
  l.append(a)

for j in l:
  n = j % 42
  l2.append(n)

for h in range(9):
  m = min(l2)
  l2.remove(min(l2))
  n = min(l2)
  if m != n:
    sum += 1
print(sum)