n, x = map(int, input("").split())
nums = [int(p)for p in input().split()]

list_a = []
for i in range(n):
  if nums[i] < x:
    a = nums[i]
    list_a.append(a)
print(*list_a, sep = ' ')