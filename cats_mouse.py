#https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
catA = int(input("Enter the poisiton of cat A : "))
catB = int(input("Enter the poisiton of cat B : "))
mouse = int(input("Enter the poisiton of Mouse : "))

x = abs(catA - mouse)
y = abs(catB - mouse)

if x < y:
	print("cat A")
elif x > y:
	print("cat B")
else:
	print("Mouse")

