hour, minuate = input("").split()
hour, minuate = int(hour), int(minuate)
total_m = hour * 60 + minuate - 45
h = total_m // 60
m = total_m % 60
if h < 0:
  print(24 + h, m)
else:
  print(h, m)