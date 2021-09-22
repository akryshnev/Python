b_true = True
b_false = False

a = "head"
b = "body"

c = 48
d = 76
e = 1325
f = 9

g = 2.5
h = 7.05
i = 4.37

print(d >= c)
print(d < f)
print(c >= f)
print(d != e)
print(f <= c)
print(f >= d)
print(f != e)
print(c <= d)
print(c != e)
print(c == f)
print(d >= f)
print(f != d)
print(d > e)
print(e != f)
print(e <= d)

print(g <= h)
print(g != i)
print(h != g)
print(h >= i)
print(i >= h)
print(i != g)
print(g >= h)
print(h >= g)
print(i <= h)

print(d == h)
if d > c and e > f:
    print("good")

if d < c or e > f:
    print("soso")

if not f > e:
    print("Muy_bien")

if f < d:
    print("sehr_gut")
if f!= d and c != e:
    print("hola")
if d >c or c <= f:
    print("soy de belarus")
if not  d < f:
    print("teclado")
if not f > c:
    print("Vivo en Madrid")
if d > e or c <= d:
    print("uno")

if e > c:
    print("toro")


print("Enter d1 =")
d1 = int(input())
if d1 > 30:
    print("You entered, =", d1, "which is bigger than 30")
elif d1 == 30:
    print("You entered, =", d1, "which equals 30")
else:
    print("You entered, =", d1, "which is less than 30")

import random

value = random.randint(1, 100)
print(value)

print("Enter d2 =")
d2 = int(input())
if d2 < value:
    print("You entered, =", d2, "which is less than the number generated")
elif d2 == value:
    print("You entered, =", d2, "which equals the number generated")
else:
     print("You entered, =", d2, "which is bigger than the number generated")

import random

value2 = int(random.randint(0, 100))
value3 = int(random.randint(0,100))
print(value2, value3)
print("Enter d3 =")
d3 = int(input())
if d3 < value2 and d3 < value3:
    print("You entered, =", d3, "which is less than the numbers generated")
elif d3 > value2 and d3 > value3:
    print("You entered, =", d3, "which is bigger than the numbers generated")
elif d3 == value2:
    print("You entered, =", d3, "which equals one of the numbers generated")
elif d3 == value3:
    print("You entered, =", d3, "which equals one of the numbers generated")
elif d3 > value2 and d3 < value3:
    print("You entered,", d3, "which is less than one of the numbers generated")
elif d3 < value2 and d3 > value3:
    print("You entered,", d3, "which is less than one of the numbers generated")




