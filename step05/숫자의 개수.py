a = int(input(""))
b = int(input(""))
c = int(input(""))
num = a * b * c
n_list =[]

string = (str(num))
l_num = len(string)

for i in range(l_num):
  n = num % 10
  n_list.append(n)
  num = num // 10

for i in range(10):
  sum = 0
  for j in range(l_num):
    if n_list[j] == i:
      sum = sum + 1
  print(sum)
