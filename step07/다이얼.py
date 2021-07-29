dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
ans = 0
print(word)
for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            ans += dial.index(j)+3
print(ans)