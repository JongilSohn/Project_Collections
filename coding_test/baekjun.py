# 백준 # 10869번   --> O

# a, b=input().split()
# print(int(a)+int(b))
# print(int(a)-int(b))
# print(int(a)*int(b))
# print(int(a)//int(b))  #//를 사용해야 정수형 계산이 되어 몫이 출력된다.
# print(int(a)%int(b))

# ========================================
# 백준 # 10430번 --> O

# A, B, C =input().split()
# print((int(A)+int(B))%int(C))
# print(((int(A)%int(C))+(int(B)%int(C)))%int(C))
# print((int(A)*int(B))%int(C))
# print((int(A)%int(C))*(int(B)%int(C))%int(C))

# ========================================
# 백준 # 2588번 --> O

# A = input()
# Be = input()
# Br = list(Be)     # A와 B를 곱하여 일의자리, 십의자리, 백의자리 순으로 출력하기 위해  B값을 리스트에 담고
# Br.reverse()      # reverse 함수를 사용하여 역순으로 정렬시킨다.

# for B in Br:      # 역순으로 정렬시킨 배열을 하나씩 빼서 곱해 출력한다.
#     A = int(A)
#     B = int(B)
#     print(A*B)
# print(int(A)*int(Be))

# ========================================
# 백준 # 1330번 --> O

# a, b = input().split()
# if int(a) > int(b):
#     print('>')
# elif int(a) < int(b):
#     print('<')
# else:
#     print('==')

# ★★★★★★★★★★★★★★★★★★
# 아래와 같이 map이라는 내장함수를 사용해서 여러개의 데이터를 한번에 다른형태로 변환할 수 있다.
# map(변환 함수, 순회 가능한 데이터)
# ★★★★★★★★★★★★★★★★★★

# a, b = map(int,input().split())
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')

# ========================================
# 백준 # 9498번 --> O

# a = int(input())

# if 90 <= a <= 100:
#     print('A')
# elif 80 <= a < 90:
#     print('B')
# elif 70 <= a < 80:  
#     print('C')
# elif 60 <= a <70:
#     print('D')
# else:
#     print('F')

# ========================================
# 백준 # 2753 번 --> O

# year = int(input())

# if (year%4) == 0 and (year%100) !=0:  # 4의 배수이면서 100의 배수가 아니면 윤년
#     print(1)
# elif (year%400) ==0:      # 400의 배수는 무조건 윤년
#     print(1)
# else:
#     print(0)

# ========================================
# 백준 # 14681 번 --> O

# x = int(input())
# y = int(input())

# if x > 0:
#     if y > 0:
#         print(1)
#     else:
#         print(4)
# else:
#     if y > 0:
#         print(2)
#     else:
#         print(3)

# ========================================
# 백준 # 2884 번 --> O

# h, m = map(int, input().split())

# if m-45 < 0 :
#     if h-1 < 0:
#         print(23, 60+(m-45))
#     else:
#         print(h-1, 60+(m-45))
# else: 
#         print(h, m-45)

# ========================================
# 백준 For문 # 2739 번 --> O

# n = int(input())

# for i in range(1, 10):
#     print(n, '*', i, '=', n*i)

# ========================================
# 백준 For문 # 10950 번 --> O

# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
#     print(a+b)

# ========================================
# 백준 For문 # 8393 번 --> O

# n = int(input())
# total = 0
# for i in range(1, n+1):
#     total +=i
# print(total)

# ========================================
# 백준 For문 # 15552 번 --> O

# n = int(input())
# for i in range(1,n+1):
#     a, b = map(int, input().split())
#     print(a+b)

# ★★★★★★★★★★★★★★★★★★
# 위와같이 for문을 사용할때 입출력방식에 의해서 시간초과가 날 수 있다.
# import sys의 sys.stdin.readline().rstrip()을 사용하자.
# ★★★★★★★★★★★★★★★★★★

# import sys
# n = int(sys.stdin.readline().rstrip())

# for i in range(1,n+1):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     print(a+b)

# ========================================
# 백준 For문 # 2741 번 --> O

# import sys
# n = int(sys.stdin.readline().rstrip())

# for i in range(n, 0, -1):
#     print(i)

# ========================================
# 백준 For문 # 11021 번 --> O

# import sys
# n = int(sys.stdin.readline().rstrip())

