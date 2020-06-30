
##########################################
# 코드업 기초 100제 - 1008 번   ->  X

# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# print("\u250C\u252C\u2510")
# print("\u251C\u253C\u2524")
# print("\u2514\u2534\u2518")



##########################################
# 코드업 기초 100제 - 1012 번   ->  X

# import sys

# a = float(sys.stdin.readline().rstrip())
# print("%.6lf"%a)



##########################################
# 코드업 기초 100제 - 1013 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())
# print(a, b)



##########################################
# 코드업 기초 100제 - 1014 번   ->  O

# import sys

# a, b = sys.stdin.readline().rstrip().split()
# print(b, a)



##########################################
# 코드업 기초 100제 - 1015 번   ->  O

# import sys

# a = float(sys.stdin.readline().rstrip())
# print("%.2f" %float(a))



##########################################
# 코드업 기초 100제 - 1017 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())
# print(a, a, a)



##########################################
# 코드업 기초 100제 - 1018 번   ->  O

# import sys

# a = sys.stdin.readline().rstrip()
# print(a)



##########################################
# 코드업 기초 100제 - 1019 번   ->  O

# import sys

# a, b, c = map(int, sys.stdin.readline().rstrip().split("."))
# print("%.4d"%int(a)+'.'+"%.2d"%int(b)+'.'+"%.2d"%int(c))



##########################################
# 코드업 기초 100제 - 1020 번   ->  O

# import sys

# a, b = sys.stdin.readline().rstrip().split("-")
# print(a+''+b)



##########################################
# 코드업 기초 100제 - 1021 번   ->  O

# import sys

# a = sys.stdin.readline().rstrip()
# print(a)



##########################################
# 코드업 기초 100제 - 1022 번   ->  O

# import sys

# a = sys.stdin.readline().rstrip()
# print(a)



##########################################
# 코드업 기초 100제 - 1023 번   ->  O

# import sys

# a, b = map(float, sys.stdin.readline().rstrip().split('.'))
# print(int(a))
# print(int(b))



##########################################
# 코드업 기초 100제 - 1024 번   ->  O

# import sys

# a = sys.stdin.readline().rstrip()

# for b in a:
#     print('\''+b+'\'')



##########################################
# 코드업 기초 100제 - 1025 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())
# li = []

# for b in str(a):
#     li.append(b)

# for x in range(len(li)):
#     # print(li[x]*(10**(x+1)))
#     print('['+str(int(li[x])*(10**(4-x)))+']')



##########################################
# 코드업 기초 100제 - 1026 번   ->  O

# import sys

# a, b, c = map(int, sys.stdin.readline().rstrip().split(':'))
# print(b)



##########################################
# 코드업 기초 100제 - 1028 번   ->  O

# import sys

# a, b, c = map(int, sys.stdin.readline().rstrip().split('.'))
# print(str("%.2d"%c)+'-'+str("%.2d"%b)+'-'+str(a))



##########################################
# 코드업 기초 100제 - 1029 번   ->  O

# import sys

# a = float(sys.stdin.readline().rstrip())
# print("%.11lf"%a)




##########################################
# 코드업 기초 100제 - 1030 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())
# print(a)



##########################################
# 코드업 기초 100제 - 1031 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())
# print(oct(a).split("0o")[1])



##########################################
# 코드업 기초 100제 - 1032 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())
# print(hex(a).split("0x")[1])



##########################################
# 코드업 기초 100제 - 1033 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())
# print(hex(a).split("0x")[1].upper())      # Upper를 사용하여 소문자를 대문자로 변환.




##########################################
# 코드업 기초 100제 - 1034 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())
# b =int('0o'+str("%.2d"%a), 8)

# print(b)



##########################################
# 코드업 기초 100제 - 1035 번   ->  O

# import sys

# a = sys.stdin.readline().rstrip() 
# b =int(a, 16)                         #위에서 처럼 지저분하게 10진법으로 바꾼것보다 훨씬 깔끔하게 변경할 수 있다.

# print("%o"%b)                         #출력 또한 깔끔하게 변경해서 출력할 수 있다.



##########################################
# 코드업 기초 100제 - 1036 번   ->  O

# import sys

# a = sys.stdin.readline().rstrip()
# b = ord(a)                            #ord() 를 사용하여 아스키코드를 정수로 변경한다. --> 특정한 문자를 아스키 코드값으로 변경
                                        #chr() 아스키코드값을 문자로 변경
# print(b)



