#https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

catA = int(input("Enter the poisiton of cat A : "))
catB = int(input("Enter the poisiton of cat B : "))
mouse = int(input("Enter the poisiton of Mouse : "))

x = catA - mouse
y = catB - mouse

if x < 0:
	x = x * - 1
if y < 0:
	y = y * - 1

if x < y:
	print("cat A")
elif x > y:
	print("cat B")
else:
	print("Mouse")
