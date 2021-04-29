#solution_1
# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))
# c = int(input("Enter the value of c : "))
# d = ((b*b)-(4*a*c))**(1/2)
# print(d)
# x = (-b + d)/(2*a)
# y = (-b -d )/(2*a)
# print(f"first value : {x}")
# print(f"second value : {y}")

#solution_2
# import math
# a,b,c = int(input("enter a :")), int(input("enter b :")), int(input("Enter c: "))
# d = ((b*b)-(4*a*c))
# val1 = (-b+math.sqrt(d))/(2*a)
# val2 = (-b-math.sqrt(d))/(2*a)
# print(val1)
# print(val2)

#solution_3
import math
def quad_eq(a,b,c):
    d = ((b*b)-(4*a*c))
    return (-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a)
a,b,c = int(input("enter a :")), int(input("enter b :")), int(input("Enter c: "))
print(quad_eq(a,b,c))




