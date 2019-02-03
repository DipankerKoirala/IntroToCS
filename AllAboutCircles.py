#!/usr/bin/python3/env python

#Calculates the Circumference, Area of a circle, Surface Area and Volume of a sphere for a given radius

#Gets user input in inches
Radius = float(input("Enter radius in inches "))

#Sets the value for pi
pi = 3.14

#Applies the appropriate formulas for the desired calculations
Circumference = 2*pi*Radius
Area = pi*(Radius)**2
Surface = 4*Area
Volume = 4/3*pi*(Radius)**3

#prints the answers
print("The radius of your circle is ", Radius, " inches")
print("The circumference of your circle is ", Circumference, " inches")
print("The area of your circle is ", Area, " inches")
print("A sphere with the radius of your circle would be have a surface area ", Surface, "square inches and a volume of ", Volume , "cubic inches" )