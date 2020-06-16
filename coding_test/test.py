# a = 3
# for n in range(1,2*a):
#     if n<=3:
#         print('*'*n)
#     else:
#         print('*'*(2*a-n))
# ----------------------------------------------------------------
# a = 5
# for n in range(1,2*a):
#     if n<=5:
#         print(' '*(n-1), '*'*(2*a-2*n+1),' '*(n-1))
#     else:
#         print(' '*(2*a-n-1), '*'*(2*n+1-2*a),' '*(2*a-n-1))
# ----------------------------------------------------------------

# n = int(input())

# nlist = list(map(int, input().split()))
# nlist.sort()
# print(nlist[0], nlist[-1])7

# ----------------------------------------------------------------
import sys


lis = []
max_n=0

for i in range(1,10):
    n = input()
    lis.append(n)
    lis = list(map(int, lis))

for j in range(0,9):

    print(lis[j])
    if max_n < lis[j]:
        max_n = lis[j]
print("최대", max_n)
print(lis.index(max_n)+1)


    
    
    