numbers = list(range(1, 10001))
remove_list = []
for num in numbers:
    for string in str(num):
        num += int(string)
    if num <= 10000:
        remove_list.append(num)

for remove_num in set(remove_list):
    numbers.remove(remove_num)
for self_num in numbers:
    print(self_num)