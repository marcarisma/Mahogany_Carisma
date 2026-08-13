import math

#ask the user to enter the coordinates of two points

x1 = float(input("enter your x1 "))
y1 = float(input("enter your x2 "))
x2 = float(input("enter your y1 "))
y2 = float(input("enter your y2 "))

#subtract the coordinates
subtract_x = (x2 - x1)
subtract_y = (y2 - y1)


#raises to the power of two to of both the coordinates
power_x = pow(subtract_x,2)
power_y = pow(subtract_y,2)


#adds the two coordinates
addition = power_x + power_y

#it square root the coordinate
x= math.sqrt = (addition)

#prints to get the distance
print ("the distance between the two point is" ,x)
