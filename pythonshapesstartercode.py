from turtle import *
import math


# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)


### Write your code below:
answer= input("Do you want to make a shape:")
while(answer=="Y"):
    length= int(input("Enter number of sides:"))
    angle= 360/length
    for x in range (0, length):
        forward(10)
        right(angle)
    clear()
    answer= input("Do you want to make a shape:")    
    
       
else:
    print ("We are now exiting the program")
    










# Close window on click.
    exitonclick()
