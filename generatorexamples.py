# write fibonacci program using generator

# num1 =0
# num2 = 1
# num3 = 0
# i = 0
# print("Fibonacci number are:",num1, ",", num2,",",end="")
# while i <= 10:
#     num3 = num1 + num2
#     print(num3,",",end="")
#     num1 = num2
#     num2 = num3
#     i += 1

#
# def fib_serice(u_num):
#     num1 = 0
#     num2 = 1
#     num3 = 0
#     i = 1
#     print("Fibonacci number are")
#     print(num1)
#     print(num2)
#     while i <= u_num-2:
#         num3 = num1 + num2
#         yield num3
#         num1 = num2
#         num2 = num3
#         i += 1
#
# print("Enter the number you want to print :")
# user_num = int(input())
# mynum = fib_serice(user_num)
# # print(mynum.__next__())
# # print(mynum.__next__())
# # print(mynum.__next__())
#
# for i in mynum:
#     print(i)


# Write factorial program
# 5 - 5*4*3*2*1

# Without generator

# print("Enter the number")
# my_num = int(input())
#
# cal = 1
# i = 1
# # for i in range(1,my_num + 1):
# while i <= my_num:
#     cal = cal * i
#     print(cal)
#     i += 1


def fact_num(num):
    fact = 1
    i = 1

    while i <= num:
        fact = fact * i
        yield fact
        i += 1


print("Enter the number you wish to see factorial :")
my_num = int(input())
ans = fact_num(my_num)
print(ans.__next__())
print(ans.__next__())
print(ans.__next__())
# for i in ans:
#     print(i)
