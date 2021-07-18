n = int(input(""))
n_list = []
for i in range(n):
  sum = 0
  num = 0
  l = []
  q = input("")
  l = list(q)
  l_long = len(l)
  for j in range(l_long):
    answer = l[j]
    if answer == 'O':
      num += 1
      sum += num
    if answer == 'X':
      sum += 0
      num = 0
  n_list.append(sum)
for i in range(n):
  print(n_list[i])