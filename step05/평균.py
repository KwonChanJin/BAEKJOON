n = int(input(""))
a = list(map(int,input().split()))
m = max(a)
sum = 0
for i in range(n):
  num = a[i]/m*100
  sum += num
print(sum/n)