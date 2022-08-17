# #3_1
#
#
# #num1=int(input("please enter number:"))
# #num2=int(input("please enter number:"))
#
# #for i in range(num1+1,num2-1):
# #    if 9<i<=99:
#  #       print(i)
# # ==============================================
# #   if num%2==0 or num%3==0 or num%4==0 or num%5==0 or num%6==0 or num%7==0 or num%8==0 or num%9==0:
# #3_2
#
# num=int(input("enter number:"))
# for i in range(2,num):
#     if i%num==0:
#         print("no prime")
#     else: print("prime")
#     num = int(input("enter number:"))
#
#
# ============================================================
#3_3
# from random import randint
# num=randint(1,9)
# gueuss=int(input("please gueuss number:"))
# print(num)
# while num!=gueuss:
#     if gueuss<num:
#         print("higher")
#     else: print("lower")
#     gueuss = int(input("please gueuss number:"))
# print("congratulation")

#==========================================================
#3_4
num=int(input("enter number between1-5:"))
from random import randint
gueuss=randint(1,5)
count=0
while num!=gueuss:
    count+=1
    print(gueuss)
    if num<gueuss:
        input("lower:")
    else: input("higher:")
    from random import randint
    gueuss = randint(1, 5)
print("congratulation")
print("trys",count)
