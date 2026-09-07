# This program is a simple area calculator for basic shapes, including a rectangle, circle, square, and a triangle. 
# The user can ask what shape needs to be calculated, then input values in cm, and the program gives the area in cm^2.

import math

while True:
    shape = input("What shape needs to be calculated (options: rectangle, circle, square, triangle)? ").lower()
    
    if shape== "rectangle":
      length= float(input("what is the length of the rectangle in cm? "))
      width= float(input("what is the width of the rectangle in cm? "))
      area= round(length * width, 2)
      print("Area:", area, "cm^2")
      
    elif shape== "circle":
      radius= float(input("what is the radius of the circle in cm? "))
      area= round(math.pi * (radius ** 2), 2)
      print("Area:", area, "cm^2")
      
    elif shape== "square":
      length= float(input("what is the side length of the square in cm? "))
      area= round(length ** 2, 2)
      print("Area:", area, "cm^2")

    elif shape== "triangle":
      base= float(input("what is the base of the triangle in cm? "))
      height= float(input("what is the height of the triangle in cm? "))
      area= round(((base*height)/2), 2)  
      print("Area:", area, "cm^2")
      
    else:
        print("invalid shape")
    
    again= input("Calculate another shape? (yes/no) ").lower()
    if again!= "yes":
        break
