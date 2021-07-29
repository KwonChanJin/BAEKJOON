a = input("")
alpha = list(range(97,123,1))
num_list = []
for i in alpha:
    num = a.find(chr(i))
    num_list.append(num)
print(' '.join(map(str,num_list)))