##########################################
# 코드업 기초 100제 - 1037 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())
# b = chr(a)

# print(b)



##########################################
# 코드업 기초 100제 - 1038 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())
# print(a+b)



##########################################
# 코드업 기초 100제 - 1040 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())
# print(-a)



##########################################
# 코드업 기초 100제 - 1041 번   ->  O

# import sys

# a = sys.stdin.readline().rstrip()
# b = int(ord(a)+1)

# print(chr(b))



##########################################
# 코드업 기초 100제 - 1042 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# print(a//b)



##########################################
# 코드업 기초 100제 - 1043 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# print(a%b)



##########################################
# 코드업 기초 100제 - 1044 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())

# print(a+1)



##########################################
# 코드업 기초 100제 - 1045 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# print(str(a+b)+'\n'+str(a-b)+'\n'+str(a*b)+'\n'+str(a//b)+'\n'+str(a%b)+'\n'+str("%.2f"%float(a/b)))



##########################################
# 코드업 기초 100제 - 1046 번   ->  O

# import sys

# a, b, c = map(int, sys.stdin.readline().rstrip().split())

# print(a+b+c)
# print("%.1f"%float((a+b+c)/3))



##########################################
# 코드업 기초 100제 - 1047 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())
# print(2*a)



##########################################
# 코드업 기초 100제 - 1048 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# print(a*(2**b))



##########################################
# 코드업 기초 100제 - 1049 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# if a > b:
#     print(1)
# else:
#     print(0)



##########################################
# 코드업 기초 100제 - 1050 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# if a == b:
#     print(1)
# else:
#     print(0)

##########################################
# 코드업 기초 100제 - 1051 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# if a <= b:
#     print(1)
# else:
#     print(0)



##########################################
# 코드업 기초 100제 - 1052 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# if a != b:
#     print(1)
# else:
#     print(0)



##########################################
# 코드업 기초 100제 - 1053 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())

# if a == 0:
#     a=1
#     print(a)
# else :
#     a=0
#     print(a)



##########################################
# 코드업 기초 100제 - 1054 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# if a == 1 and b==1:
#     print(1)
# else :
#     print(0)



##########################################
# 코드업 기초 100제 - 1055 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# if a == 1 or b==1:
#     print(1)
# else :
#     print(0)



##########################################
# 코드업 기초 100제 - 1056 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# if a != b:
#     print(1)
# else :
#     print(0)



##########################################
# 코드업 기초 100제 - 1057 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# if a == b:
#     print(1)
# else :
#     print(0)



##########################################
# 코드업 기초 100제 - 1058 번   ->  O


# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# if a==0 and b==0:
#     print(1)3

# else :
#     print(0)



##########################################
# 코드업 기초 100제 - 1059 번   ->  X

# import sys

# a = int(sys.stdin.readline().rstrip())

# print(~a)                                 #### ~연산자는 비트연산에서 비트를 모두 뒤집는 연산 (이진수에서 1을 0으로 0을 1로)




##########################################
# 코드업 기초 100제 - 1060 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# print(a&b)                                  ###########* python에서 논리연산자는 and, or, xor, not으로 쓰이지만 비트단위연산자에서는 ~,&,|,^,>>,<<로 쓰인다.



##########################################
# 코드업 기초 100제 - 1061 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# print(a|b)                                  ###########* python에서 논리연산자는 and, or, xor, not으로 쓰이지만 비트단위연산자에서는 ~,&,|,^,>>,<<로 쓰인다.



##########################################
# 코드업 기초 100제 - 1062 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().rstrip().split())

# print(a if a>b else b)                          #### 파이썬은 3항 연산자 대신 a if 조건 else b를 사용한다.



##########################################
# 코드업 기초 100제 - 1065 번   ->  O

# import sys

# a, b, c = map(int, sys.stdin.readline().rstrip().split())

# if a%2 == 0:
#     print(a)
# if b%2 == 0:
#     print(b)
# if c%2 == 0:
#     print(c)



##########################################
# 코드업 기초 100제 - 1066 번   ->  O

# import sys

# a = map(int, sys.stdin.readline().rstrip().split())

# for x in a:
#     if x%2 == 0:
#         print("even")
#     else :
#         print("odd")



##########################################
# 코드업 기초 100제 - 1067 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())

# if a>0 :
#     print('plus')
#     if a%2 == 0:
#         print('even')
#     else:
#         print('odd')
# else:
#     print('minus')
#     if a%2 == 0:
#         print('even')
#     else:
#         print('odd')




