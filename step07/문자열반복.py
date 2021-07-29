n = int(input(""))
for i in range(n):
    r_list = []
    S, R = input("").split()
    S = int(S)
    for r in R:
        r_list.append(r)
    for j in r_list:
        print(j * S, end='')
    print(sep='\n')