mi_hr = float(input("Enter a speed in miles/hour:"))
sl = 3.33564095e-9
num_SOL = 1609 * mi_hr * (1/3600) * sl
print ("Converted to a percentage of the speed of light:", num_SOL)
