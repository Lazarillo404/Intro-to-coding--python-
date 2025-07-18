"""
Edited on Sun Mar 23 2025

@author: Mateusz
"""

"""
This program will display information about parabolas.
The program will calculate the X and Y-coordinates for the vertex of a parabola,
determine the concavity of the parabola, and determine if the parabola has real
roots and what they are if they exist.
"""

import math

"""
function: get_a
Use: Gets and returns the a-coefficient of the parabola
Arguments: None
Returns: A float representing the valid a-coefficient
"""
def get_a():
    #get coefficients
    a_coefficient = float(input("Enter the a coefficient (non-zero value): "))
    while a_coefficient == 0:
        print("The a-coefficient must be non-zero. Please re-enter the value.")
        a_coefficient = float(input("Enter the a coefficient (non-zero value): "))
    
    return a_coefficient

"""
Function: calc_x_vertex
Use: Calculates the X-coordinate of the vertex.
Arguments: a-coefficient (float), b-coefficient (float)
Returns: The X-coordinate of the vertex as a float.
"""
def calc_x_vertex(a_coefficient, b_coefficient):
    #use the coefficients to calculate the X coordinates of the vertex
    X_Vertex = - b_coefficient / (2 * a_coefficient)
    
    return X_Vertex

"""
Function: calc_y_vertex
Use: Calculates the Y-coordinate of the vertex.
Arguments: a-coefficient (float), b-coefficient (float), c-coefficient (float)
Returns: The Y-coordinate of the vertex as a float.
"""
def calc_y_vertex(a_coefficient, b_coefficient, c_coefficient):
    #use the coefficients to calculate the Y coordinates of the vertex
    X_Vertex = calc_x_vertex(a_coefficient, b_coefficient)
    Y_Vertex = ( a_coefficient * X_Vertex * X_Vertex ) + ( b_coefficient * X_Vertex ) + c_coefficient
    
    return Y_Vertex

"""
Function: print_concavity
Use: Determines and prints whether the parabola opens upward or downward.
Arguments: a-coefficient (float)
Returns: None
"""
def print_concavity(a_coefficient):
    #Determine concavity
    if a_coefficient > 0:
        print("The parabola opens UPWARD")
    else:
        print("The parabola opens DOWNWARD")

"""
Function: calc_discriminant
Use: Calculates the discriminant of the quadratic equation.
Arguments: a-coefficient (float), b-coefficient (float), c-coefficient (float)
Returns: The discriminant as a float.
"""
def calc_discriminant(a_coefficient, b_coefficient, c_coefficient):
    #Calculate discriminant 
    discriminant = (b_coefficient * b_coefficient) - 4 * a_coefficient * c_coefficient
    
    return discriminant

"""
Function: print_roots
Use: Determines and prints the roots of the quadratic equation.
Arguments: a-coefficient (float), b-coefficient (float), c-coefficient (float)
Returns: None
"""
def print_roots(a_coefficient, b_coefficient, c_coefficient):
    #Determine number of real roots
    discriminant = calc_discriminant(a_coefficient, b_coefficient, c_coefficient)
    if discriminant > 0:
        root1 = (-b_coefficient + math.sqrt(discriminant)) / (2 * a_coefficient)
        root2 = (-b_coefficient - math.sqrt(discriminant)) / (2 * a_coefficient)
        print(f"Root 1 X Coordinate                   {root1:.3f}")
        print(f"Root 2 X Coordinate                  {root2:.3f}")
    elif discriminant == 0:
        root1 = -b_coefficient / (2 * a_coefficient)
        print(f"Root 1 X Coordinate                     {root1:.3f}")
    else:    
        print("The parabola has NO real roots")

def main():
    a_coefficient = get_a()
    b_coefficient = float(input("Enter the b coefficient: "))
    c_coefficient = float(input("Enter the c coefficient: "))
    print("") #adding a blank return for results
    
    X_Vertex = calc_x_vertex(a_coefficient, b_coefficient)
    Y_Vertex = calc_y_vertex(a_coefficient, b_coefficient, c_coefficient) 

    
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
    print_concavity(a_coefficient)
    print("-------------------------------------------")
    print_roots(a_coefficient, b_coefficient, c_coefficient)

main()
