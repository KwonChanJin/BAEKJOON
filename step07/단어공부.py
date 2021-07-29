word = input("").upper()
unique_word = list(set(word)) #중복값 제

cnt_list = []
for x in unique_word:
    cnt = word.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_index = max(cnt_list)
    max_num = cnt_list.index(max_index)
    print(unique_word[max_num])