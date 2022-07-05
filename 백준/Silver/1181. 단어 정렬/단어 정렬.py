n = int(input())

word_list = []

for i in range(n):
    word_list.append(str(input()))

word_list = list(set(word_list))
word_list.sort()
word_list.sort(key = lambda x : len(x))

for word in word_list:
    print(word)