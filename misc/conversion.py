#conversions

print("==========Metric Conversion Program==========")
print("Enter the value you would like to convert."
       "Enter the units it is in.\n"
       "Then enter the value you would like to convert to\n"
       "Units: (T, G, M, k, c, m, u, n, p)\n")


num1 = input("Enter value: ")
unit1 = input("Units: ")
unit2 = input("Convert to: ")

if unit1[0] == "T" and unit2[0] == "G":
    ans = float(num1)*1000
    print(ans, unit2)
