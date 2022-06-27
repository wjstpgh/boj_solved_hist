word=input().upper()
cnt_list=list(set(word))
cnt=[0]*len(cnt_list)
for x in range(len(cnt_list)):
    cnt[x]=word.count(cnt_list[x])
if(cnt.count(max(cnt))==1):
   print(cnt_list[cnt.index(max(cnt))])
else:
    print('?')