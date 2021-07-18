num = int(input(""))
add = (num%10)+(num//10)
sum = (num%10)*10+(add%10)
total = 1
while True:
  if sum != num:
    add = (sum%10)+(sum//10)
    sum = (sum%10)*10+(add%10)
    total += 1
  else:
    break

print(total)