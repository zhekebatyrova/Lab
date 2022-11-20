# задача 1
import math

a, b = int(input()), int(input())
c = math.sqrt(b*b + a*a)
print(c)

#задача 2
num = int(input())
a = (num % 100) // 10
print(a)

#задача 3
n = int(input())
print((n // 2) * 2 + 2)

#задача 4
a = int(input())
break1 = a // 2 * 5
break2 = (a-1)//2 * 15
minute = 9*60 + a*45 +break1 + break2

print(minute//60, minute%60)

#задача 5

a, b = int(input()), int(input())
if a > b:
    print(a)
elif a<b:
    print(b)
else:
    print(0)


#задача 6

a, b, c = int(input()), int(input()), int(input())
a = max(a, b, c)
print(a)

#задача 7

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a==c or b==d:
    print('YES')
else:
    print('NO')

#задача 8

a, b, c = int(input()), int(input()), int(input())
if a+b>c and a+c>b and b+c>a:
    print("YES")
else:
    print("NO")
    
#задача 9

a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

#задача 10
a, b, c = int(input()), int(input()), int(input())
if ( a <= b and a<=c ):
    if (b <= c):
        print(a, b, c)
    else:
        print(a, c, b)
elif (b <= c and b <= a):
    if (a <= c):
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if (a <= b):
        print(c, a, b)
    else:
        print(c, b, a)