# for i in range(0, n):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     print("Case #{}: {}".format(i+1, a+b))                  #이렇게 문자열{}.format(변수)를 사용하여 편리하게 출력 가능하다.

# ========================================
# 백준 For문 # 2438 번 --> O

# import sys
# n = int(sys.stdin.readline().rstrip())

# for i in range(0, n):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     print("Case #{}: {} + {} = {}".format(i+1, a, b, a+b)) 

# ========================================
# 백준 For문 # 2439 번 --> O
# import sys

# n = int(sys.stdin.readline().rstrip())

# for i in range(1,n+1):
#     print(' '*(n-i)+''+'*'*i)         # ''사이에 넣는 이유는 ''을 넣지 않으면 공백이 1칸 생긴다.

# ========================================
# 백준 For문 # 10871 번 --> X
# import sys

# a ,b = map(int, sys.stdin.readline().rstrip().split())

# str = list(map(int, sys.stdin.readline().rstrip().split())) # list()를 사용하여 입력받은 값을 리스트에 넣는다.

# for i in str:
#     if i < b:
#         print(i,end=' ')        # end=' '를 쓰게되면 줄바꿈이 되지 않고 출력한 다음  출력1end출력2 이런식으로 출력된다.

# ========================================
# 백준 While문 # 10952 번 --> X

# import sys

# while True:       #while 조건문: 실행문 이런식으로 오면 조건이 만족될때까지 무한으로 돈다.
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     if a==0 and b==0:
#         break 
    
#     print(a+b)

#     import sys

#     # if a==0 and b==0:         # 아래에 하면 안되는 이유는 0 0이 찍혔을때 출력이 0이 나오지 않은채로 끝나야 하기 때문이다.
#     #     break 
    
# ========================================
# 백준 While문 # 10951 번 --> X

# import sys

# while True:
#     try:
#         a, b = map(int, sys.stdin.readline().rstrip().split())
#         print(a+b)
#     except:                         #except 처리를 하지 않으면 끊임없이 input을 받게된다. 근데 무슨말인지????
#         break

# ========================================
# 백준 While문 # 10951 번 --> O X

# import sys        #이중 While문을 사용하여 계산했다.

# while True:
#     n = int(sys.stdin.readline().rstrip())        
#     x = n         #입력받은 변수를 x에 넣는다.
#     a = int(n//10)    
#     b = int(n%10)
#     c = int(1)

#     n = (b*10) + ((a+b)%10)
#     if n != x:
#         while n!=x:
#             a = int(n//10)
#             b = int(n%10)
#             n = (b*10) + ((a+b)%10)
#             c += 1
#     print(c)
#     break

# ========================================
# 백준 실습1 # 10039 번 --> O

# import sys

# list = []

# for n in range(5):
#     n = int(sys.stdin.readline().rstrip())
#     if n<40:
#         n=40
#     list.append(n)

# print(int(sum(list)/len(list)))

# ========================================
# 백준 실습1 # 5543 번 --> O

# import sys

# buger = []
# drink = []

# for b in range(3):
#     b = int(sys.stdin.readline().rstrip())
#     buger.append(b)

# for d in range(2):
#     d = int(sys.stdin.readline().rstrip())
#     drink.append(d)
# buger.sort()
# drink.sort()
# print(buger[0]+drink[0]-50)

# ========================================
# 백준 실습1 # 10817 번 --> O

# import sys

# lis = []
# a, b, c = map(int, sys.stdin.readline().rstrip().split())
# lis.append(a)
# lis.append(b)
# lis.append(c)
# lis.sort()
# print(lis[1])

# ========================================
# 백준 실습1 # 2523 번 --> O

# import sys

# n = int(sys.stdin.readline().rstrip())

# for a in range(n):
#     print('*'*(a+1))
# for b in range(n-1, 0, -1):
#     print('*'*(b))

# ========================================
# 백준 실습1 # 2446 번 --> O

# import sys

# n = int(sys.stdin.readline().rstrip())

# for a in range(n, 0, -1):
#     print(' '*(n-a)+'*'*(2*a-1))                  # +로 안하고 , 로 하면 틀렸다. 이유는 모르겠지만.. 꼭 +로 해라
# for b in range(n-1):
#     print(' '*(n-b-2)+'*'*(2*b+3))

# ========================================
# 백준 실습1 # 2446 번 --> O

import sys

n = int(sys.stdin.readline().rstrip())

for a in range(2*n):
    if (a+1)%2 == 0 :
        



