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