##########################################
# 코드업 기초 100제 - 1068 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())

# if 90<= a <= 100:
#     print('A')
# elif 70 <= a <90:
#     print('B')
# elif 40 <= a <70:
#     print('C')
# else:
#     print('D')



##########################################
# 코드업 기초 100제 - 1069 번   ->  O

# import sys

# a = sys.stdin.readline().rstrip()

# if a == 'A':
#     print('best!!!')
# elif a == 'B':
#     print('good!!')
# elif a == 'C':
#     print('run!')
# elif a == 'D':
#     print('slowly~')
# else:
#     print('what?')



##########################################
# 코드업 기초 100제 - 1070 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())

# if a == 12 or a == 1 or a == 2:
#     print('winter')
# elif a == 3 or a == 4 or a == 5:
#     print('spring')
# elif a == 6 or a == 7 or a == 8:
#     print('summer')
# elif a == 9 or a == 10 or a == 11:
#     print('fall')



##########################################
# 코드업 기초 100제 - 1071 번   ->  O

# import sys

# a = map(int, sys.stdin.readline().rstrip().split())

# for x in a:
#     if x == 0:
#         break
#     print(x)
    


##########################################
# 코드업 기초 100제 - 1072 번   ->  O

# import sys

# n = int(sys.stdin.readline().rstrip())
# a =map(int, sys.stdin.readline().rstrip().split())

# for x in a:
#     print(x)




##########################################
# 코드업 기초 100제 - 1073 번   ->  O


# import sys

# a = map(int, sys.stdin.readline().rstrip().split())

# for x in a:
#     if x == 0:
#         break
#     print(x)




##########################################
# 코드업 기초 100제 - 1074 번   ->  O


# import sys

# a = int(sys.stdin.readline().rstrip())
# while a != 0:
#     if a == 0:
#         break  
#     else: 
#         print(a)
#         a = a-1



##########################################
# 코드업 기초 100제 - 1075 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())
# while a != 0:
#     if a == 0:
#         break  
#     else: 

#         a = a-1
#         print(a)




##########################################
# 코드업 기초 100제 - 1076 번   ->  O

# import sys

# a = sys.stdin.readline().rstrip()

# for b in range(97, ord(a)+1):
#     print(chr(b))




##########################################
# 코드업 기초 100제 - 1077 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())

# for b in range(a+1):
#     print(b)





##########################################
# 코드업 기초 100제 - 1078 번   ->  O


# import sys

# a = int(sys.stdin.readline().rstrip())
# c = 0
# for b in range(a+1):
#     if b%2 == 0:
#         c += b
# print(c)




##########################################
# 코드업 기초 100제 - 1079 번   ->  O

# import sys

# a = map(str, sys.stdin.readline().rstrip().split())

# for b in a:
#     print(b)
#     if b == 'q':
#         break



##########################################
# 코드업 기초 100제 - 1080 번   ->  O

# import sys

# a = int(sys.stdin.readline().rstrip())
# c = 0
# for b in range(100):
#     c += b

#     if c >= a :
#         print(b)
#         break



##########################################
# 코드업 기초 100제 - 1081 번   ->  O

# import sys

# a, b = map(int, sys.stdin.readline().strip().split())

# for x in range(1, a+1):
#     for y in range(1, b+1):
#         print(x, y)



##########################################
# 코드업 기초 100제 - 1082 번   ->  O

# import sys

# a = sys.stdin.readline().rstrip()

# for x in range(1, 16):
#     print(a + '*' + hex(x).split('0x')[1].upper() + '=' + str(hex(int(a, 16)*x).split('0x')[1].upper()))


# print(hex(int(a)).split('0x')[1].upper())



##########################################
# 코드업 기초 100제 - 1083 번   ->  O

# import sys

# n = int(sys.stdin.readline().rstrip())

# for a in range(1, n+1):
#     if a%3 == 0:
#         a='X'
#     print(a ,end=' ')



##########################################
# 코드업 기초 100제 - 1084 번   ->  O

# import sys

# a, b, c = map(int, sys.stdin.readline().strip().split())

# for x in range(a):
#     for y in range(b):
#         for z in range(c):
#             print(x, y, z)
# print(a*b*c)



##########################################
# 코드업 기초 100제 - 1085 번   ->  O

# import sys

# a, b, c, d = map(int, sys.stdin.readline().rstrip().split())

# mul = a*b*c*d/8/1024/1024
# print('%.1f' %mul, 'MB')