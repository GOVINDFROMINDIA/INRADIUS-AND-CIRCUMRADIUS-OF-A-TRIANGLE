import math
print("FINDING INRADIUS AND CIRCUMRADIUS OF A TRIANGLE")
side1 = float(input("length of side 1: "))
         side2 = float(input("length of side 2: "))
         side3 = float(input("length of side 3: "))
semi = (side1+side2+side3)/2
        area = math.sqrt(semi*(semi-side1)*(semi-side2)*semi-side3))
        inradius = (area/semi)
        circumradius = (side1*side2*side3/(4 * area))
        print ('area = ', area)
         print ('CIRCUMRADIUS =' , circumradius)
         print ('INRADIUS =' , inradius)