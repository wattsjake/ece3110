import math

def min_max(value, tolerance):
    min = value*(1-tolerance)
    max = value*(1+tolerance)

    return min,max


#enter the value of the component and the tolerance
print("Enter Value of Component: ")
value = float(input())

print("Enter tolerance in decimal form: ")
tolerance = float(input())

#print(val_comp, tolerance)

min, max = min_max(value, tolerance)

print("Min: %.1f Max: %.1f" %(min, max))
