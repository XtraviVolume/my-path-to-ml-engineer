from collections import Counter
s= input()
n= len(s)
q= int(input())
l=input().split()
for c in l:
    nxt_cnt = Counter()
    for i in range(n-1):
        if s[i]==c:
            nxt_cnt[s[i+1]]+=1
    if len(nxt_cnt)==0:
        print('?',end=' ')
        continue
    nxt_cnt_i= nxt_cnt.items()
    sorted_nxt_cnt_items= sorted(nxt_cnt_i, key=lambda x : -x [1], x[0]):
    ans_c, ans_cnt = sorted_nxt_cnt_items[0]:
    print(ans_c, end=" ")