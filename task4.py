#задача 4
a = int(input())
break1 = a // 2 * 5
break2 = (a-1)//2 * 15
minute = 9*60 + a*45 +break1 + break2

print(minute//60, minute%60)