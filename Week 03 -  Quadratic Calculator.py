# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 21:47:49 2025

@author: Mateusz
"""

"""
This program will display information about parabolas.
The program will calculate the X and Y-coordinates for the vertex of a parabola,
determine the concavity of the parabola, and determine if the parabola has real
roots and what they are if they exist.
"""

import math

def main():
    #get coefficients
    a_coefficient = float(input("Enter the a coefficient (non-zero value): "))
    if a_coefficient == 0:
        print("The a-coefficient must be non-zero. Please re-enter the value.")
        a_coefficient = float(input("Enter the a coefficient (non-zero value): "))
        
    b_coefficient = float(input("Enter the b coefficient: "))
    c_coefficient = float(input("Enter the c coefficient: "))
    print("") #adding a blank return for results
    
    #use the coefficients to calculate the X and Y coordinates of the vertex
    X_Vertex = - b_coefficient / (2 * a_coefficient)
    Y_Vertex = ( a_coefficient * X_Vertex * X_Vertex ) + ( b_coefficient * X_Vertex ) + c_coefficient
    
    #Determine concavity
    if a_coefficient > 0:
        concavity = "The parabola opens UPWARD"
    else:
        concavity = "The parabola opens DOWNWARD"
        
    #Calculate discriminant 
    discriminant = b_coefficient * b_coefficient - 4 * a_coefficient * c_coefficient
    
    #Determine number of real roots
    root_info2 = None
    if discriminant > 0:
        root1 = (-b_coefficient + math.sqrt(discriminant)) / (2 * a_coefficient)
        root2 = (-b_coefficient - math.sqrt(discriminant)) / (2 * a_coefficient)
        root_info = f"Root 1 X Coordinate                   {root1:.3f}"
        root_info2 = f"Root 2 X Coordinate                  {root2:.3f}"
    elif discriminant == 0:
        root1 = -b_coefficient / (2 * a_coefficient)
        root_info = f"Root 1 X Coordinate                     {root1:.3f}"
    else:    
        root_info = "The parabola has NO real roots"

    
    print("*******************************************")
    print("        Quadratic Equation Analyzer")
    print("*******************************************")
    print(f"a Coefficient                         {a_coefficient:.3f}")
    print(f"b Coefficient                         {b_coefficient:.3f}")
    print(f"c Coefficient                        {c_coefficient:.3f}")
    print("-------------------------------------------")
    print(f"X Coordinate                         {X_Vertex:.3f}")
    print(f"Y Coordinate                         {Y_Vertex:.3f}")
    print("-------------------------------------------")
    print(concavity)
    print("-------------------------------------------")
    print(root_info)
    if root_info2:  # Only prints root_info2 if it exists
        print(root_info2)

main()
