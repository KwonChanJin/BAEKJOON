cro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input("")

for i in cro_list:
    word = word.replace(i, '*')

print(len(word))