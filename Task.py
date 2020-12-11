#1)Завдання
from math import sqrt
x = int(input("x"))
y = int(input("y"))
r=int(input("r"))
if sqrt((x-0)**2+(y-0)**2==r/sqrt(2)):
    print("Точка з координатами x,y є точкою перетину діагоналей квадрату")
else:
    print("Точка з координатами x,y не є точкою перетину діагоналей квадрату")

#2)Завдання
from random import randint
n = int(input("n"))
a = [ randint(1, 100) for i in range(n)]
b = [ randint(1, 100) for i in range(n)]
d = len(a)
i = 0
c = []

while d > i:
    c.append(a[i])
    c.append(b[i])
    i += 1
print(c)
