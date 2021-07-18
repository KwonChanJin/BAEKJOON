C = int(input(""))#테스트 케이스 개수
r = []
for i in range(C):
  sum = 0
  j = 0
  avr = 0
  s = 0
  l = 0
  answer = 0

  a = input("").split()
  l = len(a)
  a = list(map(int, a))

  for j in range(l-1):
    j += 1
    sum += a[j]
  avr = sum / a[0]

  for h in range(1, l, 1):
    if a[h] > avr:
      s += 1
  answer = s/(l-1)*100
  r.append(answer)
for i in range(C):
  print("{:.3f}%".format(r[i]))