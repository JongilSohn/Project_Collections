
################################################################
## 백준 11399 번 -> O


# import sys

# n = int(sys.stdin.readline().rstrip())
# a = list(map(int, sys.stdin.readline().rstrip().split()))
# a.sort()

# total = 0

# for x in range(len(a)):
#     total += sum(a[0:x+1])

# print(total)




################################################################
## 백준 11399 번 -> X

# import sys

# n, total = map(int, sys.stdin.readline().rstrip().split())
# arr = []
# num = 0

# for x in range(n):
#     a = int(sys.stdin.readline().rstrip())
#     arr.append(a)

# for money in range(n-1, -1, -1):    ## 거꾸로 할때도 주의하자/. n, 1, -1 이면 n부터 0이 아닌 1까지다.
#     # print(arr[money])
    
#     num += total//arr[money]          ## 몫을 사용하여 동전의 개수를 세었다.
#     total %= arr[money]
    
#     if total ==0:
#         break
#     if arr[money]>total:
#         continue
# print(num)



################################################################
## 백준 1931 번 -> 

import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for a in range(n):
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(x)

arr = sorted(arr, key=lambda x:(x[1], x[0]))        #가장 빨리 끝나는 회의 먼저 정렬시키고, 같다면 먼저 시작하는 회의를 우선.

print(arr)

