#EX1
import math
a = int(input("Enter circle radius: "))
print(a)
area = math.pi * a * a

print(int(area))

#EX2
a = float(input("Enter the temperature: "))
print (a)

f = (a * 1.8) + 32
print(int(f))

#EX3
import math
a = int(input("Enter a number: "))

if a < 2:
    prime = False
else:
    prime = True

    for i in range(2,a):
        if a % i == 0:
            prime = False
            break

if prime:
    print(f"{a} is a prime number")
else:
    print(f"{a} is not a prime number")

#EX4
a = int(input("Enter a number: "))
total = 0
for i in range (1,a):
 if a % i == 0:
    total += i

if total == a:
  print(f"{a} is a perfect number")
else:
  print(f"{a} is NOT perfect number")

   
#EX5
color = ("Purple", "Blue", "Black", "Red")

n = input("What is your favourite color: ")


for i in range(len(color)):
    if color[i] == n:
        print(f"Your color is at index {i} in my list")
        break
        
    else:
        print(f"Sorry, I couldn't find your color")
        
        
#EX6
range1 = list(range(0,7))
range2 = list(range(1,11,3))
range3 = list(range(5,0,-1))
range4 = list(range(6,-3,-2))

print(range1)
print(range2)
print(range3)
print(range4)

#EX7
def remove_dollar_sign(s):
    return s.replace("$","")

print(remove_dollar_sign("$$100$"))

#EX8
def extract_even(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

print(extract_even([1,4,5,-1,10]))


#EX9
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))


#EX10
def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors       
print(get_divisors(12))

#EX11
import math
x1 = float(input("Enter x1 point: "))
y1 = float(input("Enter y1 point: "))
x2 = float(input("Enter x2 point: "))
y2 = float(input("Enter y2 point: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) **2)
print(distance)


#EX12
def pattern(m,n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


m = int(input("Enter m: "))
n = int(input("Enter n: "))
pattern(m,n)
print(pattern)
    